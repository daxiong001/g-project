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


class Logger:

    def __init__(self):
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.INFO)

        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.INFO)
        self.filelogger.setLevel(logging.INFO)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


# def log_filter(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = 1000 * time.time()
#         logger.info(f"=============  Begin: {wrapper.__name__}  =============")
#         logger.info(f"{args}Args: {kwargs}")
#
#         try:
#             rsp = func(*args, **kwargs)
#             logger.info("请求地址: {0}".format(rsp.request.url))
#             logger.info("请求方法: {0}".format(rsp.request.method))
#             logger.info("请求头: {0}".format(rsp.request.headers))
#             logger.info("请求c参数: {0}".format(rsp.request.body))
#             # if type(rsp.request.body) == str:
#             #     logger.info("请求参数: {0}".format(rsp.request.body))
#             # else:
#             #     logger.info("请求参数: {0}".format(rsp.request.body.decode("utf-8", "ignore")))
#             logger.info("响应结果：{0}".format(json.loads(bytes.decode(rsp.content))))
#
#             end = 1000 * time.time()
#             logger.info(f"Time consuming: {end - start}ms")
#             logger.info(f"=============   End: {func.__name__}   =============\n")
#             return rsp
#         except Exception as e:
#             logger.error(repr(e))
#             raise e
#
#     return wrapper
import time
import logging
from functools import wraps

# 初始化日志配置
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

def api_log_decorator(func):
    @wraps(func)  # 保留被装饰函数的元数据
    def wrapper(*args,**kwargs):
        # 记录请求开始信息
        start_time = time.time()
        logger.info(f"🟢 接口请求开始 | 函数名: {func.__name__}")
        logger.info(f"🔍 请求参数 | 位置参数: {args} | 关键字参数: {kwargs}")

        try:
            # 执行原函数（发送请求）
            response = func(*args,**kwargs)
            # 记录响应结果
            logger.info(f"🟩 响应成功 | 状态码: {response.status_code}")
            logger.info(f"响应内容: {response.text}")  # 生产环境建议使用debug级别
            return response
        except Exception as e:
            # 记录异常信息
            logger.error(f"🔴 请求异常 | 错误类型: {type(e).__name__} | 详情: {str(e)}")
            raise
        finally:
            # 计算耗时
            end_time = time.time()
            logger.info(f"⏱️ 请求耗时: {end_time - start_time:.2f}秒\n")

    return wrapper


def retry(max_attempts=3):
    """请求重试"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts -1:
                        raise
            return wrapper
    return decorator

# 组合使用装饰器

logger = Logger().logger
