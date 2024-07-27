*** Settings ***
Documentation    Loop operations using list

*** Variables ***
@{names}     sriram    kumar    balu    nagesh

*** Test Cases ***
For Loop with list
    FOR    ${I}    IN    @{names}
        Log    ${I}    WARN
    END




