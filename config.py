import os


current_path = os.path.dirname(os.path.realpath(__file__))
db_path = "sqlite:///" + current_path + "\\food_delivery.db"


class Config:
    DEBUG = True
    SECRET_KEY = "654e`sdxfc!gvhuij9io?lmkn\\\jbhvyug-ihk"
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
