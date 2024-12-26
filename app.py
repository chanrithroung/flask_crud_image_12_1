from flask import Flask, render_template, request
import services

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/create-post", methods=["GET", "POST"])
def create_post():
    if request.method == 'GET':
        return render_template('create.html')

    services.createPost(request.form, request.files)
    return "Post create success"
    
if __name__ == '__main__':
    app.run(debug=True)