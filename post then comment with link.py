import praw
import time
reddit = praw.Reddit(client_id='Y96vOOmy2OfZoQ',
                     client_secret='9bipazlzIhnLHums7uyeQkEVu1IYDg',
                     user_agent='a reddit instance',
                     username='queenhailey1',
                     password='12334561233456')
def image_comment():
    subreddit = reddit.subreddit("onlyfansgirls101")
    titles = ["""The queen is here.
Check in the comments."""]
    reddit.validate_on_submit = True
    images = ["D:\jhadd\Pictures\haleys.jpg"]      # you must change this to the path on your computer
    x = subreddit.submit_image(titles[0], images[0])
    x
    x.reply("onlyfans.com/haley")     # change this to the url as you didn't give me it

image_comment()
