from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm,
    PasswordResetForm, SetPasswordForm
)
from django.contrib.auth import get_user_model
from .models import Article, Comment, Category, User

from django.core.mail import send_mail
from django.conf import settings

import logging
User = get_user_model()


def info(msg):
    logger = logging.getLogger('command')
    logger.info(msg)


class LoginForm(AuthenticationForm):
    """
    ログインフォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる


class CreateUserForm(UserCreationForm):
    """
    ユーザー登録用フォーム
    """
    class Meta:
        model = User
        fields = ('email', 'nickname', 'agegroup')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    agegroup = forms.ChoiceField(label='年代', choices=User.AGEGROUPS)


class UpdateUserForm(forms.ModelForm):
    """
    ユーザー情報更新フォーム
    """
    class Meta:
        model = User
        fields = ('email', 'nickname', 'agegroup',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    agegroup = forms.ChoiceField(label='年代' ,choices=User.AGEGROUPS)


class MyPasswordChangeForm(PasswordChangeForm):
    """
    パスワード変更フォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MyPasswordResetForm(PasswordResetForm):
    """
    パスワード忘れたときのフォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MySetPasswordForm(SetPasswordForm):
    """
    パスワード再設定用フォーム(パスワード忘れて再設定)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ArticleForm(forms.ModelForm):
    """
    Article投稿フォーム
    """
    class Meta:
        model = Article
        fields = ('category_id', 'title', 'text', 'failure_image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    # CATEGORYS = ((e.id, e.name) for e in Category.objects.all())
    CATEGORIES = ((1, '日常'), (2, '仕事'), (3, '学校'), (4, '恋愛'), (5, '勉強'), (6, 'その他'))

    category_id = forms.ChoiceField(label='カテゴリ', choices=CATEGORIES)
    title = forms.CharField(label='タイトル', max_length=100, widget=forms.TextInput(
            attrs={'placeholder':'タイトル',}))
    text = forms.CharField(label='本文', widget=forms.Textarea(
            attrs={'placeholder':'本文', 'class':'article_text'}), max_length=2500)
    failure_image = forms.ChoiceField(label='画像選択', choices=Article.IMAGES)


class CommentForm(forms.ModelForm):
    """
    コメント投稿フォーム
    """
    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ContactForm(forms.Form):
    """
    問い合わせフォーム
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    name = forms.CharField(label='お名前', required=True,)
    email = forms.EmailField(label='メールアドレス', required=True,)
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea,  required=True)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        subject = self.cleaned_data['name']
        message = self.cleaned_data['message']
        from_email = self.cleaned_data['email']
        to = [settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, to)

