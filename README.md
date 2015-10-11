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
  - [ ] new.html has a form for submitting a new story
    - name: content, title
    - should have max characters

  - [ ] app.py gives info to util.py
    - use util.newStory()

  - [ ] util.py writes the info to a database
    - call it newStory()
    -new table story
    - columns: SID, UID, content, title, lines
    - UID defualt 0 for now, lines: 1

  - ######Problems:
    - [ ] SID(storyID): how to generate
    - [ ] UID(userID): how to pass

- [ ] Add on to the Story
  - [ ] story.html displays the existing story
    - {{story}}
  - [ ] story.html has a form for sumbmitting content
    - name: content
    - should have max character

  - [ ] app.py gives info to util.py
    - use util.addContent()
  - [ ] app.py gets the content from util.py redirect to story.html
    - call the content story and give it to story.html
    - use util.get() to get the content

  - [ ] util.py adds on to existing content
    - call it addContent()
    - new table body
      - columns: UID, content, SID, line#
    - line# based on lines column of SID
    - go crazy just add it
  - [ ] util.py gets the content from the database with the SID
    - call it get()


- [ ] Have multiple stories
- [ ] Have multiple users
- [ ] User registration
- [ ] Delete story
- [ ] Delete line
