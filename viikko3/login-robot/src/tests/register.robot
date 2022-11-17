*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  testuser  testpassword12345
    Output Should Contain  Username is not available.

Register With Too Short Username And Valid Password
    Input Credentials  xd  testpassword12345
    Output Should Contain  Username must have min lenght of 3.

Register With Valid Username And Too Short Password
    Input Credentials   testuserrr  abc2
    Output Should Contain  Password must have min lenght of 8.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  luketheduke  luketheduke
    Output Should Contain  Password must not consist only of symbols from [a-z].

*** Keywords ***
Input New Command And Create User
    Input New Command 
    Create User  testuser  testpassword12345