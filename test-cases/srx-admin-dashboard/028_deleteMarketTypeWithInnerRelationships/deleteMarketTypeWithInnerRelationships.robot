*** Settings ***
Suite Setup                         Preparation
Suite Teardown                      Finish Suite
Library                             SeleniumLibrary
Resource                            ../../../resources/resource.robot
Resource                            ../../../resources/testData.robot

*** Test Cases ***
Valid Create New Market Type
    Set Global Variable             ${right size}                   ${number of row}
    Click Element                   css:.btn-primary
    Is Add Market Type
    Input Text                      id:name_id                      ${market del type}
    Click Element                   css:.modal-dialog-ok-button
    Sleep                           1 second
    Is Market Types

Checking New Market Type On Distributor Portal Not Delete
    [Tags]                          CheckingOnDistributorPortal
    Goto Customer Menu Sub
    Click Element                   ${edit customer button sub}
    Go Down
    Sleep                           1 second
    Click Element                   css:.modal-dialog-ok-button
    Sleep                           5 second
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${static row c}]/td[5]/div      ${market del type}
    Finish Suite

Delete Market Type Not Delete
    Sleep                           5 second
    Preparation
    Click Element                   ${delete button}
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]          ${market del type}
    Click Element                   css:button.btn:nth-child(2)
    Element Text Should Be          css:.external-page-alert > strong:nth-child(2)                                  Operation failed!
    Click Element                   css:.modal-footer > button:nth-child(1)
    Sleep                           5 second

Checking New Market Type On Distributor Portal Delete
    [Tags]                          CheckingOnDistributorPortal
    Goto Customer Menu Sub
    Click Element                   ${edit customer button sub}
    Go Up
    Sleep                           1 second
    Click Element                   css:.modal-dialog-ok-button
    Sleep                           5 second
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${static row c}]/td[5]/div      Not specified
    Finish Suite

Delete Market Type Delete
    Sleep                           5 second
    Preparation
    Click Element                   ${delete button}
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]          ${market del type}
    Click Element                   css:button.btn:nth-child(2)
    Sleep                           5 second
    ${current size}                 Get Element Count                   xpath:${table xpath}/tbody/tr
    Run Keyword If                  ${current size}==${right size}      Pass Execution      Pass    ELSE        Fail    Fail

*** Keywords ***
Goto Customer Menu Sub
    Finish Suite
    Run Keyword If                  "${browser}"=="xvfb"            Run Xvfb Sub    ELSE IF     "${browser}"=="chrome"      Run Chrome Sub      ELSE    Run Ff Sub
    Set Selenium Implicit Wait                                      20 second
    Set Selenium Timeout                                            10 second
    Enter Correct Email Sub
    Enter Password
    Correct Submit Login
    Click Link                      xpath://*[@href="/customers"]
    Sleep                           5 second
    Is Customer Management
    Number Of Rows Sub
    Number Of Static Row Sub
    Set Global Variable             ${edit customer button sub}     xpath:${table xpath}/tbody/tr[${static row c}]/td[6]/div/div[1]/button

Preparation
    Goto Market Types
    Sleep                           1 second
    Is Market Types
    Number Of Rows
    ${number of new row}=           Evaluate                        ${number of row}+1
    Set Global Variable             ${number of new row}
    Set Global Variable             ${edit button}                  xpath:${table xpath}/tbody/tr[${number of row}]/td[3]/div/div[1]/button
    Set Global Variable             ${delete button}                xpath:${table xpath}/tbody/tr[${number of row}]/td[3]/div/div[2]/button
    ${SUB HOST}                     Return Sub Link
    Set Global Variable             ${SUB HOST}
    ${SUB EMAIL}                    Return Sub Email
    Set Global Variable             ${SUB EMAIL}

Is Add Market Type
    Element Text Should Be          css:.modal-title                Add market type

Is Edit Market Type
    Element Text Should Be          css:.modal-title                Edit market type

Number Of Rows Sub
    ${number of row sub}            Get Element Count               xpath:${table xpath}/tbody/tr
    Set Global Variable             ${number of row sub}

Number Of Static Row Sub
    : FOR   ${counter c sub}        IN RANGE    1   ${number of row sub}+1
    \   ${text buffer1 c sub}       Get Text    xpath:${table xpath}/tbody/tr[${counter c sub}]/td[1]/a
    \   Exit For Loop If            "Customer Z"=="${text buffer1 c sub}"
    Set Global Variable             ${static row c}     ${counter c sub}

Go Down
    Click Element                   xpath:(${select control})[2]
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]            \ue015
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]            \ue007
    ${text buffer sub}              Get Text                                    xpath:(${select control})[2]/div[1]/div[1]/span
    Sleep                           1 second
    Run Keyword If                  "${text buffer sub}"!="${market del type}"        Go Down

Go Up
    Click Element                   xpath:(${select control})[2]
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]            \ue015
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]            \ue007
    ${text buffer sub}              Get Text                                    xpath:(${select control})[2]/div[1]/div[1]/span
    Sleep                           1 second
    Run Keyword If                  "${text buffer sub}"!="Not specified"       Go Down