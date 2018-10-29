*** Settings ***
Library                             XvfbRobot

*** Variables ***
${LOGIN URL}                        https://${HOST}/sign-in
${browser}                          ff
${X}                                1920
${Y}                                1080
${correct wrong email}              example@example.com
${incorrect email}                  example.agilevision.io
${element login button}             css:.btn

*** Keywords ***
Login In Distributor Portal
    Start Suite
    Enter Correct Email
    Enter Password
    Correct Submit Login
    Is Warehouse Management

Goto Customer Menu
    Goto Customer Management
    Number Of Rows C
    Number Of Static Row C
    Click Element                   xpath:/html/body/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/div/div/div/div[1]/div[2]/table/tbody/tr[${static row c}]/td[1]/a

Goto Security Groups
    Login In Distributor Portal
    Click Element                   css:li.sidebar-item:nth-child(7) > a:nth-child(1) > span:nth-child(2) > span:nth-child(1)
    Sleep                           5 second

Goto Settings
    Login In Distributor Portal
    Sleep                           5 second
    Click Element                   css:li.sidebar-item:nth-child(9) > a:nth-child(1)
    Sleep                           3 second

Goto Usage History
    Login In Distributor Portal
    Click Element                   css:.sidebar-items-container > div:nth-child(2) > li:nth-child(4) > a:nth-child(1)
    Sleep                           5 second
    Is Usage History

Goto Transactions
    Login In Distributor Portal
    Click Element                   css:.sidebar-items-container > li:nth-child(3) > a:nth-child(1)
    Sleep                           5 second
    Is Transactions

Goto Transaction Log
    Login In Distributor Portal
    Click Element                   css:.sidebar-items-container > li:nth-child(4) > a:nth-child(1)
    Sleep                           5 second
    Is Transaction Log

Goto Locations
    Login In Distributor Portal
    Click Element                   css:li.sidebar-item:nth-child(6) > a:nth-child(1)
    Sleep                           5 second
    Is Locations

Goto Customer Management
    Login In Distributor Portal
    Click Element                   css:li.sidebar-item:nth-child(2) > a:nth-child(1)
    Sleep                           5 second
    Is Customer Management

Goto User Managemant
    Login In Distributor Portal
    Click Element                   css:.sidebar-items-container > li:nth-child(1) > a:nth-child(1)
    Sleep                           5 second
    Is User Management

Goto Fees
    Login In Admin Portal
    Click Element                   css:li.sidebar-item:nth-child(2) > a:nth-child(1)
    Sleep                           5 second
    Is Fees Managemant

Goto Catalog
    Login In Distributor Portal
    Click Element                   css:.sidebar-items-container > div:nth-child(2) > li:nth-child(3) > a:nth-child(1)
    Sleep                           5 second
    Is Catalog

Goto Customer Types
    Login In Admin Portal
    Click Element                   css:li.sidebar-item:nth-child(4) > a:nth-child(1)
    Sleep                           5 second
    Is Customer Types

Goto Market Types
    Login In Admin Portal
    Click Element                   css:li.sidebar-item:nth-child(5) > a:nth-child(1)
    Sleep                           5 second
    Is Market Types

Goto Admin Users
    Login In Admin Portal
    Sleep                           7 second
    Click Element                   css:#pageDropDown
    Click Element                   css:li.dropdown-item:nth-child(4) > a:nth-child(1)
    Sleep                           2 second
    Number Of Rows E
    Number Of Static Row E
    Click Element                   xpath:/html/body/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/div/div/div/div[1]/div[2]/table/tbody/tr[${static row e}]/td[1]/a

Login In Admin Portal
    Start Suite
    Enter Correct Email
    Enter Password
    Correct Submit Login
    Is Distributors Page

Enter Correct Email
    Input Text                      id:email        ${email}

Enter Password
    Input Text                      id:password     ${password}

Correct Submit Login
    Click Element                   ${element login button}

Sign Out
    Click Element                   css:li.sidebar-item:nth-child(7) > a:nth-child(1)

Start Suite
    Run Keyword If                  "${browser}"=="xvfb"    Run Xvfb    ELSE IF     "${browser}"=="chrome"      Run Chrome  ELSE    Run Ff
    Set Selenium Implicit Wait      20 second
    Set Selenium Timeout            10 second

Run Xvfb
    Start Virtual Display           ${X}                    ${Y}
    Open Browser                    ${LOGIN URL}
    Set Window Size                 ${X}                    ${Y}

Run Chrome
    Open Browser                    ${LOGIN URL}            chrome
Run Ff
    Open Browser                    ${LOGIN URL}            ff

Finish Suite
    Close All Browsers

Is Security Groups
    Element Text Should Be          css:.security-groups-management-header > h1:nth-child(1)    Security Groups

