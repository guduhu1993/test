pipeline {
  agent none
  stages {
    stage('pull_code') {
      steps {
        git(url: 'git@github.com:guduhu1993/test.git', branch: 'main', poll: true)
      }
    }

    stage('shell') {
      steps {
        sh 'python py_test.py'
      }
    }

  }
}