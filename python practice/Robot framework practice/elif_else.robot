***Settings***
Documentation    To know how do the conditional statements

***Test cases***
If and Else Statements
    Run Keyword If   5 >= 6    Add
    ...   ELSE IF    3 == 3    Log    FIRST ELIF    WARN
    ...   ELSE IF    3 >= 6    Log    Second Elif   WARN
    ...   ELSE                 Log    Else block is     ERROR

*** Keywords ***
Add
    ${r}    Evaluate    190 + 5
    Log     SUM of 190 + 5 is ==> ${r}    ERROR

***Settings***
Documentation    To know how to do conditinal statements

***Test cases***
If and Else statements
    Run keyword If    10 >= 12    Add
    Else If    3==3  Log    first elif    warn
    else  	