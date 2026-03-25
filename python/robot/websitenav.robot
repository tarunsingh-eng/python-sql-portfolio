*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${HEADLESS}    True
${CF_TEST_SECRET}     %{CF_TEST_SECRET}  

*** Keywords ***
Open Chrome For CI
    ${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --HEADLESS
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Call Method    ${chrome_options}    add_argument    --disable-dev-shm-usage
    Call Method    ${chrome_options}    add_argument    --disable-gpu

    ${ua}=         Set Variable         --user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115 Safari/537.36
    Call Method    ${chrome_options}    add_argument    ${ua}    

    Create Webdriver    Chrome    options=${chrome_options}
    Set Window Size    1920    1080
    Set Selenium Timeout    20s

*** Test Cases ***
Navigation Test
    Open Chrome For CI

    Go To       https://tarunsingh.co.in
    Capture Page Screenshot    debug-cloudflare-block.png
   
    Add Cookie    CF_Authorization    ${CF_TEST_SECRET}    domain=.tarunsingh.co.in    path=/

    ${url}=     Set Variable    https://tarunsingh.co.in/?ci_token=${CF_TEST_SECRET}
    Go To   ${url}

    Wait Until Page Contains Element    //a[normalize-space()='Courses']    20s
    Scroll Element Into View    //a[normalize-space()='Courses']
    Click Element    //a[normalize-space()='Courses']

    ${title}=    Get Title
    Log To Console    TITLE=${title}
    Capture Page Screenshot

    Page Should Contain Element    //a[normalize-space()='Projects']

    Wait Until Page Contains Element    //a[normalize-space()='Projects']    20s
    Scroll Element Into View    //a[normalize-space()='Projects']
    
    Click Element    //a[normalize-space()='Projects']
    Scroll Element Into View    //a[normalize-space()='Video Portfolio']
    Click Element    //a[normalize-space()='Video Portfolio']
    Scroll Element Into View    //a[normalize-space()='Behind The Lens']
    Click Element    //a[normalize-space()='Behind The Lens']
    Scroll Element Into View    //a[normalize-space()='Digital Art']
    Click Element    //a[normalize-space()='Digital Art']
    Scroll Element Into View    //a[normalize-space()='About']
    Click Element    //a[normalize-space()='About']
    Scroll Element Into View    //a[normalize-space()='Gaming']
    Click Element    //a[normalize-space()='Gaming']
    Scroll Element Into View    //a[normalize-space()='Reviews']
    Click Element    //a[normalize-space()='Reviews']
    Scroll Element Into View    //a[normalize-space()='blog']
    Click Element    //a[normalize-space()='blog']
    Scroll Element Into View    //a[@href='https://tarunsingh.co.in/'][normalize-space()='Tarun Singh']
    Click Element    //a[@href='https://tarunsingh.co.in/'][normalize-space()='Tarun Singh']
