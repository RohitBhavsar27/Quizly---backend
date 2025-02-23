from django.shortcuts import render

from Exam_api.serializers import QuestionSerializers, UsersSerilizers, ResultsSerilizers
from .models import Questions, Results, Users, Admin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.


@api_view(["POST"])
def validateUser(request):
    userFromClient = request.data
    try:
        userFromDb = Users.objects.get(username=userFromClient["username"])

        if (
            userFromClient["username"] == userFromDb.username
            and userFromClient["password"] == userFromDb.password
        ):
            return Response({"success": True}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
    except Users.DoesNotExist:
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["POST"])
def validateAdmin(request):
    adminFromClient = request.data
    try:
        adminFromDb = Admin.objects.get(username=adminFromClient["username"])
        if (
            adminFromClient["username"] == adminFromDb.username
            and adminFromClient["password"] == adminFromDb.password
        ):
            return Response({"success": True}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
    except Users.DoesNotExist:
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["GET"])
def getAllQuestions(request, subject):
    allQuestions = Questions.objects.filter(subject=subject)
    serializer = QuestionSerializers(allQuestions, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getAllSubjects(request):
    allquestions = Questions.objects.all()
    subjects = list(set(question.subject for question in allquestions))
    return Response({"subjects": subjects})


@api_view(["POST"])
def addQuestions(request):
    question_data = request.data
    if Questions.objects.filter(
        qno=question_data["qno"], subject=question_data["subject"]
    ).exists():
        return Response(
            {"error": "Question already exists"}, status=status.HTTP_400_BAD_REQUEST
        )

    serializer = QuestionSerializers(data=question_data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True}, status=status.HTTP_201_CREATED)
    return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def updateQuestions(request):
    question_data = request.data
    try:
        question = Questions.objects.get(
            qno=question_data["qno"], subject=question_data["subject"]
        )
    except Questions.DoesNotExist:
        return Response(
            {"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = QuestionSerializers(question, data=question_data, partial=False)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def viewQuestions(request, qno, subject):
    try:
        question = Questions.objects.get(qno=qno, subject=subject)
        serializer = QuestionSerializers(question)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Questions.DoesNotExist:
        return Response(
            {"error": "Question with given data is not available."},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["DELETE"])
def deleteQuestions(request, qno, subject):
    if not Questions.objects.filter(qno=qno, subject=subject).exists():
        return Response(
            {"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND
        )

    Questions.objects.filter(qno=qno, subject=subject).delete()
    return Response({"success": True}, status=status.HTTP_200_OK)


@api_view(["POST"])
def signUp(request):
    serializer = UsersSerilizers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(True)
    return Response(serializer.errors, status=400)


@api_view(["POST"])
def saveResults(request):
    serializer = ResultsSerilizers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(True)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def getResults(request, subject):
    allResults = Results.objects.filter(subject=subject)
    serializer = ResultsSerilizers(allResults, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getAllResults(request):
    allResults = Results.objects.all()
    serializer = ResultsSerilizers(allResults, many=True)
    return Response(serializer.data)
