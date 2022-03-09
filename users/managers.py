from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def _create_user(self, name, email, dateOfBirth, password, username, **extra_fields):

        """ Create and save user with the supplied details"""

        if not email:
            raise ValueError('The email must be given')
        # username = username
        name = name
        email = self.normalize_email(email)
        dateOfBirth = dateOfBirth
        password = password
        user = self.model(email=email,name=name, dateOfBirth=dateOfBirth, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, name, email, dateOfBirth, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user( name, email, dateOfBirth, password, **extra_fields)



    def create_superuser(self, email, password, **extra_fields):
        # username = username
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must have is_staff = True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('is_active must have is_active = True.')
        return self.create_user(email=email, password=password, **extra_fields)

