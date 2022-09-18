import pytest
import requests
import json
import pytest_check as check
from pytest_check import check_func
import auto.common.httprestclient as Client
import auto.utils.excel_util as XLutil

def test_createbooking(gconfig):
    resp = Client.create_booking(gconfig)
    assert resp.status_code == 200
    json_obj = resp.json()
    booking_id = json_obj['bookingid']
    assert booking_id > 0

def test_createbooking_data(gconfig):
    data_path = "data/auth_data.xlsx"
    sheet_name = "booking_data"
    rows = XLutil.getRowCount(data_path,sheet_name)
    for row in range(2,rows+1):
        print()
        print("*********** Test Data for Row -> ", row)
        firstname = XLutil.readData(data_path,sheet_name,row,1)
        lastname = XLutil.readData(data_path,sheet_name,row,2)
        totalprice = XLutil.readData(data_path,sheet_name,row,3)
        depositpaid = XLutil.readData(data_path,sheet_name,row,4)
        checkin = XLutil.readData(data_path,sheet_name,row,5)
        checkout = XLutil.readData(data_path,sheet_name,row,6)
        additionalneeds = XLutil.readData(data_path,sheet_name,row,7)
        expected_result = XLutil.readData(data_path,sheet_name,row,8)

        body = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }

        resp = Client.create_booking(gconfig,body)
        status_code= resp.status_code
        json_obj = resp.json()
        booking_id = json_obj['bookingid']
        is_200(status_code)
        is_bookingid(booking_id)

@check_func
def is_200(status_code):
    assert status_code == 200

@check_func
def is_bookingid(id):
    assert id > 0
