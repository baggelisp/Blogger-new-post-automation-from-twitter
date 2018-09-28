# -*- coding: utf-8 -*-

import datetime
import tweepy
from tweepy import OAuthHandler
import auto_posting
import sys  
import string

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

posaret=100 #number of retweets

def log():
    login = Tk()
    login.title("Log in")
    login["padx"] = 50
    login["pady"] = 50
    Label(login, text="Access Token",padx=40,pady=5).grid(row=0)
    Label(login, text="Access Token Secret",padx=40,pady=5).grid(row=1)
    Label(login, text="API Key",padx=40,pady=5).grid(row=2)
    Label(login, text="API Secret",padx=40,pady=5).grid(row=3)
    e1 = Entry(login,width=50)
    e2 = Entry(login,width=50)
    e3 = Entry(login,width=50)
    e4 = Entry(login,width=50)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    
#------------------------------------

access_token='######################################'
access_secret='#####################################'
consumer_key='#####################################'
consumer_secret='#####################################'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

def user_tweet(tweet):
    t1 = tweet.split('@')[1]
    user = t1.split(':')[0]
    return user

def text_tweet(tweet):
    tw = tweet.split(':')[1]
    return tw


def post_to_blogger_from_twitter_user(username):
    tmpTweets = api.user_timeline(username,lang = 'gr',tweet_mode='extended')
    
    for tweet in tmpTweets:
        re_tweet_text=tweet.full_text
        
        ### restrictions ### 
        if 'retweeted_status' in dir (tweet):
            re_tweet_text = tweet.retweeted_status.full_text
        if re_tweet_text.find('http')!=-1 or re_tweet_text.find('via')!=-1 or re_tweet_text.find('.com')!=-1 \
           or len(re_tweet_text)<40 or (tweet.in_reply_to_status_id is not None) or tweet.retweet_count<posaret \
           or re_tweet_text.find('@')!=-1:
            continue
        if tweet.created_at.date() == datetime.date.today() or \
           tweet.created_at.date() == datetime.date.today() - datetime.timedelta(days = 1):
            pass
        else:
            break
        #an einai agglika
        abcd=False
        apag_lekseis = ['Ευχαριστ','τουι','τουί','ρτ','Καλημέρα','βοήθεια','βοηθεια','Τουί','Τουι','ακάου','Πέθανε','ανεγκέφ','ακαου','πέθανε','Εκλαπη','Εκλάπη','κοινοποι','πολιτ','νοσοκομ','αναπήρ','ντιεμ']
        for word in apag_lekseis:
           if re_tweet_text.find(word)!=-1:
                abcd=True
                break   
        for abc in list(string.ascii_lowercase):
            if abc in re_tweet_text:
                abcd=True
                break
        if abcd==True:
            continue
        #end of restrictions
        
        #changes
        re_tweet_text=re_tweet_text.replace('&amp;','και')
        re_tweet_text=re_tweet_text.replace('ναπουμε','')
        #if is in status.txt continue (if is posted)
        if re_tweet_text in open('status.txt', 'r',encoding="utf8").read():
            continue
        else:
            file = open('status.txt', 'a',encoding="utf8")
            file.write(re_tweet_text + ' \n')
            file.close()
            blogger.new_post(re_tweet_text)
            print ("*** POSTED ***")
            print ("Tweet: ")
            print(re_tweet_text.translate(non_bmp_map))
            
#### MAIN PROGRAM ####
username = raw_input("Blogger Username:")
password = raw_input("Blogger Password:")
blogger=auto_posting.BloggerBot(username, password)
blogger.login()

# ---AFTER LOGGED IN
list_of_users=['@stls92','@bloody_pantzari', \
               '@adiasistos','@demexereis','@Batzalakos','@Kentavros_Eirwn','@best___TWEETS', \
               '@La_cookaracha','@eVaN_GiAn','@theodorosunny','@N_Liviti',  \
               '@el__el__ant','@alexdom2','@ogunner','@MrsSourjelo‏','@Sampsonius_','@StefanosNtampos', \
               '@natou92121','@fouiter','@Lampatzampa','@Groupteamlogist', \
               '@pennyd36','@to_vatraxi','@Partalia','@akispanagiot','@AniatiPeriptosi', \
               '@_bourdas','@beeroas','@PouNaStaLeo','@AchillesFT','@baggelas']
for user in list_of_users:
    print ("**** USER: ",user," ***")
    try:
        post_to_blogger_from_twitter_user(user)                                    
    except tweepy.error.TweepError:
        pass
    


blogger.closeBrowser()

