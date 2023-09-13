from django.shortcuts import render

# Create your views here.
from django.http import *


# 视图层, 书写响应逻辑, 作用类似 Spring Boot Controller
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# 捕获单帧
def capture(request):
    file_count = request.FILES.__len__()
    if file_count == 1:
        ret_file = _process(list(request.FILES.values())[0])
        return HttpResponse(ret_file, content_type='image/jpeg')
    else:
        return HttpResponseBadRequest()


# 模型处理, 此处缺省
def _process(file):
    return file
