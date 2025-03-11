from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django_daraja.mpesa.core import MpesaClient
from rest_framework import status
from rest_framework.decorators import api_view

from student.forms import StudentForm, CourseForm
from student.models import Student, Course
from django.contrib import messages

from student.serializers import StudentSerializer, CourseDetailSerializer


# Create your views here.
def index(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
            form = StudentForm()
    return render(request, "index.html", {'form': form})

def course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("course")
    else:
            form = CourseForm()
    return render(request, "course.html", {'form': form})
def studentlist(request):
    data = Student.objects.all()
    return render(request, "studentlist.html", {'data': data})
def editstudent(request,id ):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES,instance=student)
        if form.is_valid():
            form.save()
        return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "editstudent.html",{'form': form, 'student': student})
def deletestudent(request,id ):
    student = get_object_or_404(Student, id=id)
    try:
        student.delete()
    except Exception as e:
        messages.error(request, "student not deleted")
    return redirect("student_list")
@api_view(['GET', 'POST'])
def studentapi(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def courseapi(request):
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseDetailSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        serializer = CourseDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def mpesaapi(request):
    mpesa = MpesaClient()
    phone_number = '0797710340'
    amount = 1
    account_reference = 'emobilis'
    transaction_desc = 'Payment for fullStack Course'
    callback_url = 'https://darajambili.heroku.com/express-payment';
    response = mpesa.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)



