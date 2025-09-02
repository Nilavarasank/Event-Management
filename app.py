from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="event_db"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        event = request.form["event"]
        cursor = mydb.cursor()
        sql = "INSERT INTO registrations (name,email,phone,event) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (name,email,phone,event))
        mydb.commit()
        return redirect("/success")
    return render_template("register.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=="POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        cursor = mydb.cursor()
        sql = "INSERT INTO contacts (name,email,message) VALUES (%s,%s,%s)"
        cursor.execute(sql, (name,email,message))
        mydb.commit()
        return redirect("/success")
    return render_template("contact.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/admin")
def admin():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM registrations")
    data = cursor.fetchall()
    return render_template("admin.html", registrations=data)



if __name__=="__main__":
    app.run(debug=True)
