#Background
#Since we're all redditors here, let's make something dealing with reddit. If you go to a 
#user's profile and add .json to the end of it, you can get the all sorts of Json data about 
#the user (think of Json as a giant dictionary of smaller dictionaries and lists). For 
#example, if I go to my own profile and view it's Json data, it would look like this. At 
#first it might look intimidating, but if you break it down, you can see it's just one 
#giant dictionary with all sorts of information about my latest posts.

#Goal
#Create a program that gets information about two different users, and then sees whose most 
#recent post received the most karma. The program should then print out which user received 
#more karma, and what the difference was. This is a pretty open project, so I encourage you 
#to take it further by adding more features if you find it interesting.

#Remember - Elements in a list are referenced by their index numbers while entries in a 
#dictionary are referenced by their keys.

#Subgoals
#Allow the user to put in the name of two different users when the program first begins.
#If one of the names of the users does not exist (because of a spelling error), print out a 
#message saying so.

#Allow the user to keep comparing other users until the program is closed.
#Display the amount of upvotes and downvotes each user received for their posts.
#Not sure how to turn json data into usable python data? Check this out.

#author: David Seidenberg
#project: Karma game for Reddit Beginner Projects


# importing modules
import json
import urllib2
from time import sleep

# program intro message
print '''
This program gets information about reddit users, and sees whose most recnet post received the most karma.
Check it out!
'''
not_real = "Not a real user.\n"

# gets users from the user
while True:
	while True:
		try:
			user1 = raw_input("Who is the first user? ")
			url1 = "https://www.reddit.com/user/" + user1 + ".json"
			urllib2.urlopen(url1)
			break
		except urllib2.HTTPError, e:
			
			print not_real
		
		
	while True:
		try:
			user2 = raw_input("And the second user? ")
			url2 = "https://www.reddit.com/user/" + user2 + ".json"
			urllib2.urlopen(url2)
			break
		except urllib2.HTTPError, e:
			print not_real
		except urllib2.URLError, e:
			print not_real


	# This takes a python object and dumps it to a string which is a JSON representation of that object
	data1 = json.load(urllib2.urlopen(url1))
	data2 = json.load(urllib2.urlopen(url2))

	user1_score = data1['data']['children'][0]['data']['score']
	user2_score = data2['data']['children'][0]['data']['score']
	
	ups1 = data1['data']['children'][0]['data']['ups']
	downs1 = data1['data']['children'][0]['data']['downs']
	
	ups2 = data2['data']['children'][0]['data']['ups']
	downs2 = data2['data']['children'][0]['data']['downs']
	
	if user1_score > user2_score:
		print "On their last posts, %s received %s more karma than %s." % (user1, (user1_score - user2_score), user2)
	elif user1_score < user2_score:
		print "On their last posts, %s received %s more karma than %s." % (user2, (user2_score - user1_score), user1)
	elif user1_score == user2_score:
		print "They both had the same score! A score of %s." % (user1_score)

	print "%s had %s upvotes and %s downvotes on their last post." % (user1, ups1, downs1)
	print "%s had %s upvotes and %s downvotes on their last post." % (user2, ups2, downs2)


	
	again = raw_input("Hit RETURN to compare more users, or type 'Quit' to close the program.\n\n>>" )
	
	if again == "Quit":
		break
	else:
		pass

