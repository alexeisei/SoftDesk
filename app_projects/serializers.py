from rest_framework import serializers
from .models import Comment, Contributor, Issue, Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        read_only__fields = ('author', 'id')


class ContributorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'
        read_only__fields = ('project', 'role', 'id')


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = '__all__'
        read_only__fields = ('project', 'author', 'created_time', 'id')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only__fields = ('author', 'issue', 'created_time', 'id')
