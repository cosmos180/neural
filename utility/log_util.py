"""
Author       : bughero jinxinhou@tuputech.com
Date         : 2023-12-15 15:16:47
LastEditors  : bughero jinxinhou@tuputech.com
LastEditTime : 2023-12-15 15:21:30
FilePath     : /neural-networks-and-deep-learning/src/utility/log_util.py
Description  : 

Copyright (c) 2023 by 图普科技, All Rights Reserved. 
"""
import logging
import os
from logging.handlers import RotatingFileHandler


def create_logger(name: str, file_mode: bool = True, log_path: str = "."):
    # 创建一个日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not os.path.exists(log_path):
        os.makedirs(log_path)

    # 创建一个日志处理器
    handler = RotatingFileHandler(
        f"{log_path}/{name}.log", maxBytes=4 * 1024 * 1024, backupCount=5
    )

    # 设置日志格式器
    formatter = logging.Formatter(
        "%(asctime)s [%(funcName)s:%(lineno)s] [%(levelname)s]: %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
