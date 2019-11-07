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


def get_path(collection):
    for repo in collection:
        repo = g.get_repo(repo)
        # print(repo)
        try:
            contents = repo.get_contents("")
        except:
            pass
        for content_file in contents:
            file_name = content_file.path

    return file_name


def get_articles_path():
    repo = g.get_repo(proj)
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            article_path = file_content.path
            articles.append(article_path)

    return articles
