from django.shortcuts import get_object_or_404, render
import jwt

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer

from config.settings import SECRET_KEY
from .models import Question, Answer, Ending
from accounts.models import User
from rest_framework import status
from .serializers import QuestionSerializer, AnswerSerializer, EndingSerializer


from rest_framework import viewsets, mixins
from publicfarewell.models import PublicFarewell
# 질문 리스트 보여주기
class QuesListAPIView(APIView):
    def get(self, request):
        theme = request.query_params.get('theme')
        if theme is not None:
            questions = Question.objects.filter(theme=theme)
            serializer = QuestionSerializer(questions, many=True)

            # 질문과 대답을 하나의 리스트로 병합
            combined_data = [
                {
                    "question_id" : q.id,
                    "question": q.text,
                }
                    for q in questions
            ]

            context = {
                "theme" : theme,
                "questions" : combined_data
            }

            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'error': '쿼리 문자열 "theme"이 필요합니다.'}, status=status.HTTP_400_BAD_REQUEST)


# 회고록 리스트 및 회고록 작성하기
class AnswerQuestionView(APIView):

    def get_user(self, request):
        access = request.COOKIES.get('access')  # 'access' 쿠키를 가져옴
        if access:
            payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
            pk = payload.get('user_id')
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(instance=user)
            return user
        return Response({
            'message': "로그인된 사용자가 아닙니다."
        }, status=status.HTTP_404_NOT_FOUND)


    def get_answer(self, user_profile, question_id):
        try:
            question = Question.objects.get(id=question_id)
            return Answer.objects.get(user=user_profile, question=question)
        except (Question.DoesNotExist, Answer.DoesNotExist):
            return None

    # 사용자가 작성한 질문 리스트 보여주기
    def get(self, request):
        user = self.get_user(request)
        answers = Answer.objects.filter(user=user)
        answer_serializer = AnswerSerializer(answers, many=True)

        questions = []  # 질문을 저장할 빈 리스트
        for answer in answers:
            questions.append(answer.question)  # 각 대답의 질문을 가져와 리스트에 추가

        question_serializer = QuestionSerializer(questions, many=True)  # 질문 직렬화

        # 질문과 대답을 하나의 리스트로 병합
        combined_data = [
            {
                "answer_id" : a.id,
                "question": q.text,
                "answer_content": a.answer_content,
            }
            for a, q in zip(answers, questions)
        ]

        return Response({
            'answers': combined_data,
        }, status=status.HTTP_200_OK)


    # 질문 작성하기
    def post(self, request):
        user = self.get_user(request)
        question_id = request.data.get('question_id')
        response = request.data.get('answer')

        try:
            answer = Answer.objects.get(user=user, question_id=question_id)
            # 이미 대답이 존재하는 경우 아무 작업도 하지 않고 그대로 유지
        except Answer.DoesNotExist:
            # 대답이 존재하지 않는 경우 생성
            answer = Answer(user=user, question_id=question_id, answer_content=response)
            answer.save()

        question = Question.objects.get(id=question_id)

        context = {
            "answer_id": answer.id,
            "question": question.text,
            "answer_content": answer.answer_content,
        }

        return Response(context, status=status.HTTP_201_CREATED)



# 특정 회고록 조회 및 수정하기
class GetPatchAnswerView(APIView):

    def get_user(self, request):
        access = request.COOKIES.get('access')  # 'access' 쿠키를 가져옴

        if access:
            payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
            pk = payload.get('user_id')
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(instance=user)
            return user
        return Response({
            'message': "로그인된 사용자가 아닙니다."
        }, status=status.HTTP_404_NOT_FOUND)


    def get_answer(self, user_profile, question_id):
        try:
            question = Question.objects.get(id=question_id)
            return Answer.objects.get(user=user_profile, question=question)
        except (Question.DoesNotExist, Answer.DoesNotExist):
            return None

    # 특정 회고록 가져오기
    def get(self, request, id):
        user = self.get_user(request)

        question = Question.objects.get(id=id)

        answer = Answer.objects.get(user=user, question=question)
        answer_serializer = AnswerSerializer(answer, many=True)

        # question = answer.question
        question_serializer = QuestionSerializer(question, many=True)  # 질문 직렬화

        # 질문과 대답
        context = {
            "question_id" : question.id,
            "answer_id" : answer.id,
            "question": question.text,
            "answer_content": answer.answer_content,
        }

        return Response(context, status=status.HTTP_200_OK)

    def patch(self, request, id):
        user = self.get_user(request)
        response = request.data.get('answer')
        
        try:
            question = Question.objects.get(id=id)
            
            answer = Answer.objects.get(user=user, question=question)
            
            # 받은 대답으로 업데이트
            answer.answer_content = response
            answer.save()
            
            context = {
                "question_id" : question.id,
                "answer_id" : answer.id,
                "question": question.text,
                "answer_content": response,
                'message': '질문에 대한 답변이 업데이트되었습니다.',
            }
            
            return Response(context, status=status.HTTP_200_OK)
        except Answer.DoesNotExist:
            return Response({"message": "존재하지 않는 회고록입니다."}, status=status.HTTP_404_NOT_FOUND)
        
        
class EndingListView(APIView):
    
    queryset = Ending.objects.all()
    
    def get(self, request):
        endings = Ending.objects.all()
        serializer = EndingSerializer(endings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
