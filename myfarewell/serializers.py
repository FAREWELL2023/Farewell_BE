from rest_framework import serializers
from .models import Question, Answer, Ending

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'user', 'question', 'answer_content')
        


class EndingSerializer(serializers.ModelSerializer):
    # 여기에서 ForeignKey 필드를 직접 가져와야 합니다.
    questions = serializers.CharField(source='questions.text')
    answer_content = serializers.CharField(source='answer_content.answer_content')
    public_questions = serializers.CharField(source='public_questions.question')
    public_name = serializers.CharField(source='public_name.name')
    public_content = serializers.CharField(source='public_content.content')

    class Meta:
        model = Ending
        fields = '__all__'

        