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
                    sh("./mpl-specs/update.sh")

                    def hasChanges = !sh(returnStdout: true, script: 'git status -s mpl-specs').trim().isEmpty()

                    env.NEED_REBUILD = hasChanges || !params.CHECK_SCHEMAS_ONLY
                }
            }
        }

        stage('Rebuild client stubs') {
            when {
                expression { env.NEED_REBUILD == 'true' }
            }
            steps {
                sh "./generate-protobuf.sh"
                sh "./generate-api-client.sh"

                sh "git add mpl_api"
                sh "git commit -m 'Automatic update API spec from CI' mpl-specs mpl_api mpl_sdk/grpc"
                sh "git push"
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

