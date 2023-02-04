from django.shortcuts import render, get_object_or_404
from .models import Teacher
from django.utils.crypto import get_random_string


# Create your views here.
def view_teachers(request, pk=None) -> render:
    if 'create' in request.path:
        kravtz = Teacher.objects.filter(first_name='Кравец')
        if not kravtz:
            Teacher.objects.create(first_name='Кравец',
                                   second_name='Боб',
                                   birth_day='2000-12-15',
                                   email='bob@kravetx.eau',
                                   phone='+998901002030'
                                   )
        else:
            teacher_tmp = Teacher.objects.filter(first_name='Кравец').first()
            teacher_tmp.second_name = get_random_string(length=10, allowed_chars='АБВГДЕЁЖЗИКЛМНОПРСТУФХЧШЩЭЮЯ')
            teacher_tmp.email = get_random_string(length=6,
                                                  allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789') + '@kravetz.eau'
            teacher_tmp.phone = '+' + get_random_string(length=13, allowed_chars='0123456789')
            teacher_tmp.save()

    if not pk:
        template_ = 'teachers.html'
        teachers = Teacher.objects.all()
        context = {
            'teachers': teachers
        }
    else:
        current_teacher = get_object_or_404(Teacher, pk=pk)
        teachers = Teacher.objects.all()
        template_ = 'teacher_detail.html'
        context = {
            'teachers': teachers,
            'current_teacher': current_teacher
        }

    return render(request=request, template_name=template_, context=context)
