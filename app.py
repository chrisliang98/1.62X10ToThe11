from flask import Flask, render_template, request, session, redirect, url_for, Markup
import sqlite3
import module

app = Flask(__name__)


@app.route("/home",methods=['GET','POST'])
@app.route("/home/",methods=['GET','POST'])
@app.route("/",methods=['GET','POST'])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
	button = request.form['button']
        #uname = request.form['username']
	#pword = request.form['password']
        if button == "Create Account":
            newUser = request.form['newUser']
            newPass = request.form['newPass']
            newPassC = request.form['newPassC']
            #password match check
            if (newPass == newPassC):
                #username and password lengths check
                if len(newUser)<4:
                    return render_template('home.html',error2="Username must be longer than 4 characters")
                if len(newPass)<4:
                    return render_template('home.html',error2="Password must be longer than 4 characters")
                #accoutn created successfully
                if  module.newUser(newUser,newPass):
                    return render_template('home.html',success="Account created!")
                #username taken error
                else:
                    return render_template('home.html',error2="Username taken")            
            else:
                return render_template('home.html',error2="Passwords do not match!")
        #Login
    	#if credentials valid, log them in with session
        if button == "Login":
            uname = request.form['username']
            pword = request.form['password']
            if module.authenticate(uname,pword):
                if 'n' not in session:
                    session['n'] = uname
                    return redirect(url_for('home'))
                    #else renders login w/ error message
            else:
                    return render_template("home.html",error="Invalid Username or Password")


@app.route('/logout', methods=['GET','POST'])
def logoff():
    #remove the username from the session if it's there
    session.pop('n', None)
    return redirect(url_for('home'))



@app.route("/newStory", methods=['GET','POST'])
def nStory():
    if request.method=="GET":
        return render_template("new.html")
    else:
        username=session['n']
        button=request.form['button']
        title=request.form['sTitle']
        line=request.form['entry']
        #add default period at end of submission
        #line=punctCheck(line)
        if len(line)>0:
            if line[-1] != ".":
                if line[-1] !="?":
                    if line[-1] !="!":
                        return line+"."        
#redirect to newly created story
        if button=="Submit":
            module.makePost(username, title, line)
            return redirect('/story/%s' %title)
        #redirect home
        if button=="Cancel":
            return redirect(url_for('home'))
        else:
            return render_template("new.html")
        return render_template("new.html")


@app.route("/story/<title>",methods=['GET','POST'])
def story(title=""):
    if 'n' in session:
        delete=''
        #show admin option for delete a story
        if session['n'] == "Admin":
            delete = '<input type="submit" name="button" value="Delete Story">'
            delete = Markup(delete)
        if request.method == "GET":
            return render_template("story.html", title=title, poster=module.getPoster(title),line=module.getPost(title), delete=delete)
        else:
            newLine = request.form['newLine']
            #puncuation check
            if len(newLine)>0:
                if newLine[-1] != ".":
                    if newLine[-1] !="?":
                        if newLine[-1] !="!":
                            return newLine+"."
            #newLine = punctCheck(newLine)
            button = request.form['button']
            #add to story
            if button == "Add to Story":
                if(module.addToPost(session['n'],title," " + newLine)):
                    return render_template("story.html", title=title, poster=module.getPoster(title),line=module.getPost(title), delete=delete) 
                #consecutive contribution error
                else:
                    return render_template("story.html",title=title,poster=module.getPoster(title), line=module.getPost(title),delete=delete,error="You cannot write two sentences in a row!")
            #deletes story
            else:
                module.removePost(title)
                return redirect(url_for('stories'))
    else:
        return render_template("story.html")

@app.route("/stories")
def stories():
    #generates html for displaying the title as a link
    str=""
    stories=module.getAllPosts()
    for item in stories:
        str+="<h1> <a href='story/%s'> %s</a> </h1>" %(item[1], item[1])
        str+="<h2> Posted by: %s </h2>" %item[0]
        str+="<h3> %s </h3>" %item[2] + "<hr>"
        
    str= Markup(str)

    return render_template("stories.html", link=str) 

#def punctCheck(newLine):
#    if len(newLine)>0:
#        if newLine[-1] != ".":
#            if newLine[-1] !="?":
#                if newLine[-1] !="!":
#                    return newLine+"."
#    else:
#        return newLine
                
if __name__ == "__main__":
    app.debug = True
    app.secret_key="c720minusboying"
    app.run(host='0.0.0.0', port=5000)







