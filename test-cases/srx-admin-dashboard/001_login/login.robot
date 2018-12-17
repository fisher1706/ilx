*** Settings ***
Suite Setup                         Start Suite
Suite Teardown                      Finish Suite
Library                             SeleniumLibrary
Resource                            ../../../resources/resource.robot
Resource                            ../../../resources/testData.robot

*** Variables ***
${element forgot button}            css:.btn
${forget or go back}                xpath:/html/body/div/div/div/div/div/form/div[5]/a

*** Test Cases ***
Invalid Login
    [Tags]                          InvalidLogin
    Enter Incorrect Email
    Click Element                   id:password
    Element Should Be Visible       css:.svg-inline--fa
    Enter Password
    Incorrect Submit Login
    Enter Correct Wrong Email
    Correct Submit Login
    Element Text Should Be          xpath:/html/body/div/div/div/div/div/form/div[5]/div[1]/strong      Failed to sign in!

Valid Login
    [Tags]                          ValidLogin
    Enter Correct Email
    Enter Password
    Correct Submit Login
    Spinner
    Is Distributors Page
    Sign Out
    Is Login Page

Forget Password
    [Tags]                          ForgetPassword
    Click Element                   ${forget or go back}
    Is Forgot Password Page
    Enter Incorrect Email
    Element Should Be Disabled      ${element forgot button}
    Enter Correct Wrong Email
    Submit Reset
    Element Text Should Be          xpath:/html/body/div/div/div/div/div/form/div[5]/div[1]/p[1]/strong     Failed to reset the password!
    Enter Correct Email
    Click Element                   ${forget or go back}
    Is Login Page

*** Keywords ***
Is Forgot Password Page
    Element Text Should Be          xpath:/html/body/div/div/div/div/div/form/div[5]/a      Go back

Spinner
    ${spinner Y}=                   Get Vertical Position       css:.spinner-container
    ${width}    ${height}=          Get Element Size            css:.spinner-container
    Log	        ${spinner Y}
    Log         ${height}
    ${button Y}=                    Get Vertical Position       css:.external-page-button-toolbar
    ${result}=                      Evaluate                    ${button Y}-${spinner Y}
    ${spinner Y}=                   Evaluate                    ${result}-${height}
    Log         ${button Y}
    Log         ${result}
    Log         ${spinner Y}
    Run Keyword If                  ${spinner Y}<1      Fail    Spinner error down
    Run Keyword If                  ${spinner Y}>15     Fail    Spinner error up

Enter Correct Wrong Email
    Input Text                      id:email            ${correct wrong email}

Enter Incorrect Email
    Input Text                      id:email            ${incorrect email}

Incorrect Submit Login
    Element Should Be Disabled      ${element login button}

Submit Reset
    Click Element                   ${element forgot button}

