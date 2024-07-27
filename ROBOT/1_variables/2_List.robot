*** Settings ***
Documentation   To know how to do list operations

*** Variables ***
@{NAMES}    sriram    RAJU    Balu    RAMESH    222

*** Test Cases ***
List Operations
    Log    LIST VALUES ARE : ${NAMES}    ERROR
    Log    ${NAMES}[-3]    WARN


