*** Settings ***
Suite Setup                         Preparation
Suite Teardown                      Finish Suite
Library                             SeleniumLibrary
Resource                            ../../../resources/resource.robot
Resource                            ../../../resources/testData.robot

*** Test Cases ***
Valid Add Admin User
    [Tags]                          ContentSuperUser                ValidAddAdminUser
    Set Suite Variable              ${const number admin}           ${number of row}
    Click Element                   id:distributor-details-tab-2
    Sleep                           2 second
    Click Element                   xpath:${distributors admin pane}${button primary}
    Is Add User
    Input Text                      id:email_id                     ${admin email}
    Input Text                      id:firstName_id                 ${admin first}
    Input Text                      id:lastName_id                  ${admin last}
    Click Element                   css:.modal-dialog-ok-button

Checking New User
    [Tags]                          ContentSuperUser
    Sleep                           5 second
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of new row}]/td[1]/div       ${admin email}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of new row}]/td[2]/div       ${admin first}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of new row}]/td[3]/div       ${admin last}

Checking User On Distributor Portal
    [Tags]                          ContentSuperUser
    Goto Users Sub
    ${const number distributor}     Evaluate                ${number of row u}-1
    Set Suite Variable              ${const number distributor}
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of row u}]/td[1]/div                ${admin email}
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of row u}]/td[2]/div                ${admin first}
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of row u}]/td[3]/div                ${admin last}

Edit From Distributor Portal
    [Tags]                          ContentSuperUser
    Click Element                   xpath:${users pane super users}${table xpath}/tbody/tr[${number of row u}]/td[4]/div/div[1]/button
    Input Text                      id:firstName_id             ${edit admin first}
    Input Text                      id:lastName_id              ${edit admin last}
    Click Element                   css:.modal-dialog-ok-button

Checking Edit User From Distributor Portal
    [Tags]                          ContentSuperUser
    Sleep                           5 second
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of row u}]/td[1]/div            ${admin email}
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of row u}]/td[2]/div            ${edit admin first}
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of row u}]/td[3]/div            ${edit admin last}
    Finish Suite
    Sleep                           5 second

Checking Edit User On Admin Portal
    [Tags]                          ContentSuperUser
    Preparation
    Click Element                   id:distributor-details-tab-2
    Sleep                           2 second
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of row}]/td[1]/div       ${admin email}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of row}]/td[2]/div       ${edit admin first}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of row}]/td[3]/div       ${edit admin last}

Edit From Admin Portal
    [Tags]                          ContentSuperUser
    Click Element                   id:distributor-details-tab-2
    Sleep                           2 second
    Click Element                   ${edit user button}
    Input Text                      id:firstName_id         ${admin first}
    Input Text                      id:lastName_id          ${admin last}
    Click Element                   css:.modal-dialog-ok-button 

Checking Edit User From Admin Portal
    [Tags]                          ContentSuperUser
    Sleep                           5 second
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of row}]/td[1]/div       ${admin email}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of row}]/td[2]/div       ${admin first}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of row}]/td[3]/div       ${admin last}

Checking Edit User On Distributor Portal
    [Tags]                          ContentSuperUser
    Goto Users Sub
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of row u}]/td[1]/div            ${admin email}
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of row u}]/td[2]/div            ${admin first}
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of row u}]/td[3]/div            ${admin last}

Delete User From Distributor Portal
    [Tags]                          ContentSuperUser
    Click Element                   xpath:${users pane super users}${table xpath}/tbody/tr[${number of row u}]/td[4]/div/div[2]/button
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[1]            ${admin email}
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]            ${admin first}
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[3]            ${admin last}
    Click Element                   css:button.btn:nth-child(2)
    Sleep                           2 second

Checking Users Number On Distributor Portal After Delete From Distributor Portal
    [Tags]                          ContentSuperUser
    ${number of row u}              Get Rows Count                  ${users pane super users}${table xpath}
    Run Keyword If                  ${number of row u}==${const number distributor}     Log To Console      Pass    ELSE    Fail    Fail
    Finish Suite
    Sleep                           5 second

Checking Users Number On Admin Portal After Delete From Distributor Portal
    [Tags]                          ContentSuperUser
    Preparation
    Click Element                   id:distributor-details-tab-2
    ${number of row}                Get Rows Count          ${table xpath}
    Run Keyword If                  ${number of row}==${const number admin}     Log To Console      Pass    ELSE    Fail    Fail

Delete User From Admin Portal
    [Tags]                          ContentSuperUser
    Sleep                           2 second
    Click Element                   xpath:${distributors admin pane}${button primary}
    Is Add User
    Input Text                      id:email_id             ${admin email}
    Input Text                      id:firstName_id         ${admin first}
    Input Text                      id:lastName_id          ${admin last}
    Click Element                   css:.modal-dialog-ok-button
    Sleep                           5 second
    ${number of row}                Get Rows Count          ${table xpath}
    Click Element                   xpath:${table xpath}/tbody/tr[${number of row}]/td[4]/div/div[2]/button
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[1]            ${admin email}
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]            ${admin first}
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[3]            ${admin last}
    Click Element                   css:button.btn:nth-child(2)
    Sleep                           2 second

Checking Users Number On Admin Portal After Delete From Admin Portal
    [Tags]                          ContentSuperUser
    Click Element                   id:distributor-details-tab-2
    ${number of row}                Get Rows Count          ${table xpath}
    Run Keyword If                  ${number of row}==${const number admin}     Log To Console      Pass    ELSE    Fail    Fail

