import sqlite3

conn = sqlite3.connect("myDataBase.db")
c = conn.cursor()

def authenticate(username, password):
    ans = c.execute('select * from logins where username = "'+username+'" and password = "'+password+'";') 
    for r in ans:
        return True;
    return False;
    #returns a boolean that describes whether the user has succesfully logged in.

def makePost(username, title, contents):
    ans = c.execute('insert into posts values("'+username+'","'+title+'","'+contents+'");')
    return False;
    #adds a post to the databes from username with title = title and contents = contents
    #returns a boolean representing if the operation was successful

def getPost(title):
    ans = c.execute('select * from posts where title ="%s";' % title) 
    for r in ans:
        return r[2]

def addToPost(username, title, content):
    return False;
    #adds content to content

authenticate("jion","password")
makePost("jion", "This is another test post", "TEST DATA")
print getPost("This is another test post")
