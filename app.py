from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# المدن وإحداثياتها على الخريطة
cities = {
    "القدس": {"x": 282, "y": 368},
    "الخليل": {"x": 249, "y": 428},
    "غزة": {"x": 142, "y": 424},
    "نابلس": {"x": 293, "y": 259},
    "بيت لحم": {"x": 270, "y": 400},  # تأكد أن القيم دقيقة
    "يافا": {"x": 199, "y": 313},
    "بئر السبع": {"x": 198, "y": 490},
    "رفح": {"x": 106, "y": 477},
    "جنين": {"x": 299, "y": 207},
    "أريحا": {"x": 325, "y": 349},
    "عكا": {"x": 258, "y": 113},
    "الناصرة": {"x": 297, "y": 161},
    "صفد": {"x": 339, "y": 98},
    "حيفا": {"x": 237, "y": 139},
    "طبريا": {"x": 344, "y": 153}
}

# المدينة الحالية
current_city = None

@app.route("/")
def index():
    return render_template("index.html", cities=cities)

@app.route("/get_question")
def get_question():
    import random
    global current_city
    current_city = random.choice(list(cities.keys()))
    return jsonify({"question": f"أين تقع {current_city}؟", "city": current_city})

@app.route("/check_answer", methods=["POST"])
def check_answer():
    global current_city
    if not current_city:
        return jsonify({"error": "No active question!"})

    data = request.get_json()
    x, y = data["x"], data["y"]

    correct_x = cities[current_city]["x"]
    correct_y = cities[current_city]["y"]

    # السماح بهامش خطأ ±10 بيكسل
    margin = 10
    correct = (correct_x - margin <= x <= correct_x + margin) and (correct_y - margin <= y <= correct_y + margin)

    return jsonify({"correct": correct})

if __name__ == "__main__":
    app.run(debug=True)
