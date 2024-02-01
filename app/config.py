import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "..", "webapp.db")

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "hlhlhluh45i76uyghjd64er67589fdtrt87087643edfghjk"
