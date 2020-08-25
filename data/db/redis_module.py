import redis
import settings

class RedisModule():
    def __init__(self):
        self.r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

    def set(self, key, value):
        return self.r.set(key, value)

    def get(self, key):
        return self.r.get(key)

    def keys(self, pattern):
        return self.r.keys(pattern)

    def delete(self, key):
        return self.r.delete(key)
