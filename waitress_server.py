# pip install waitress
from waitress import serve

# under cmsimde import fossilapp
import fossiloauth

# run cmsimde dynamic site with production waitress
serve(fossiloauth.app, host='127.0.0.1', port=5000, url_scheme='https')