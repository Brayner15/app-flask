node {
    stage('SCM') {
        checkout scm
    }
    stage('SonarQube Analysis') {
        def scannerHome = tool 'SonarScanner'
        withSonarQubeEnv('sonar-1') {
            sh "${scannerHome}/bin/sonar-scanner"
        }
    }
}