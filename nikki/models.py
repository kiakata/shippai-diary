# coding: utf-8

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    ユーザーマネージャー
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        メールアドレスでの登録を必須にする
        """

        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        is_staff(管理サイトにログインできるか)と、is_superuer(全ての権限)をFalseに
        """

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        スーパーユーザーは、is_staffとis_superuserをTrueに
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    カスタムユーザーモデル
    """
    email = models.EmailField(_('email address'), unique=True)
    nickname = models.CharField(_('ニックネーム'), max_length=50, blank=True)
    agegroup = models.CharField('年代', max_length=10, blank=False)
    # gender = models.CharField('性別', max_length=2, blank=True)

    AGEGROUPS = (('10歳未満', '10歳未満'), ('10代', '10代'), ('20代', '20代'), ('30代', '30代'),
    ('40代', '40代'), ('50代', '50代'), ('60代', '60代'), ('70代', '70代'), ('80代', '80代'), ('90歳以上', '90歳以上'))


    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    # NICKNAME_FIELD = 'nickname'
    # USERAGE_FIELD = 'age'
    # USERGENDER_FIELD = 'gender'

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        """username属性のゲッター

        他アプリケーションが、username属性にアクセスした場合に備えて定義
        メールアドレスを返す
        """
        return self.email


class Category(models.Model):
    """
    カテゴリ
    """
    name = models.CharField('カテゴリ名', max_length=10)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    日記記事
    """
    title = models.CharField('タイトル', max_length=255, blank=False ,null=False)
    text = models.TextField('本文', max_length=1000, blank=False ,null=False)
    created_at = models.DateTimeField('作成日時', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='ユーザー名', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='カテゴリー名', on_delete=models.PROTECT)
    failure_image = models.IntegerField('失敗の画像イメージ', blank=False, null=True)

    IMAGES = ((0, '該当なし'), (1, '【１】'), (2, '【２】'), (3, '【３】'), (4, '【４】'), (5, '【５】'), (6, '【６】'), )

    def __str__(self):
        return self.title


class Comment(models.Model):
    """"
    ブログのコメント
    """
    text = models.TextField('本文')
    user = models.ForeignKey(User, verbose_name='ユーザー名', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name='紐づく記事', on_delete=models.CASCADE)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日時', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.text[:10]
