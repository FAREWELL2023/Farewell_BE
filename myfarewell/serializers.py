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
    
    
    
    publicfarewell_ques = serializers.ReadOnlyField(source='PublicFarewell.question')
    publicfarewell_ans = serializers.ReadOnlyField(source='PublicFarewell.content')
    publicfarewell_ans_cnt =serializers.SerializerMethodField()
    progress_rate = serializers.SerializerMethodField()
    
    def get_publicfarewell_ans_cnt(self, instance):
        return instance.answer.count()
    

    def get_progress_rate(self, instance):
        total_cnt = 30
        ans_cnt = self.get_publicfarewell_ans_cnt(instance)

        percentage = (ans_cnt / total_cnt) * 100
        return round(percentage)
    
    

    # def get_progress_rate(self, obj):
        
    #     if total_question > 30:
    #         user_responses = Ending.objects.filter(answer_content__user=obj.answer_content.user).count()
    #         return f"{(user_responses / total_questions) * 100:.2f}%"
    #     return "0%"


    class Meta:
        model = Ending
        fields = '__all__'

        