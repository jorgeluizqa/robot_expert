*Settings*
Documentation           POST /partners

Resource        ${EXECDIR}/resources/base.robot

*Test Cases*
Should create a new partner

    ${payload}     Factory New Partner
    
    Remove Partner By Name      ${payload}[name]

    ${response}  Post Partner   ${payload}

    Status Should Be  201
    ${result}        Find Partner By name        ${payload}[name]
    Should Be Equal      ${response.json()}[partner_id]      ${result}[_id]      

Should return duplicate company name

    ${payload}     Factory Dup Name
    
    Remove Partner By Name      ${payload}[name]
    POST Partner                ${payload}

    ${response}  Post Partner   ${payload}
    Status Should Be  409

    Should Be Equal      ${response.json()}[message]      Duplicate company name    