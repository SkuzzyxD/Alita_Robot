import pickle
from alita import redisClient


def set_key(key: str, value):
    redisClient.set(key, pickle.dumps(value))


def get_key(key: str):
    return pickle.loads(redisClient.get(key))


def flushredis():
    redisClient.flushall()


def allkeys():
    return redisClient.keys()