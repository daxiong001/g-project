import json
import os
import time
from functools import wraps
import logging
import json as complexjson

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger(object):

    def __init__(self):
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


def log_filter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = 1000 * time.time()
        logger.info(f"=============  Begin: {func.__name__}  =============")
        logger.info(f"{args}Args: {kwargs}")

        try:
            rsp = func(*args, **kwargs)
            logger.info("请求地址: {0}".format(rsp.request.url))
            logger.info("请求方法: {0}".format(rsp.request.method))
            logger.info("请求头: {0}".format(rsp.request.headers))
            if type(rsp.request.body) == str:
                logger.info("请求参数: {0}".format(rsp.request.body))
            else:
                logger.info("请求参数: {0}".format(rsp.request.body.decode("utf-8", "ignore")))
            logger.info("响应结果：{0}".format(json.loads(bytes.decode(rsp.content))))
            end = 1000 * time.time()
            logger.info(f"Time consuming: {end - start}ms")
            logger.info(f"=============   End: {func.__name__}   =============\n")
            return rsp
        except Exception as e:
            logger.error(repr(e))
            raise e

    return wrapper


logger = Logger().logger
