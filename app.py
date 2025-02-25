from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# الإحداثيات المحدثة للخريطة الجديدة بحجم 467x506 بكسل
locations = {
    "الخليل": (240, 370, "governorate", "تشتهر بصناعة الزجاج والخزف"),
    "بيت لحم": (260, 340, "city", "تشتهر بكنيسة المهد"),
    "القدس": (270, 320, "city", "مشهورة بالمعالم التاريخية والدينية"),
    "أريحا": (310, 310, "city", "من أقدم مدن العالم"),
    "رام الله": (260, 290, "governorate", "مركز ثقافي مهم"),
    "نابلس": (270, 250, "governorate", "مشهورة بالكنافة النابلسية"),
    "بئر السبع": (190, 420, "governorate", "أكبر مدن النقب"),
    "رفح": (160, 460, "city", "مدينة حدودية مع مصر"),
    "غزة": (160, 420, "city", "معروفة بمينائها وتاريخها العريق"),
    "يافا": (200, 200, "city", "تشتهر بالبرتقال اليافاوي"),
    "الرملة": (220, 240, "city", "مدينة تاريخية قديمة"),
    "طبريا": (350, 150, "city", "تقع على بحيرة طبريا"),
    "بيسان": (360, 190, "city", "مدينة أثرية"),
    "حيفا": (250, 120, "city", "مشهورة بمينائها"),
    "عكا": (270, 100, "city", "معروفة بالأسوار التاريخية"),
    "صفد": (340, 80, "city", "مدينة جبلية تاريخية"),
    "جنين": (290, 200, "city", "تشتهر بمخيم جنين"),
    "الناصرة": (300, 160, "city", "مشهورة بكنيسة البشارة")
}

def get_random_cities(count=10):
    return random.sample(list(locations.keys()), count)

@app.route('/')
def index():
    return render_template('index.html', locations=locations)

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
