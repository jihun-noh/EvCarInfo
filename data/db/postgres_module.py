from sqlalchemy import create_engine
import settings

class PostgresModule():
    def __init__(self):
        self.engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{db}'
                        .format(user = settings.POSTGRES_USER,
                                password = settings.POSTGRES_PASSWORD,
                                host = settings.POSTGRES_HOST,
                                port = settings.POSTGRES_PORT,
                                db = settings.POSTGRES_DB))

    def connect(self, **kargs):
        self.conn = self.engine.connect(**kargs)
        return self.conn


        #     conn.close()
        # db.dispose()
