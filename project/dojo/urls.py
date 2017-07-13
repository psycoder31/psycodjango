'''dojo/urls.py
'''

from django.conf.urls import url
from . import views, views_cbv

urlpatterns = [
    url(r'^sum/(?P<x>\d+)/$', views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),

    url(r'^total/(?P<numbers>[\d/]+)/$', views.total),

    url(r'^post_list1/$', views.post_list1),
    url(r'^post_list2/$', views.post_list2),
    url(r'^post_list3/$', views.post_list3),
    url(r'^excel/$', views.excel_download),

    url(r'^cbv/post_list1/$', views_cbv.post_list),
    url(r'^cbv/post_list2/$', views_cbv.post_list2),
    url(r'^cbv/post_list3/$', views_cbv.post_list3),
    url(r'^cbv/excel/$', views_cbv.ExcelDownloadView.as_view),
]