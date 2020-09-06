"""ex_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from ex_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create, name='create'),
    path('storage/',views.storage, name='storage'),

    path('index/',views.index, name='index'),

    path('<int:id>/',views.specific, name='specific'),

    path('update/<int:id>',views.update, name='update'), #update를 할 페이지를 보여줌 
    path('<int:id>/update',views.doupdate, name='doupdate'), #update를 수행하는 모습과 수행 후를 보여줌

    path('delete/<int:id>',views.delete, name='delete'),
]
