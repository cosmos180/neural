"""
Author       : bughero jinxinhou@tuputech.com
Date         : 2023-12-15 15:15:00
LastEditors  : bughero jinxinhou@tuputech.com
LastEditTime : 2023-12-15 15:38:33
FilePath     : /neural-networks-and-deep-learning/unittest/test_mnist.py
Description  : 

Copyright (c) 2023 by 图普科技, All Rights Reserved. 
"""
from mnist.mnist_loader import load_data_wrapper
from mnist.network import Network
from utility.log_util import create_logger

# 创建日志对象
TLog = create_logger(__name__, False)


class TestMnist:
    def setup_method(self, method):
        TLog.info("setup_method...")

    def teardown_method(self, method):
        TLog.info("teardown_method...")

    def test_mnist(self):
        TLog.info("test_mnist_01...")
        training_data, validation_data, test_data = load_data_wrapper()
        TLog.info(f"type: {type(test_data)}")
        net = Network([784, 30, 10])
        net.SGD(list(training_data), 30, 10, 3.0, test_data=list(test_data))
