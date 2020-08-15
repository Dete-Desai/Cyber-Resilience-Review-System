"""crrs_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from accounts.views import Login,Registration,crrshome, LogOut, UserProfile,Access
from crrs_app.views import GoalChartView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('crrs_app.urls')),


    #AUTHENTICATION

    #Login
    path('Login/', Login, name='Login'),

    #Registration
    path('Registration/', Registration, name='Registration'),

    #LoginOut
    path('LogOut/', LogOut, name='LogOut'),

    #Home
    path('', crrshome, name='home'),

    #UserProfile
    path('UserProfile/', UserProfile, name='UserProfile'),

    #Access
    path('Access/', Access, name='Access'),

    #GoalChart
    path('GoalChartView/', GoalChartView.as_view(), name='GoalChartView'),

]