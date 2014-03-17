from fabric.api import local, settings, abort, cd, env, run

env.hosts = ['root@foofish.net']

def prepare_deploy():
    #test() 
    with settings(warn_only=True):
        local('git add *.py *.html *js *.css && git commit')
        local('git push origin master')

def test():
    with settings(warn_only=True):
        result = local("python ./manage.py test apps.blog", capture=True)
        if result.failed and not confirm("Test failed, Continue anyway"):
            abort("aborting at user request")

def deploy():
    project_dir = '/home/django_blog'
    with cd(project_dir):
        run("git pull origin master")
        run("/root/envs/foofish/bin/python ./manage.py collectstatic")
        run("supervisorctl restart foofish")

def go():
    prepare_deploy()
    deploy()

