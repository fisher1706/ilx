*** Settings ***
Suite Setup                         Preparation
Suite Teardown                      Finish Suite
Library                             SeleniumLibrary
Resource                            ../../../resources/resource.robot
Resource                            ../../../resources/testData.robot

*** Variables ***
${filter clear}                     css:button.button-right-margin:nth-child(2)
${filter apply}                     css:button.btn:nth-child(2)
${filter button}                    css:.filtering-options > button:nth-child(1)
${dynamic row}
${static row}
${number of row}
${edit button}
${remove button}
${text buffer1}
${text buffer2}

*** Test Cases ***
Invalid Add Distributor
    [Tags]                          InvalidAddDistributor
    Click Element                   css:.btn-primary
    Is Add Distributor
    Press Key                       id:name_id                      \ue004
    Element Should Be Visible       css:div.item-form-field:nth-child(1) > div:nth-child(2) > span:nth-child(2) > svg:nth-child(1)
    Press Key                       id:address.line1_id             \ue004
    Element Should Be Visible       css:div.item-form-field:nth-child(2) > div:nth-child(2) > span:nth-child(2) > svg:nth-child(1)
    Click Element                   xpath:(${select control})[1]
    Press Key                       xpath:(${select control})[1]/div[1]/div[2]        \ue004
    Press Key                       xpath:(${select control})[1]/div[1]/div[2]        \ue004
    Element Should Be Visible       css:div.item-form-field:nth-child(4) > div:nth-child(2) > span:nth-child(2) > svg:nth-child(1)
    Press Key                       id:address.city_id              \ue004
    Element Should Be Visible       css:div.item-form-field:nth-child(5) > div:nth-child(2) > span:nth-child(2) > svg:nth-child(1)
    Press Key                       id:invoiceEmail_id              \ue004
    Element Should Be Visible       css:div.item-form-field:nth-child(6) > div:nth-child(2) > span:nth-child(2) > svg:nth-child(1)
    Click Element                   xpath:(${select control})[2]
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]        \ue004
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]        \ue004
    Element Should Be Visible       css:div.item-form-field:nth-child(7) > div:nth-child(2) > span:nth-child(2) > svg:nth-child(1)
    Press Key                       id:address.zipCode_id           \ue004
    Element Should Be Visible       css:div.item-form-field:nth-child(8) > div:nth-child(2) > span:nth-child(2) > svg:nth-child(1)
    Click Element                   css:.close
    Is Distributors Page
    Sleep                           2 second
    Click Element                   css:.btn-primary
    Click Element                   css:.modal-dialog-cancel-button
    Is Distributors Page
    Sleep                           2 second

Valid Add Distributor
    [Tags]                          ValidAddDistributor
    Click Element                   css:.btn-primary
    Is Add Distributor
    Input Text                      id:name_id                                                                                          ${dynamic name}
    Input Text                      id:address.line1_id                                                                                 ${dynamic adress1}
    Input Text                      id:address.line2_id                                                                                 ${dynamic adress2}
    Click Element                   xpath:(${select control})[1]
    Press Key                       xpath:(${select control})[1]/div[1]/div[2]        \ue015
    Press Key                       xpath:(${select control})[1]/div[1]/div[2]        \ue007
    Input Text                      id:address.city_id                                                                                  ${dynamic city}
    Input Text                      id:invoiceEmail_id                                                                                  ${dynamic email}
    Click Element                   xpath:(${select control})[2]
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]        \ue015
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]        \ue015
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]        \ue007
    Input Text                      id:address.zipCode_id                                                                               ${dynamic code}
    Click Element                   css:.modal-dialog-ok-button

Checking New Data
    Sleep                           5 second
    Click Element                   css:#pageDropDown
    Click Element                   css:li.dropdown-item:nth-child(4) > a:nth-child(1)
    Sleep                           2 second
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${dynamic row}]/td[1]/a          ${dynamic name}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${dynamic row}]/td[3]/div        ${dynamic full adress}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${dynamic row}]/td[4]/div        Singular Billing
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${dynamic row}]/td[5]/div        ${dynamic email}

Remove Distributor
    [Tags]                          RemoveDistributor
    Click Element                   ${remove button}
    Is Delete Distributor
    Click Element                   css:.close
    Sleep                           2 second
    Is Distributors Page
    Click Element                   ${remove button}
    Is Delete Distributor
    Click Element                   css:.modal-footer > button:nth-child(1)
    Sleep                           2 second
    Is Distributors Page
    Click Element                   ${remove button}
    Table Cell Should Contain       css:table.table:nth-child(2)    2       1       ${dynamic name}	
    Table Cell Should Contain       css:table.table:nth-child(2)    2       3       ${dynamic full adress}
    Table Cell Should Contain       css:table.table:nth-child(2)    2       4       Singular Billing
    Table Cell Should Contain       css:table.table:nth-child(2)    2       5       ${dynamic email}
    Click Element                   css:button.btn:nth-child(2)
    Sleep                           2 second

