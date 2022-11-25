import argparse

import requests

# Get username
parser = argparse.ArgumentParser()
parser.add_argument("userName", help="Get Github repos info of user")
userName = parser.parse_args()

# Get Info
ses = requests.session()
info = ses.get("https://api.github.com/users/{}/repos".format(userName.userName), timeout=5).json()
for count, repo in enumerate(info, 1):
    print("- Repo no.{} name: {}\n  Url: {}".format(count, repo["name"], repo["html_url"]))
