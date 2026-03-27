*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${HEADLESS}    True
${CF_TEST_SECRET}     %{CF_TEST_SECRET} 

*** Keywords ***
Title Should Not Be Empty
    ${title}=    Get Title
    Should Not Be Empty     ${title}
Open Chrome For CI
    ${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --headless
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
    Go To       https://tarunsingh.co.in/?ci_token=${CF_TEST_SECRET}
     
    Wait Until Keyword Succeeds        20s      1s      Title Should Not Be Empty
    
    ${title}=       Get Title
    ${url}=         Get Location
    ${html}=        Get Source
    ${html_lower}=      Evaluate        """${html}""".lower()

    Log To Console         Title: ${title}
    Log To Console         URl: ${url}
    Log To Console         HAS_COURSES_TEXT: ${"Courses" in """${html}"""}
    Log To Console         HAS_CLOUDFLARE: ${"cloudflare" in $html_lower}
    Log To Console         HAS_JUST_A_MOMENT: ${"just a moment" in $html_lower}
    Log To Console         HAS_VERIFY_HUMAN: ${"verify you are human" in $html_lower}
    Log To Console         HAS_ACCESS_DENIED: ${"access denied" in $html_lower}
    
    ${courses_count}=      Get Element Count    xpath=//a[normalize-space()='Courses']
    Log To Console      Courses links found: ${courses_count}

    Wait Until Page Contains Element    //a[normalize-space()='Courses']    20s
    Scroll Element Into View    //a[normalize-space()='Courses']
    Click Element    //a[normalize-space()='Courses']

    ${title}=    Get Title
    Log To Console    TITLE=${title}

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
