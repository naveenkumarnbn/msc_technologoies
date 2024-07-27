*** Settings ***
Documentation    Provides a set of often needed generic keywords. Always automatically available without imports

Library    BuiltIn

*** Variables ***
${name}    SRIRAM

*** Test Cases ***
Testcase:1
     #Log To Console    ${name}
     #Log    Name is = ${name}    WARN
     #Run Keyword If    3 == 3    Log    IF    ERROR
     #Continue For Loop If    2 == 2    Log   SRIRAM    WARN
     #Exit For Loop If        2 == 2    Log   SRIRAM    WARN
     Sleep    5s
     Repeat Keyword    5    Log   SRIRAM    WARN


