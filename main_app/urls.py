from django.conf.urls import include,url
from . import views
app_name = 'main_app'
urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^newbook/$', views.newbook_view, name='newbook'),
    url(r'^update/$', views.update, name='update'),
    url(r'^delete/$', views.delete, name='delete'),
    
]
