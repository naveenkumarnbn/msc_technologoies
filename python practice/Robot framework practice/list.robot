***Settings***
Documentation    To know how to da list oparations

***Variables***
@{NAMES}    RAMESH    RAMU    1234    BHAVANA    RRR    

***Test cases***
List oparations
    Log    LIST VALUES ARE : ${NAMES}    ERROR
    Log    ${NAMES}[-3]    WARN
