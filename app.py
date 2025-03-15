from flask import Flask, render_template, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"  # ضروري لاستخدام session

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

@app.route("/")
def index():
    # تصفير الجلسة عند بدء اللعبة
    session["asked_cities"] = []
    return render_template("index.html")

@app.route("/get_question")
def get_question():
    asked_cities = session.get("asked_cities", [])
    remaining_cities = [city for city in cities.keys() if city not in asked_cities]

    if not remaining_cities:
        session["asked_cities"] = []  # إعادة ضبط القائمة عند انتهاء كل الأسئلة
        remaining_cities = list(cities.keys())

    city = random.choice(remaining_cities)
    asked_cities.append(city)
    session["asked_cities"] = asked_cities  # حفظ القائمة المحدثة

    return jsonify({"question": f"أين تقع مدينة {city}؟", "city": city, "coords": cities[city]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
