title = input ("what is the title of your video ? ")
description = input ("what is your video about ?")

def creating_video(title , description) :
	details_of_the_video = {"title" : title , "description" : description, "likes" : 0 , "dislikes" : 0 , "comments": {}}
	details_of_the_video["title"] = title
	details_of_the_video["description"]=description

	return(details_of_the_video)

def add_likes(details_of_the_video) :
	if "likes" in details_of_the_video :
		details_of_the_video["likes"] = int (likes + 1 )
	return(details_of_the_video)

adding_495_likes = input("do you want to add 494 likes ??")
if adding_495_likes == "yes" :
	details_of_the_video[likes] = 495


def add_dislikes(details_of_the_video) :
	if "dislikes" in details_of_the_video :
		details_of_the_video["dislikes"] = int (likes + 1 )
	return(details_of_the_video)


def add_comment(details_of_the_video) : 
	user = input("what is your username ?? ")
	input_com = input ("your comment ?? ")
	details_of_the_video[user] = input_com
	return(details_of_the_video)

my_video=creating_video(title,description)
comment_Question = input ("do you want add comment ?? ")
if comment_Question == "yes" :
	add_comment(my_video)