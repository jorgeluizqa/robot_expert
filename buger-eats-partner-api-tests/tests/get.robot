*Settings*
Documentation           GET /partners

Resource        ${EXECDIR}/resources/base.robot

Suite Setup     Create Partner List

*Test Cases*
Should return a partner list

   ${response}     GET Partners
    status Should Be    200

    ${size}     Get Length      ${response.json()}

    Should Be True      ${size} > 0

Should search partner by name

    ${response}     Search Partner      Do Papa     

    status Should Be    200

    ${size}     Get Length      ${response.json()}

    Should Be True      ${size} == 1

    Should Be Equal     ${response.json()}[0][name]      Do Papa

*Keywords*

Create Partner List

     ${partners}     Factory Partner List

    FOR     ${p}    IN  @{partners}
        POST Partner    ${p}      
    END 