Edit Distributor
    [Tags]                          EditDistributor
    Click Element                   ${edit button}
    Is Edit Distributor
    Click Element                   css:.modal-dialog-cancel-button
    Sleep                           2 second
    Is Distributors Page
    Click Element                   ${edit button}
    Is Edit Distributor
    Click Element                   css:.close
    Sleep                           2 second
    Is Distributors Page
    Click Element                   ${edit button}
    Input Text                      id:name_id                                                                                          ${edit name}
    Input Text                      id:address.line1_id                                                                                 ${edit adress1}
    Input Text                      id:address.line2_id                                                                                 ${edit adress2}
    Click Element                   xpath:(${select control})[1]
    Press Key                       xpath:(${select control})[1]/div[1]/div[2]        \ue015
    Press Key                       xpath:(${select control})[1]/div[1]/div[2]        \ue007
    Input Text                      id:address.city_id                                                                                  ${edit city}
    Input Text                      id:invoiceEmail_id                                                                                  ${edit email}
    Click Element                   xpath:(${select control})[2]
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]        \ue013
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]        \ue007
    Input Text                      id:address.zipCode_id                                                                               ${edit code}
    Click Element                   css:.modal-dialog-ok-button

Checking Edit Data
    Sleep                           5 second
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${static row}]/td[1]/a       ${edit name}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${static row}]/td[3]/div     ${edit full adress}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${static row}]/td[4]/div     Bill By Warehouse
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${static row}]/td[5]/div     ${edit email}

Return Static Data
    [Tags]                          ReturnStaticData
    Click Element                   ${edit button}
    Input Text                      id:name_id                                                                                          ${static name}
    Input Text                      id:address.line1_id                                                                                 ${static adress1}
    Input Text                      id:address.line2_id                                                                                 ${static adress2}
    Click Element                   xpath:(${select control})[1]
    Press Key                       xpath:(${select control})[1]/div[1]/div[2]        \ue013
    Press Key                       xpath:(${select control})[1]/div[1]/div[2]        \ue007
    Input Text                      id:address.city_id                                                                                  ${static city}
    Input Text                      id:invoiceEmail_id                                                                                  ${static email}
    Click Element                   xpath:(${select control})[2]
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]        \ue015
    Press Key                       xpath:(${select control})[2]/div[1]/div[2]        \ue007
    Input Text                      id:address.zipCode_id                                                                               ${static code}
    Click Element                   css:.modal-dialog-ok-button

Checking Returned Static Data
    Sleep                           5 second
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${static row}]/td[1]/a       ${static name}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${static row}]/td[3]/div     ${static full adress}
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${static row}]/td[4]/div     Singular Billing
    Element Text Should Be          xpath:${table xpath}/tbody/tr[${static row}]/td[5]/div     ${static email}

Sorting Distributors By Name
    [Tags]                          Sorting
    Click Element                   css:th.sort-column:nth-child(1)
    ${text buffer1}                 Get Text            xpath:${table xpath}/tbody/tr[1]/td[1]/a
    Click Element                   css:th.sort-column:nth-child(1)
    ${text buffer2}                 Get Text            xpath:${table xpath}/tbody/tr[${number of row}]/td[1]/a
    Should Be Equal	                ${text buffer1}     ${text buffer2}
    Click Element                   css:th.sort-column:nth-child(1)

Sorting Distributors By Number
    [Tags]                          Sorting
    Click Element                   css:th.sort-column:nth-child(2)
    ${text buffer1}                 Get Text            xpath:${table xpath}/tbody/tr[1]/td[2]/div
    Click Element                   css:th.sort-column:nth-child(2)
    ${text buffer2}                 Get Text            xpath:${table xpath}/tbody/tr[${number of row}]/td[2]/div
    Should Be Equal                 ${text buffer1}     ${text buffer2}
    Click Element                   css:th.sort-column:nth-child(2)

Sorting Distributors By Email
    [Tags]                          Sorting
    Click Element                   css:th.sort-column:nth-child(5)
    ${text buffer1}                 Get Text            xpath:${table xpath}/tbody/tr[1]/td[5]/div
    Click Element	                css:th.sort-column:nth-child(5)
    ${text buffer2}                 Get Text            xpath:${table xpath}/tbody/tr[${number of row}]/td[5]/div
    Should Be Equal                 ${text buffer1}     ${text buffer2}
    Click Element                   css:th.sort-column:nth-child(5)
    
