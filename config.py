import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'asmaa.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'asmaa-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'asmaasaeed'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'As1234567890'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'asmaastorge'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'TeFe84k/MDT0V0TN5y8LW+z/HHBQthFXTEKOoxrgvzu6Qvy79U3MSsbnAIVDuCJHugA3I6FRMyZ2+AStrdPTdw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
