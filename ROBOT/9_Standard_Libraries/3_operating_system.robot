*** Settings ***
Documentation   *  Enables various operating system related tasks to be performed in the system where Robot Framework is running. *

Library    OperatingSystem

*** Test Cases ***
#First Test Case
    #Create Directory    LOG
    #Create File     LOG/log_file.txt
    #File Should Exist    LOG/log_file.txt    Please create a log_file.txt
    #Remove File    LOG/log_file.txt
    #Remove Directory    LOG


Run System Command
    ${r}    Run    dir
    Log    ${r}    WARN







