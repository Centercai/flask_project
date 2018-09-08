import redis


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


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


# 定义配置字典
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
