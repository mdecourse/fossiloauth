import authomatic
from authomatic.providers import oauth2

# read client_id and client_secret from safe place other than put into script
keyFile = open('./../cycu_org_secret.txt', 'r')
with open('./../cycu_org_secret.txt', 'r') as f:
    key = f.read().splitlines()

CONFIG = {
        'google': {
            'class_': oauth2.Google,
            'consumer_key': key[0],
            'consumer_secret': key[1],
            'scope': oauth2.Google.user_info_scope
        }
    }

domain_name = "c11.cycu.org"
default_repo = "pj2022"
repo_caps = "bfjk234C"
# for Windows 
repo_path = "c:/pj2022/repo/"
# for Ubuntu
#repo_path = "/home/wcm2021/repository/"
#fossil_port = "5443"
fossil_port = "443"
flask_port = "8443"
uwsgi = True

# derived
default_repo_path = repo_path+default_repo+".fossil"
flask_url = "https://"+domain_name+":"+flask_port
flask_forum = "https://"+domain_name+":"+flask_port+"/forum"
#login_url = "https://"+domain_name+":"+fossil_port+"/"+default_repo+"/login"
login_url = "https://"+domain_name+":"+fossil_port+"/login"
#forum_url = "https://"+domain_name+":"+fossil_port+"/"+default_repo+"/forum"
forum_url = "https://"+domain_name+":"+fossil_port+"/forum"
CALLBACK_URL = flask_forum
