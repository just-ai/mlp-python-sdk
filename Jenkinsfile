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

//         stage('Lint') {
//             steps {
//                 updateGitlabCommitStatus name: STAGE_NAME, state: "running"
//                 withPythonEnv('/opt/ansible-venv-python3/bin/python') {
//                     sh "/opt/ansible-venv-python3/bin/pip install ruff==0.6.4"
//                     sh "ruff check --config pyproject.toml ."
//                 }
//             }
//         }
//         stage('Tests') {
//             when {
//                 expression { params.RUN_TESTS ?: false || env.NEED_REBUILD == 'true' }
//             }
// 
//             environment {
//                 NEXUS_CREDS = credentials('jenkins-for-pypi')
//                 S3_SECRET_KEY = credentials('rnd_s3_secret_key')
//                 S3_STORAGE_CONFIG = """{
//                     "mlp_bucket": "rnd-models",
//                     "service_name": "s3",
//                     "region": "ru-1a",
//                     "access_key": "72116_rnd-models-user",
//                     "secret_key": "${S3_SECRET_KEY}",
//                     "endpoint": "https://248305.selcdn.ru",
//                     "data_dir": "Z8ht8D1YNM/rnd-models"
//                 }"""
//             }
//             steps {
//                 script {
//                     updateGitlabCommitStatus name: STAGE_NAME, state: "running"
//                     sh "sh ./run_mlp_tests.sh"
//                 }
//             }
//         }
    }
    post {
        failure {
            updateGitlabCommitStatus name: "Prepare", state: "failed"
            updateGitlabCommitStatus name: "Lint", state: "failed"
            updateGitlabCommitStatus name: "Tests", state: "failed"
        }
        success {
            updateGitlabCommitStatus name: "Prepare", state: "success"
            updateGitlabCommitStatus name: "Lint", state: "success"
            updateGitlabCommitStatus name: "Tests", state: "success"
        }
        unstable {
            updateGitlabCommitStatus name: "Prepare", state: "failed"
            updateGitlabCommitStatus name: "Lint", state: "failed"
            updateGitlabCommitStatus name: "Tests", state: "failed"
        }
        aborted {
            updateGitlabCommitStatus name: "Prepare", state: "canceled"
            updateGitlabCommitStatus name: "Lint", state: "canceled"
            updateGitlabCommitStatus name: "Tests", state: "canceled"
        }
    }
}
