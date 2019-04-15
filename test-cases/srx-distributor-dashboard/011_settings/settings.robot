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
    Click Element                   xpath:${keys pane}${button primary}
    Click Element                   css:.modal-dialog-cancel-button
    Sleep                           2 second
    Click Element                   xpath:${keys pane}${button primary}
    Input Text                      css:.rdt > input:nth-child(1)               10/18/2018, 12:00 A
    Element Should Be Visible       css:.fa-exclamation-circle > path:nth-child(1)
    Click Element                   xpath:${button close}
    Sleep                           2 second
    Click Element                   xpath:${keys pane}${button primary}
    Clear Element Text              css:.rdt > input:nth-child(1)
    Input Text                      css:.rdt > input:nth-child(1)               7/18/2020, 12:00 A
    Input Text                      id:description_id                           ${keyword}
    Click Element                   xpath:${button modal dialog ok}
    Sleep                           5 second
    ${number of rows}               Get Rows Count      ${keys pane}${table xpath}
    Element Text Should Be          xpath:${keys pane}${table xpath}/tbody/tr[${number of rows}]/td[3]      ${keyword}
    Click Element                   xpath:${keys pane}${table xpath}/tbody/tr[${number of rows}]${button danger}
    Element Text Should Be          xpath:${modal dialog}${simple table}/tbody/tr/td[3]     ${keyword}
    Click Element                   xpath:${modal dialog}${button danger}
    Sleep                           5 second

Transaction Submission
    [Tags]                          TransactionSubmission
    Goto Transaction Submission
    Click Element                   xpath:${transaction submission pane}${control button}
    Sleep                           1 second
    Select Radio Button             transactionSubmissionSetting        API
    Click Element                   xpath:${transaction submission pane}${control button}
    Sleep                           1 second
    Reload Page
    Sleep                           3 second
    Goto Transaction Submission
    Radio Button Should Be Set To   transactionSubmissionSetting        API
    Select Radio Button             transactionSubmissionSetting        EDI
    Click Element                   xpath:${transaction submission pane}${control button}
    Sleep                           1 second
    Reload Page
    Sleep                           3 second
    Goto Transaction Submission
    Radio Button Should Be Set To   transactionSubmissionSetting        EDI

