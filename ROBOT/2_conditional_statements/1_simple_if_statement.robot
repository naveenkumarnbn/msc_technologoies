*** Settings ***
Documentation    To know how to do conditional operations

*** Test Cases ***
If Statement
    Run Keyword If    2 == 2    Add


*** Keywords ***
Add
    ${r}    Evaluate    45 + 5
    Log     SUM of 45 + 5 is ==> ${r}    ERROR