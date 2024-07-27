*** Settings ***
Documentation    Loop operations using range function


*** Test Cases ***
Test For Loop
    FOR    ${k}    IN RANGE    10    21    3
        log    ${k}    WARN
    END

