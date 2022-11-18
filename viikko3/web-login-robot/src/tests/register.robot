*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Register

*** Test Cases ***
Register With Valid Username And Password
    Set Username  luketheduke
    Set Password  luketheduke1
    Set Password Confirmation  luketheduke1
    Submit Register Credentials
    Registration Should Succeed
# ...

Register With Too Short Username And Valid Password
    Set Username  x
    Set Password  luketheduke1
    Set Password Confirmation  luketheduke1
    Submit Register Credentials
    Registration Should Fail With Message  Username must be min 3 characters long.

# ...

Register With Valid Username And Too Short Password
    Set Username  luketheduke
    Set Password  Luke
    Set Password Confirmation  Luke
    Submit Register Credentials
    Registration Should Fail With Message  Password must be min 8 characters long.


# ...

Register With Nonmatching Password And Password Confirmation
    Set Username  luketheduke
    Set Password  LukeTheDuke
    Set Password Confirmation  ekuDetHekuL
    Submit Register Credentials
    Registration Should Fail With Message  Passwords don't match!
# ...

Login After Successful Registration
    Set Username  lukethedukeee
    Set Password  luketheduke123
    Set Password Confirmation  luketheduke123
    Submit Register Credentials
    Registration Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  lukethedukeee
    Set Password  luketheduke123
    Submit Login Credentials
    Login Should Succeed
# ...

Login After Failed Registration
    Set Username  x
    Set Password  luketheduke1
    Set Password Confirmation  luketheduke1
    Submit Register Credentials
    Registration Should Fail
    Go To Login Page
    Login Page Should Be Open
    Set Username  x
    Set Password  luketheduke1
    Submit Login Credentials
    Login Should Fail
# ...
