from django.conf.urls import url
app_name='marrageapp'
urlpatterns=[
    url(r'^home$',view='home',name='home')
]