*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${HEADLESS}     True

*** Test Cases ***
Navigation Test
    Open Browser    https:tarunsingh.co.in  chrome
    Scroll Element Into View    //a[normalize-space()='Courses']
    Click Element   //a[normalize-space()='Courses']
    Scroll Element Into View      //a[normalize-space()='Projects']
    Click Element                  //a[normalize-space()='Projects']
    Scroll Element Into View    //a[normalize-space()='Video Portfolio']
    Click Element                 //a[normalize-space()='Video Portfolio']
    Scroll Element Into View        //a[normalize-space()='Behind The Lens']
    Click Element                 //a[normalize-space()='Behind The Lens']
    Scroll Element Into View        //a[normalize-space()='Digital Art']
    Click Element                 //a[normalize-space()='Digital Art']
    Scroll Element Into View        //a[normalize-space()='About']
    Click Element                 //a[normalize-space()='About']
    Scroll Element Into View        //a[normalize-space()='Gaming']
    Click Element                 //a[normalize-space()='Gaming']
    Scroll Element Into View        //a[normalize-space()='Reviews']
    Click Element                 //a[normalize-space()='Reviews']
    Scroll Element Into View        //a[normalize-space()='blog']
    Click Element                 //a[normalize-space()='blog']
    Scroll Element Into View        //a[@href='https://tarunsingh.co.in/'][normalize-space()='Tarun Singh']
    Click Element                   //a[@href='https://tarunsingh.co.in/'][normalize-space()='Tarun Singh']