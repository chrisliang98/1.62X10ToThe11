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
        #login form submission
	button = request.form['button']
        #uname = request.form['username']
	#pword = request.form['password']
    	#if credentials valid, log them in with session
        if button == "Create Account":
            newUser = request.form['newUser']
            newPass = request.form['newPass']
            newPassC = request.form['newPassC']
            if (newPass == newPassC):
                if  module.newUser(newUser,newPass):
                    return render_template('home.html',success="Account created!")
                else:
                    return render_template('home.html',error2="Username taken")            
            else:
                return render_template('home.html',error2="Passwords do not match!")
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
        if line[-1] != ".":
            if line[-1] != "?":
                if line[-1] != "!":
                    line=line+"."
        if button=="Submit":
            module.makePost(username, title, line)
            return redirect('/story/%s' %title)
        if button=="Cancel":
            return redirect(url_for('home'))
        else:
            return render_template("new.html")
        return render_template("new.html")


@app.route("/story/<title>",methods=['GET','POST'])
def story(title=""):
    delete=''
    if 'n' in session:
        if session['n'] == "Admin":
            delete = '<input type="submit" name="button" value="Delete Story">'
            delete = Markup(delete)
        if request.method == "GET":
            return render_template("story.html", title=title, line=module.getPost(title), delete=delete)
        else:
            newLine = request.form['newLine']
            if newLine[-1] != ".":
                if newLine[-1] !="?":
                    if newLine[-1] !="!":
                        newLine=newLine+"."
            button = request.form['button']
            if button == "Add to Story":
                module.addToPost(session['n'],title," " + newLine)
                return render_template("story.html", title=title, line=module.getPost(title), delete=delete) 
            else:
                module.removePost(title)
                return redirect(url_for('stories'))
    else:
        return render_template("story.html")

@app.route("/stories")
def stories():

    str=""
    stories=module.getAllPosts()
    for item in stories:
        str+="<h1> <a href='story/%s'> %s</a> </h1>" %(item[1], item[1])
        str+="<h2> Posted by: %s </h2>" %item[0]
        str+="<h3> %s </h3>" %item[2] + "<hr>"
        
    str= Markup(str)

    return render_template("stories.html", link=str) 


if __name__ == "__main__":
    app.debug = True
    app.secret_key="c720minusboying"
    app.run(host='0.0.0.0', port=5000)







