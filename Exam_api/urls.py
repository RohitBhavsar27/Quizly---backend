from django.urls import path
from . import views

urlpatterns = [
    path("validateUser/", views.validateUser),
    path("getAllQuestions/<subject>", views.getAllQuestions),
    path("getAllSubjects/", views.getAllSubjects),
    path("viewQuestions/<qno>/<subject>", views.viewQuestions),
    path("addQuestions/", views.addQuestions),
    path("updateQuestions/", views.updateQuestions),
    path("deleteQuestions/<qno>/<subject>", views.deleteQuestions),
    path("validateAdmin/", views.validateAdmin),
    path("signUp/", views.signUp),
    path("saveResults/", views.saveResults),
    path("getResults/<subject>", views.getResults),
    path("getAllResults/", views.getAllResults),
]
