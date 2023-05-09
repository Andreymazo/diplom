"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import re_path as url

from price.views import CustomAuthToken
from rest_framework.authtoken import views
urlpatterns = [
    path('', include('price.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('/rest-auth/login/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('api-token-auth/', CustomAuthToken.as_view()),

    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api-token-auth/', views.obtain_auth_token)
    ##When using TokenAuthentication, you may want to provide a mechanism for clients to obtain a token given the username and password. REST framework provides a built-in view to provide this behaviour. To use it, add the obtain_auth_token view to your URLconf




]
urlpatterns += [
# url(r'rest-auth/', include('rest_auth.urls')),

    # path('api-auth/login/', include('rest_framework.urls')),
    # path('/rest-auth/login/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('/api/v1/rest-auth/login/', include('rest_auth.urls'))
]