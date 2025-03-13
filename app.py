from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# كل المدن مع الإحداثيات بناءً على الخريطة 486x900
cities = {
    "الخليل": {"x": 249, "y": 428},
    "بئر السبع": {"x": 198, "y": 490},
    "رفح": {"x": 106, "y": 477},
    "غزة": {"x": 142, "y": 424},
    "يافا": {"x": 199, "y": 313},
    "أريحا": {"x": 325, "y": 349},
    "القدس": {"x": 282, "y": 368},
    "نابلس": {"x": 293, "y": 259},
    "جنين": {"x": 299, "y": 207},
    "طبريا": {"x": 344, "y": 153},
    "الناصرة": {"x": 297, "y": 161},
    "صفد": {"x": 339, "y": 98},
    "عكا": {"x": 258, "y": 113},
    "حيفا": {"x": 237, "y": 139}
}

# المدينة الحالية للسؤال
current_question = {"city": None}

@app.route('/')
def index():
    return render_template('index.html', cities=cities)

@app.route('/get_question')
def get_question():
    """إرسال سؤال عشوائي عن مدينة"""
    current_question["city"] = random.choice(list(cities.keys()))
    return jsonify({"question": f"أين تقع مدينة {current_question['city']}؟", "city": current_question["city"]})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    """التأكد إذا كان اللاعب اختار الموقع الصحيح"""
    data = request.json
    selected_x = data['x']
    selected_y = data['y']
    correct_city = current_question["city"]

    if correct_city:
        correct_x = cities[correct_city]["x"]
        correct_y = cities[correct_city]["y"]
        distance = ((selected_x - correct_x) ** 2 + (selected_y - correct_y) ** 2) ** 0.5

        if distance < 20:  # السماح بهامش خطأ بسيط
            return jsonify({"correct": True})
        else:
            return jsonify({"correct": False})

    return jsonify({"error": "لم يتم تحديد سؤال بعد!"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
