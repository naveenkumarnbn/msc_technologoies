*** Settings ***
Documentation    To know how to do scalar operations

*** Variables ***
${EMP_NAME} =    SRIRAM
${EID}    123

*** Test Cases ***
Testcase:1
    Log To Console    ${EMP_NAME}
    Log To Console    ${EID}

Testcase:2
    Log    ${EMP_NAME}    WARN
    Log    ${EID}    ERROR
