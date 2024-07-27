
***Settings***
Documentation    Loop oparations using list

***Variables***
@{names}    babu    mahesh    sunil    harish    suresh

***Test cases***
For Loop with list
    FOR    ${I}    IN    ${names}
        Log    ${I}    WARN
    END 		
