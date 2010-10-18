ALLDIRS = [ '/home/webdev/.virtualenvs/sentry/lib/python2.6/site-packages' ]

# note that the above directory depends on the locale of your virtualenv,
# and will thus be *different for each project!*
import os
import sys
import site

sys.stdout = sys.stderr

prev_sys_path = list(sys.path)

for directory in ALLDIRS:
    site.addsitedir(directory)

new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
       new_sys_path.append(item)
       sys.path.remove(item)
sys.path[:0] = new_sys_path

# this will also be different for each project!
sys.path.append('/home/webdev/domains/sentry-server-stack/sentry_server')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

