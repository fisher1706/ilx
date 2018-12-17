*** Settings ***
Test Setup                          Preparation
Test Teardown                       Finish Suite
Library                             SeleniumLibrary
Library                             RequestsLibrary
Resource                            ../../../resources/resource.robot
Resource                            ../../../resources/testData.robot

*** Test Cases ***
Integrations
    [Tags]                          Integrations
    Goto Integrations
    Click Element                   css:#erp-integration-pane-api-keys > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:.modal-dialog-cancel-button
    Sleep                           2 second
    Click Element                   css:#erp-integration-pane-api-keys > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Input Text                      css:.rdt > input:nth-child(1)               10/18/2018, 12:00 A
    Element Should Be Visible       css:.fa-exclamation-circle > path:nth-child(1)
    Click Element                   css:.close
    Sleep                           2 second
    Click Element                   css:#erp-integration-pane-api-keys > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Clear Element Text              css:.rdt > input:nth-child(1)
    Input Text                      css:.rdt > input:nth-child(1)               7/18/2020, 12:00 A
    Input Text                      id:description_id                           ${keyword}
    Click Element                   css:.modal-dialog-ok-button
    Sleep                           5 second
    Element Text Should Be          xpath:${keys pane}${table xpath}/tbody/tr[2]/td[3]/div          ${keyword}
    Click Element                   xpath:${keys pane}${table xpath}/tbody/tr[2]/td[5]/div/div/button
    Element Text Should Be          xpath:/html/body/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[3]           ${keyword}
    Click Element                   css:button.btn-danger:nth-child(2)
    Sleep                           5 second

Transaction Submission
    [Tags]                          TransactionSubmission
    Goto Transaction Submission
    Click Element                   xpath:${transaction submission pane}${control button}
    Sleep                           1 second
    ${checked1}                     Get Element Attribute       xpath:(${transaction submission pane}${checkbox})[1]/label/input    checked
    ${checked3}                     Get Element Attribute       xpath:(${transaction submission pane}${checkbox})[3]/label/input    checked
    Element Should Be Disabled      xpath:(${transaction submission pane}${checkbox})[2]/label/input
    Click Element                   xpath:(${transaction submission pane}${checkbox})[1]/label/input
    Click Element                   xpath:(${transaction submission pane}${checkbox})[3]/label/input
    Click Element                   xpath:${transaction submission pane}${control button}
    Sleep                           1 second
    ${rechecked1}                   Get Element Attribute       xpath:(${transaction submission pane}${checkbox})[1]/label/input    checked
    ${rechecked3}                   Get Element Attribute       xpath:(${transaction submission pane}${checkbox})[3]/label/input    checked
    Should Not Be Equal             "${checked1}"       "${rechecked1}"
    Should Not Be Equal             "${checked3}"       "${rechecked3}"

Pricing Information
    [Tags]                          PricingInformation
    Goto Pricing Information
    Sleep                           3 second
    Element Should Be Enabled       css:label.select-options:nth-child(1) > input:nth-child(1)
    Click Element                   css:label.select-options:nth-child(1) > input:nth-child(1)
    Element Should Be Enabled       css:label.select-options:nth-child(2) > input:nth-child(1)
    Element Should Be Disabled      css:label.select-options:nth-child(3) > input:nth-child(1)
    Element Should Be Disabled      css:label.select-options:nth-child(4) > input:nth-child(1)
    Click Element                   css:#erp-integration-pane-pricing-integration > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Sleep                           5 second
    Element Should Be Enabled       css:label.select-options:nth-child(1) > input:nth-child(1)
    Click Element                   css:label.select-options:nth-child(1) > input:nth-child(1)
    Element Should Be Enabled       css:label.select-options:nth-child(2) > input:nth-child(1)
    Element Should Be Disabled      css:label.select-options:nth-child(3) > input:nth-child(1)
    Element Should Be Disabled      css:label.select-options:nth-child(4) > input:nth-child(1)
    Reload Page
    Sleep                           5 second
    Goto Pricing Information
    Sleep                           3 second
    Element Should Be Enabled       css:label.select-options:nth-child(1) > input:nth-child(1)
    Click Element                   css:label.select-options:nth-child(1) > input:nth-child(1)
    Element Should Be Enabled       css:label.select-options:nth-child(2) > input:nth-child(1)
    Element Should Be Disabled      css:label.select-options:nth-child(3) > input:nth-child(1)
    Element Should Be Disabled      css:label.select-options:nth-child(4) > input:nth-child(1)

