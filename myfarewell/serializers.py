from rest_framework import serializers
from .models import Question, Answer, Ending
from publicfarewell.serializers import PublicFarewellSerializer
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'user', 'question', 'answer_content')
        


class EndingSerializer(serializers.ModelSerializer):
    progress_rate = serializers.SerializerMethodField()

    def get_progress_rate(self, obj):
        total_questions = Question.objects.count()
        if total_questions > 0:
            user_responses = Ending.objects.filter(answer_content__user=obj.answer_content.user).count()
            return f"{(user_responses / total_questions) * 100:.2f}%"
        return "0%"


    class Meta:
        model = Ending
        fields = '__all__'

        