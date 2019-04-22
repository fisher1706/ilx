*** Settings ***
Suite Setup                         Preparation
Suite Teardown                      Finish Suite
Library                             SeleniumLibrary
Resource                            ../../../resources/resource.robot
Resource                            ../../../resources/testData.robot

*** Test Cases ***
Valid Create New Customer Type
    Set Suite Variable              ${right size}                   ${number of row}
    Click Element                   xpath:${button info}
    Input Text                      id:name_id                      ${test del type}
    Click Element                   xpath:${button modal dialog ok}
    Sleep                           5 second

Checking New Customer Type On Distributor Portal Not Delete
    [Tags]                          CheckingOnDistributorPortal
    Goto Customer Menu Sub
    Click Element                   xpath:(${react table raw})[1]
    Select From Dropdown            (${dropdown menu})[1]       ${test del type}
    Click Element                   xpath:${button submit}
    Goto Sidebar Customers
    Element Text Should Be          xpath:((${react table raw})[1]${react table column})[4]     ${test del type}
    Finish Suite

Delete Customer Type Not Delete
    Sleep                           5 second
    Preparation
    Click Element                   ${delete button}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td[2]         ${test del type}
    Click Element                   xpath:${modal dialog}${button danger}
    Element Text Should Be          css:.external-page-alert > strong:nth-child(2)              Operation failed!
    Click Element                   css:.modal-footer > button:nth-child(1)
    Sleep                           5 second

Checking New Customer Type On Distributor Portal Delete
    [Tags]                          CheckingOnDistributorPortal
    Goto Customer Menu Sub
    Click Element                   xpath:(${react table raw})[1]
    Select From Dropdown            (${dropdown menu})[1]       Not specified
    Click Element                   xpath:${button submit}
    Goto Sidebar Customers
    Element Text Should Be          xpath:((${react table raw})[1]${react table column})[4]     Not specified
    Finish Suite

Delete Customer Type Delete
    Sleep                           5 second
    Preparation
    Click Element                   ${delete button}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td[2]     ${test del type}
    Click Element                   xpath:${modal dialog}${button danger}
    Sleep                           5 second
    ${current size}                 Get Element Count                   xpath:${table xpath}/tbody/tr
    Run Keyword If                  ${current size}==${right size}      Pass Execution      Pass    ELSE        Fail    Fail

*** Keywords ***
Goto Customer Menu Sub
    Finish Suite
    Start Distributor
    Sleep                           5 second
    Goto Sidebar Customers
    Sleep                           5 second

Preparation
    Start Admin
    Sleep                           5 second
    Click Link                      xpath://*[@href="/customer-types"]
    Sleep                           1 second
    ${number of row}                Get Rows Count          ${table xpath}
    ${number of new row}=           Evaluate                ${number of row}+1
    Set Suite Variable              ${number of new row}
    Set Suite Variable              ${number of row}
    Set Suite Variable              ${edit button}          xpath:${table xpath}/tbody/tr[${number of row}]${button success}
    Set Suite Variable              ${delete button}        xpath:${table xpath}/tbody/tr[${number of row}]${button danger}