"""RestF2 URL Configuration

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
from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path,include
from RFD import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


router = DefaultRouter()     

router.register('stuapi',views.StudentModelViewset,basename="Student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('gettoken/',TokenObtainPairView.as_view(),name='token.obtain.pair'),
    # path('refreshtoken/',TokenRefreshView.as_view(),name='token.refresh'),
    # path('Verifytoken/',TokenVerifyView.as_view(),name='token.Verify')
    # path('gettoken1/',obtain_auth_token),
    # path('stuapi/',views.studentAPI.as_view()),
    # path('stuapi/<int:pk>/',views.studentAPI.as_view()),   
    

]