Pricing And Ordering
    [Tags]                          PricingAndOrdering
    Goto Pricing And Ordering
    Sleep                           3 second
    Element Should Be Enabled       css:.pricing-options-container > div:nth-child(3) > label:nth-child(1) > input:nth-child(1)
    Element Should Be Enabled       css:.pricing-options-container > div:nth-child(3) > label:nth-child(2) > input:nth-child(1)
    Element Should Be Enabled       css:.pricing-options-container > div:nth-child(3) > label:nth-child(3) > input:nth-child(1)
    Click Element                   css:.pricing-options-container > div:nth-child(3) > label:nth-child(3) > input:nth-child(1)
    Click Element                   css:#enterprise-workflow-pane-pricing-ordering > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)
    Sleep                           5 second
    Reload Page
    Goto Pricing And Ordering
    Sleep                           3 second
    ${checked}                      Get Element Attribute       css:.pricing-options-container > div:nth-child(3) > label:nth-child(3) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="true"        Log To Console      Pass    ELSE    Fail    Fail
    ${checked}                      Get Element Attribute       css:.pricing-options-container > div:nth-child(3) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="None"        Log To Console      Pass    ELSE    Fail    Fail
    ${checked}                      Get Element Attribute       css:.pricing-options-container > div:nth-child(3) > label:nth-child(2) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="None"        Log To Console      Pass    ELSE    Fail    Fail

Order Close Logic
    [Tags]                          OrderCloseLogic
    Goto Order Close Logic
    Sleep                           3 second
    Click Element                   css:div.radio:nth-child(1) > label:nth-child(1) > input:nth-child(1)
    Click Element                   css:#enterprise-workflow-pane-order-close > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Sleep                           5 second
    ${checked}                      Get Element Attribute       css:div.radio:nth-child(4) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="None"        Log To Console      Pass    ELSE    Fail    Fail
    ${checked}                      Get Element Attribute       css:div.radio:nth-child(2) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="None"        Log To Console      Pass    ELSE    Fail    Fail
    ${checked}                      Get Element Attribute       css:div.radio:nth-child(1) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="true"        Log To Console      Pass    ELSE    Fail    Fail
    ${aria}                         Get Element Attribute       xpath:(${order close logic}${select control})[1]/div/div[2]     aria-disabled
    Run Keyword If                  "${aria}"=="true"           Log To Console      Pass    ELSE    Fail    Fail
    ${aria}                         Get Element Attribute       xpath:(${order close logic}${select control})[2]/div/div[2]     aria-disabled
    Run Keyword If                  "${aria}"=="true"           Log To Console      Pass    ELSE    Fail    Fail
    Click Element                   css:div.radio:nth-child(2) > label:nth-child(1) > input:nth-child(1)
    Click Element                   css:#enterprise-workflow-pane-order-close > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Sleep                           5 second
    ${checked}                      Get Element Attribute       css:div.radio:nth-child(4) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="None"        Log To Console      Pass    ELSE    Fail    Fail
    ${checked}                      Get Element Attribute       css:div.radio:nth-child(2) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="true"        Log To Console      Pass    ELSE    Fail    Fail
    ${checked}                      Get Element Attribute       css:div.radio:nth-child(1) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="None"        Log To Console      Pass    ELSE    Fail    Fail
    ${aria}                         Get Element Attribute       xpath:(${order close logic}${select control})[1]/div/div[2]     aria-disabled
    Run Keyword If                  "${aria}"=="false"          Log To Console      Pass    ELSE    Fail    Fail
    ${aria}                         Get Element Attribute       xpath:(${order close logic}${select control})[2]/div/div[2]     aria-disabled
    Run Keyword If                  "${aria}"=="true"           Log To Console      Pass    ELSE    Fail    Fail
    Click Element                   css:div.radio:nth-child(4) > label:nth-child(1) > input:nth-child(1)
    Click Element                   css:#enterprise-workflow-pane-order-close > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Sleep                           5 second
    ${aria}                         Get Element Attribute       xpath:(${order close logic}${select control})[1]/div/div[2]     aria-disabled
    Run Keyword If                  "${aria}"=="true"           Log To Console      Pass    ELSE    Fail    Fail
    ${aria}                         Get Element Attribute       xpath:(${order close logic}${select control})[2]/div/div[2]     aria-disabled
    Run Keyword If                  "${aria}"=="false"          Log To Console      Pass    ELSE    Fail    Fail
    ${checked}                      Get Element Attribute       css:div.radio:nth-child(4) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="true"        Log To Console      Pass    ELSE    Fail    Fail
    ${checked}                      Get Element Attribute       css:div.radio:nth-child(2) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="None"        Log To Console      Pass    ELSE    Fail    Fail
    ${checked}                      Get Element Attribute       css:div.radio:nth-child(1) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked}"=="None"        Log To Console      Pass    ELSE    Fail    Fail

