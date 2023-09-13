"""hello_django URL Configuration

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
from django.contrib import admin
from django.urls import path, include

# 顶层路由规则, 不会匹配 GET 和 POST 参数或域名,
# 如处理请求 https://www.example.com/myapp/?page=3 时，也只会尝试匹配 myapp/
urlpatterns = [
    path('admin/', admin.site.urls),
    # 如果路径中匹配到 polls 则截断并将剩余的部分转发到 polls.urls 更进一步匹配
    path('polls/', include('polls.urls')),
]
