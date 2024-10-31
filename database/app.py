from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

con = mysql.connector.connect(host="localhost", user="root", password="grannygear1952", database="pcpartfinder")
cur = con.cursor()


@app.route("/")
def home():
    
    return render_template("home.jinja")

@app.route("/cpu")
def get_cpu():
    cur.execute("SELECT * FROM cpu LIMIT 200")
    motherboards = cur.fetchall()
    
    return render_template("cpu.jinja", data=motherboards)

@app.route("/cpu/<code>")
def get_cpu_code(code):
    cur.execute(f"SELECT * FROM cpu WHERE name = '{code}'")
    cpu = cur.fetchone()
    rest = cur.fetchall()
    return render_template("cpu_code.jinja", data=cpu)

@app.route("/cpu/search/<code>")
def search_cpu(code):
    cur.execute(f"SELECT * FROM cpu WHERE name LIKE '%{code}%'")
    result = cur.fetchall()
    return render_template("cpu.jinja",data=result)

@app.route("/motherboard")
def get_motherboard():
    cur.execute("SELECT * FROM motherboard LIMIT 200")
    motherboards = cur.fetchall()
    return render_template("motherboard.jinja",data=motherboards)
          
@app.route("/motherboard/<code>")
def get_mobo_code(code):
    cur.execute(f"SELECT * FROM motherboard WHERE name = '{code}'")
    mobo = cur.fetchone()
    rest = cur.fetchall()
    return render_template("motherboard_code.jinja", data=mobo)

@app.route("/motherboard/search/<code>")
def search_motherboard(code):
    cur.execute(f"SELECT * FROM motherboard WHERE name LIKE '%{code}%'")
    result = cur.fetchall()
    return render_template("motherboard.jinja",data=result)

@app.route("/build")
def get_build():
    cur.execute(f"SELECT * FROM build JOIN cpu ON cpu.name = cpu_name JOIN motherboard ON motherboard.name = motherboard_name WHERE build_id = 1")
    build = cur.fetchone()
    return render_template("build.jinja", data=build)

@app.route("/build/motherboard/<code>")
def add_mobo(code):
    cur.execute(f"UPDATE build SET motherboard_name = '{code}' WHERE build_id = 1")
    con.commit()
    return get_build()

@app.route("/build/cpu/<code>")
def add_cpu(code):
    cur.execute(f"UPDATE build SET cpu_name = '{code}' WHERE build_id = 1")
    con.commit()
    return get_build()