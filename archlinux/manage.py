#!/usr/bin/env python

''' Settings import  '''

from django.core.management import execute_manager

ERR_MSG = '''Error: Can't find the file 'settings.py' in the directory
containing %r. It appears you've customized things.\nYou'll have to
run django-admin.py, passing it your settings module.\n(If
the filea settings.py does indeed exist, it's causing an ImportError
somehow.)\n'''

try:
	import settings # Assumed to be in the same directory.
except ImportError:
	import sys
	sys.stderr.write(ERR_MSG % __file__)
	sys.exit(1)

if __name__ == "__main__":
	execute_manager(settings)
