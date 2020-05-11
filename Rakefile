namespace :tool do
    desc 'Task description'
    task :init do
        sh 'python3 -m venv .env'
        puts 'source .env/bin/activate'
        puts 'rake tool:pip'
    end

    desc 'Task description'
    task :pip do
        sh 'pip list | grep cdk'
        sh 'pip install -r requirements.txt'
        sh 'pip install --upgrade pip'
    end

    desc 'update cdk'
    task :cdk do
        sh 'cdk --version'
        sh 'npm list -g | grep cdk'
        sh 'npm update -g cdk'
        sh 'cdk --version'
        sh 'npm list -g | grep cdk'
        sh 'pip list | grep cdk'
        sh 'pip install --upgrade aws-cdk.core'
        sh 'pip list | grep cdk'
    end
end

namespace :cdk do
    desc 'test'
    task :test do
        sh 'cdk diff notify-change-aws-ip-range'
        sh 'pytest -v tests/unit/test_notify_change_ip_stack.py'
    end

    desc 'build'
    task :build do
        sh 'cdk deploy notify-change-aws-ip-range'
    end

    desc 'ci'
    task :ci do
        Rake::Task["cdk:build"].invoke
        Rake::Task["cdk:test"].invoke
    end
end
