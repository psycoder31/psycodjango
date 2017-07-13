'''dojo/view.py
'''

import os
from psycoDjango import settings

from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
# Create your views here.

def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x)+int(y)+int(z))


def total(request, numbers):
    return HttpResponse(sum(map(lambda s: int(s or 0), numbers.split("/"))))


def post_list1(request):
    name = '스티브'
    return HttpResponse('''
        <h1>PsycoLearn</h1>
        <p>{name}</p>
        <p>여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>'''.format(name=name))


def post_list2(request):
    name = '스티브'
    response = render(request, 'dojo/post_list.html', {'name': name})
    return response


def post_list3(request):
    'FBV: JSON 형식 응답하기'

    return JsonResponse({
        'message' : '안녕, 파이썬& 장고',
        'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS']
    }, json_dumps_params={'ensure_ascii' : True})


def excel_download(request):
    'FBV: 엑셀 다운로드 하기'
    
    # filepath = 'C:\Dev\psycolearn\싸이코더 연락처.xlsx'
    filepath = os.path.join(settings.BASE_DIR, '싸이코더 연락처.xlsx')
    filename = 'sample.excel'

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="%s"'%filename.encode('utf8')
        print(response['Content-Disposition'])
        return response