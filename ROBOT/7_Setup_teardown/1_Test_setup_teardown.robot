*** Settings ***
Documentation    To know how to use setup and teardown options

*** Test Cases ***
Testcase1
    [Setup]    Log    SETUP FOR FIRST TEST CASE    WARN
    Log    Test Case : 1    ERROR
    [Teardown]    Log    TEARDOWN FOR FIRST TEST CASE    WARN

Testcase2
    [Teardown]    Log    TEARDOWN FOR SECOND TEST CASE    WARN
    [Setup]    Log    Setup FOR SECOND TEST CASE    WARN
    Log    Test Case : 2   ERROR




