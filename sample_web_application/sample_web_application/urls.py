"""sample_web_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home_view),
    path('menu/',views.menu_view),
    path('about/',views.about_us_view),
    path('contact/',views.contact_info_view),
    path('review/',views.review_view),
    path('view_review/',views.view_review),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/',views.signup_view),
    path('signin/',views.signin_view)

]
