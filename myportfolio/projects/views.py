from django.shortcuts import render
from .github_api import fetch_github_repos
from .models import GitHubProject

def home(request):
    fetch_github_repos("xnxrhbclub")  # Замените на ваш GitHub username
    projects = GitHubProject.objects.all().order_by('-stars')
    return render(request, 'projects/home.html', {'projects': projects})