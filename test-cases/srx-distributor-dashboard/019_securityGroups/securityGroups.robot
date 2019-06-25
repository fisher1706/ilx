*** Settings ***
Suite Setup                         Preparation
Suite Teardown                      Finish Suite
Library                             SeleniumLibrary
Library                             String
Resource                            ../../../resources/resource.robot
Resource                            ../../../resources/testData.robot

*** Variable ***
${edit security group}              auto-edit-security-group

*** Test Cases ***
Invalid Create New Security Group
    Click Element                   xpath:${button info}
    Is Create Security Group
    Press Key                       id:name_id                 \ue004
    Element Should Be Visible       css:.fa-exclamation-circle > path:nth-child(1)
    Click Element                   xpath:${button close}
    Sleep                           1 second

Valid Create New Security Group
    Click Element                   xpath:${button info}
    Is Create Security Group
    ${security group}               Generate Random Name L
    Set Suite Variable              ${security group}
    Input Text                      id:name_id                  ${security group}
    Click Element                   xpath:${button modal dialog ok}

Checking New Security Group
    Sleep                           5 second
    Element Text Should Be          xpath:(${table xpath})[2]/tbody/tr[${number of new row}]/td[1]          ${security group}

Create User With New Security Group
    [Tags]                          Test
    Goto Sidebar Users
    Click Element                   id:users-tab-users
    Click Element                   xpath:${users pane users}${button info}
    Input Text                      id:email_id                 ${security user email}
    Input Text                      id:firstName_id             ${user first name}
    Input Text                      id:lastName_id              ${user last name}
    Click Element                   css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)
    Choose From Select Box          ${select control}           ${security group}
    Click Element                   xpath:${button modal dialog ok}
    Sleep                           4 second
    ${number of row u}              Get Rows Count                  ${users pane users}${table xpath}
    Set Suite Variable              ${number of row u}

Checking New User
    [Tags]                          Test
    Sleep                           5 second
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of row u}]/td[1]/div      ${security user email}
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of row u}]/td[2]/div      ${user first name}
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of row u}]/td[3]/div      ${user last name}
    Element Text Should Be          xpath:${users pane users}${table xpath}/tbody/tr[${number of row u}]/td[5]/div      ${security group}

Try To Delete Security Group
    Goto Sidebar Security Groups
    Click Element                   ${delete group button}
    Sleep                           1 second
    Click Element                   xpath:${button close}
    Sleep                           2 second
    Click Element                   ${delete group button}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td     ${security group}
    Click Element                   css:button.btn:nth-child(2)
    Element Should Be Visible       css:.external-page-alert > br:nth-child(3)
    Page Should Contain             Can't delete SecurityGroup with inner relationships.
    Click Element                   css:.modal-footer > button:nth-child(1)
    Sleep                           2 second
    Goto Sidebar Users
    Click Element                   id:users-tab-users

Delete User
    [Tags]                          Test
    Click Element                   xpath:${users pane users}${table xpath}/tbody/tr[${number of row u}]/td[6]/div/div[2]/button
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td[1]          ${security user email}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td[2]          ${user first name}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td[3]          ${user last name}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td[5]          ${security group}
    Click Element                   css:button.btn:nth-child(2)
    Sleep                           5 second
    Goto Sidebar Security Groups

Edit Security Group
    Click Element                   ${edit group button}
    Is Edit Security Group
    Click Element                   xpath:${button close}
    Click Element                   ${edit group button}
    Is Edit Security Group
    Input Text                      id:name_id                  ${edit security group}
    Set Permission                  2           1
    Set Permission                  3           1
    Click Element                   xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div[2]/ul/li[2]/a
    Set Settings Permission         2           1
    Click Element                   xpath:${button modal dialog ok}
    