Is Customer Types
    Element Text Should Be          css:.customer-types-management-header > h1:nth-child(1)     Customer Types Management

Is Market Types
    Element Text Should Be          css:.market-types-management-header > h1:nth-child(1)       Market Types Management

Is Login Page
    Element Text Should Be          xpath:/html/body/div/div/div/div/div/form/div[4]/label      Password

Is Customer Management
    Element Text Should Be          css:.customer-management-header > h1:nth-child(1)           Customer Management

Is Distributors Page
    Element Text Should Be          xpath:/html/body/div/div/div/div[2]/div/div[1]/div/div/h1   Distributor Management
    Element Text Should Be          css:.sidebar-user-info > p:nth-child(2)                     ${email}

Is Distributor Info
    Element Text Should Be          css:.back-link                                              Back to Distributors List

Is Fees Managemant
    Element Text Should Be          css:.distributor-management-header > h1:nth-child(1)        Fees Management

Is Usage History
    Element Text Should Be          css:.page-header > h1:nth-child(1)                          Usage History

Is Transactions
    Element Text Should Be          css:.customer-management-header > h1:nth-child(1)           Transactions

Is Setting General Settings
    Element Text Should Be          css:#settings-pane-1 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(1) > strong:nth-child(1)      Distributor logo:

Is Transaction Log
    Element Text Should Be          css:.customer-management-header > h1:nth-child(1)           Transaction Log

Is Locations
    Element Text Should Be          css:.locations-management-header > h1:nth-child(1)          Locations

Is User Management
    Element Text Should Be          css:.user-management-header > h1:nth-child(1)               User Management

Is Warehouse Management
    Element Text Should Be          css:.warehouse-management-header > h1:nth-child(1)          Warehouse Management

Is Catalog
    Element Text Should Be          css:.customer-management-header > h1:nth-child(1)           Catalog

Number Of Rows C
    ${number of row c}              Get Element Count   xpath:/html/body/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/div/div/div/div[1]/div[2]/table/tbody/tr
    Set Global Variable             ${number of row c}

Number Of Static Row C
    : FOR   ${counter c}            IN RANGE    1   ${number of row c}+1
    \   ${text buffer1 c}           Get Text    xpath:/html/body/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/div/div/div/div[1]/div[2]/table/tbody/tr[${counter c}]/td[1]/a
    \   Exit For Loop If            "Static Customer"=="${text buffer1 c}"
    Set Global Variable             ${static row c}     ${counter c}

Number Of Rows E
    ${number of row e}              Get Element Count   xpath:/html/body/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/div/div/div/div[1]/div[2]/table/tbody/tr
    Set Global Variable             ${number of row e}

Number Of Static Row E
    : FOR   ${counter e}            IN RANGE    1   ${number of row e}+1
    \   ${text buffer1 e}           Get Text    xpath:/html/body/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/div/div/div/div[1]/div[2]/table/tbody/tr[${counter e}]/td[1]/a
    \   Exit For Loop If            "${static name}"=="${text buffer1 e}"
    Set Global Variable             ${static row e}     ${counter e}

Successfull Upload
    Pass Execution                  Successfully imported!

Fail Upload
    Fail                            Operation failed!

Return Sub Link
    Return From Keyword If          "${HOST}"=="admin-dev.storeroomlogix.com"               distributor-dev.storeroomlogix.com
    Return From Keyword If          "${HOST}"=="distributor-dev.storeroomlogix.com"         admin-dev.storeroomlogix.com
    Return From Keyword If          "${HOST}"=="admin-staging.storeroomlogix.com"           distributor-staging.storeroomlogix.com
    Return From Keyword If          "${HOST}"=="distributor-staging.storeroomlogix.com"     admin-staging.storeroomlogix.com
    
Return Sub Email
    Return From Keyword If          "${HOST}"=="admin-dev.storeroomlogix.com"               srx-group+dev-distributor@agilevision.io
    Return From Keyword If          "${HOST}"=="distributor-dev.storeroomlogix.com"         srx-group+dev@agilevision.io
    Return From Keyword If          "${HOST}"=="admin-staging.storeroomlogix.com"           srx-group+staging-distributor@agilevision.io
    Return From Keyword If          "${HOST}"=="distributor-staging.storeroomlogix.com"     srx-group+staging@agilevision.io

Run Xvfb Sub
    Start Virtual Display           1920                            1080
    Open Browser                    https://${SUB HOST}/sign-in
    Set Window Size                 1920                            1080

Run Chrome Sub
    Open Browser                    https://${SUB HOST}/sign-in     chrome
    
Run Ff Sub
    Open Browser                    https://${SUB HOST}/sign-in     ff

Enter Correct Email Sub
    Input Text                      id:email                        ${SUB EMAIL}
    