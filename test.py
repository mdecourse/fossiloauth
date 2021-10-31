import config

def ecprint(input):
    try:
        g.es(input)
    except:
        print(input)
        
ecprint(config.domain_name)