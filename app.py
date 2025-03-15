from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

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
    return render_template("index.html")

@app.route("/get_question")
def get_question():
    import random
    city = random.choice(list(cities.keys()))
    return jsonify({"question": f"أين تقع مدينة {city}؟", "city": city, "coords": cities[city]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
