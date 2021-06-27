import fossiloauth
from config import site

uwsgi = True

domain_name = site[0]
port = site[1]

application = fossiloauth.app



if __name__ == "__main__":
    
    if uwsgi:
        application = fossiloauth.app
    else:
        fossiloauth.app.run(host=domain_name, port=port, ssl_context='adhoc')
        
