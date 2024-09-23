pipeline {
    options {
        gitLabConnection("gitlab just-ai")
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        disableConcurrentBuilds()
        timeout(time: 60, unit: 'MINUTES')
        timestamps()
    }
    agent {
        label 'caila-dev-cloud-agent'
    }
    parameters {
        string(name: "BRANCH", defaultValue: "dev", description: "")
        booleanParam(name: 'NEED_REBUILD', defaultValue: false, description: '')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: '')
    }
    stages {
        stage('Prepare') {
            steps {
                script {
                    RESULT_BRANCH = env.gitlabBranch != null ? env.gitlabBranch : params.BRANCH
                    manager.addShortText("${RESULT_BRANCH}")
                    echo "${env.gitlabBranch}"
                }

                git url: "git@gitlab.just-ai.com:mpl-public/mpl-python-sdk.git",
                        branch: "${RESULT_BRANCH}",
                        credentialsId: 'bitbucket_key'
            }
        }

        stage('Update spec') {
            steps {
                script {
                    updateGitlabCommitStatus name: STAGE_NAME, state: "running"

                    sh("./mlp-specs/update.sh")

                    def hasChanges = !sh(returnStdout: true, script: 'git status -s mlp-specs').trim().isEmpty()

                    env.NEED_REBUILD = hasChanges
                }
            }
        }

        stage('Rebuild client stubs') {
            when {
                expression { env.NEED_REBUILD == 'true' || params.NEED_REBUILD }
            }
            steps {
                updateGitlabCommitStatus name: STAGE_NAME, state: "running"
                sh "./generate-protobuf.sh"
                sh "./generate-api-client.sh"

                sh "echo `docker images --digests | grep openapitools/openapi-generator-cli`"
                sh "git add mlp_api"
                sh "git commit -m 'Automatic update API spec from CI' mlp-specs mlp_api mlp_sdk/grpc"
                sh "git push"
            }
        }
        stage('Lint') {
            steps {
                updateGitlabCommitStatus name: STAGE_NAME, state: "running"
                withPythonEnv('/opt/ansible-venv-python3/bin/python') {
                    sh "pip install ruff==0.6.4"
                    sh "ruff check --config pyproject.toml ."
                }
            }
        }
        stage('Tests') {
            when {
                expression { params.RUN_TESTS ?: false || env.NEED_REBUILD == 'true' }
            }

            environment {
                NEXUS_CREDS = credentials('jenkins-for-pypi')
                S3_SECRET_KEY = credentials('rnd_s3_secret_key')
                S3_STORAGE_CONFIG = """{
                    "mlp_bucket": "rnd-models",
                    "service_name": "s3",
                    "region": "ru-1a",
                    "access_key": "72116_rnd-models-user",
                    "secret_key": "${S3_SECRET_KEY}",
                    "endpoint": "https://248305.selcdn.ru",
                    "data_dir": "Z8ht8D1YNM/rnd-models"
                }"""
            }
            steps {
                script {
                    updateGitlabCommitStatus name: STAGE_NAME, state: "running"
                    sh "sh ./run_mlp_tests.sh"
                }
            }
        }
        stage('Rebuild MLP Services') {
            when {
                expression { RESULT_BRANCH in ['dev','stable','release'] }
            }
            steps {
                parallel (
//                     "build mlp-aimyvoice-base-service" : {
//                         build job: "mlp-aimyvoice-base-service-build/${RESULT_BRANCH}", wait: false
//                     },
                    "build mlp_task_zoo" : {
                        build job: "mlp_task_zoo-build/${RESULT_BRANCH}", wait: false
                    },
                    "build sd" : {
                        build job: "sd-build/${RESULT_BRANCH}", wait: false
                    }
                )
            }
        }
        stage('Merge release to stable') {
            when {
                expression {
                    params.BRANCH == 'release'
                }
            }
            steps {
                sshagent(credentials: ['bitbucket_key']) {
                    sh "git config user.email 'jenkins@just-ai.com'"
                    sh "git  config user.name 'Jenkins'"
                    sh """git checkout stable --force"""
                    sh """git pull origin stable"""
                    sh """git merge origin/release -m 'Automatic merge from release to stable'"""
                    sh """git push"""
                }
            }
        }
        stage('Merge stable to dev') {
            when {
                expression {
                    params.BRANCH == 'stable'
                }
            }
            steps {
                sshagent(credentials: ['bitbucket_key']) {
                    sh "git config user.email 'jenkins@just-ai.com'"
                    sh "git  config user.name 'Jenkins'"
                    sh """git checkout dev --force"""
                    sh """git pull origin dev"""
                    sh """git merge origin/stable -m 'Automatic merge from stable to dev'"""
                    sh """git push"""
                }
            }
        }
    }
    post {
        failure {
            updateGitlabCommitStatus name: "Prepare", state: "failed"
            updateGitlabCommitStatus name: "Update spec", state: "failed"
            updateGitlabCommitStatus name: "Rebuild client stubs", state: "failed"
            updateGitlabCommitStatus name: "Lint", state: "failed"
            updateGitlabCommitStatus name: "Tests", state: "failed"
            updateGitlabCommitStatus name: "Rebuild MLP Services", state: "failed"
        }
        success {
            updateGitlabCommitStatus name: "Prepare", state: "success"
            updateGitlabCommitStatus name: "Update spec", state: "success"
            updateGitlabCommitStatus name: "Rebuild client stubs", state: "success"
            updateGitlabCommitStatus name: "Lint", state: "success"
            updateGitlabCommitStatus name: "Tests", state: "success"
            updateGitlabCommitStatus name: "Rebuild MLP Services", state: "success"
        }
        unstable {
            updateGitlabCommitStatus name: "Prepare", state: "failed"
            updateGitlabCommitStatus name: "Update spec", state: "failed"
            updateGitlabCommitStatus name: "Rebuild client stubs", state: "failed"
            updateGitlabCommitStatus name: "Lint", state: "failed"
            updateGitlabCommitStatus name: "Tests", state: "failed"
            updateGitlabCommitStatus name: "Rebuild MLP Services", state: "failed"
        }
        aborted {
            updateGitlabCommitStatus name: "Prepare", state: "canceled"
            updateGitlabCommitStatus name: "Update spec", state: "canceled"
            updateGitlabCommitStatus name: "Rebuild client stubs", state: "canceled"
            updateGitlabCommitStatus name: "Lint", state: "canceled"
            updateGitlabCommitStatus name: "Tests", state: "canceled"
            updateGitlabCommitStatus name: "Rebuild MLP Services", state: "canceled"
        }
    }
}
