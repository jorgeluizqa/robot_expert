
def factory_404_partner():

    partner = {
        'name':'Frangão',
        'email':'contato@frangao.com.br',
        'whatsapp':'11999999999',
        'business':'Restaurante'
    }

    return partner

def factory_remove_partner():
    
    partner = {
        'name':'Casarão',
        'email':'contato@casarao.com.br',
        'whatsapp':'11999999999',
        'business':'Restaurante'
    }

    return partner

def factory_enable_partner():

    partner = {
        'name':'Casa do Cabral',
        'email':'contato@cabral.com.br',
        'whatsapp':'11999999999',
        'business':'Restaurante'
    }

    return partner

def factory_disable_partner():

    partner = {
        'name':'Mercado Noite',
        'email':'contato@noite.com.br',
        'whatsapp':'11999999999',
        'business':'Supermercado'
    }

    return partner


def factory_new_partner():

    partner = {
        'name':'Pizzas Papito',
        'email':'contato@papito.com.br',
        'whatsapp':'11999999999',
        'business':'Restaurante'
    }

    return partner

def factory_dup_name():
    
    partner = {
        'name':'Adega do João',
        'email':'contato@joao.com.br',
        'whatsapp':'11999999999',
        'business':'Restaurante'
    }

    return partner

def factory_partner_list():

    p_list = [
        {       
        'name':'Adega do Pedro',
        'email':'contato@jpedro.com.br',
        'whatsapp':'13999999999',
        'business':'Conveniência'
        },
        {       
        'name':'mercabom',
        'email':'contato@mercabom.com.br',
        'whatsapp':'11999999999',
        'business':'Supermercado'
        },
        {       
        'name':'Do Papa',
        'email':'contato@papa.com.br',
        'whatsapp':'15999999999',
        'business':'Restaurante'
        }
    ]   
    
    return p_list