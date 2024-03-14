from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('dashboard/', views.HomePage, name='dashboard'),
    path('blog/', views.blog, name='blog'),
    path('subscription/', views.subscription_page, name='subscription_page'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('edit/<int:category_id>/<int:post_id>/', views.edit, name='edit'),
    path('create-subscription/<str:plans>/', views.create_subscription, name='create_subscription'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)