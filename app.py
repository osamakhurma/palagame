from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import random
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

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

# ملف تخزين أسماء الطلاب
PLAYERS_FILE = "players.json"

def save_player(name):
    """يحفظ اسم اللاعب في ملف JSON"""
    if not os.path.exists(PLAYERS_FILE):
        with open(PLAYERS_FILE, "w") as f:
            json.dump([], f)

    with open(PLAYERS_FILE, "r") as f:
        players = json.load(f)

    if name not in players:
        players.append(name)

    with open(PLAYERS_FILE, "w") as f:
        json.dump(players, f)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            session["player_name"] = name
            save_player(name)
            session["asked_cities"] = []  # تصفير قائمة الأسئلة
            return redirect(url_for("game"))
    return render_template("register.html")

@app.route("/game")
def game():
    if "player_name" not in session:
        return redirect(url_for("register"))
    return render_template("index.html", player_name=session["player_name"])

@app.route("/get_question")
def get_question():
    asked_cities = session.get("asked_cities", [])
    remaining_cities = [city for city in cities.keys() if city not in asked_cities]

    if not remaining_cities:
        session["asked_cities"] = []
        remaining_cities = list(cities.keys())

    city = random.choice(remaining_cities)
    asked_cities.append(city)
    session["asked_cities"] = asked_cities

    return jsonify({"question": f"أين تقع مدينة {city}؟", "city": city, "coords": cities[city]})

@app.route("/players")
def players():
    """عرض قائمة الطلاب اللي لعبوا"""
    if not os.path.exists(PLAYERS_FILE):
        return jsonify([])

    with open(PLAYERS_FILE, "r") as f:
        players = json.load(f)
    
    return jsonify(players)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
