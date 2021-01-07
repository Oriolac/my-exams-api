from rest_framework import serializers

from apps.exams.models import Exam, ExamLocation, Question, Choice


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamLocation
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


def create_question_depth(validated_data):
    choices = []
    for choice in validated_data['choices']:
        choices.append(Choice.objects.create(choice_id=choice['choice_id'], response=choice['response']))
    validated_data.pop('choices')
    instance = Question.objects.create(title=validated_data['title'],
                                       correct_choice=validated_data['correct_choice'])
    instance.choices.set(choices)
    return instance


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(read_only=False, many=True)

    class Meta:
        model = Question
        fields = ('title', 'choices', 'correct_choice')

    def create(self, validated_data):
        instance = create_question_depth(validated_data)
        return instance


class CompleteExamSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=False, many=False)
    questions = QuestionSerializer(read_only=False, many=True)

    class Meta:
        model = Exam
        fields = ('id', 'title', 'description', 'date_start', 'date_finish', 'location', 'questions')

    def create(self, validated_data):
        questions = []
        for question in validated_data.pop('questions'):
            questions.append(create_question_depth(question))
        location = validated_data.pop('location')
        location_instance = ExamLocation.objects.create(**location)
        validated_data['location'] = location_instance
        instance = Exam.objects.create(**validated_data)
        instance.questions.set(questions)
        return instance


class ExamDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['description']
