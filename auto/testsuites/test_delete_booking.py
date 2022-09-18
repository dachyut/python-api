import requests
import json
from auto.common import httprestclient

def test_deletebooking_id(gconfig,get_token,get_booking_id):
    json_obj = json.loads(get_token)
    token = "token=" + json_obj['token']
    headers = {'Cookie': token}
    bookingid = get_booking_id
    url = gconfig.build_item_url('booking',bookingid)
    resp = gconfig.conn.delete(url,headers=headers)
    assert resp.status_code == 201
    assert resp.text == 'Created'