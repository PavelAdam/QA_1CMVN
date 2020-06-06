*** Settings ***
Library  SeleniumLibrary


*** Variables ***


*** Test Cases ***
RegisterTest
    open browser    https://1cm.vn/     chrome
    click link  xpath://*[@id="name-home"]
    input text  id:Name     robot TestCases\TC1.robotFull Name


*** Keywords ***