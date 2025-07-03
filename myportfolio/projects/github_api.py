import requests
from datetime import datetime
from .models import GitHubProject

def fetch_github_repos(username):
    url = f"https://api.github.com/users/xnxrhbclub/repos"
    response = requests.get(url, params={'sort': 'updated', 'direction': 'desc'})
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            GitHubProject.objects.update_or_create(
                name=repo['name'],
                defaults={
                    'description': repo.get('description', ''),
                    'url': repo['html_url'],
                    'stars': repo['stargazers_count'],
                    'language': repo.get('language', 'Unknown'),
                    'updated_at': datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ'),
                }
            )