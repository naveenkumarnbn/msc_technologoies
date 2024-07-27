***Settings***
Documentation    To know how to do scalar oparations

***Variables***
${EMP_NAME} =    BABU 
${EID}    123
***Test cases***
Test case1:
    Log To Console    ${EMP_NAME}
	Log To Console    ${EID}
	
Test case:2
    Log    ${EMP_NAME}    WARN
    Log    ${EID}    ERROR	
 