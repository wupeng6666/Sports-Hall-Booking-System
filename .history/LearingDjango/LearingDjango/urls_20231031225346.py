"""LearingDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app01 import views
from django.contrib import admin
from django.urls import path


# urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# 导入app01 的views文件
# url和函数关系，常常要操作
urlpatterns = [
    # path('admin/', admin.site.urls),
    # www.xxx.com/index/ ->执行函数,views文件里的index函数
    path('', views.desired_page_view, name='home'),  # 定义根URL
    path('user/denglu/', views.user_denglu, name='desired_page'),
    path('user/zhuce/', views.user_zhuce),
    path('user/yuyuebiao/', views.yuyuebiao),
    path('user/shenyucishu/', views.shenyucishu),
]
