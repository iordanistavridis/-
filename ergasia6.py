import tweepy

import re

from collections import Counter

#συμπληρώστε τα δικά σας consumer_key, consumer_secret, access_token και access_token_secret

consumer_key =

consumer_secret =

access_token =

access_token_secret = 

userID = input("εισάγετε το username του χρήστη που θέλετε να αναζητήσετε:\n")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name=userID, count=200, include_rts = False, tweet_mode = 'extended')

list_1 = [] * 10

for info in tweets[:10]:

    list_1.append(info.full_text) #εισαγώγη των τελευταίων 10 tweet σε λίστα

listToStr = " "

listToStr = listToStr.join(list_1) #μετατροπή λίστας σε str

print (" ")

print (listToStr) #εκτυπώνει str που περιέχει τα 10 τελευταία tweets

print (" ")

new_str = re.sub(r"http\S+", "", listToStr) #αφαίρεση των urls

new_str = re.sub("@[_A-Za-z]+", "", new_str) #αφαίρεση των @..

new_str = re.sub("[^ΆΈΉΊΌΎΏΪΫάέήίόύώϊϋα-ωΑ-Ωa-zA-Z]+", " ", new_str) #αφαίρεση σημείων στήξης

finalist = new_str.split() #μετατροπή str ξανά σε λίστα

finalist = map(str.lower,finalist) #μετατροπή όλων των κεφαλαίων σε μικρά

finalist = sorted(Counter(finalist),
                 key=lambda w: w.lower()) #αφαίρεση των λέξεων που επαναλαμβάνονται απο την λίστα
#print(finalist)

finalist = sorted(finalist, key=len) #ταξινόμιση με βάση το μέγεθος των λέξεων

print ("Οι 5 μεγαλύτερες λέξεις είναι: ")
print (" ")
print (finalist[-1])
print (finalist[-2])
print (finalist[-3])
print (finalist[-4])
print (finalist[-5])
print (" ")
print ("Οι 5 μικρότερες λέξεις είναι:")
print (" ")
print (finalist[0])
print (finalist[1])
print (finalist[2])
print (finalist[3])
print (finalist[4])
