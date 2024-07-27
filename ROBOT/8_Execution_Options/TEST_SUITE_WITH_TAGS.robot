*** settings ***
Documentation   Using tags we can run group of test cases based on tag name

*** Test Cases ***
Testcase:1
    [Tags]    windows
    Log    WIN TestCase 1    ERROR

Testcase:2
    [Tags]    Linux
    Log    Linux TestCase 2    ERROR

Testcase:3
    [Tags]    windows
    Log    WIN TestCase 3    ERROR

Testcase:4
    [Tags]    MAC
    Log    MAC TestCase 4    ERROR

Testcase:5
    [Tags]    Linux
    Log    Linux TestCase 5    ERROR
