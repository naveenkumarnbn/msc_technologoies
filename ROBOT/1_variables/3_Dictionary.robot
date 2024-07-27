*** Settings ***
Documentation   To know how to do Dictionary operations

*** Variables ***
&{EMP_DET}    name=kumar    eid=345    dname=IT


*** Test Cases ***
Dict Operations
    #Log    ${EMP_DET}    WARN
    Log    ${EMP_DET}[name]    WARN