Transaction Status Updates Logic Tab
    [Tags]                          TransactionStatusUpdatesLogicTab
    Goto Transaction Status Updates Logic
    Sleep                           3 second
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    ${checked1}                     Get Element Attribute           css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)     checked
    ${checked2}                     Get Element Attribute           css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked1}"=="${checked2}"    Click For Check     ELSE    No Operation
    Click Element                   css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)
    Click Element                   css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    Reload Page
    Sleep                           5 second
    Goto Transaction Status Updates Logic
    Sleep                           2 second
    ${rechecked1}                   Get Element Attribute               css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)     checked
    ${rechecked2}                   Get Element Attribute               css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked1}"=="${rechecked2}"      Log To Console      Pass    ELSE    Fail    Fail
    Run Keyword If                  "${checked2}"=="${rechecked1}"      Log To Console      Pass    ELSE    Fail    Fail
    Run Keyword If                  "${checked1}"!="${rechecked1}"      Log To Console      Pass    ELSE    Fail    Fail
    Run Keyword If                  "${checked2}"!="${rechecked2}"      Log To Console      Pass    ELSE    Fail    Fail

Transaction Status Updates Logic
    [Tags]                          TransactionStatusUpdatesLogic
    Create Session                  httpbin                         https://api-dev.storeroomlogix.com/api/distributor          verify=true
    Goto Transaction Status Updates Logic
    Sleep                           3 second
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    ${checked1}                     Get Element Attribute           css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)     checked
    ${checked2}                     Get Element Attribute           css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked1}"=="None"           Click Element       css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)
    Run Keyword If                  "${checked2}"=="true"           Click Element       css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    Reload Page
    Goto Transaction Status Updates Logic
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    Click Link                      xpath://*[@href="/transactions"]
    Click Element                   css:.checkbox-inline > input:nth-child(1)
    Click Element                   xpath:${header xpath}/thead/tr/th[1]/div[1]
    Element Should Be Enabled       xpath:${table xpath}/tbody/tr[1]/td[11]/div/button
    Element Should Be Enabled       xpath:${table xpath}/tbody/tr[1]/td[12]/div/div/button
    Click Element                   xpath:${table xpath}/tbody/tr[1]/td[12]/div/div/button
    Input Text                      id:reorderQuantity_id           40
    Click Element                   css:.modal-dialog-ok-button
    Sleep                           4 second
    &{headers}=                     Create Dictionary               Accept=application/json                                     ApiKey=m4DAfPuRurdzlsVrlen2
    ${error}                        Post Request                    httpbin    /items/71/split/30       headers=${headers}
    Should Be Equal As Strings      ${error}                        <Response [400]>
    Click Link                      xpath://*[@href="/settings"]
    Goto Transaction Status Updates Logic
    Sleep                           3 second
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    ${checked1}                     Get Element Attribute           css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)     checked
    ${checked2}                     Get Element Attribute           css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked1}"=="true"           Click Element       css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)
    Run Keyword If                  "${checked2}"=="None"           Click Element       css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    Reload Page
    Goto Transaction Status Updates Logic
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    Click Link                      xpath://*[@href="/transactions"]
    Click Element                   css:.checkbox-inline > input:nth-child(1)
    Sleep                           10 second
    ${rows}                         Get Element Count               xpath:${table xpath}/tbody/tr[1]/td
    Should Be Equal                 "${rows}"                       "10"
    &{headers}=                     Create Dictionary               Accept=application/json                                     ApiKey=m4DAfPuRurdzlsVrlen2
    ${error}                        Post Request                    httpbin    /items/71/split/30       headers=${headers}
    Should Be Equal As Strings      ${error}                        <Response [200]>
    Click Link                      xpath://*[@href="/settings"]
    Goto Transaction Status Updates Logic
    Sleep                           3 second
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    ${checked1}                     Get Element Attribute           css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)     checked
    ${checked2}                     Get Element Attribute           css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)     checked
    Run Keyword If                  "${checked1}"=="None"           Click Element       css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)
    Run Keyword If                  "${checked2}"=="None"           Click Element       css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    Reload Page
    Goto Transaction Status Updates Logic
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    Click Link                      xpath://*[@href="/transactions"]
    Click Element                   css:.checkbox-inline > input:nth-child(1)
    Click Element                   xpath:${header xpath}/thead/tr/th[1]/div[1]
    Element Should Be Enabled       xpath:${table xpath}/tbody/tr[1]/td[11]/div/button
    Element Should Be Enabled       xpath:${table xpath}/tbody/tr[1]/td[12]/div/div/button
    Click Element                   xpath:${table xpath}/tbody/tr[1]/td[12]/div/div/button
    Input Text                      id:reorderQuantity_id           40
    Click Element                   css:.modal-dialog-ok-button
    Sleep                           4 second
    &{headers}=                     Create Dictionary               Accept=application/json                                     ApiKey=m4DAfPuRurdzlsVrlen2
    ${error}                        Post Request                    httpbin    /items/71/split/30       headers=${headers}
    Should Be Equal As Strings      ${error}                        <Response [200]>

