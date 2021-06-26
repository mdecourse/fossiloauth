import authomatic
from authomatic.providers import oauth2

site = ["fossil.kmol.info", "8443"]
domain_name = site[0]
port = site[1]
CALLBACK_URL = "https://"+domain_name+":"+port

# read Fossil SCM repository username and password for testing
with open('./../fossil_user.txt', 'r') as f:
    fossil = f.read().splitlines()
# user_name = fossil[0]
# password = fossil[1]

# read client_id and client_secret from safe place other than put into script
# current setting only allow @gm user login
keyFile = open('./../scrum2_client_secret.txt', 'r')
with open('./../scrum2_client_secret.txt', 'r') as f:
    key = f.read().splitlines()

CONFIG = {
        'google': {
            'class_': oauth2.Google,
            'consumer_key': key[0],
            'consumer_secret': key[1],
            'scope': oauth2.Google.user_info_scope
        }
    }