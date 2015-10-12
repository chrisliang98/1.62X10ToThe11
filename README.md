# 1.62X10ToThe11

###Origin of project name
3 out of 4 of us in the group have Acer C720, and (3/4)\*72\**c* is 1.62\*10^11.  
The carrot didn't work when we were creating the repository.  
So we're 1.62X10ToThe11. :D

###Contributors
Boying Tang - Leader  
Christopher Liang - UX  
Javis Wu - Middleware  
Jion Fairchild - Backend  

###Task List
- [ ] Write a New Story

  - [x] 10/09/2015 Login with 1 hardcoded user 
  - [x] 10/11/2015 new.html has a form for submitting a new story
    - name: content, title
    - should have max characters

  - [ ] app.py gives info to util.py
    - use module.makePost()
    - variables: username, title, contents

  - [x] 10/11/2015 util.py writes the info to a database
    - call it makePost()

- [ ] Add on to the Story
  - [x] 10/11/2015 story.html displays the current story
    - {{post}}
  - [ ] story.html has a form for sumbmitting content
    - name: content
    - should have max character

  - [ ] app.py gives info to module.py
    - use module.addToPost()
    - variables: title, content
  - [ ] app.py gets the content from module.py redirect to story.html
    - use module.getPost() to get the content
    - give it to story.html as story

  - [x] 10/11/2015 module.py adds on to existing content
    - call it addToPost()
    - go crazy just add it
  - [x] 10/11/2015 module.py gets the content from the database with the title
    - call it getPost()

- [ ] Have multiple stories
  - [x] 10/11/2015 home.html has a list of all the stories 

  - [ ] app.py formats the titles of all the posts and gives it to table as post
    - for item in getAllPosts():
      <a href='story/"%s"'> "%s" </a> %item[1]

  - [ ]

- [ ] Have multiple users
- [ ] User registration
- [ ] Delete story
- [ ] Delete line
