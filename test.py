import dj_database_url
import os
# print(os.environ.get('DATABASE_URL'))
#
# print(os.environ)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ["PGDATABASE"],
#         'USER': os.environ["PGUSER"],
#         'PASSWORD': os.environ["PGPASSWORD"],
#         'HOST': os.environ["PGHOST"],
#         'PORT': os.environ["PGPORT"],
#     }
# }
#
# db_url = os.environ.get('DATABASE_URL')
# if not db_url or db_url == '':
#     raise ValueError("DATABASE_URL is not set or is empty!")
# print(db_url)

db_url = "postgresql://postgres:EsTEpgjpfqXHQfANCxUILqGTNHjGMIiY@caboose.proxy.rlwy.net:10330/railway"
db_url_test = os.environ.get('DATABASE_URL')

print(db_url)
print(db_url_test)

DATABASES = {'default': dj_database_url.config(default=db_url_test,
                                               conn_max_age=600)}

# print(db_url)
# print(db_url_test)
# #
print(DATABASES['default'])