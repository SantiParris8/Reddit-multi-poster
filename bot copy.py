import praw
with open ("sublista.txt", "r") as myfile: #Import subs from sublista.txt file accepts r/sub1 or sub1. File example> 'sub1,r/sub2,r/sub3,sub,etc'
    subreddits=myfile.readlines()

reddit = praw.Reddit(
    client_id="",#https://www.reddit.com/prefs/apps
    client_secret="",#https://www.reddit.com/prefs/apps
    user_agent="autopost/python/madeby@u/cookiexplorer",
    username="",#reddit user
    password="",#reddit pass
    )


subs = ''.join(subreddits)
list = subs.split(',')

print('Titulo')#Post title
title = input()
print('Url/Imgur')#Post url content
url = input()
url = 'https://i.imgur.com/xgi1VO9.jpg'

for i in list:#Post each suburedit in the list make the post.
    print(i)#Prints name before posting, can be used to debug post not posting.
    reddit.subreddit(i).submit(title, url=url)



