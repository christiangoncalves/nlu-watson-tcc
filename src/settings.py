from decouple import config

NATURAL_LANGUAGE_UNDERSTANDING_APIKEY = config('NATURAL_LANGUAGE_UNDERSTANDING_APIKEY')
NATURAL_LANGUAGE_UNDERSTANDING_IAM_APIKEY = config('NATURAL_LANGUAGE_UNDERSTANDING_IAM_APIKEY')
NATURAL_LANGUAGE_UNDERSTANDING_URL = config('NATURAL_LANGUAGE_UNDERSTANDING_URL')
NATURAL_LANGUAGE_UNDERSTANDING_AUTH_TYPE = config('NATURAL_LANGUAGE_UNDERSTANDING_AUTH_TYPE')
HOST = config('HOST')
DATABASE = config('DATABASE')
USER = config('USER')
PASSWORD = config('PASSWORD', default='')
CHARSET = config('CHARSET')