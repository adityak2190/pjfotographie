import os


class Config(object):
    '''
    Default configuration settings.
    '''
    # Application IP address
    APP_HOST = os.environ.get('HOST', '0.0.0.0')
    APP_PORT = int(os.environ.get('PORT', 5000))
    APP_DEBUG = False
    EMAIL_TEMPLATE_LOCATION = '/templates/email_template.j2'
    WEDDING_THUMBNAILS_DIR = '/static/images/wedding/thumbnails/'
    ASSORTED_THUMBNAILS_DIR = '/static/images/assorted/thumbnails/'


class ProductionConfig(Config):
    '''
    Production configuration settings.
    '''
    pass


class DevelopmentConfig(Config):
    '''
    Development configuration settings.
    '''
    # Enable debugging
    APP_DEBUG = True
