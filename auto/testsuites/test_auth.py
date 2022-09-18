import pytest
import json

import auto.common.httprestclient as Client

def test_auth_valid_data(gconfig):
    resp = Client.create_auth(gconfig)
    assert resp.status_code==200
    json_obj = resp.json()
    assert 'token' in json_obj

def test_auth_invalid_data(gconfig):
    payload = {'username': 'foo',
               'password': 'password'}
    resp = Client.create_auth(gconfig,body=payload)
    assert resp.status_code==200
    json_obj = json.loads(resp.text)
    assert 'token' in json_obj



