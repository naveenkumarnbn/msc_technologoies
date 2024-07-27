*** Settings ***
Documentation    Exit For Loop If


*** Test Cases ***
For Loop with list
    FOR    ${V}    IN RANGE    1    11
        log    ${V}    WARN
        Exit For Loop If    ${V} == 7
    END