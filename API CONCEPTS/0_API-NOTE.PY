# What is API?
API  : API stands for Application Programming Interface which allows software applications to communicate with each other via API calls.

# EXAMPLE
AMAZON ==> Phonepay
           Gpay
           paytm
           SBI
           HDFC
           CITI
           ICICI

# NEED TO ENTER BELOW DETAILS IN AMAZON WEBSITE TO DO PAYMENT 
# THEN THIS DETAILS AMAZON SEND TO SBI BANK
D = {BANK NAME : SBI
    CARD NAME : SRIRAM
    CARD NUMBER : 854837
    CVV      : 345
    AMOUNT   : 1000
    EXP DATE : 2025
    }

# SBI WILL VALIDATE THIS DETAILS AND SEND OTP TO MOBILE NUMBER WHICH IS LIKED FOR THAT ACCOUNT
D = {OTP:3456}

# NEED ENTER OTP IN AMAZON WEBSITE THEN AMAZON WILL SEND THIS OTP TO THE SBI
# THEN SBI VALIDATE THIS OTP AND TRANSFOR AMOUNT TO AMZON ACCOUNT
D = {OTP:3456}

#  What are the main HTTP Methods(API CALLS)?
GET       ==> Used to get information from web server
POST      ==> Used to create new record in web server
PUT       ==> used to update existing record in web server
DELETE    ==> Used to remove record in web servers

## Follow Below steps to do API testing 

    # 1. Install Below two required modules using below commands
        python -m pip install flask
        python -m pip install requests


    # 2. Run Flask script like below then " don't close command prompt "
        python 1_server_side_script_flask.py


# IMP STATUS CODES
    200 --> SUCCESS
    201 --> CREATE
    400 --> Bad Request
    401 --> Unauthorized
    404 --> NOT FOUND
    405 --> Method Not Allowed
    500 --> Internal Server Error

# What is JSON ?
    JSON stands for JavaScript Object Notation
    JSON is a lightweight format for storing and transporting data