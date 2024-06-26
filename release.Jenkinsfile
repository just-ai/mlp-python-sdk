pipeline {
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        disableConcurrentBuilds()
        timeout(time: 60, unit: 'MINUTES')
        timestamps()
    }
    agent {
        label 'caila-dev-cloud-agent'
    }
    parameters {
        string(name: "RELEASE_BRANCH", defaultValue: "release", description: "")
        string(name: "NEW_VERSION", defaultValue: "1.0.0", description: '')
    }
    environment {
        GITLAB_REPO = 'git@gitlab.just-ai.com:mpl-public/mpl-python-sdk.git'
        GITHUB_REPO = 'git@github.com:just-ai/mlp-python-sdk.git'
    }
    stages {
        stage('Prepare') {
            steps {
                script {
                    manager.addShortText("${params.RELEASE_BRANCH}")
                    manager.addShortText("${params.NEW_VERSION}")
                }

                git url: env.GITLAB_REPO,
                    branch: "${params.RELEASE_BRANCH}",
                    credentialsId: 'bitbucket_key'
            }
        }
        stage('Set Version') {
            steps {
                script {
                    sh """
                        sed -i "s/version=.*/version='${params.NEW_VERSION}',/" setup.py
                    """
                }
            }
        }
        stage('Build and deploy') {
            steps {
                script {
                    sh "./build_wheel.sh"
                    sh "twine upload --repository nexus mlp_sdk-${params.NEW_VERSION}-py3-none-any.whl"
                }
            }
        }
        stage('Commit and Tag') {
            steps {
                script {
                    sh """
                        git add setup.py
                        git commit -m "update release version to ${params.NEW_VERSION}"
                        git tag -a v${params.NEW_VERSION} -m 'Release version ${params.NEW_VERSION}'
                    """
                }
            }
        }
        stage('Push Changes') {
            steps {
                script {
                    sh """
                        git push ${env.GITLAB_REPO} ${params.RELEASE_BRANCH}
                        git push ${env.GITLAB_REPO} --tags
                        git push ${env.GITHUB_REPO} ${params.RELEASE_BRANCH}
                        git push ${env.GITHUB_REPO} --tags
                    """
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}