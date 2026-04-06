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

Jump To 
    [Arguments]     ${text}
    Execute javascript         window.location.href = document.evaluate("//a[normalize-space()='${text}']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.href + "?cf_secret=${CF_TEST_SECRET}"

*** Test Cases ***
Navigation Test
    Open Chrome For CI
    Go To       ${BASE_URL}/?cf_secret=${CF_TEST_SECRET}
     
    Wait Until Page Contains Element    xpath=//a[normalize-space()='Courses']    20s

    ${title}=       Get Title
    ${url}=         Get Location
    ${html}=        Get Source
    ${html_lower}=      Convert To Lower Case        ${html}

    ${has_courses}=     Evaluate       "Courses" in $html
    ${has_projects}=     Evaluate       "Projects" in $html
    ${has_cloudflare}=  Evaluate        "cloudflare" in $html_lower
    ${has_just_a_moment}=   Evaluate    "just a moment" in $html_lower
    ${has_verify_human}=    Evaluate    "verify you are human" in $html_lower
    ${has_access_denied}=   Evaluate    "access denied" in $html_lower

    Log To Console         Title: ${title}
    Log To Console         URl: ${url}
    Log To Console         HAS_COURSES_TEXT: ${has_courses}
    Log To Console         HAS_Project_TEXT: ${has_projects}
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
    Jump To         Courses
    Sleep           2s

    Wait Until Location Contains    /courses    20s
    
    ${projects_count}=      Get Element Count    xpath=//a[normalize-space()='Projects']
    Log To Console      Projects links found: ${projects_count}

    ${title}=    Get Title
    Log To Console         TITLE=${title}
    Log To Console         URl: ${url}
    Log To Console         HAS_Project_TEXT: ${has_projects}
    Log To Console         HAS_CLOUDFLARE: ${has_cloudflare}
    Log To Console         HAS_JUST_A_MOMENT: ${has_just_a_moment}
    Log To Console         HAS_VERIFY_HUMAN: ${has_verify_human}
    Log To Console         HAS_ACCESS_DENIED: ${has_access_denied}

    ${html}=            Get Source
    ${has_projects}=    Evaluate        "Projects" in $html
    Jump To         Projects
    Sleep           2s

    Wait Until Page Contains Element    xpath=//a[normalize-space()='Video Portfolio']    20s  

    
    Jump To      Video Portfolio
    Jump To      Behind The Lens
    Jump To      Digital Art
    Jump To      About
    Jump To      Gaming
    Jump To      Reviews
    Jump To      blog
    Jump To      Tarun Singh