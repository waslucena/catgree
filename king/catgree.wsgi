import os, sys
sys.path.append('/home/tbridge/apps_wsgi')
sys.path.append('/home/tbridge/apps_wsgi/catgree')

HOME = os.getcwd()
apps_home = HOME + "/apps_wsgi/"
sys.path.append(apps_home)

nome_app = "catgree"
virtual_env = HOME + "/.virtualenvs/" + nome_app
app_path = apps_home + nome_app
sys.path.append(app_path)
activate_this = virtual_env + "/bin/activate_this.py"
with open(activate_this) as file_: 
  exec(file_.read(), dict(__file__=activate_this))

os.environ['PYTHON_EGG_CACHE'] = '/home/tbridge/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'catgree.settings'

os.environ['ALLOWED_HOSTS'] = 'www.tbridge.com.br,catgree.tbridge.com.br'
os.environ['DATABASE_URL'] = 'postgres://tbridge:pos.kin8@pgsql.tbridge.com.br:5432/tbridge'
os.environ['DEBUG'] = 'True'
#os.environ['DEBUG'] = 'False'
os.environ['SECRET_KEY'] = 'u*ki-nneljqvcv6beh%omc7+*(fk0r@#z(yhz7%r56jl8)@f(v'

# https://integricho.github.io/2014/02/22/running-django-on-a-subpath/
os.environ['HTTP_X_SCRIPT_NAME'] = '/catgree/'
#os.environ['PATH_INFO'] = ''
#os.environ['HTTP_X_SCHEME'] = 'http'

#from run import app as application 
#if __name__ == "__main__": application.run()

from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

_application = get_wsgi_application()


def application(environ, start_response):
    script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
    if script_name:
        environ['SCRIPT_NAME'] = script_name
        path_info = environ['PATH_INFO']
        if path_info.startswith(script_name):
            environ['PATH_INFO'] = path_info[len(script_name):]

    scheme = environ.get('HTTP_X_SCHEME', '')
    if scheme:
        environ['wsgi.url_scheme'] = scheme

    print('HTTP_X_SCRIPT_NAME')
    print(script_name)
    print('PATH_INFO')
    print(environ.get('PATH_INFO',''))
    #print(path_info)
    print('HTTP_X_SCHEME')
    print(scheme)

    return _application(environ, start_response)


