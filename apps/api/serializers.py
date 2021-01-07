from rest_framework import serializers

from apps.exams.models import Exam, ExamLocation, Question, Choice, Student


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamLocation
        fields = ['port', 'host', 'bind_key']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['choice_id', 'response']


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


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentID']


class CompleteExamSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=False, many=False)
    questions = QuestionSerializer(read_only=False, many=True)
    students = StudentSerializer(read_only=False, many=True)

    class Meta:
        model = Exam
        fields = ('title', 'description', 'date_start', 'date_finish', 'location', 'questions', 'students')

    def create(self, validated_data):
        questions = []
        for question in validated_data.pop('questions'):
            questions.append(create_question_depth(question))
        students = []
        print(validated_data)
        validated_data.pop('students')
        for student in self.initial_data.pop('students'):
            stud = Student.objects.get(studentID=student['studentID'])
            print(stud)
            if not stud:
                stud = Student.objects.create(studentID=student['studentID'])
            students.append(stud)
        location = validated_data.pop('location')
        location_instance = ExamLocation.objects.create(**location)
        validated_data['location'] = location_instance
        instance = Exam.objects.create(**validated_data)
        instance.questions.set(questions)
        instance.students.set(students)
        return instance


class ExamDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['description']
