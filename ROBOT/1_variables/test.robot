*** Settings ***
Documentation     To do robot framework operations


*** Variables ***
${name} =    SRIRAM
${EID}    333

*** Test Cases ***
Print Ename
    Log To Console    ${name}
    Log To Console    ${EID}

Print Eid
    Log    ${name}    WARN
    Log    ${EID}    ERROR

