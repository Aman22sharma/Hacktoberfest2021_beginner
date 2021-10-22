#!/usr/bin/python3

# AUTHOR: Daniel 'Dirox'
# Python3 Concept: Get top submissions in a certain category of a subreddit
# GITHUB: https://github.com/Dir0x

import praw

reddit = praw.Reddit(client_id="Enter_ID", client_secret="Enter_Your_Secret", password="Enter_Your_Password", user_agent="Example by Dirox with <3 to contribute to hacktoberfest 2021", username="Your_User")
pythonsr = reddit.subreddit('Python')
pyseen_submissions = set()

for submission in pythonsr.hot(limit=50):
	print(submission.title + "\n\n" + str(submission.author) + "\n\n--------------------------------------------------------")
