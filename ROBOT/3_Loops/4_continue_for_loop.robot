*** Settings ***
Documentation    Continue For Loop If


*** Test Cases ***
For Loop with list
    FOR    ${V}    IN RANGE    1    11
        Continue For Loop If    ${V} == 3
        log    ${V}    WARN
    END