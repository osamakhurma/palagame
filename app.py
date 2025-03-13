from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# بيانات المواقع مع المعلومات
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

# تعريف المراحل
stages = [
    {"name": "المدن", "questions": 5},
    {"name": "المحافظات", "questions": 5}
]

# الزمن لكل مرحلة
max_time_per_stage = 30

@app.route('/')
def index():
    return render_template('index.html', locations=locations, stages=stages, time=max_time_per_stage)

# API لتحديث النقاط أو تسجيل الإجابات
@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    if not data or "city" not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    city = data["city"]
    if city in locations:
        return jsonify({"correct": True, "info": locations[city][3]})
    return jsonify({"correct": False, "info": "إجابة غير صحيحة"}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)