Distributor Contact Info
    [Tags]                          DistributorContactInfo
    Goto Distributor Contact Info
    Sleep                           4 second
    Clear Element Text              id:name_id
    Input Text                      id:name_id              ${dynamic name}
    Clear Element Text              id:phone_id
    Input Text                      id:phone_id             ${dynamic code}
    Clear Element Text              id:email_id
    Input Text                      id:email_id             ${dynamic email}
    Clear Element Text              id:emergencyPhone_id
    Input Text                      id:emergencyPhone_id    ${test number}
    Click Element                   css:#enterprise-profile-pane-contact-info > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)
    Sleep                           4 second
    Click Link                      xpath://*[@href="/customers"]
    Sleep                           4 second
    Number Of Rows C
    Number Of Static Row C
    Click Element                   xpath:${table xpath}/tbody/tr[${static row c}]/td[1]/a
    Sleep                           4 second
    Goto Customer Contact Info
    Sleep                           4 second
    ${value}                        Get Value               id:name_default_id
    Run Keyword If                  "${value}"=="${dynamic name}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:phone_default_id
    Run Keyword If                  "${value}"=="${dynamic code}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:email_default_id
    Run Keyword If                  "${value}"=="${dynamic email}"  Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:emergencyPhone_default_id
    Run Keyword If                  "${value}"=="${test number}"    Log To Console      Pass    ELSE    Fail    Fail
    Click Element                   css:.item-form-fields > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:.item-form-fields > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:.item-form-fields > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:.item-form-fields > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   xpath:${customer contact info}${control button}
    Sleep                           5 second
    Reload Page
    Sleep                           2 second
    Goto Customer Contact Info
    Sleep                           4 second
    ${value}                        Get Value               id:name_id
    Run Keyword If                  "${value}"=="${dynamic name}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:phone_id
    Run Keyword If                  "${value}"=="${dynamic code}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:email_id
    Run Keyword If                  "${value}"=="${dynamic email}"  Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:emergencyPhone_id
    Run Keyword If                  "${value}"=="${test number}"    Log To Console      Pass    ELSE    Fail    Fail
    Click Link                      xpath://*[@href="/settings"]
    Sleep                           3 second
    Goto Distributor Contact Info
    Sleep                           1 second
    Clear Element Text              id:name_id
    Input Text                      id:name_id              ${edit name}
    Clear Element Text              id:phone_id
    Input Text                      id:phone_id             ${edit code}
    Clear Element Text              id:email_id
    Input Text                      id:email_id             ${edit email}
    Clear Element Text              id:emergencyPhone_id
    Input Text                      id:emergencyPhone_id    ${edit test number}
    Click Element                   css:#enterprise-profile-pane-contact-info > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)
    Sleep                           4 second
    Click Link                      xpath://*[@href="/customers"]
    Sleep                           4 second
    Click Element                   xpath:${table xpath}/tbody/tr[${static row c}]/td[1]/a
    Sleep                           4 second
    Goto Customer Contact Info
    Sleep                           4 second
    ${value}                        Get Value               id:name_default_id
    Run Keyword If                  "${value}"=="${edit name}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:phone_default_id
    Run Keyword If                  "${value}"=="${edit code}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:email_default_id
    Run Keyword If                  "${value}"=="${edit email}"  Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:emergencyPhone_default_id
    Run Keyword If                  "${value}"=="${edit test number}"    Log To Console      Pass    ELSE    Fail    Fail
    Click Element                   css:.item-form-fields > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:.item-form-fields > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:.item-form-fields > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:.item-form-fields > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   xpath:${customer contact info}${control button}
    Sleep                           5 second
    Reload Page
    Sleep                           2 second
    Goto Customer Contact Info
    Sleep                           4 second
    ${value}                        Get Value               id:name_id
    Run Keyword If                  "${value}"=="${edit name}"          Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:phone_id
    Run Keyword If                  "${value}"=="${edit code}"          Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:email_id
    Run Keyword If                  "${value}"=="${edit email}"         Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:emergencyPhone_id
    Run Keyword If                  "${value}"=="${edit test number}"   Log To Console      Pass    ELSE    Fail    Fail
    Click Link                      xpath://*[@href="/settings"]
    Sleep                           3 second

