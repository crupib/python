from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^polls/', include('polls.urls')),
   url('', include('main.urls')),
]
