from django.core import serializers
from django.db import transaction
from django.db.models import F
from django.shortcuts import render, HttpResponse, redirect
# 重要，常常动，视图
# Create your views here.
from django.http import JsonResponse
from django.contrib import messages
from app01 import models
from django.core.exceptions import ObjectDoesNotExist
import json


def user_zhuce(request):
    if request.method == "GET":
        return render(request, "user_denglu.html")
    else:
        zhuce_xuehao = request.POST.get('zhuce_xuehao')
        zhuce_username = request.POST.get('zhuce_username')
        zhuce_chances = 10

        if not zhuce_xuehao or not zhuce_username:
            # messages.error(request, '学号和姓名不能为空')
            # return redirect('register')
            return JsonResponse({"success": False, "msg": "学号和姓名不能为空"})

        # 创建新用户
        try:
            models.Student.objects.create(
                student_number=zhuce_xuehao,
                student_name=zhuce_username,
                student_chances=zhuce_chances
            )
            # messages.success(request, '注册成功，请登录')
        except Exception as e:
            return JsonResponse({"success": False, "msg": "注册失败"})
        return JsonResponse({"success": True})


def user_denglu(request):
    if request.method == "GET":
        return render(request, "user_denglu.html")
    else:
        denglu_username = request.POST.get("denglu_username")
        denglu_xuehao = request.POST.get("denglu_xuehao")

        try:
            models.Student.objects.get(
                student_name=denglu_username, student_number=denglu_xuehao)
        except models.Student.DoesNotExist:
            return JsonResponse({"success": False, "msg": "学号或姓名错误或未注册"})

    # 如果登录成功，返回用户信息（以 JSON 格式）
    return JsonResponse({"success": True, "yuyue_name": denglu_username, "yuyue_xuehao": denglu_xuehao})


@transaction.atomic
def yuyuebiao(request):
    if request.method == 'POST':
        # 获取表单数据
        yuyue_day = request.POST.get('yuyue_day')
        yuyue_time = request.POST.get('yuyue_time')
        yuyue_gym = request.POST.get('yuyue_gym')
        yuyue_name = request.POST.get('yuyue_name')
        yuyue_hao = request.POST.get('yuyue_hao')

        if not yuyue_day or not yuyue_time or not yuyue_gym or not yuyue_name or not yuyue_hao:
            return JsonResponse({"success": False, "msg": "预约信息不能为空"})

        try:
            # 查询是否已经有相同的预约记录
            record = models.Comeing_time.objects.filter(
                yuyue_time=yuyue_time, yueye_xingqi=yuyue_day, gym_name__gym_name=yuyue_gym).first()
            if record:
                # 已经有相同的预约记录，直接更新该记录的 now_people 字段
                updated_count = models.Comeing_time.objects.filter(
                    pk=record.pk).update(now_people=F('now_people') + 1)
                print(updated_count)  # 打印更新的记录数量
            else:
                # 创建新的预约记录
                created_record = models.Comeing_time.objects.create(
                    yuyue_time=yuyue_time,
                    yueye_xingqi=yuyue_day,
                    gym_name=models.Gym.objects.get(gym_name=yuyue_gym),
                    student_name=models.Student.objects.get(
                        student_name=yuyue_name),
                    student_number=models.Student.objects.get(
                        student_number=yuyue_hao)
                )
                print(created_record)  # 打印创建的记录对象
            # 查询所有预约记录并序列化为JSON格式
            queryset = models.Comeing_time.objects.all()
            # queryset = models.Comeing_time.objects.values('yuyue_time', 'yueye_xingqi', 'gym_name', 'student_number')
            serialized_data = serializers.serialize('json', queryset)
            dataa = json.loads(serialized_data)
            # 将JSON数据作为响应返回给前端
            return JsonResponse({"success": True, "msg": "预约成功", "dataa": dataa})

        except:
            return JsonResponse({"success": False, "msg": "预约失败"})

    else:
        return JsonResponse({"success": False, "msg": "请使用 POST 方法提交数据"})
    # 在处理完所有情况后，都返回一个 HttpResponse 对象
    return JsonResponse({"success": False, "msg": "处理请求失败"})


def shenyucishu(request):
    if request.method == 'POST':
        try:
            yuyue_hao = request.POST.get('yuyue_hao')
            obj = models.Student.objects.get(student_number=yuyue_hao)
            obj.student_chances -= 1
            obj.save()
            queryset = models.Student.objects.all()
            serialized_data = serializers.serialize('json', queryset)
            dataa = json.loads(serialized_data)
            # 将JSON数据作为响应返回给前端
            return JsonResponse({"success": True, "msg": "预约成功", "dataa": dataa})
        except models.Student.DoesNotExist:
            return JsonResponse({"success": False, "msg": "找不到对应的学生记录"})
        except:
            return JsonResponse({"success": False, "msg": "改变剩余次数失败"})







