*** Settings ***
Documentation    To know how to create keywords

*** Test Cases ***
testcase:1
    Addition
    Multiplication

*** Keywords ***
Addition
    [Documentation]    This keyword used to add 2 numbers
    ${SUM}    Evaluate    5 + 5
    Log    SUM OF 5 + 5 = ${SUM}    WARN

Multiplication
    [Documentation]   This keyword used to MUL 2 numbers
    ${RES}    Evaluate    5 * 5
    Log    MUL OF 5 * 5 = ${RES}    WARN




