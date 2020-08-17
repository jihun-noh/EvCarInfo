import redis

class RedisModule():
    def __init__(self, host, port, db):
        self.conn = redis.Redis(host=host, port=port, db=db)

    def set(self, key, value):
        return self.conn.set(key, value)

    def get(self, key):
        return self.conn.get(key)
