# 1.62X10ToThe11

1.62X10ToThe11 is a storyboard where users can add an sentence to existing stories or start a new story of their own.

###Origin of project name
3 out of 4 of us in the group have Acer C720, and (3/4)\*72\**c* is 1.62\*10^11.  
The carrot didn't work when we were creating the repository.  
So we're 1.62X10ToThe11. :D

###Contributors
Boying Tang - Leader  
Christopher Liang - UX  
Javis Wu - Middleware  
Jion Fairchild - Backend  

###Instructions
1. Run app.py
2. Go to http://0.0.0.0:5000/ or http://localhost:5000/
3. Interact  

Note: Must have flask and sqlite3 installed  
flask: http://flask.pocoo.org/docs/0.10/installation/  
sqlite3: https://www.sqlite.org/download.html 

###Task List
- [ ] (ongoing) Improving the aesthetics
- [x] 10/11/2015 Write a New Story

  - [x] Login with 1 hardcoded user 
  - [x] new.html has a form for submitting a new story

  - [x] app.py gives info to util.py

  - [x] util.py writes the info to a database

- [x] 10/11/2015 Add on to the Story
  - [x] story.html displays the current story
  - [x] story.html has a form for sumbmitting content

  - [x] app.py gives info to module.py
  - [x] app.py gets the content from module.py redirect to story.html

  - [x] module.py adds on to existing content
  - [x] module.py gets the content from the database with the title

- [x] 10/11/2015 Have multiple stories
  - [x] home.html has a list of all the stories 

  - [x] app.py formats the titles of all the posts and gives it to table as post

- [x] 10/11/2015 Have multiple users
- [x] 10/11/2015 User registration
- [x] 10/12/2015 Delete story option for admin account
- [x] 10/12/2015 Password encryption
- [x] 10/13/2015 Database input sanitizing
- [ ] Password changing option
- [ ] Limiting continuous user input on the same story