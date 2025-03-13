from flask import Flask, render_template, jsonify, request
import os
import random

app = Flask(__name__)

# بيانات المدن مع الإحداثيات
locations = {
    "الخليل": (346, 347),
    "بيت لحم": (299, 396),
    "القدس": (279, 399),
    "أريحا": (239, 430),
    "رام الله": (236, 380),
    "نابلس": (190, 390),
    "بئر السبع": (416, 280),
    "رفح": (401, 205),
    "غزة": (363, 206),
    "يافا": (211, 309),
    "الرملة": (249, 326),
    "طبريا": (115, 444),
    "بيسان": (162, 443),
    "حيفا": (103, 336),
    "عكا": (77, 360),
    "صفد": (64, 441),
    "جنين": (160, 390),
    "الناصرة": (127, 404),
}

# توليد سؤال عشوائي
def get_random_city():
    return random.choice(list(locations.keys()))

@app.route('/')
def index():
    return render_template('index.html', locations=locations, question=get_random_city())

@app.route('/get_question')
def get_question():
    return jsonify({"question": get_random_city()})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    city = data.get("city")
    x, y = data.get("x"), data.get("y")

    if city not in locations:
        return jsonify({"correct": False})

    actual_x, actual_y = locations[city]
    tolerance = 20  # مدى السماح للخطأ بالنقر

    if abs(x - actual_x) <= tolerance and abs(y - actual_y) <= tolerance:
        return jsonify({"correct": True})
    
    return jsonify({"correct": False})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
