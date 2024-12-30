from flask import Flask, render_template, request, jsonify, redirect
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


# ---------------------------------
@app.route("/edit/<id>", methods=["GET"])
def edit(id):
    # return f"{id}"
    
    return render_template("edit.html", product=services.get_one_product_by_id(id))


# @Edit Submit
@app.route('/edit_submit', methods=["POST"])
def edit_submit():
    edit_id = request.form['id']
    services.update(request.form, request.files, edit_id)
    return redirect('list-product')


if __name__ == '__main__':
    app.run(debug=True)