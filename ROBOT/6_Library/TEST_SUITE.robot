*** settings ***
Documentation   To know how to import library files

Library    common_library.py

*** Test Cases ***
Calling Python Function
    Emp Details
    ${R}    Get Value    RRR
    Log    RETURN VALUE :: ${R}    WARN





