import redis
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)


class Config(object):
    """添加配置信息"""
    DEBUG = True
    # """添加数据库配置"""
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/flask_project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    SECRET_KEY = "Z58Xyt2fwEXo+dIC7mna8Yo6GbCap7Du8Qh52O6lKjUNo6rtmAuxiLXZU1A+dm50"
    # flask-session 配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒


app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启CSRF跨站请求
CSRFProtect(app)
Session(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.route("/")
def index():
    return "hello world 世界真美好"


if __name__ == '__main__':
    manager.run()
