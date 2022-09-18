import pytest
import json

import auto.common.httprestclient as Client
from auto.utils import excel_util

#testdata = (username, password, expected_result)
testdata = [
    ('admin','password123','pass'),
    ('foo','password','fail'),
    ('bar','test123','fail'),
]

@pytest.mark.parametrize("username,password,expected",testdata)
def test_auth_ddd(username,password,expected,gconfig):
    payload = {'username': username,
               'password': password}
    resp = Client.create_auth(gconfig,body=payload)
    json_obj = json.loads(resp.text)
    status_code = resp.status_code
    is_token_found = 'token' in json_obj
    actul = 'pass' if (status_code == 200 and is_token_found) else 'fail'
    assert actul == expected