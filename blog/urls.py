from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'), 
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_pk>/reply/', views.add_reply, name='add_reply'),
    path('comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete')
]