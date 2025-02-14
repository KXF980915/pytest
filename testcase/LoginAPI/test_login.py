#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/2/14 22:14
# @Author  : Kolt.Kuang
# @Site    : 
# @File    : test_login.py
# @Project : pytest
# @Software: PyCharm
import allure
import pytest

from base.apiutil import RequestBase
from base.generateId import m_id, c_id
from common.operyaml import get_testcase_yaml


@allure.feature(next(m_id) + '用户登录')
class TestLogin:
    @allure.story(next(c_id) + "登录")
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml(r"D:\pytest\testcase\LoginAPI\login.yaml"))
    def test_login(self, base_info, testcase):
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)
