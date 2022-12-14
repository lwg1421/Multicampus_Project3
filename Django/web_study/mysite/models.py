from django.db import models


# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    create_date = models.DateField()


class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.postname


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MenuScoreAll(models.Model):
    menu = models.TextField(blank=True, null=True)
    restaurant = models.TextField(blank=True, null=True)
    happy_winter = models.FloatField(blank=True, null=True)
    happy_winter_snow = models.FloatField(blank=True, null=True)
    happy_winter_rain = models.FloatField(blank=True, null=True)
    happy_fall = models.FloatField(blank=True, null=True)
    happy_fall_rain = models.FloatField(blank=True, null=True)
    happy_summer = models.FloatField(blank=True, null=True)
    happy_summer_rain = models.FloatField(blank=True, null=True)
    happy_spring = models.FloatField(blank=True, null=True)
    happy_spring_rain = models.FloatField(blank=True, null=True)
    sad_spring_rain = models.FloatField(blank=True, null=True)
    sad_spring = models.FloatField(blank=True, null=True)
    sad_summer_rain = models.FloatField(blank=True, null=True)
    sad_summer = models.FloatField(blank=True, null=True)
    sad_fall_rain = models.FloatField(blank=True, null=True)
    sad_fall = models.FloatField(blank=True, null=True)
    sad_winter_rain = models.FloatField(blank=True, null=True)
    sad_winter = models.FloatField(blank=True, null=True)
    sad_winter_snow = models.FloatField(blank=True, null=True)
    angry_winter = models.FloatField(blank=True, null=True)
    angry_winter_snow = models.FloatField(blank=True, null=True)
    angry_winter_rain = models.FloatField(blank=True, null=True)
    angry_fall = models.FloatField(blank=True, null=True)
    angry_fall_rain = models.FloatField(blank=True, null=True)
    angry_summer = models.FloatField(blank=True, null=True)
    angry_summer_rain = models.FloatField(blank=True, null=True)
    angry_spring = models.FloatField(blank=True, null=True)
    angry_spring_rain = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_score_all'


class MysiteAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=200)
    create_date = models.DateField()
    question = models.ForeignKey('MysiteQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mysite_answer'


class MysitePost(models.Model):
    id = models.BigAutoField(primary_key=True)
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    mainphoto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mysite_post'


class MysiteQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    content = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'mysite_question'


class resultall(models.Model):
    restaurant = models.CharField(max_length=300)
    menu = models.CharField(max_length=300)
    emotion = models.CharField(max_length=300, null=True, default='')
    season = models.CharField(max_length=300, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"({self.season},{self.emotion})"


class fullist(models.Model):
    emot = models.CharField(max_length=300, null=True)
    sea = models.CharField(max_length=300, null=True)
    first= models.CharField(max_length=300, null=True)
    second= models.CharField(max_length=300, null=True)
    third = models.CharField(max_length=300, null=True)
    cr_at = models.DateTimeField(auto_now_add=True, null=True)
    fourth = models.CharField(max_length=300, null=True)
    fifth = models.CharField(max_length=300, null=True)
    wea = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return f"({self.emot},{self.sea})"

class choice(models.Model):
    res = models.CharField(max_length=300,null=True)
    menu = models.CharField(max_length=300,null=True)
    emotion = models.CharField(max_length=300,null=True)
    cr_at = models.DateTimeField(auto_now_add=True, null =True)
    weather = models.CharField(max_length=300,null=True)
    season = models.CharField(max_length=300,null=True)

    def __str__(self):
            return f"({self.res})"


