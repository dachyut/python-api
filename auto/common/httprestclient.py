
def create_auth(gconfig,headers=None,body=None):
    url = gconfig.build_url('auth')
    headers = {
        'Content-Type': 'application/json'
    }
    if body is None:
        username = gconfig.username
        password = gconfig.password
        body = {'username': username,
                'password': password}
    response = gconfig.conn.post(url,headers=headers,json=body)
    return response

#TBD - Generate Random body data
def create_booking(gconfig,body=None):
    if body is None:
        body = {
            "firstname": "Tom",
            "lastname": "Jerry",
            "totalprice": 555,
            "depositpaid": 'true',
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Cheese"
        }
    url = gconfig.build_url('booking')
    resp = gconfig.conn.post(url,json=body)
    print(resp.text)
    return resp