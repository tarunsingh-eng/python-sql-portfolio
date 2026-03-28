*** Settings ***
Library    SeleniumLibrary
Library    String

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
    Call Method    ${chrome_options}    add_argument    --window-size=1920,1080
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Call Method    ${chrome_options}    add_argument    --disable-dev-shm-usage
    Call Method    ${chrome_options}    add_argument    --disable-gpu
    Call Method    ${chrome_options}    add_argument    --remote-debugging-port=9222
    Call Method    ${chrome_options}    add_argument    --disable-blink-features=AutomationControlled
    Call Method    ${chrome_options}    add_argument    --disable-features=IsolateOrigins,site-per-process
    Call Method    ${chrome_options}    add_argument    --disable-site-isolation-trials


    ${ua}=         Set Variable         --user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115 Safari/537.36
    Call Method    ${chrome_options}    add_argument    ${ua}    

    Create Webdriver    Chrome    options=${chrome_options}
    Execute Javascript    Object.defineProperty(navigator, 'webdriver', {get: () => undefined})
    Set Window Size    1920    1080
    Set Selenium Timeout    20s

*** Test Cases ***
Navigation Test
    Open Chrome For CI
    Go To       https://tarunsingh.co.in/?ci_token=${CF_TEST_SECRET}
     
    Wait Until Page Contains Element    xpath=//a[normalize-space()='Courses']    20s

    Sleep    2s
    Execute Javascript    window.scrollTo(0, document.body.scrollHeight)
    Sleep    1s
    Execute Javascript    window.scrollTo(0, 0)


    Add Cookie      CF_Authorization        ${CF_TEST_SECRET}       path=/      domain=.tarunsingh.co.in
    ${cookies}=     Get Cookies
    Log         COOKIES:    ${cookies}      console=True
    
    Reload Page
    
    ${title}=       Get Title
    ${url}=         Get Location
    ${html}=        Get Source
    ${html_lower}=      Convert To Lower Case        ${html}

    ${has_courses}=     Evaluate       "Courses" in $html
    ${has_cloudflare}=  Evaluate        "cloudflare" in $html_lower
    ${has_just_a_moment}=   Evaluate    "just a moment" in $html_lower
    ${has_verify_human}=    Evaluate    "verify you are human" in $html_lower
    ${has_access_denied}=   Evaluate    "access denied" in $html_lower

    Log To Console         Title: ${title}
    Log To Console         URl: ${url}
    Log To Console         HAS_COURSES_TEXT: ${has_courses}
    Log To Console         HAS_CLOUDFLARE: ${has_cloudflare}
    Log To Console         HAS_JUST_A_MOMENT: ${has_just_a_moment}
    Log To Console         HAS_VERIFY_HUMAN: ${has_verify_human}
    Log To Console         HAS_ACCESS_DENIED: ${has_access_denied}

  

    ${courses_count}=      Get Element Count    xpath=//a[normalize-space()='Courses']
    Log To Console      Courses links found: ${courses_count}

    Wait Until Page Contains Element    css://a[normalize-space()='Courses']    20s
    Scroll Element Into View    css://a[normalize-space()='Courses']
    Click Element    css://a[normalize-space()='Courses']



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




    Wait Until Page Does Not Contain    Just a moment    30s
    Wait Until Page Does Not Contain    verify you are human    30



    Scroll Element Into View    //a[normalize-space()='About']
    Click Element    //a[normalize-space()='About']



    Wait Until Page Does Not Contain    Just a moment    30s
    Wait Until Page Does Not Contain    verify you are human    30



    Scroll Element Into View    //a[normalize-space()='Gaming']
    Click Element    //a[normalize-space()='Gaming']


    Wait Until Page Does Not Contain    Just a moment    30s
    Wait Until Page Does Not Contain    verify you are human    30



    Scroll Element Into View    //a[normalize-space()='Reviews']
    Click Element    //a[normalize-space()='Reviews']



    Wait Until Page Does Not Contain    Just a moment    30s
    Wait Until Page Does Not Contain    verify you are human    30



    Scroll Element Into View    //a[normalize-space()='blog']
    Click Element    //a[normalize-space()='blog']



    Wait Until Page Does Not Contain    Just a moment    30s
    Wait Until Page Does Not Contain    verify you are human    30


    Scroll Element Into View    //a[@href='https://tarunsingh.co.in/'][normalize-space()='Tarun Singh']
    Click Element    //a[@href='https://tarunsingh.co.in/'][normalize-space()='Tarun Singh']
