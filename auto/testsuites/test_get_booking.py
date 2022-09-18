import requests
import json
from auto.common import httprestclient
import auto.common.httprestclient as Client

def test_get_all_bookings(gconfig):
    url = gconfig.build_res_url('booking')
    resp = gconfig.conn.get(url)
    assert resp.status_code==200
    json_obj = json.loads(resp.text)
    assert len(json_obj)>0      #TBD  json_obj['bookingid'].lenghth > 0

def test_get_specific_booking_id(gconfig):
    firstname = 'Testuser789456'
    lastname = 'Lname4578'
    body = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": 100,
        "depositpaid": 'true',
        "bookingdates": {
            "checkin": '2009-02-02',
            "checkout": '2009-03-03'
        },
        "additionalneeds": 'none'
    }
    resp = Client.create_booking(gconfig,body=body)
    assert resp.status_code == 200
    json_object = json.loads(resp.text)
    bookingid = json_object.get('bookingid')
    url = gconfig.build_item_url('booking', bookingid)
    resp_get_booking = gconfig.conn.get(url)
    assert resp_get_booking.status_code == 200
    get_booking_details = json.loads(resp_get_booking.text)
    assert get_booking_details.get('firstname') == firstname
