import datetime
from redis import Redis

class Config:
    DEBUG = True
    SECRET_KEY = 'dfasldvnsagsefjweas'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=20)
    SESSION_PEFRESH_EACH_REQUEST = True
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(host='127.0.0.1',port=6379)
