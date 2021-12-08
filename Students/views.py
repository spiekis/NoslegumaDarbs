from django.shortcuts import render



from .models import StudentModel

from .forms import (
    CreateStudentForm,

)
# Create your views here.

class Student:
    def __init(self):
        self.name = 'Andris'
        self.grades=[7, 4, 10],

    def get_avarage_grade(self):
        avarage = sum(grades) / len(grades)
        return avarage
#te vēl jāpadomā :)

grades_tmp = ''
avarage_tmp = ''
grades_tmp2 = []
def add_student(request):

    form = CreateStudentForm(request.POST or None)

    if request.method == 'POST':
        #grades_tmp = []
        if form.is_valid():
            #grades_tmp = []
            #grades_tmp = form.cleaned_data['grades'].split(',')
            grades_tmp2=grades_tmp.split(',')
            #avarage_tmp=sum(grades_tmp) / len(grades_tmp)
            print(grades_tmp, avarage_tmp)
            student = StudentModel(
                name=form.cleaned_data['name'],
                grades=form.cleaned_data['grades'],
                average_grade=3,
            )

            student.save()

            context = {
                'student': student,
            }

            return render(
                request,
                template_name='student.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='add_student.html',
        context=context,
    )



def get_students(request):
    students = StudentModel.objects.all()
    context = {
        'students': students,
    }

    return render(
        request,
        template_name='students.html',
        context=context,
    )

def get_student(request, student_id):
    student = StudentModel.objects.get(id=student_id)
    context = {
        'student': student,
    }

    return render(
        request,
        template_name='student.html',
        context=context,
    )