Name Filter
    [Tags]                          NameFilter          Filter
    Click Element                   ${filter button}
    Is Filter Dialog
    Click Element                   css:.close
    Sleep                           2 second
    Is Distributors Page
    Click Element                   ${filter button}
    Click Element                   css:button.btn:nth-child(2)
    Sleep                           2 second
    Is Distributors Page
    Click Element                   ${filter button}
    Input Text                      css:div.row-spaced:nth-child(1) > div:nth-child(2) > input:nth-child(1)     ${static name}
    Apply Filter

Number Filter
    [Tags]                          NumberFilter                    Filter
    Click Element                   ${filter button}
    Input Text                      css:div.row-spaced:nth-child(2) > div:nth-child(2) > input:nth-child(1)     ${static number}
    Apply Filter

Email Filter
    [Tags]                          EmailFilter                     Filter
    Click Element                   ${filter button}
    Input Text                      css:div.row-spaced:nth-child(3) > div:nth-child(2) > input:nth-child(1)     ${static email}
    Apply Filter

Name And Number Filter
    [Tags]                          NameAndNumberFilter             Filter
    Click Element                   ${filter button}
    Input Text                      css:div.row-spaced:nth-child(1) > div:nth-child(2) > input:nth-child(1)     Test
    Input Text                      css:div.row-spaced:nth-child(2) > div:nth-child(2) > input:nth-child(1)     ${static number}
    Apply Filter

Name And Email Filter
    [Tags]                          NameAndEmailFilter              Filter
    Click Element                   ${filter button}
    Input Text                      css:div.row-spaced:nth-child(1) > div:nth-child(2) > input:nth-child(1)     Test
    Input Text                      css:div.row-spaced:nth-child(3) > div:nth-child(2) > input:nth-child(1)     ${static email}
    Apply Filter

Number And Email Filter
    [Tags]                          NumberAndEmailFilter            Filter
    Click Element                   ${filter button}
    Input Text                      css:div.row-spaced:nth-child(2) > div:nth-child(2) > input:nth-child(1)     ${static number}
    Input Text                      css:div.row-spaced:nth-child(3) > div:nth-child(2) > input:nth-child(1)     ${static email}
    Apply Filter

Name And Number And Email Filter
    [Tags]                          NameAndNumberAndEmailFilter     Filter
    Click Element                   ${filter button}
    Input Text                      css:div.row-spaced:nth-child(1) > div:nth-child(2) > input:nth-child(1)     Test
    Input Text                      css:div.row-spaced:nth-child(2) > div:nth-child(2) > input:nth-child(1)     ${static number}
    Input Text                      css:div.row-spaced:nth-child(3) > div:nth-child(2) > input:nth-child(1)     ${static email}
    Apply Filter

*** Keywords ***
Preparation
    Login In Admin Portal
    Sleep                           5 second
    Click Element                   id:pageDropDown
    Click Element                   css:li.dropdown-item:nth-child(4) > a:nth-child(1)
    Sleep                           2 second
    Number Of Rows
    Number Of Static Row
    Number Of Delete Row
    ${dynamic row}=                 Evaluate                        ${number of row}+1
    Set Global Variable             ${dynamic row}
    Set Global Variable             ${edit button}                  xpath:${table xpath}/tbody/tr[${static row}]/td[6]/div/div[1]/button
    Set Global Variable             ${remove button}                xpath:${table xpath}/tbody/tr[${dynamic row}]/td[6]/div/div[2]/button
    Set Global Variable             ${delete row button}            xpath:${table xpath}/tbody/tr[${delete row}]/td[6]/div/div[2]/button

Number Of Static Row
    : FOR   ${counter}              IN RANGE        1   ${number of row}+1
    \   ${text buffer1}             Get Text        xpath:${table xpath}/tbody/tr[${counter}]/td[1]/a
    \   Exit For Loop If            "${static name}"=="${text buffer1}"
    Set Global Variable             ${static row}   ${counter}
    ${static number}                Get Text        xpath:${table xpath}/tbody/tr[${static row}]/td[2]/div
    Set Global Variable             ${static number}

Number Of Delete Row
    : FOR   ${counter}              IN RANGE        1   ${number of row}+1
    \   ${text buffer1}             Get Text        xpath:${table xpath}/tbody/tr[${counter}]/td[1]/a
    \   Exit For Loop If            "del distr"=="${text buffer1}"
    Set Global Variable             ${delete row}   ${counter}

Apply Filter
    Sleep                           1 second
    Click Element                   ${filter apply}
    Sleep                           3 second
    Element Text Should Be          xpath:${table xpath}/tbody/tr[1]/td[1]/a       ${static name}
    Click Element                   ${filter clear}

Is Add Distributor
    Element Text Should Be          css:.modal-title    Add distributor

Is Delete Distributor
    Element Text Should Be          css:.modal-title    Removal Confirmation

Is Edit Distributor
    Element Text Should Be          css:.modal-title    Edit distributor

Is Filter Dialog
    Element Text Should Be          css:.modal-title    Filtering options
    
