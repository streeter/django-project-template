import os

## Import our defaults (globals)
from {{ project_name }}.conf.default import *

## Inherit from environment specifics
DJANGO_CONF = os.environ.get('DJANGO_CONF', 'default')
if DJANGO_CONF != 'default':
    module = __import__(DJANGO_CONF, globals(), local(), ['*'])
    for k in dir(module):
        locals()[k] = getattr(module, k)

## Import local settings
try:
    from {{ project_name }}.local_settings import *
except ImportError, e:
    pass

## Remove any disabled apps
if 'DISABLED_APPS' in locals():
    INSTALLED_APPS = [k for k in INSTALLED_APPS if k not in DISABLED_APPS]
    
    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS)
    
    for a in DISABLED_APPS:
        for x, m in enumerate(MIDDLEWARE_CLASSES):
            if m.startswith(a):
                MIDDLEWARE_CLASSES.pop(x)
        
        for x, m in enumerate(TEMPLATE_CONTEXT_PROCESSORS):
            if m.startswith(a):
                TEMPLATE_CONTEXT_PROCESSORS.pop(x)

## All done