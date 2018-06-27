from django.urls import path
from . import views

app_name = 'nikki'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('search/', views.SearchList.as_view(), name='search'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('rules/', views.RulesView.as_view(), name='rules'),
    path('privacy/', views.PrivacyView.as_view(), name='privacy'),
    # User
    path('create_user/', views.CreateUser.as_view(), name='create_user'),
    path('create_user/done', views.CreateUserDone.as_view(), name='create_user_done'),
    path('create_user/complete/<uidb64>/<token>/', views.CreateUserComplete.as_view(), name='create_user_complete'),
    path('user_detail/<int:pk>/', views.DetailUser.as_view(), name='detail_user'),
    path('user_update/<int:pk>/', views.UpdateUser.as_view(), name='update_user'),
    path('user_delete/<int:pk>/', views.DeleteUser.as_view(), name='delete_user'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
    # Article
    path('create_article/<int:user_id>', views.create_article, name='create_article'),
    path('detail_article/<int:pk>', views.DetailArticle.as_view(), name='detail_article'),
    path('update_article/<int:pk>', views.update_article, name='update_article'),
    path('delete_article/<int:pk>', views.DeleteArticle.as_view(), name='delete_article'),
    path('author_articles/<int:user_id>', views.AuthorArticles.as_view(), name='author_articles'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    # Comment
    path('comment/<int:article_id>', views.create_comment, name='comment'),
    path('detail_comment/<int:pk>', views.DetailComment.as_view(), name='detail_comment'),
    path('update_comment/<int:pk>', views.UpdateComment.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>', views.DeleteComment.as_view(), name='delete_comment'),

]
