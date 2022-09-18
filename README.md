##Setup

###Install Python
Install python version 3.x from
[Python](https://www.python.org/)

###Setting up virtual environment
TBD

####Install python modules
Run 
`pip install -r requirements.txt`

###Install PyCharm/VSCode
TBD

##Application under test
https://restful-booker.herokuapp.com/apidoc/index.html

##How to Run Testcases
###Running all testcases/testsuites
pytest  -v --html .\reports\report.html  --disable-warnings auto\testsuites\

###Running spcific testsuite
pytest  -v --html .\reports\report.html  --disable-warnings auto\testsuites\test_create_booking.py

#TBD
Logging