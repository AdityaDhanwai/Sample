from flask import Flask,render_template
app=Flask(__name__)
app.secret_key = 'Amazon'  # set a secret key for session management
@app.get("/")
def index_get():
    global login
    login=False
    return render_template("login.html")

# End
if __name__=="__main__":
    app.run(debug=False,host='0.0.0')