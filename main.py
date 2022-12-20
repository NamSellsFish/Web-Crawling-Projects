import datetime
import requests
import argparse
import json
from bs4 import BeautifulSoup

# Get args
argp = argparse.ArgumentParser()
argp.add_argument("skill", type=str)
argp.add_argument("job", type=str)
argp.add_argument(
    "location", choices=["da-nang", "ha-noi", "ho-chi-minh-hcm"], type=str
)
args = argp.parse_args()
skill = args.skill.lower()
title = args.job.lower().replace(" ", "-")
location = args.location.lower().replace(" ", "-")


print("Assume that all args are correct, we will get a result like this..")
ses = requests.session()
resp = ses.get(
    f"https://itviec.com/viec-lam-it/{title}-{skill}/{location}?", timeout=5)
soup = BeautifulSoup(resp.content, "html.parser")
jobList = []
for indx, job in enumerate(soup.find_all("div", class_="job"), 1):
    checkingJob = BeautifulSoup(
        requests.get(
            f'https://itviec.com/{job.attrs.get("data-search--job-selection-job-url-value")}'
        ).content,
        "html.parser",
    )
    jobInfo = {
        "title": checkingJob.find("h1", class_="job-details__title").contents[0],
        "url": f'https://itviec.com/it-jobs/{job.attrs.get("data-search--job-selection-job-slug-value")}',
        "address": checkingJob.find(
            "a", class_="job-details__address-map hidden-xs d-none d-sm-inline-block"
        )
        .find_previous()
        .contents[0],
    }
    jobList.append(jobInfo)

    print(
        f"""
    No {indx}:
    - Tiltle: {jobInfo["title"]}
    - Address: {jobInfo["address"]}    
    - Detail: {jobInfo["url"]}
    """
    )
    today = datetime.date.today().strftime("%Y%m%d")
    with open("/{}_all_itviec_jobs.json".format(today), "wt") as f:
        json.dump(jobList, f)
