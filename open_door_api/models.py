from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


from django.contrib.auth.hashers import make_password, check_password


class UserProfileManager(BaseUserManager):
    """ Manager for user profile """
    def create_user(self, email, name, dni, password=None):
        ''' Create a new User Profile'''
        if not email: 
            raise ValueError('You need have an email')
        #convertir en lowerCase
        email = self.normalize_email(email)

        user  =  self.model(email=email, name=name, dni= dni)
        
        #usuario necesita password
        user.set_password(password)
        #guardado en hash
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email,name, dni, password):
        user              = self.create_user(email, name, dni, password)
        
        user.is_superuser = True
        user.is_staff     = True
        user.save(using=self._db) 
        
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    ''' Modelo base de Datos para usuarios en el sistema'''
    email        = models.EmailField(max_length=255, unique=True)
    name         = models.CharField(max_length=255)
    dni          = models.CharField(max_length=20)
    movil_user   = models.BooleanField(default=False) ##Una vez autenticado la aplicación en el Celular
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)
   
    # para manejar modelo de usuario, (para actualizar, borrar y crear usuarios)
    objects = UserProfileManager()
    
    # Campo de Login
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name', 'dni']

    # funcion que devuelve string al consultar el nombre
    def get_full_name(self):
        '''Obtener nombre completo'''
        return self.name
    
    def __str__(self):
        '''Retorna cadena representando nuestro usuario'''
        return self.email


class Door(models.Model):
    id         = models.AutoField(primary_key=True) #Modelo autoincremental
    name       = models.CharField(max_length=255)
    hash       = models.CharField(max_length=100)
    users_door = models.ManyToManyField(UserProfile)
      
    # funcion que devuelve string al consultar el nombre
    def get_doors(self):
        '''Obtener puertas'''
        return self.name
    
    def get_users(self):
        '''Obtener puertas'''
        return self.users_door

    def __str__(self):
        # return "%s %s" % (self.name, self.users)
        return "{},{}".format(self.name, self.users_door)


    
