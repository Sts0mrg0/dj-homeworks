import datetime
import os

from django.shortcuts import render


def file_list(request, year=None, month=None, day=None):
    template_name = 'index.html'
    
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    # context = {
    #     'files': [
    #         {'name': 'file_name_1.txt',
    #          'ctime': datetime.datetime(2018, 1, 1),
    #          'mtime': datetime.datetime(2018, 1, 2)}
    #     ],
    #     'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    # }
    context = {
        'files': [],
        'date': None
    }
    list_of_files = os.listdir('./')

    for file in list_of_files:
        if os.path.isfile(file):
            context['files'].append(
                {
                    'name': file,
                    'ctime': str(datetime.datetime.fromtimestamp(os.stat(file).st_ctime).date()),
                    'mtime': str(datetime.datetime.fromtimestamp(os.stat(file).st_mtime).date())
                }
            )
    if (year != None) and (month != None) and (day != None):
        context['date'] = datetime.date(year, month, day)
    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    with open(name, 'r') as file:
        return render(
            request,
            'file_content.html',
            context={'file_name': name, 'file_content': file.read()}
        )

