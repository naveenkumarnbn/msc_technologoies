*** Settings ***
Documentation    To know how to create keywords

*** Test Cases ***
testcase:2
    Addition    99    100
    Addition    55    1000

*** Keywords ***
Addition    [Arguments]    ${A}    ${B}
    [Documentation]   Keyword with arguments
    ${R}    Evaluate    ${A} + ${B}
    Log     Addition OF ${A} + ${B} = ${R}    WARN




