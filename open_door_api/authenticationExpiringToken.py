
from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

# Tiempo de expiración lo definimos en el setting

class ExpiringTokenAuthentication(TokenAuthentication):
    '''
    SobreEscribimos el metodo de TokenAutenticathion
    Para limitar tiempo del token
    Necesita un token
    
    En: settings.TOKEN_EXPIRED_AFTER_SECONDS definimos los segundos para que expire
    '''
    expired = False
    
    def expires_in(self,token):
        # return left time of token
        time_elapsed = timezone.now() - token.created   #Tiempo que ha pasado
        left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed #tiempo que falta
        return left_time
    def is_token_expired(self,token):
        '''
        # Indica si el toquen ha expirado
        '''
        # return True if token is alive or False if token is expired
        return self.expires_in(token) < timedelta(seconds = 0) #si es menor a la hora a actual

    def token_expire_handler(self,token):
        """
        Return:
            * is_expire     : True if token is alive, False if token is expired
            * token         : New token or actual token
        """
        is_expire = self.is_token_expired(token)
        if is_expire:
            self.expired = True
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user = user)
        
        return is_expire,token

    # Sobreescribimos este metodo de TOKENAUTENTIATION para poner tiempo de expiración del token
    # gran parte de la estructura es similar al metodo original, se agrega parte expired
    def authenticate_credentials(self,key):
        """
        Return:
            * user      : Instance User that sended request
            * token     : New Token or actual token for user
            * message   : Error message
            * expired   : True if token is alive or False if token is expired
        """
        message,token,user = None,None,None
        try:
            token = self.get_model().objects.select_related('user').get(key = key) #getModel ya importa el token y retorna la CLase Token
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Invalid token.'
            self.expired = True

        if token is not None:
            if not token.user.is_active:
                message = 'User inactive or deleted.'

            is_expired = self.token_expire_handler(token)
            
            if is_expired:
                message = 'Token expired.'

        return (user,token,message,self.expired)

