*** Settings ***
Suite Setup                         Preparation
Suite Teardown                      Finish Suite
Library                             SeleniumLibrary
Library                             String
Resource                            ../../../resources/resource.robot
Resource                            ../../../resources/testData.robot

*** Variables ***
${number of new row}
${number of row}

*** Test Cases ***
Invalid Create New User
    Click Element                   xpath:${users pane users}${button info}
    Sleep                           1 second
    Click Element                   xpath:${button close}
    Sleep                           2 second
    Click Element                   xpath:${users pane users}${button info}
    Press Key                       id:email_id                 \ue004
    Element Should Be Enabled       xpath:(${modal dialog}${help block})[1]/*
    Press Key                       id:firstName_id             \ue004
    Element Should Be Visible       xpath:(${modal dialog}${help block})[2]/*
    Press Key                       id:lastName_id              \ue004
    Element Should Be Visible       xpath:(${modal dialog}${help block})[3]/*
    Press Key                       css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)         \ue004
    Element Should Be Visible       css:.red-help-block > svg:nth-child(1) > path:nth-child(1)
    Click Element                   xpath:${button modal dialog cancel}
    Sleep                           2 second

Valid Create New User
    [Tags]                          ValidCreateNewUser
    Click Element                   xpath:${users pane users}${button info}
    Input Text                      id:email_id                 ${incorrect email}
    Element Should Be Enabled       xpath:(${modal dialog}${help block})[1]/*
    Input Text                      id:email_id                 ${distributor user email}
    Input Text                      id:firstName_id             ${user first name}
    Input Text                      id:lastName_id              ${user last name}
    Click Element                   xpath:${button modal dialog ok}
    Element Should Be Enabled       css:.red-help-block > svg:nth-child(1) > path:nth-child(1)
    Click Element                   css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)
    ${warehouse}                    Get Text                    xpath:(${modal dialog}${checkbox})[1]/*
    Set Suite Variable              ${warehouse}
    Choose From Select Box          ${modal dialog}${select control}    User
    Click Element                   xpath:${button modal dialog ok}
    Sleep                           2 second
    

Checking New User
    [Tags]                          ValidCreateNewUser
    Sleep                           5 second
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of new row}]/td[1]/div      ${distributor user email}
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of new row}]/td[2]/div      ${user first name}
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of new row}]/td[3]/div      ${user last name}
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of new row}]/td[4]/div      ${warehouse}
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of new row}]/td[5]/div      User

Edit User
    [Tags]                          EditUser
    Click Element                   ${edit user button}
    Sleep                           1 second
    Click Element                   xpath:${button close}
    Sleep                           2 second
    Click Element                   ${edit user button}
    Click Element                   xpath:${button modal dialog cancel}
    Sleep                           2 second
    Click Element                   ${edit user button}
    Input Text                      id:firstName_id             ${edit first name}
    Input Text                      id:lastName_id              ${edit last name}
    Choose Last From Select Box     ${modal dialog}${select control}
    ${role}                         Get Text                    ${modal dialog}${select control}/div/div
    Set Suite Variable              ${role}
    Click Element                   css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)
    Click Element                   css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)
    Click Element                   xpath:${button modal dialog ok}
    Sleep                           2 second

Checking Edit User
    [Tags]                          EditUser
    Sleep                           5 second
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of new row}]/td[1]/div      ${distributor user email}
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of new row}]/td[2]/div      ${edit first name}
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of new row}]/td[3]/div      ${edit last name}
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of new row}]/td[5]/div      ${role}

Delete User
    [Tags]                          DeleteUser
    Click Element                   ${delete user button}
    Sleep                           1 second
    Click Element                   xpath:${button close}
    Sleep                           2 second
    Click Element                   ${delete user button}
    Click Element                   css:.modal-footer > button:nth-child(1)
    Sleep                           2 second
    Click Element                   ${delete user button}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td[1]          ${distributor user email}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td[2]          ${edit first name}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td[3]          ${edit last name}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td[5]          ${role}
    Click Element                   css:button.btn:nth-child(2)
    Sleep                           10 second

*** Keywords ***
Preparation
    Start Distributor
    Sleep                           2 second
    Goto Sidebar Security Groups
    Sleep                           3 second
    ${permission test group}        Get Row By Text     (${table xpath})[2]     1       Permissions Test
    Set Suite Variable              ${edit group button}            xpath:(${table xpath})[2]/tbody/tr[${permission test group}]${button success}
    Click Element                   ${edit group button}
    Clear All Permissions
    Set Permission                  2       1
    Click Element                   xpath:(${dialog tab})[2]
    Clear All Settings Permissions
    Click Element                   xpath:${button modal dialog ok}
    Sleep                           3 second
    Finish Suite
    Sleep                           3 second
    Start Permission
    ${buffer}                       Generate Random Name L  10
    Set Suite Variable              ${distributor user email}   distributor.${buffer}@example.com
    Goto Sidebar Users
    Click Element                   id:users-tab-users
    ${number of row}                Get Rows Count              ${users pane users}${table xpath}
    ${number of new row}=           Evaluate                    ${number of row}+1
    Set Suite Variable              ${number of row}
    Set Suite Variable              ${number of new row}
    Set Suite Variable              ${edit user button}         xpath:${users pane users}${table xpath}/tbody/tr[${number of new row}]${button success}
    Set Suite Variable              ${delete user button}       xpath:${users pane users}${table xpath}/tbody/tr[${number of new row}]${button danger}