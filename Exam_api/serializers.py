from rest_framework import serializers
from Exam_api.models import Admin, Questions, Results, Users


class QuestionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = "__all__"


class UsersSerilizers(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = "__all__"


class AdminSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = "__all__"


class ResultsSerilizers(serializers.ModelSerializer):

    class Meta:
        model = Results
        fields = "__all__"
