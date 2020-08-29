import sys
import json
sys.path.append('..')
import settings
sys.path.append(settings.BASE_DIR)
from data.db import redis_module, postgres_module

p = postgres_module.PostgresModule()
conn = p.connect()
print(p.show_models())
