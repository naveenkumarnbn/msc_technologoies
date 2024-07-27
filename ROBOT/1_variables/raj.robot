*** Settings ***
Documentation    To know how do the dictionary oparations

*** Variables ***
&{EMP_DET}    name=raj    age=25    city=bangalore    

*** Test cases ***
dictionary oparations:
    Log    ${EMP_DET}    WARN
    Log    ${EMP_DET}[name]    ERROR
	
*** Keywords ***