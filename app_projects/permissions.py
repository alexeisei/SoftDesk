from .models import Project
from rest_framework import permissions


class ProjectPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author


class ContributorPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        usr_projects = Project.objects.filter(contributors__user=request.user)
        if project in usr_projects:
            project = Project.objects.get(id=view.kwargs['project_pk'])
            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user == project.author
        return False

    def has_object_permission(self, request, view, obj):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == project.author


class IssuePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        usr_projects = Project.objects.filter(contributors__user=request.user)
        if project in usr_projects:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author


class CommentPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        usr_projects = Project.objects.filter(contributors__user=request.user)
        if project in usr_projects:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author
