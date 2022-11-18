*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***
Go To Register Page And Register
    Go To Register Page
    Register Page Should Be Open

Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Register Page Should Be Open
    Title Should Be  Register

Login Page Should Be Open
    Title Should Be  Login

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Go To Register Page
    Go To  ${REGISTER URL}

Go To Main Page
    Go To  ${HOME URL}

Go To Login Page
    Go To  ${LOGIN URL}

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Registration Should Fail With Message
    [Arguments]   ${message}
    Register Page Should Be Open
    Page Should Contain   ${message}

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail
    Login Page Should Be Open
