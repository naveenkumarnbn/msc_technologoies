*** Settings ***
Documentation    To know how to use setup and teardown options

Suite Setup       Log    SUITE SETUP       ERROR
Suite Teardown    Log    SUITE TEARDOWN    ERROR

*** Test Cases ***
Testcase1
    Log    Test Case 1   ERROR
    [Teardown]    Log    TEARDOWN FOR FIRST TEST CASE    WARN
    [Setup]    Log    SETUP FOR FIRST TEST CASE    WARN

Testcase2
    [Setup]    Log    SETUP FOR SECOND TEST CASE    WARN
    Log    Test Case 2   ERROR
    [Teardown]    Log    TEARDOWN FOR SECOND TEST CASE    WARN



