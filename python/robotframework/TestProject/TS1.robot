*** Variables ***
${NamS}           ${EMPTY}
@{FavL}           Apple    Banana    Mango

*** Test Cases ***
TC1
    log    ${NamS[1:3]}
    log many    @{FavL[1:2]}
    log    %{path}
    ${TestVers}    Set Variable    ${2.6}    2.6

TC2
    ${NamS}    Set Variable    Cindy
    ${NameCC}    Set VariableIF    '${NamS}' =='Cindy'    Good
    ${GetCC}    Get Length    ${NameCC}
    log    ${GetCC}, 'Test'
    ${cal}    Evaluate    ${GetCC}+1
    log    '--Trans---'
    ${St1}    Set Variable    '347'
    ${St1Add}    Evaluate    int(${St1})+5

TC3
    @{Val}    Set Variable    1    2    3    4
    @{ListVal}    Create List    4    3    2    1
    Run Keyword    log    ABCD    Warn
    @{argVal}    Create List    log    EFGH    Error
    Run Keyword    @{argVal}

TC4
    @{ListA}    Create List    1    2
    @{ListB}    Create List    3    4
    @{ListC}    Create List    ${ListA}    5
    @{ListD}    Create List    ${ListB}    6
    @{ListE}    Create List    ${ListC}    ${ListD}
    log    ${ListE}
    log    @{ListE[1][0]}[1]
