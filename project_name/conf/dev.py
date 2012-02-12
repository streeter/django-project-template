from {{ project_name }}.conf.default import *
import getpass


###############################################################################
## Debug Flags

DEVELOPMENT = True
DEBUG = True
TEMPLATE_DEBUG = True


###############################################################################
## Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tracker',
        'USER': getpass.getuser(),
        'PASSWORD': '',
        'HOST': '/tmp/mysql.sock',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
    }
}


###############################################################################
## Debug Toolbar

try:
    import debug_toolbar
except ImportError:
    pass
else:
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }


###############################################################################
## Installed Apps

INSTALLED_APPS += (
)


###############################################################################
## Middleware

MIDDLEWARE_CLASSES += (
    # Middleware goes here
)

###############################################################################
## Templates

TEMPLATE_CONTEXT_PROCESSORS += (
)

###############################################################################
## Cache

CACHE_BACKEND = 'locmem://'

###############################################################################
## Email

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
