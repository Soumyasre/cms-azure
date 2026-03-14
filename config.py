import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ENTER_STORAGE_ACCOUNT_NAME'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ENTER_BLOB_STORAGE_KEY'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'ENTER_IMAGES_CONTAINER_NAME'
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'ENTER_SQL_SERVER_NAME.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'ENTER_SQL_DB_NAME'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ENTER_SQL_SERVER_USERNAME'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'ENTER_SQL_SERVER_PASSWORD'

    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc:///?odbc_connect=' +
        urllib.parse.quote_plus(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + (os.environ.get('SQL_SERVER') or 'ENTER_SQL_SERVER_NAME.database.windows.net') + ',1433;'
            'DATABASE=' + (os.environ.get('SQL_DATABASE') or 'ENTER_SQL_DB_NAME') + ';'
            'UID=' + (os.environ.get('SQL_USER_NAME') or 'ENTER_SQL_SERVER_USERNAME') + ';'
            'PWD=' + (os.environ.get('SQL_PASSWORD') or 'ENTER_SQL_SERVER_PASSWORD') + ';'
            'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = "ENTER_CLIENT_SECRET_HERE"
    AUTHORITY = "https://login.microsoftonline.com/common"
    CLIENT_ID = "ENTER_CLIENT_ID_HERE"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
