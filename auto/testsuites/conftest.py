import requests
import json
import os
import pytest

import auto.common.httprestclient as Client

testenv_f = ".\\config\\testenv.json"

#base_url = "https://restful-booker.herokuapp.com/auth"


class GlobalConfig:
    def __init__(self):
        self.testenv = {}
        if os.path.exists(testenv_f):
            self.testenv = json.load(open(testenv_f))
        self.base_url = self.testenv.get("base_url")
        self.username = self.testenv.get("username")
        self.password = self.testenv.get("password")
        self.res_paths = self.testenv.get("res_paths")
        self._init_connection()

    def build_res_url(self, res):
        if os.path.exists(testenv_f):
            self.testenv = json.load(open(testenv_f))
        return self.build_url(self.testenv.get('res_paths')[res])

    def build_item_url(self, res, _id):
        return "{}/{}".format(self.build_res_url(res), _id)

    def build_url(self, path):
        url = self.testenv.get("base_url")
        if not path.startswith("/"):
            url = url + "/"
        return url + path

    def _init_connection(self):
        self.base_url = self.testenv.get("base_url")
        conn = requests.Session()
        conn.verify = False
        conn.headers.update({"Content-Type": "application/json"})
        conn.headers.update({"Accept": "application/json"})
        self.conn = conn

@pytest.fixture(scope="session")
def gconfig():
    return GlobalConfig()


@pytest.fixture(scope="session")
def get_token(gconfig,headers=None,body=None):
    token = Client.create_auth(gconfig,headers,body)
    return token.text

@pytest.fixture(scope="session")
def get_booking_id(gconfig):
    booking = Client.create_booking(gconfig)
    json_obj = json.loads(booking.text)
    booking_id = json_obj['bookingid']
    return booking_id

