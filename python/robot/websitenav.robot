*** Settings ***
Library    SeleniumLibrary
Library    String

*** Variables ***
${HEADLESS}    True
${CF_TEST_SECRET}     %{CF_TEST_SECRET} 
${BASE_URL}           https://tarunsingh.co.in

*** Keywords ***
Title Should Not Be Empty
    ${title}=    Get Title
    Should Not Be Empty     ${title}
Open Chrome For CI
    ${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --headless\=new
    Call Method    ${chrome_options}    add_argument    --window-size\=1920,1080
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Call Method    ${chrome_options}    add_argument    --disable-dev-shm-usage
    Call Method    ${chrome_options}    add_argument    --disable-gpu
    Call Method    ${chrome_options}    add_argument    --remote-debugging-port\=9222
    Call Method    ${chrome_options}    add_argument    --disable-blink-features\=AutomationControlled
    Call Method    ${chrome_options}    add_argument    --disable-features\=IsolateOrigins,site-per-process
    Call Method    ${chrome_options}    add_argument    --disable-site-isolation-trials

    ${ua}=         Set Variable         --user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115 Safari/537.36
    Call Method    ${chrome_options}    add_argument    ${ua}    

    Create Webdriver    Chrome    options=${chrome_options}
    Set Window Size    1920    1080
    Set Selenium Timeout    20s

    ${sl}=      Get Library Instance        SeleniumLibrary
    ${driver}=      Evaluate        $sl.driver
    ${empty}=       Evaluate        {}
    ${headers}=     Evaluate        {"x-ci-secret": $CF_TEST_SECRET}
    ${payload}=     Evaluate        {"headers": $headers}

    Call Method     ${driver}       execute_cdp_cmd     Network.enable      ${empty}
    Call Method     ${driver}       execute_cdp_cmd     Network.setExtraHTTPHeaders     ${payload}

Click Nav Link
    [Arguments]     ${text}
    ${el}=         Get WebElement       xpath=//a[normalize-space()='${text}']
    Execute Javascript    arguments[0].scrollIntoView({block: 'center', inline: 'center'});    ARGUMENTS    ${el}
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${el}

*** Test Cases ***
Navigation Test
    Open Chrome For CI
    Go To       ${BASE_URL}/
     
    Wait Until Page Contains Element    xpath=//a[normalize-space()='Courses']    20s

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

    ${projects_count}=      Get Element Count    xpath=//a[normalize-space()='Projects']
    Log To Console      Projects links found: ${projects_count}

    Wait Until Page Contains Element    xpath=//a[normalize-space()='Courses']    20s
    Scroll Element Into View    xpath=//a[normalize-space()='Courses']
    Click Element    xpath=//a[normalize-space()='Courses']

    Wait Until Location Contains    /courses    20s
    
    ${projects_count}=      Get Element Count    xpath=//a[normalize-space()='Projects']
    Log To Console      Projects links found: ${projects_count}

    ${title}=    Get Title
    Log To Console         TITLE=${title}
    Log To Console         URl: ${url}
    Log To Console         HAS_PROJECTS_TEXT: ${has_projects}
    Log To Console         HAS_CLOUDFLARE: ${has_cloudflare}
    Log To Console         HAS_JUST_A_MOMENT: ${has_just_a_moment}
    Log To Console         HAS_VERIFY_HUMAN: ${has_verify_human}
    Log To Console         HAS_ACCESS_DENIED: ${has_access_denied}

    Page Should Contain Element    xpath=//a[normalize-space()='Projects']

    Wait Until Page Contains Element    xpath=//a[normalize-space()='Projects']    20s
    Scroll Element Into View    xpath=//a[normalize-space()='Projects']
    
    Click Element    xpath=//a[normalize-space()='Projects']

    Scroll Element Into View    xpath=//a[normalize-space()='Video Portfolio']
    Click Element    xpath=//a[normalize-space()='Video Portfolio']

    Scroll Element Into View    xpath=//a[normalize-space()='Behind The Lens']
    Click Element    xpath=//a[normalize-space()='Behind The Lens']

    Scroll Element Into View    xpath=//a[normalize-space()='Digital Art']
    Click Element    xpath=//a[normalize-space()='Digital Art']

    Scroll Element Into View    xpath=//a[normalize-space()='About']
    Click Element    xpath=//a[normalize-space()='About']

    Scroll Element Into View    xpath=//a[normalize-space()='Gaming']
    Click Element    xpath=//a[normalize-space()='Gaming']

    Scroll Element Into View    xpath=//a[normalize-space()='Reviews']
    Click Element    xpath=//a[normalize-space()='Reviews']

    Scroll Element Into View    xpath=//a[normalize-space()='blog']
    Click Element    xpath=//a[normalize-space()='blog']

    Scroll Element Into View    xpath=//a[normalize-space()='Tarun Singh']
    Click Element    xpath=//a[normalize-space()='Tarun Singh']