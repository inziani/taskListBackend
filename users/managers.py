from django.contrib.auth.models import BaseUserManager

class UserManager():
    def _create_user(self, email, username, name, password, **extra_fields):

        """ Create and save user with the supplied details"""

        if not email:
            raise ValueError('The email must be given')
        username = username
        password = password
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        username = username
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must have is_staff = True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('is_active must have is_active = True.')
        return self.create_user(email, password, username, **extra_fields)

