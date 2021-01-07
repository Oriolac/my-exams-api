from rest_framework import serializers

from apps.exams.models import Exam, ExamLocation, Question, Choice


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'title', 'description', 'date_start', 'date_finish', 'location')


class CompleteExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'title', 'description', 'date_start', 'date_finish', 'location', 'questions')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamLocation
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(read_only=False, many=True)

    class Meta:
        model = Question
        fields = ('title', 'choices', 'correct_choice')

    def create(self, validated_data):
        choices = []
        for choice in validated_data['choices']:
            choices.append(Choice.objects.create(choice_id=choice['choice_id'], response=choice['response']))
        validated_data.pop('choices')
        instance = Question.objects.create(title=validated_data['title'], correct_choice=validated_data['correct_choice'])
        instance.choices.set(choices)
        return instance


class BasicQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'choices', 'correct_choice')