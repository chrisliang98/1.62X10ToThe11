def authenticate(uname,pword):
	if uname=="test" and pword=="c720":
		return True
	else:
		return False

def newStory(username, title, line):
        module.makePost(username,title,line)
#def newStory(SID, UID, title, content, lines):

#def get(SID):

#def addContent(SID, UID, content, lineNo):
	