Checking Users Number On Distributor Portal After Delete From Admin Portal
    [Tags]                          ContentSuperUser
    Goto Users Sub
    ${number of row}                Get Rows Count          ${table xpath}
    Run Keyword If                  ${number of row u}==${const number distributor}     Log To Console      Pass    ELSE    Fail    Fail
    Finish Suite
    Sleep                           5 second

Create Admin On Distributor Portal
    [Tags]                          AddSuperUser
    Goto Users Sub
    Sleep                           2 second
    Click Element                   xpath:${users pane super users}${button primary}
    Input Text                      id:email_id                         ${admin email}
    Input Text                      id:firstName_id                     ${admin first}
    Input Text                      id:lastName_id                      ${admin last}
    Click Element                   css:.modal-dialog-ok-button
    Sleep                           3 second
    Set Suite Variable              ${const number distributor 2}       ${number of row u}
    ${number of new row u}          Evaluate                            ${number of row u}+1
    Set Suite Variable              ${number of new row u}

Checking Admin On Distributor Portal
    [Tags]                          AddSuperUser
    Sleep                           5 second
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of new row u}]/td[1]/div            ${admin email}
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of new row u}]/td[2]/div            ${admin first}
    Element Text Should Be          xpath:${users pane super users}${table xpath}/tbody/tr[${number of new row u}]/td[3]/div            ${admin last}

Edit Admin From Distributor Portal
    [Tags]                          ContentSuperUser
    Click Element                   xpath:${table xpath}/tbody/tr[${number of new row u}]/td[4]/div/div[1]/button
    Input Text                      id:firstName_id             ${edit admin first}
    Input Text                      id:lastName_id              ${edit admin last}
    Click Element                   css:.modal-dialog-ok-button
    Sleep                           5 second
    Finish Suite
    Sleep                           3 second

Checking Admin On Admin Portal
    [Tags]                          AddSuperUser
    Preparation
    ${const number admin 2}         Evaluate                            ${number of row}-1
    Set Suite Variable              ${const number admin 2}
    Click Element                   id:distributor-details-tab-2
    Sleep                           2 second
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of row}]/td[1]/div       ${admin email}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of row}]/td[2]/div       ${edit admin first}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${number of row}]/td[3]/div       ${edit admin last}

Delete Admin
    [Tags]                          AddSuperUser
    ${number of row}                Get Rows Count          ${table xpath}
    Click Element                   xpath:${table xpath}/tbody/tr[${number of row}]/td[4]/div/div[2]/button
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[1]            ${admin email}
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]            ${edit admin first}
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[3]            ${edit admin last}
    Click Element                   css:button.btn:nth-child(2)
    Sleep                           2 second

Checking Admins Number On Admin Portal After Delete From Admin Portal
    [Tags]                          AddSuperUser
    Click Element                   id:distributor-details-tab-2
    ${number of row}                Get Rows Count          ${table xpath}
    Run Keyword If                  ${number of row}==${const number admin 2}     Log To Console      Pass    ELSE    Fail    Fail

Checking Admins Number On Distributor Portal After Delete From Admin Portal
    [Tags]                          AddSuperUser
    Goto Users Sub
    ${number of row u}              Get Rows Count                  ${users pane super users}${table xpath}
    Run Keyword If                  ${number of row u}==${const number distributor 2}     Log To Console      Pass    ELSE    Fail    Fail
    Finish Suite
    Sleep                           5 second

*** Keywords ***
Preparation
    Goto Admin Users Sub
    ${number of row}                Get Rows Count          ${table xpath}
    ${number of new row}=           Evaluate                ${number of row}+1
    Set Suite Variable              ${number of row}
    Set Suite Variable              ${number of new row}
    Set Suite Variable              ${edit user button}     xpath:${table xpath}/tbody/tr[${number of row}]/td[4]/div/div[1]/button
    Set Suite Variable              ${delete user button}   xpath:${table xpath}/tbody/tr[${number of row}]/td[4]/div/div[2]/button
    ${SUB HOST}                     Return Sub Link
    Set Suite Variable              ${SUB HOST}
    ${SUB EMAIL}                    Return Sub Email
    Set Suite Variable              ${SUB EMAIL}
    
Goto Users Sub
    Finish Suite
    Run Keyword If                  "${browser}"=="xvfb"            Run Xvfb Sub    ELSE IF     "${browser}"=="chrome"      Run Chrome Sub      ELSE    Run Ff Sub
    Set Selenium Implicit Wait                                      20 second
    Set Selenium Timeout                                            10 second
    Enter Correct Email Sub
    Enter Password
    Correct Submit Login
    Sleep                           7 second
    Click Link                      xpath://*[@href="/users"]
    Sleep                           1 second
    Click Element                   id:users-tab-super-users
    Sleep                           2 second
    ${number of row u}              Get Rows Count                  ${users pane super users}${table xpath}
    Set Suite Variable              ${number of row u}

Goto Admin Users Sub
    Login In Admin Portal
    Sleep                           7 second
    Click Element                   css:#pageDropDown
    Click Element                   css:li.dropdown-item:nth-child(4)
    Sleep                           2 second
    ${static distributor}           Get Row By Text         ${table xpath}      1       Srx-group-test-distributor
    Click Element                   xpath:${table xpath}/tbody/tr[${static distributor}]/td[1]/a

Is Delete User
    Element Text Should Be          css:.modal-title                                    Removal Confirmation

Is Edit User
    Element Text Should Be          css:.modal-title                                    Edit user

Is Add User
    Element Text Should Be          css:.modal-title                                    Add user