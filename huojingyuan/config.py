import os
from huojingyuan import app

# dev_db = 'sqlite:////'+os.path.join(os.path.dirname(app.root_path),'test_mac.db')
# dev_db = 'sqlite:///'+os.path.join(os.path.dirname(app.root_path),'test_mac.db')

SECRET_KEY = os.getenv('SECRET_KEY', '11111111')
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Dallasryp123@localhost:8889/huojingyuan'     #mac
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:HJ0527LY@172.17.98.125:3306/huojingyuan'   #win
POST_PER_PAGE = 5
DEBUG = True



