import os

user='jona'
passwd='nathanoj35'

class Config:
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://{}:{}@localhost/apidb'.format(user,passwd)

    SQLALCHEMY_TRACK_MODIFICATIONS=False

    SECRET_KEY='945d1cdee40cf0f66925d1356fdfbec3331488778cd69c35299b87dad6863b4e'

    DEBUG=True