pipeline {
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        disableConcurrentBuilds()
        timeout(time: 60, unit: 'MINUTES')
        timestamps()
    }
    agent {
        label 'build'
    }
    parameters {
        booleanParam(defaultValue: false, name: 'SKIP_TESTS', description: '')
    }
    stages {
        stage('Build with maven') {
            environment {
                NEXUS_CREDS = credentials('gerbylev-for-pypi')
            }
            steps {
                script {
                    manager.addShortText(env.BRANCH_NAME)
                }
                sh """./build.sh \
                  ${env.NEXUS_CREDS_USR} \
                  ${env.NEXUS_CREDS_PSW} \
                  ${BUILD_NUMBER} \
                  ${BRANCH_NAME.toLowerCase().replaceAll("-","").replaceAll("_","")} \
                  """
            }
        }
    }
}
