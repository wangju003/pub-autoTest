#!/usr/bin/python
# -*- coding: utf-8 -*-

from caseManage.common.getdb import db

# 测试用例表
class TestCase(db.Model):
    __tablename__ = "testcase"
    id = db.Column(db.Integer, primary_key=True)
    api_purpose = db.Column(db.String(50))
    request_url = db.Column(db.String(100))
    request_method = db.Column(db.Enum("POST", "GET"))
    request_data_type = db.Column(db.Enum("Data", "Form", "File"))
    request_data = db.Column(db.Text, nullable=False)
    assert_method = db.Column(db.Enum("assertIn", "assertNotIn In"), default="assertIn")
    check_point = db.Column(db.String(255))
    correlation = db.Column(db.String(100))
    active = db.Column(db.Enum("Yes", "No"))
    creater = db.Column(db.String(50))
    project = db.Column(db.Enum("gw", "hw", "gw_lt"), default="gw")

    def __repr__(self):
        return "<TestCase.%s>" % self.api_purpose