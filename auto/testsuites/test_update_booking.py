import requests
import json
from auto.common import httprestclient

def test_booking(gconfig,get_token,get_booking_id):
    json_obj = json.loads(get_token)
    token = "token=" + json_obj['token']
    headers = {'Cookie': token}
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": "true",
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Cheese"
    }
    bookingid = get_booking_id
    url = gconfig.build_item_url('booking', bookingid)
    resp = gconfig.conn.put(url, headers=headers,json=payload)
    print(resp.text)
    assert resp.status_code == 200
    #TBD verify data updated