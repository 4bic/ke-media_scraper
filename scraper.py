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


def collect_and_save(articles):
    article_url = []
    for article in articles:
        url = raw_url + proj + tree + str(article)
        print(article_url)
    #     save to file
        year = url.split('/')[4]
        month = url.split('/')[6]

        print(year + ":>><<:"+month)

        Dir = str(year)+"/"+str(month)+"/"

        file_path = './media/' + Dir  # Change path to suit local dir
        file_name = data[:50].title()

        if not os.path.exists(file_path):
          os.mkdir(file_path)

        with open(file_path+file_name+'.txt', 'w+') as f:

          f.write(data)
          f.close()
