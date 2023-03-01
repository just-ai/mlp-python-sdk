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
                    manager.addShortText(params.BRANCH)
                }

                updateGitlabCommitStatus name: "build", state: "running"

                git url: "git@gitlab.just-ai.com:mpl-public/mpl-python-sdk.git",
                        branch: "${params.BRANCH}",
                        credentialsId: 'bitbucket_key'
            }
        }

        stage('Update spec') {
            steps {
                script {
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
                sh "./generate-protobuf.sh"
                sh "./generate-api-client.sh"

                sh "git add mlp_api"
                sh "git commit -m 'Automatic update API spec from CI' mlp-specs mlp_api mlp_sdk/grpc"
                sh "git push"
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
                    sh "sh ./run_mlp_tests.sh"
                }
            }
        }
    }
    post {
        failure {
            updateGitlabCommitStatus name: "build", state: "failed"
        }
        success {
            updateGitlabCommitStatus name: "build", state: "success"
        }
        unstable {
            updateGitlabCommitStatus name: "build", state: "failed"
        }
    }
}

