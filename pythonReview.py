def create_youtube_video(title, description):
	youtube_video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments" : {}}
	return youtube_video

def like (youtube_video):
	if "like" in youtube_video:
		youtube_video ["likes"] = ["likes"] +1
	return youtube_video

def dislike (youtube_video):
	if "dislike" in youtube_video:
		youtube_video ["dislikes"] = ["dislikes"] +1
	return youtube_video

def add_comment (youtube_video, username, comment_text):
	youtube_video["comments"][username] = comment_text
	return youtube_video

test=create_youtube_video ("hello", "world")
test=like (test)
test=dislike (test)
test = add_comment(test, "clil", "amazing")
print (test)