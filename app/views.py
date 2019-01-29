from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from . forms import SurveyCreateForm
from . models import Survey
from . data import countries, year, sleep_time, wake_time, size, campuses, gender, yes_no
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .algorithm import executeAlgorithm
from django.conf import settings
import csv, os
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
    # list_json = serializers.serialize('json', list)
    # matchings = generate_matchings.delay(list_json)
    return render(request, 'StableRoom8/NarynMale.html',{'list': list})
@login_required
def NarynFemale(request):
    list = Survey.objects.all().filter(campus=0).filter(gender=1)
    # list_json = serializers.serialize('json', list)
    # matchings = generate_matchings.delay(list_json)
    return render(request, 'StableRoom8/NarynFemale.html',{'list': list})
@login_required
def KhorogMale(request):
    list = Survey.objects.all().filter(campus=1).filter(gender=0)
    # list_json = serializers.serialize('json', list)
    # matchings = generate_matchings.delay(list_json)
    return render(request, 'StableRoom8/KhorogMale.html',{'list': list})
@login_required
def KhorogFemale(request):
    list = Survey.objects.all().filter(campus=1).filter(gender=1)
    # list_json = serializers.serialize('json', list)
    # matchings = generate_matchings.delay(list_json)
    return render(request, 'StableRoom8/KhorogFemale.html',{'list': list})
@login_required
def TekeliMale(request):
    list = Survey.objects.all().filter(campus=2).filter(gender=0)
    # list_json = serializers.serialize('json', list)
    # matchings = generate_matchings.delay(list_json)
    return render(request, 'StableRoom8/TekeliMale.html',{'list': list})
@login_required
def TekeliFemale(request):
    list = Survey.objects.all().filter(campus=2).filter(gender=1)
    # list_json = serializers.serialize('json', list)
    # matchings = generate_matchings.delay(list_json)
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
                      'extra6': survey.extra6,
                      'want_roommate' : yes_no[survey.want_roommate],
                      'email_roommate': survey.email_roommate,}
    return render(request, 'StableRoom8/SurveyDetail.html',{'info': converted_data})

@login_required
def Match(request, campus, gender):
    filename = ''
    result_string = "Results of matching for "
    if campus == 0:
        result_string += "Naryn campus "
        filename += 'Naryn'
    elif campus == 1:
        result_string += "Khorog campus "
        filename += 'Khorog'
    elif campus == 2:
        result_string += "Tekeli campus "
        filename += 'Tekeli'
    else:
        return HttpResponseNotFound("<h1 style='margin: 0 auto;text-align:center;'>invalid id for campus such campus does not exist</h1>")

    if gender == 0:
        result_string += "Male section"
        filename += 'Male'
    elif gender == 1:
        result_string += "Female section"
        filename += 'Female'
    else:
        return HttpResponseNotFound("<h1 style='margin: 0 auto;text-align:center;'>Invalid id for gender. Such gender does not exist</h1>")

    result = executeAlgorithm(Survey.objects.filter(campus=campus).filter(gender=gender))

    if result:

        full_filename = os.path.join(settings.MEDIA_ROOT, filename+'.csv')
        with open(full_filename, 'w') as csvFile:
            writer = csv.writer(csvFile,quoting=csv.QUOTE_ALL)
            for row in result:
                writer.writerow([row,result[row]])
        csvFile.close()


        return render(request, 'StableRoom8/match.html', {"result": result, 'addr': filename})
    else:
        return render(request, 'StableRoom8/match.html', {"result": {'No records for this particular campus and gender,': 'matching did not occur'}})
#
# def download_csv():
#
#     listOfFiles = listdir('media/.')
#     for i in listOfFiles:
#         if i.startswith("asdf"):
#             name = i
#             remove('media/{}'.format(name))


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
