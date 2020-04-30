from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class UserManager(BaseUserManager):

    def create_user(self, phone, password=None, first_name=None, last_name=None, email=None, address_house_street=None, address_area=None, city=None, pincode=None, is_staff=False, is_active=True, is_admin=False, fcm_token=None):

        if not phone:
            raise ValueError('users must have a valid phone number')
        if not password:
            raise ValueError('user must have a password')

        user_obj = self.model(
            phone = phone
        )
        user_obj.set_password(password)
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.email = self.normalize_email(email)
        user_obj.address_house_street = address_house_street
        user_obj.address_area = address_area
        user_obj.city = city
        user_obj.pincode = pincode
        user_obj.fcm_token = fcm_token
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, phone, password=None):

        user = self.create_user(
            phone,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

class CustomUser(AbstractBaseUser):

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',message="Phone number must be entered in the format:'+9999999999'. Up to 14 digists allowed.")
    phone = models.CharField(validators=[phone_regex], max_length = 15,unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True);
    email_verified = models.BooleanField(blank=True, null=True)
    address_house_street = models.CharField(max_length=60,blank=True, null=True)
    address_area = models.CharField(max_length=30,blank=True, null=True)
    city = models.CharField(max_length=20,blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    user_attributes = models.CharField(max_length=1000,blank=True, null=True)
    first_login = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    fcm_token = models.CharField(max_length=500,blank=False, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone

    def get_full_name(self):
        if self.first_name:
            if self.last_name:
                return self.first_name+" "+self.last_name
            else:
                return self.first_name
        else:
            return self.phone

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def convertToJson(self):
    
        user_json = {
            "phone":self.phone,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "email":self.email,
            "address_house_street":self.address_house_street,
            "address_area":self.address_area,
            "city":self.city,
            "pincode":self.pincode,
            "first_login":self.first_login,
            "active":self.active,
            "staff":self.staff,
            "admin":self.admin,
            "fcm_token":self.fcm_token,
            "email_verified":self.email_verified
            }
        return user_json