Cost Saving
    [Tags]                          CostSaving
    Goto Cost Saving
    Sleep                           4 second
    Clear Element Text              id:laborCost_id
    Input Text                      id:laborCost_id             ${test number 1}
    Clear Element Text              id:timeToReplenish_id
    Input Text                      id:timeToReplenish_id       ${test number 2}
    Clear Element Text              id:timeToQuote_id
    Input Text                      id:timeToQuote_id           ${test number 3}
    Clear Element Text              id:timeToAudit_id
    Input Text                      id:timeToAudit_id           ${test number 4}
    Clear Element Text              id:deliveryCost_id
    Input Text                      id:deliveryCost_id          ${test number 5}
    Click Element                   css:#enterprise-profile-pane-cost-savings > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)
    Sleep                           4 second
    Click Link                      xpath://*[@href="/customers"]
    Sleep                           4 second
    Number Of Rows C
    Number Of Static Row C
    Click Element                   xpath:${table xpath}/tbody/tr[${static row c}]/td[1]/a
    Sleep                           4 second
    Goto Customer Cost Saving
    Sleep                           4 second
    ${value}                        Get Value               id:laborCost_default_id
    Run Keyword If                  "${value}"=="${test number 1}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToReplenish_default_id
    Run Keyword If                  "${value}"=="${test number 2}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToQuote_default_id
    Run Keyword If                  "${value}"=="${test number 3}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToAudit_default_id
    Run Keyword If                  "${value}"=="${test number 4}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:deliveryCost_default_id
    Run Keyword If                  "${value}"=="${test number 5}"      Log To Console      Pass    ELSE    Fail    Fail
    Click Element                   css:#customer-settings-pane-cost-savings > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:#customer-settings-pane-cost-savings > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:#customer-settings-pane-cost-savings > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:#customer-settings-pane-cost-savings > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:#customer-settings-pane-cost-savings > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   xpath:${customer cost saving}${control button}
    Sleep                           5 second
    Reload Page
    Sleep                           2 second
    Goto Customer Cost Saving
    Sleep                           4 second
    ${value}                        Get Value               id:laborCost_id
    Run Keyword If                  "${value}"=="${test number 1}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToReplenish_id
    Run Keyword If                  "${value}"=="${test number 2}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToQuote_id
    Run Keyword If                  "${value}"=="${test number 3}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToAudit_id
    Run Keyword If                  "${value}"=="${test number 4}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:deliveryCost_id
    Run Keyword If                  "${value}"=="${test number 5}"      Log To Console      Pass    ELSE    Fail    Fail
    Click Link                      xpath://*[@href="/settings"]
    Sleep                           3 second
    Goto Cost Saving
    Sleep                           1 second
    Clear Element Text              id:laborCost_id
    Input Text                      id:laborCost_id             ${edit test number 1}
    Clear Element Text              id:timeToReplenish_id
    Input Text                      id:timeToReplenish_id       ${edit test number 2}
    Clear Element Text              id:timeToQuote_id
    Input Text                      id:timeToQuote_id           ${edit test number 3}
    Clear Element Text              id:timeToAudit_id
    Input Text                      id:timeToAudit_id           ${edit test number 4}
    Clear Element Text              id:deliveryCost_id
    Input Text                      id:deliveryCost_id          ${edit test number 5}
    Click Element                   css:#enterprise-profile-pane-cost-savings > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)
    Sleep                           4 second
    Click Link                      xpath://*[@href="/customers"]
    Sleep                           4 second
    Number Of Rows C
    Number Of Static Row C
    Click Element                   xpath:${table xpath}/tbody/tr[${static row c}]/td[1]/a
    Sleep                           4 second
    Goto Customer Cost Saving
    Sleep                           4 second
    ${value}                        Get Value               id:laborCost_default_id
    Run Keyword If                  "${value}"=="${edit test number 1}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToReplenish_default_id
    Run Keyword If                  "${value}"=="${edit test number 2}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToQuote_default_id
    Run Keyword If                  "${value}"=="${edit test number 3}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToAudit_default_id
    Run Keyword If                  "${value}"=="${edit test number 4}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:deliveryCost_default_id
    Run Keyword If                  "${value}"=="${edit test number 5}"      Log To Console      Pass    ELSE    Fail    Fail
    Click Element                   css:#customer-settings-pane-cost-savings > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:#customer-settings-pane-cost-savings > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:#customer-settings-pane-cost-savings > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:#customer-settings-pane-cost-savings > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   css:#customer-settings-pane-cost-savings > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)
    Click Element                   xpath:${customer cost saving}${control button}
    Sleep                           5 second
    Reload Page
    Sleep                           2 second
    Goto Customer Cost Saving
    Sleep                           4 second
    ${value}                        Get Value               id:laborCost_id
    Run Keyword If                  "${value}"=="${edit test number 1}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToReplenish_id
    Run Keyword If                  "${value}"=="${edit test number 2}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToQuote_id
    Run Keyword If                  "${value}"=="${edit test number 3}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:timeToAudit_id
    Run Keyword If                  "${value}"=="${edit test number 4}"      Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               id:deliveryCost_id
    Run Keyword If                  "${value}"=="${edit test number 5}"      Log To Console      Pass    ELSE    Fail    Fail
    Click Link                      xpath://*[@href="/settings"]
    Sleep                           3 second

