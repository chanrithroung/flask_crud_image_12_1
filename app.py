from flask import Flask, render_template, request, jsonify
import services

app = Flask(__name__)

# ---------------------------------------------
@app.route("/")
def index():
    return render_template("base.html")

# ---------------------------------------------
@app.route("/create-post", methods=["GET", "POST"])
def create_post():
    if request.method == 'GET':
        return render_template('create.html')
    services.createPost(request.form, request.files)
    return "Post create success"


# ---------------------------------------------
@app.route('/list-product')
def list_product():
    products = services.getAllProducts()
    return render_template('list_product.html', products=products)


# -------------------------------------------------------
@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        return render_template("edit.html", product=services.get_one_product_by_id(id))
    else:
        services.update(request.form, request.files, id)
    

if __name__ == '__main__':
    app.run(debug=True)