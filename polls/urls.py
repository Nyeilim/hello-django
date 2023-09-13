from django.urls import path

from . import views

# 路由层, 作用类似 Spring @RequestMapping 注解
app_name = 'polls'
urlpatterns = [
    # 处理逻辑映射到 view.py 文件的 index 方法
    path('', views.index, name='index'),
    path('capture', views.capture, name='capture')
]