Pricing Information
    [Tags]                          PricingInformation
    Goto Pricing Information
    Sleep                           3 second
    Select Radio Button             pricingInfoSettings                 API
    Click Element                   xpath:${pricing integrations}${button primary}
    Sleep                           3 second
    Reload Page
    Sleep                           3 second
    Goto Pricing Information
    Sleep                           3 second
    Radio Button Should Be Set To   pricingInfoSettings                 API
    Select Radio Button             pricingInfoSettings                 NO_PRICING
    Click Element                   xpath:${pricing integrations}${button primary}
    Sleep                           3 second
    Reload Page
    Sleep                           3 second
    Goto Pricing Information
    Sleep                           3 second
    Radio Button Should Be Set To   pricingInfoSettings                 NO_PRICING
    Select Radio Button             pricingInfoSettings                 SRX
    Click Element                   xpath:${pricing integrations}${button primary}
    Sleep                           5 second
    Reload Page
    Sleep                           3 second
    Goto Pricing Information
    Radio Button Should Be Set To   pricingInfoSettings                 SRX

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
    [Tags]                          TransactionStatusTab
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
    [Tags]                          TransactionStatus
    ${request url}                  Get Request URL
    Create Session                  httpbin                          ${request url}          verify=true
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
    Goto Sidebar Order Status
    Sleep                           3 second
    Open Minimum Table
    Sleep                           3 second
    Click Element                   css:.checkbox-inline > input:nth-child(1)
    Sleep                           6 second
    Click Element                   xpath:${header xpath}/thead/tr/th[1]
    Element Should Be Enabled       xpath:${table xpath}/tbody/tr[1]/td[12]/div/button
    Element Should Be Enabled       xpath:${table xpath}/tbody/tr[1]/td[13]/div/div/button
    Click Element                   xpath:${table xpath}/tbody/tr[1]/td[13]/div/div/button
    Input Text                      id:reorderQuantity_id           40
    Click Element                   xpath:${button modal dialog ok}
    Sleep                           4 second
    &{headers}=                     Create Dictionary               Accept=application/json                                     ApiKey=${API_key}
    ${error}                        Post Request                    httpbin    /       headers=${headers}
    Should Be Equal As Strings      ${error}                        <Response [400]>
    Goto Sidebar Settings
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
    Goto Sidebar Order Status
    Sleep                           3 second
    Open Minimum Table
    Sleep                           3 second
    Click Element                   css:.checkbox-inline > input:nth-child(1)
    Sleep                           6 second
    #${rows}                         Get Element Count               xpath:${table xpath}/tbody/tr[1]/td
    #Should Be Equal                 "${rows}"                       "10"
    &{headers}=                     Create Dictionary               Accept=application/json                                     ApiKey=${API_key}
    ${error}                        Post Request                    httpbin    /       headers=${headers}
    Should Be Equal As Strings      ${error}                        <Response [200]>
    Goto Sidebar Settings
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
    Goto Sidebar Order Status
    Sleep                           3 second
    Open Minimum Table
    Sleep                           3 second
    Click Element                   css:.checkbox-inline > input:nth-child(1)
    Sleep                           6 second
    Click Element                   xpath:${header xpath}/thead/tr/th[1]
    Element Should Be Enabled       xpath:${table xpath}/tbody/tr[1]/td[12]/div/button
    Element Should Be Enabled       xpath:${table xpath}/tbody/tr[1]/td[13]/div/div/button
    Click Element                   xpath:${table xpath}/tbody/tr[1]/td[13]/div/div/button
    Input Text                      id:reorderQuantity_id           40
    Click Element                   xpath:${button modal dialog ok}
    Sleep                           4 second
    &{headers}=                     Create Dictionary               Accept=application/json                                     ApiKey=${API_key}
    ${error}                        Post Request                    httpbin    /       headers=${headers}
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
    Click Element                   xpath:${pricing integrations}${button primary}
    Sleep                           4 second
    Goto Sidebar Customers
    Sleep                           4 second
    ${row number}                   Get React Rows Count    ${react table}
    Click Element                   xpath:(${react table}${react table raw})[${row number}]
    Sleep                           4 second
    Goto Customer Contact Info
    Sleep                           4 second
    ${value}                        Get Element Attribute           xpath:(${checkbox type})[1]     value
    Run Keyword If                  "${value}"!="true"          Select Checkbox         xpath:(${checkbox type})[1]
    Sleep                           2 second
    ${value}                        Get Value               xpath://input[contains(@name, 'name')]
    Run Keyword If                  "${value}"=="${dynamic name}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               xpath://input[contains(@name, 'phone')]
    Run Keyword If                  "${value}"=="${dynamic code}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               xpath://input[contains(@name, 'email')]
    Run Keyword If                  "${value}"=="${dynamic email}"  Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               xpath://input[contains(@name, 'emergencyPhone')]
    Run Keyword If                  "${value}"=="${test number}"    Log To Console      Pass    ELSE    Fail    Fail
    Click Element                   xpath:${button submit}
    Sleep                           5 second
    Reload Page
    Sleep                           2 second
    Goto Customer Contact Info
    Sleep                           4 second
    ${value}                        Get Value               xpath://input[contains(@name, 'name')]
    Run Keyword If                  "${value}"=="${dynamic name}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               xpath://input[contains(@name, 'phone')]
    Run Keyword If                  "${value}"=="${dynamic code}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               xpath://input[contains(@name, 'email')]
    Run Keyword If                  "${value}"=="${dynamic email}"  Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               xpath://input[contains(@name, 'emergencyPhone')]
    Run Keyword If                  "${value}"=="${test number}"    Log To Console      Pass    ELSE    Fail    Fail
    Goto Sidebar Settings
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
    Click Element                   xpath:${pricing integrations}${button primary}
    Sleep                           4 second
    Goto Sidebar Customers
    Sleep                           4 second
    Click Element                   xpath:(${react table}${react table raw})[${row number}]
    Sleep                           4 second
    Goto Customer Contact Info
    Sleep                           4 second
    ${value}                        Get Value               xpath://input[contains(@name, 'name')]
    Run Keyword If                  "${value}"=="${edit name}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               xpath://input[contains(@name, 'phone')]
    Run Keyword If                  "${value}"=="${edit code}"   Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               xpath://input[contains(@name, 'email')]
    Run Keyword If                  "${value}"=="${edit email}"  Log To Console      Pass    ELSE    Fail    Fail
    ${value}                        Get Value               xpath://input[contains(@name, 'emergencyPhone')]
    Run Keyword If                  "${value}"=="${edit test number}"    Log To Console      Pass    ELSE    Fail    Fail
    Goto Sidebar Settings
    Sleep                           3 second

*** Keywords ***
Preparation
    Start Distributor
    Sleep                           2 second
    Goto Sidebar Settings
    Sleep                           3 second

Click For Check
    Click Element                   css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)
    Click Element                   css:.row-spaced > div:nth-child(1) > button:nth-child(1)
    Sleep                           3 second
    ${checked1}                     Get Element Attribute       css:div.checkbox:nth-child(1) > label:nth-child(1) > input:nth-child(1)     checked
    ${checked2}                     Get Element Attribute       css:div.checkbox:nth-child(2) > label:nth-child(1) > input:nth-child(1)     checked
    Set Suite Variable              ${checked1}
    Set Suite Variable              ${checked2}

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

Get Request URL
    Return From Keyword If          "${environment}"=="dev"                 https://api-dev.storeroomlogix.com/api/distributor/items/71/split/30
    Return From Keyword If          "${environment}"=="staging"             https://api-staging.storeroomlogix.com/api/distributor/items/37/split/30

Goto Customer Contact Info
    Click Element                   xpath:(${tab element})[6]
    Sleep                           2 second
    Click Element                   xpath:(${expanded not})[1]
