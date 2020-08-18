import redis

class RedisModule():
    HOST = '54.180.99.44'
    PORT = '6379'

    def __init__(self):
        self.r = redis.Redis(host=RedisModule.HOST, port=RedisModule.PORT, db=0)

    def set(self, key, value):
        return self.r.set(key, value)

    def get(self, key):
        return self.r.get(key)

    def keys(self, pattern):
        return self.r.keys(pattern)
