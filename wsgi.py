import fossiloauth
import config

uwsgi = config.uwsgi

domain_name = config.domain_name
port = config.flask_port

application = fossiloauth.app



if __name__ == "__main__":
    
    if uwsgi:
        application = fossiloauth.app
    else:
        domain_name = "127.0.0.1"
        fossiloauth.app.run(host=domain_name, port=port, ssl_context='adhoc')
        