*** Keywords ***
Preparation
    Goto Settings

Click For Check
    Click Element                   css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    ${checked1}                     Get Element Attribute       css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)     checked
    ${checked2}                     Get Element Attribute       css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)     checked
    Set Global Variable             ${checked1}
    Set Global Variable             ${checked2}

Goto Documents
    Click Element                   id:settings-tab-pricing-billing
    Sleep                           1 second
    Click Element                   id:pricing-billing-tab-documents
    Sleep                           3 second

Goto Integrations
    Click Element                   id:settings-tab-erp-integration
    Sleep                           1 second
    Click Element                   id:erp-integration-tab-api-keys
    Sleep                           3 second

Goto Distributor Contact Info
    Click Element                   id:settings-tab-enterprise-profile
    Sleep                           1 second
    Click Element                   id:enterprise-profile-tab-contact-info
    Sleep                           3 second

Goto Cost Saving
    Click Element                   id:settings-tab-enterprise-profile
    Sleep                           1 second
    Click Element                   id:enterprise-profile-tab-cost-savings
    Sleep                           3 second

Goto Pricing Information
    Click Element                   id:settings-tab-erp-integration
    Sleep                           1 second
    Click Element                   id:erp-integration-tab-pricing-integration
    Sleep                           3 second

Goto Pricing And Ordering
    Click Element                   id:settings-tab-enterprise-workflow
    Sleep                           1 second
    Click Element                   id:enterprise-workflow-tab-pricing-ordering
    Sleep                           3 second

Goto Order Close Logic
    Click Element                   id:settings-tab-enterprise-workflow
    Sleep                           1 second
    Click Element                   id:enterprise-workflow-tab-order-close
    Sleep                           3 second

Goto Transaction Status Updates Logic
    Click Element                   id:settings-tab-erp-integration
    Sleep                           1 second
    Click Element                   id:erp-integration-tab-transaction-status
    Sleep                           3 second

Goto Transaction Submission
    Click Element                   id:settings-tab-erp-integration
    Sleep                           1 second
    Click Element                   id:erp-integration-tab-rl-submit-integration
    Sleep                           3 second