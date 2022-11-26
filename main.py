import argparse
import requests
import json

# Get args
parser = argparse.ArgumentParser()
parser.add_argument('N', type=int)
parser.add_argument('LABEL')
args = parser.parse_args()

# Get Questions
ses = requests.session()
quesList = ses.get(
    "https://api.stackexchange.com/2.3/questions?order=desc&sort=votes&tagged={}&site=stackoverflow".format(args.LABEL),
    timeout=5).json()["items"][:args.N]

# Get Answer
for top, ques in enumerate(quesList, 1):
    print("Top {}: {}".format(top, ques['title']))
    print("Most trusted answer: https://stackoverflow.com/a/{}\n".format(ses.get(
        "https://api.stackexchange.com/2.3/questions/{}/answers?order=desc&sort=votes&site=stackoverflow".format(
            ques['question_id'])).json()['items'][0]['answer_id']))
