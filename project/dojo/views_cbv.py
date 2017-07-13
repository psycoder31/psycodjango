'''dojo/views_cbv.py
'''

import os

from psycoDjango import settings

from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView


class PostListView1(View):
    'CBV: 직접 문자열로 HTML형식 응답하기'

    def get(self, request):
        name = '스티브'
        html = self.get_template_sring().format(name=name)
        return HttpResponse(html)

    def get_template_sring(self):
        return '''
            <h1>PsycoLearn</h1>
            <p>{name}</p>
            <p>여러분 방학을 바치세요</p>'''


post_list = PostListView1.as_view()

class PostListView2(TemplateView):
    'CBV: 템플릿을 통해 HTML형식 응답하기'
    
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = 'steve'
        return context


post_list2 = PostListView2.as_view()


class PostListView3(View):
    'CBV: JSON 형식 응답하기'

    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii' : True})

    def get_data(self):
        return {
            'message' : '안녕, 파이썬 & 장고',
            'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
        }


post_list3 = PostListView3.as_view()


class ExcelDownloadView(View):
    'CBV: 엑셀 다운로드 응답하기'

    excel_path = os.path.join(settings.BASE_DIR, '싸이코더 연락처.xlsx')

    def get(self, request):
        filename = 'sample.xlsx'
        with open(self.excel_path, 'rb') as f:
            response= HttpResponse(f, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
            return response