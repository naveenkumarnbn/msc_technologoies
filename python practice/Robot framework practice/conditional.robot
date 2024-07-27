#***Settings***
#Documentation    To know how do the Conditional staements

#***Test cases***
#If satement
 #   Run keyword If    2==2    Add
	

#***Keywords***
#Add
#    ${N}    Evaluate    45 + 5
#    Log     SUM of 45 + 5 is ==> ${N}    ERROR

***Settings***
Documentations    To know how do the conditional statements

***Test cases***
If statements
    Run keyword If    90==90    sub
	
***Keywords***
sub    ${name}    Evaluate    50*50
       Log        SUM of 50*50 is==> ${name}   ERROR
	   
	