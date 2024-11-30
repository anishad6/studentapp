

from django.urls import path
from studentapp import views

urlpatterns = [
    path("",views.home),
    path("addStudent/",views.addStudent),
    path("update/<int:studentsid>",views.update),
    path("delete/<int:studentsid>",views.delete),
]
