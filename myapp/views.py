from django.shortcuts import render, redirect
from django.contrib import messages
from myapp.forms import StudentForm
from myapp.models import Student
# Create your views here.

def home(request):
    if request.method == "POST":
        fm = StudentForm(request.POST,  request.FILES)
        if fm.is_valid():
            # name = fm.cleaned_data('name')
            # age = fm.cleaned_data('age')
            # add = fm.cleaned_data('address')
            # img = fm.cleaned_data('image')

            # stu = Student.objects.create(name = name, age = age, address = add, image = img)
            # stu.save()
            fm.save()
            messages.success(request, "form Submitted successfully !")
            return redirect('myapp:home')
    else:
        fm = StudentForm()
    data = Student.objects.all()
    context = {'fm':fm, 'data':data}
    return render(request, 'index.html', context)