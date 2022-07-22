import os
# from .instance.config import NEWS_API_KEY


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'

    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

    HIGHLIGHTS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&language=en&apiKey={}'

    CATEGORY_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?category={}&apiKey={}'


    NEWS_API_KEY = "4db0fda9f39c4d3d932dbd2db03ead2e"


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development': DevConfig,
'production': ProdConfig
}
