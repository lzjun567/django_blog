#!/bin/bash
NAME="foofish_app"
DJANGODIR=/home/django_blog
SOCKFILE=/tmp/foofish.sock
USER=root
GROUP=root
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=django_blog.settings.prod
DJANGO_WSGI_MODULE=django_blog.wsgi

echo "Starting $NAME as `whoami`"

cd $DJANGODIR
source /root/envs/foofish/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec /root/envs/foofish/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--log-level=error \
--bind=unix:$SOCKFILE
