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

        if form.is_valid():

            grades_str = form.cleaned_data['grades']

            grades_int_list = list(map(int, grades_str.split(',')))
            avarage=sum(grades_int_list) / len(grades_int_list)
            print(avarage, grades_int_list)
            student = StudentModel(
                name=form.cleaned_data['name'],
                grades=form.cleaned_data['grades'],
                average_grade=avarage,
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