from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

#The next step is to point the root URLconf at the polls.urls module. In mysite/urls.py, 
# add an import for django.urls.include and insert an include() in the urlpatterns lis