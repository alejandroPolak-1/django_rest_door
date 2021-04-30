from rest_framework.authentication import get_authorization_header #para agarrar el token, y validar dentro la información
from open_door_api.authenticationExpiringToken import ExpiringTokenAuthentication

class Authentication(object):
    
    def get_user(self,request):
        token = get_authorization_header(request).split()     
        if token:
            print(token)
        return None
    
    # dispatch metodo que toda clase de Django ejecuta primero, aqui interrumpiremos la secuencia
    def dispatch(self, request, *args, **kwargs):
        
        return super(CLASS_NAME, self).dispatch(request, *args, **kwargs)
    