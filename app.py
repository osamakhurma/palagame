import os
import csv
import random
from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__, static_url_path='/static')
app.secret_key = "supersecretkey"

# ملف تخزين أسماء اللاعبين  
USERS_FILE = "players.csv"

# قائمة المدن مع إحداثياتها
cities = {
    "القدس": {"x": 282, "y": 368},
    "الخليل": {"x": 249, "y": 428},
    "نابلس": {"x": 293, "y": 259},
    "جنين": {"x": 299, "y": 207},
    "غزة": {"x": 142, "y": 424},
    "يافا": {"x": 199, "y": 313},
    "حيفا": {"x": 237, "y": 139},
    "عكا": {"x": 258, "y": 113},
    "صفد": {"x": 339, "y": 98},
    "طبريا": {"x": 344, "y": 153},
    "أريحا": {"x": 325, "y": 349},
    "بئر السبع": {"x": 198, "y": 490},
    "رفح": {"x": 106, "y": 477},
    "الناصرة": {"x": 297, "y": 161},
}

# قائمة المدن التي تم سؤالها خلال الجولة
asked_cities = set()

@app.route("/")
def index():
    if "player_name" not in session:
        return redirect(url_for("register"))
    return render_template("index.html", player_name=session["player_name"])

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        player_name = request.form["player_name"].strip()
        if player_name:
            session["player_name"] = player_name
            save_player_name(player_name)
            return redirect(url_for("index"))
    return render_template("register.html")

@app.route("/get_question")
def get_question():
    global asked_cities
    available_cities = list(set(cities.keys()) - asked_cities)

    if not available_cities:  # إذا انتهت المدن، نعيد القائمة
        asked_cities.clear()
        available_cities = list(cities.keys())

    city = random.choice(available_cities)
    asked_cities.add(city)

    return jsonify({"question": f"أين تقع مدينة {city}؟", "city": city, "coords": cities[city]})

def save_player_name(name):
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["اللاعب"])
    
    with open(USERS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
    
