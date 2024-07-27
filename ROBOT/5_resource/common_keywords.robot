*** settings ***
Documentation   This file is used to make math operations

*** Keywords ***
Addition    [Arguments]    ${A}    ${B}
    ${R}    Evaluate    ${A} + ${B}
    Log     SUM OF ${A} + ${B} = ${R}    WARN

Multiplication
    [Documentation]   This keyword used to MUL 2 numbers
    ${RES}    Evaluate    5 * 5
    Log    MUL OF 5 * 5 = ${RES}    WARN