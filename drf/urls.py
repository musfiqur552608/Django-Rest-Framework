from django.contrib import admin
from django.urls import path
from apiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/', views.student_detail),
    path('stuinfos/', views.student_list),
]