Checking Edit Security Group
    Sleep                           5 second
    Element Text Should Be          xpath:(${table xpath})[2]/tbody/tr[${number of new row}]/td[1]      ${edit security group}
    Click Element                   ${edit group button}
    ${checked}                      Get Permission      2       1
    Run Keyword If                  "${checked}"=="true"        Log To Console      Pass    ELSE    Fail Fail
    ${checked}                      Get Permission      3       1
    Run Keyword If                  "${checked}"=="true"        Log To Console      Pass    ELSE    Fail Fail
    Click Element                   xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div[2]/ul/li[2]/a
    ${checked}                      Get Settings Permission      2       1
    Run Keyword If                  "${checked}"=="true"        Log To Console      Pass    ELSE    Fail Fail
    Click Element                   css:.modal-dialog-cancel-button

Delete Security Group
    Click Element                   ${delete group button}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td     ${edit security group}
    Click Element                   css:button.btn:nth-child(2)
    Sleep                           7 second

Sorting Security Groups
    [Tags]                          Sorting
    Click Element                   xpath:(${header xpath})[2]/thead/tr/th[1]
    ${text buffer1up}               Get Text                    xpath:(${table xpath})[2]/tbody/tr[1]/td[1]
    ${text buffer1down}             Get Text                    xpath:(${table xpath})[2]/tbody/tr[${number of row}]/td[1]
    Click Element                   xpath:(${header xpath})[2]/thead/tr/th[1]
    ${text buffer2up}               Get Text                    xpath:(${table xpath})[2]/tbody/tr[1]/td[1]
    ${text buffer2down}             Get Text                    xpath:(${table xpath})[2]/tbody/tr[${number of row}]/td[1]
    Run Keyword If                  "${text buffer1up}"!="${text buffer2down}"          Log To Console      Sorting 1 is failed
    Run Keyword If                  "${text buffer1down}"!="${text buffer2up}"          Log To Console      Sorting 1 is failed
    Click Element                   xpath:(${header xpath})[2]/thead/tr/th[1]

Filter Security Groups
    [Tags]                          Filter
    Click Element                   css:.button-right-margin
    Input Text                      css:.form-control           Static Group
    Click Element                   css:button.btn:nth-child(2)
    Sleep                           5 second
    Element Text Should Be          xpath:(${table xpath})[2]/tbody/tr/td[1]     Static Group
    ${number of row}                Get Rows Count              (${table xpath})[2]
    Should Be Equal                 "${number of row}"      "1"

*** Keywords ***
Preparation
    Start Distributor
    Sleep                           2 second
    Goto Sidebar Security Groups
    Sleep                           2 second
    ${buffer}                       Generate Random Name L  10
    Set Suite Variable              ${security user email}   distributor.${buffer}@example.com
    ${number of row}                Get Rows Count              (${table xpath})[2]
    ${number of new row}=           Evaluate                    ${number of row}+1
    Set Suite Variable              ${number of row}
    Set Suite Variable              ${number of new row}
    Set Suite Variable              ${edit group button}        xpath:(${table xpath})[2]/tbody/tr[${number of new row}]${button success}
    Set Suite Variable              ${delete group button}      xpath:(${table xpath})[2]/tbody/tr[${number of new row}]${button danger}

Is Create Security Group
    Element Text Should Be          css:.modal-title            Create new custom security group

Is Edit Security Group
    Element Text Should Be          css:.modal-title            Edit custom security group

Set Permission
    [Arguments]                     ${row}      ${column}
    Click Element                   xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div[2]/div/div[1]/div/table/tbody/tr[${row}]/td[${column}+1]/label/input

Set Settings Permission
    [Arguments]                     ${row}      ${column}
    Click Element                   xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div[2]/div/div[2]/div/table/tbody/tr[${row}]/td[${column}+1]/label/input

Get Permission
    [Arguments]                     ${row}      ${column}
    ${checked}                      Get Element Attribute       xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div[2]/div/div[1]/div/table/tbody/tr[${row}]/td[${column}+1]/label/input     checked
    Return From Keyword             ${checked}

Get Settings Permission
    [Arguments]                     ${row}      ${column}
    ${checked}                      Get Element Attribute       xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/div/form/div[2]/div/div[2]/div/table/tbody/tr[${row}]/td[${column}+1]/label/input     checked
    Return From Keyword             ${checked}
