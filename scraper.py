import os
import os.path
from github import Github
import requests
from urllib.request import urlopen


# links = []
# collection = []

def get_links(media):
    for proj in media:
        link = base_url+proj
        links.append(link)
    return links


def collect_repos(links):
    for link in links:
        response = requests.get(link, headers)
        json = response.json()
        for repo in json:
            repo_name = repo['full_name']
            collection.append(repo_name)
    return collection
