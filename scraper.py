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



BD = ["2017-business-daily-kenya","2018-business-daily-kenya","2019-business-daily-kenya"]
Standard_digital=["2015-standard-digital","2016-standard-digital","2017-standard-digital",
                  "2018-standard-digital","2019-standard-digital"]
Star=["2013-the-star","2014-the-star","2015-the-star","2016-the-star",
        "2017-the-star","2018-the-star","2019-the-star"]
EA=["1970-the-east-african","2015-the-east-african","2016-the-east-african",
      "2017-the-east-african","2018-the-east-african","2019-the-east-african"]

media = [BD,Standard_digital, Star, EA]
