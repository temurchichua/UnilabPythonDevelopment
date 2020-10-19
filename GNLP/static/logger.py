import logging, logging.config

LOGGING_CONFIG = {
    'version': 1, # required
    'disable_existing_loggers': True, # this config overrides all other loggers
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s -- %(message)s'
        },
        'whenAndWhere': {
            'format': '%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'whenAndWhere'
        }
    },
    'loggers': {
        '': { # 'root' logger
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
log = logging.getLogger('') # factory method
