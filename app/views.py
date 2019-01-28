from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from . forms import SurveyCreateForm
from . models import Survey
from . data import countries, year, sleep_time, wake_time, size, campuses, gender
from django.contrib.auth.decorators import login_required

def HOME(request):
    num = len(Survey.objects.all())
    return render(request, 'StableRoom8/index.html', {'num': num} )

def SURVEY(request):
    if request.method == 'POST':
        form = SurveyCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HOME')
    else:
        form = SurveyCreateForm()
    return render(request, 'StableRoom8/survey.html', {'form': form})

@login_required
def SurveyList(request):
    return render(request, 'StableRoom8/survey_list.html')

@login_required
def NarynMale(request):
    list = Survey.objects.all().filter(campus=0).filter(gender=0)
    return render(request, 'StableRoom8/NarynMale.html',{'list': list})
@login_required
def NarynFemale(request):
    list = Survey.objects.all().filter(campus=0).filter(gender=1)
    return render(request, 'StableRoom8/NarynFemale.html',{'list': list})
@login_required
def KhorogMale(request):
    list = Survey.objects.all().filter(campus=1).filter(gender=0)
    return render(request, 'StableRoom8/KhorogMale.html',{'list': list})
@login_required
def KhorogFemale(request):
    list = Survey.objects.all().filter(campus=1).filter(gender=1)
    return render(request, 'StableRoom8/KhorogFemale.html',{'list': list})
@login_required
def TekeliMale(request):
    list = Survey.objects.all().filter(campus=2).filter(gender=0)
    return render(request, 'StableRoom8/TekeliMale.html',{'list': list})
@login_required
def TekeliFemale(request):
    list = Survey.objects.all().filter(campus=2).filter(gender=1)
    return render(request, 'StableRoom8/TekeliFemale.html',{'list': list})
@login_required
def SurveyDetail(request, id):
    survey = Survey.objects.get(id=id)
    converted_data = {'full_name':survey.full_name,
                      'email':survey.email,
                      'country': countries[survey.country],
                      'campus': campuses[survey.campus],
                      'gender': gender[survey.gender],
                      'year': year[survey.year],
                      'scale1': survey.scale1,
                      'scale2': survey.scale2,
                      'scale3': survey.scale3,
                      'scale4': survey.scale4,
                      'scale5': survey.scale5,
                      'scale6': sleep_time[survey.scale6],
                      'scale7': wake_time[survey.scale7],
                      'scale8': survey.scale8,
                      'extra1': survey.extra1,
                      'extra2': survey.extra2,
                      'extra3': survey.extra3,
                      'extra4': size[survey.extra4],
                      'extra5': size[survey.extra5],
                      'extra6': survey.extra6,}
    return render(request, 'StableRoom8/SurveyDetail.html',{'info': converted_data})

# def apiSurveyList(request):
#     surveys = Survey.objects.all()
#     data = {"results": list(surveys.values('full_name', 'email', 'country','gender', 'year',
#                                            'scale1','scale2','scale3','scale4','scale5','scale6','scale7','scale8',
#                                            'extra1','extra2','extra3','extra4','extra5','extra6'))}
#     return JsonResponse(data)
#
# def apiSurveyDetail(request, pk):
#     survey = get_object_or_404(Survey, pk=pk)
#     data = {"results": {
#                 "full_name": survey.full_name,
#                 "email": survey.email,
#                 "country": survey.country,
#                 "gender": survey.gender,
#                 "year": survey.year,
#                 "scale1": survey.scale1,
#                 "scale2": survey.scale2,
#                 "scale3": survey.scale3,
#                 "scale4": survey.scale4,
#                 "scale5": survey.scale5,
#                 "scale6": survey.scale6,
#                 "scale7": survey.scale7,
#                 "scale8": survey.scale8,
#                 "extra1": survey.extra1,
#                 "extra2": survey.extra2,
#                 "extra3": survey.extra3,
#                 "extra4": survey.extra4,
#                 "extra5": survey.extra5,
#                 "extra6": survey.extra6,
#     }}
#     return JsonResponse(data)
