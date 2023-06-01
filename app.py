from flask import Flask,render_template,request,redirect
import db
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/category",methods=['GET','POST'])
def category():
    categories = db.getCategories()
    print(request.args.get('status'))
    if request.method == "POST":
        name = request.form.get("name")
        status = db.addCategory(name)
        return redirect("/category?status="+status)
        return render_template("category.html",status=status,categories=categories)
    
    return render_template("category.html",categories=categories)


@app.route("/animal",methods=['GET','POST'])
def animal():
    animals = db.getAnimals()
    categories = db.getCategories()

    print(request.args.get('status'))
    if request.method == "POST":
        code = request.form.get("code")
        cid = request.form.get("cid")

        status = db.addAnimal(code, cid)
        return redirect("/animal?status="+status)
        return render_template("category.html",status=status,categories=categories)
    
    return render_template("animal.html",animals=animals,categories=categories)

app.run(debug=True)