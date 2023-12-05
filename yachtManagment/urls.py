
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("yachtStore.urls")),
    path('members/', include("django.contrib.auth.urls")),
    path('members/', include("members.urls")),
    re_path(r'^.*/$', TemplateView.as_view(template_name='404.html'), name='404'),

]
