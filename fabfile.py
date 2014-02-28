from fabric.api import local

def prepare_deploy():
    local("python ./manage.py test apps.blog")
    local('git add -p && git commit')
    local('git push')
