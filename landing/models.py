from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, username, nickname,password=None):
        """
        Creates and saves a User with the given username, nickname and password.
        """

        user = self.model(
            username=username,
            nickname=nickname,
            date_joined=timezone.now(),
            is_superuser=0,
            is_staff=0,
            is_active=1
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, password=None):
        """
        Creates and saves a superuser with the given username, nickname, password.
        """
        user = self.create_user(
            username=username,
            nickname=nickname,
            password=password,
        )
        user.is_superuser = 1
        user.is_staff = 1
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    is_superuser = models.IntegerField()
    nickname = models.CharField(max_length=150, null=False)
    date_joined = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = 'auth_user'# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BoardCategories(models.Model):
    category_type = models.CharField(max_length=45, blank=True, null=True)
    category_code = models.CharField(max_length=100, blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    category_desc = models.CharField(max_length=200, blank=True, null=True)
    list_count = models.IntegerField(blank=True, null=True)
    authority = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board_categories'

class Review_search_task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    search_keyword = models.CharField(max_length=50,blank=True,null=True)
    registered_date = models.DateField(blank=True,null=True,auto_now_add=True)
    last_update = models.DateField(blank=True,null=True)
    class Meta:
        managed = False
        db_table = 'review_search_task'

class Review_product(models.Model):
    search_keyword = models.CharField(max_length=50,blank=True,null=True)
    review_search_task = models.ForeignKey(Review_search_task, on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField(blank=True,null=True)
    link =  models.TextField(blank=True,null=True)
    image = models.TextField(blank=True,null=True)
    lprice = models.TextField(blank=True,null=True)
    hprice = models.TextField(blank=True,null=True)
    mallName = models.TextField(blank=True,null=True)
    productId = models.TextField(blank=True,null=True)
    productType = models.TextField(blank=True,null=True)
    brand = models.TextField(blank=True,null=True)
    maker = models.TextField(blank=True,null=True)
    category1 = models.TextField(blank=True,null=True)
    category2 = models.TextField(blank=True,null=True)
    category3 = models.TextField(blank=True,null=True)
    category4 = models.TextField(blank=True,null=True)
    class Meta:
        managed = False
        db_table = 'review_product'

class Datacast_request(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    analysis_type = models.SmallIntegerField(blank=False,null=False,default=0)
    request_json = models.CharField(max_length=500, blank=False,null=False)
    request_time= models.DateTimeField(null=False, auto_now_add=True)
    request_status = models.SmallIntegerField(default=0)
    class Meta:
        managed = False
        db_table = 'datacast_request'

class Datacast_batch(models.Model):
    keyword = models.CharField(max_length=300, blank=True, null=True)
    product = models.CharField(max_length=300, blank=True, null=True)
    channel = models.CharField(max_length=300, blank=True, null=True)
    post_date = models.DateField(blank=True, null=False)
    class Meta:
        managed = False
        db_table = 'datacast_batch'

class Datacast_request_batch(models.Model):
    datacast_request = models.ForeignKey(Datacast_request,on_delete=models.CASCADE, blank=True, null=True)
    datacast_batch = models.ForeignKey(Datacast_batch,on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'datacast_request_batch'

class Boards(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    registered_date = models.DateTimeField(blank=True, null=False, auto_now_add=True)
    last_update_date = models.DateTimeField(blank=True, null=False)
    gather_st_time = models.DateTimeField(blank=True, null=True)
    gather_en_time = models.DateTimeField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    keywordA = models.CharField(max_length=300, blank=True, null=True)
    keywordB = models.CharField(max_length=300, blank=True, null=True)
    channel = models.CharField(max_length=300, blank=True, null=True)
    periodStartA = models.DateField(blank=True, null=False)
    periodEndA = models.DateField(blank=True, null=False)
    periodStartB = models.DateField(blank=True, null=False)
    periodEndB = models.DateField(blank=True, null=False)
    status = models.CharField(max_length=300, blank=True, null=False, default='분석요청')
    nTotal = models.IntegerField(blank=True, null=True)
    nCrawl = models.IntegerField(blank=True, null=False, default=500, help_text='기본값은 500으로 자동 입력됩니다.')
    nCrawled = models.IntegerField(blank=True, null=True)
    analysis_type = models.CharField(max_length=100,null=False,default=False)
    analysis_how = models.CharField(max_length=100, null=False, default=False)
    saved_path = models.CharField(max_length=300,blank=True,null=True)
    saved_name = models.CharField(max_length=300, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'boards'

class Boards_keyword_number(models.Model):
    boards = models.ForeignKey(Boards, on_delete=models.CASCADE, blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    analysis_type = models.CharField(max_length=100,blank=True,null=True)
    A_top300 = models.TextField(blank=True,null=True)
    B_top300 = models.TextField(blank=True, null=True)
    AB_top300 = models.TextField(blank=True, null=True)
    class Meta:

        managed = False
        db_table = 'boards_keyword_number'