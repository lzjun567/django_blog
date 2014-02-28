from fabric.api import local

def prepare_deploy():
    local("python ./manage.py test apps.blog")
    local('git add *.py *.html && git commit')
    local('git push origin master')
