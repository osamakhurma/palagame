import csv
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

# تخزين أسماء اللاعبين
def save_name(name):
    with open(USERS_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name])

# جلب أسماء اللاعبين المسجلين
def get_names():
    try:
        with open(USERS_FILE, mode="r", encoding="utf-8") as file:
            return [row[0] for row in csv.reader(file)]
    except FileNotFoundError:
        return []

# قائمة المدن اللي تم سؤالها خلال الجولة
asked_cities = set()

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        player_name = request.form.get("player_name")
        if player_name:
            save_name(player_name)
            return render_template("index.html", player_name=player_name)
    return render_template("register.html")

@app.route("/game")
def index():
    return render_template("index.html")

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

@app.route("/players")
def players():
    return jsonify(get_names())

if __name__ == "__main__":
    app.run(debug=True)
