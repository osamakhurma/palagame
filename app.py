from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

locations = {
    "الخليل": (347, 346, "governorate", "تشتهر بصناعة الزجاج والخزف"),
    "بيت لحم": (396, 299, "city", "تشتهر بكنيسة المهد"),
    "القدس": (399, 279, "city", "مشهورة بالمعالم التاريخية والدينية"),
    "أريحا": (430, 239, "city", "من أقدم مدن العالم"),
    "رام الله": (380, 236, "governorate", "مركز ثقافي مهم"),
    "نابلس": (390, 190, "governorate", "مشهورة بالكنافة النابلسية"),
    "بئر السبع": (280, 416, "governorate", "أكبر مدن النقب"),
    "رفح": (205, 401, "city", "مدينة حدودية مع مصر"),
    "غزة": (206, 363, "city", "معروفة بمينائها وتاريخها العريق"),
    "يافا": (309, 211, "city", "تشتهر بالبرتقال اليافاوي"),
    "الرملة": (326, 249, "city", "مدينة تاريخية قديمة"),
    "طبريا": (444, 115, "city", "تقع على بحيرة طبريا"),
    "بيسان": (443, 162, "city", "مدينة أثرية"),
    "حيفا": (336, 103, "city", "مشهورة بمينائها"),
    "عكا": (360, 77, "city", "معروفة بالأسوار التاريخية"),
    "صفد": (441, 64, "city", "مدينة جبلية تاريخية"),
    "جنين": (390, 160, "city", "تشتهر بمخيم جنين"),
    "الناصرة": (404, 127, "city", "مشهورة بكنيسة البشارة")
}

def get_random_cities(count=10):
    return random.sample(list(locations.keys()), count)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['GET'])
def start_game():
    cities = get_random_cities()
    return jsonify({"cities": cities})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    city = data['city']
    if city in locations:
        info = locations[city][3]
        return jsonify({"status": "correct", "info": info})
    else:
        return jsonify({"status": "wrong"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
