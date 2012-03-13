============
GolfDoksy.cz
============

Just simple website for hobby activity.

Install
=======

::
 $ mkvirtualenv --no-site-packages golfdoksy
 $ workon golfdoksy
 $ echo > $VIRTUAL_ENV/bin/postactivate << EOF
 #!/bin/bash
 # This hook is run after this virtualenv is activated.

 PROJECT_PATH=`pwd`
 export DJANGO_SETTINGS_MODULE=settings
 export PYTHONPATH=$PROJECT_PATH/src
 cd $PROJECT_PATH

 EOF
 $ deactivate
 $ workon golfdoksy
 $ #install supporting libraries
 $ sudo yum install libjpeg-turbo libjpeg-turbo-devel # on fedora
 $ # apt-get install libpq-dev python-dev libjpeg8 libjpeg8-dev libevent-dev gettext # on debian
 $ pip install -r requirements
