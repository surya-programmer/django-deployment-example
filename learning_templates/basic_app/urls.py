from django.conf.urls import url
from basic_app import views
#Template Tagging
app_name='basic_app'

urlpatterns=[
    url('relative',views.relative,name='relative'),
    url('other',views.other,name='other')
]
