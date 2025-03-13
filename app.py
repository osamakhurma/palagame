from flask import Flask, render_template, request, jsonify
import os
import random

app = Flask(__name__)

locations = {
    "الخليل": (346, 347, "governorate", "تشتهر بصناعة الزجاج والخزف"),
    "بيت لحم": (299, 396, "city", "تشتهر بكنيسة المهد"),
    "القدس": (279, 399, "city", "مشهورة بالمعالم التاريخية والدينية"),
    "أريحا": (239, 430, "city", "من أقدم مدن العالم"),
    "رام الله": (236, 380, "governorate", "مركز ثقافي مهم"),
    "نابلس": (190, 390, "governorate", "مشهورة بالكنافة النابلسية"),
    "بئر السبع": (416, 280, "governorate", "أكبر مدن النقب"),
    "رفح": (401, 205, "city", "مدينة حدودية مع مصر"),
    "غزة": (363, 206, "city", "معروفة بمينائها وتاريخها العريق"),
    "يافا": (211, 309, "city", "تشتهر بالبرتقال اليافاوي"),
    "الرملة": (249, 326, "city", "مدينة تاريخية قديمة"),
    "طبريا": (115, 444, "city", "تقع على بحيرة طبريا"),
    "بيسان": (162, 443, "city", "مدينة أثرية"),
    "حيفا": (103, 336, "city", "مشهورة بمينائها"),
    "عكا": (77, 360, "city", "معروفة بالأسوار التاريخية"),
    "صفد": (64, 441, "city", "مدينة جبلية تاريخية"),
    "جنين": (160, 390, "city", "تشتهر بمخيم جنين"),
    "الناصرة": (127, 404, "city", "مشهورة بكنيسة البشارة"),
}

stages = ["مدن", "محافظات"]
num_questions_per_stage = 5
max_time_per_stage = 30  # بالثواني

@app.route('/')
def index():
    return render_template('index.html', stages=stages, time=max_time_per_stage)

@app.route('/start_game', methods=['POST'])
def start_game():
    stage = request.json.get("stage", 0)
    if stage >= len(stages):
        return jsonify({"message": "اللعبة انتهت!", "success": False})
    
    questions = random.sample(list(locations.keys()), num_questions_per_stage)
    return jsonify({"stage": stages[stage], "questions": questions, "time": max_time_per_stage})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    city = data.get("city")
    answer = data.get("answer")
    
    if city in locations and answer == city:
        return jsonify({"correct": True, "info": locations[city][3]})
    return jsonify({"correct": False})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
