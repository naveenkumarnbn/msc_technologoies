*** Settings ***
Documentation    To know how to create keywords

*** Test Cases ***
testcase:1
    ${RV}    Addition    5    10
    Log      ${RV}    ERROR

*** Keywords ***
Addition    [Arguments]    ${A}    ${B}
    [Documentation]    Keyword with RETURN
    ${R}    Evaluate    ${A} + ${B}
    [Return]    ${R}


