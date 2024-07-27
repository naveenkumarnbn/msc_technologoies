*** Settings ***
Documentation   * Library for generating, modifying and verifying strings *

Library    String

*** Test Cases ***
Testcase:1
    #${name} =    Convert To Lowercase    SRIRAM
    #Log    After Converting Lowercase :: ${name}    ERROR

    #${NAME}    Remove String    srikumar    sri
    #Log    After Removing SUB STRING ==> ${NAME}    WARN

    #${NAME}    Replace String    sriramsri    sri    RRR    2
    #Log    After Replace ==> ${NAME}    WARN

    ${SPLIT}    Split String    sri=ram=kumar    
    Log    After spliting ==> ${SPLIT}    ERROR


