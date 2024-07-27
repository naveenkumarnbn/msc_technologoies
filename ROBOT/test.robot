*** Settings ***
Documentation    TO LEARN ROBOT FRAMEWORK

*** Variables ***
${NAME}    SRIRAM
${EID}     234

*** Test Cases ***
Print Name
    Log To Console    ${NAME}

Tescase-2
    Log    ${EID}    WARN