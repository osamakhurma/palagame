from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# المدن مع إحداثياتها والمعلومات عنها
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

# قائمة المدن المختارة حتى الآن
chosen_cities = []
score = 0

def get_random_city():
    remaining_cities = list(set(locations.keys()) - set(chosen_cities))
    return random.choice(remaining_cities) if remaining_cities else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['GET'])
def start_game():
    global chosen_cities, score
    chosen_cities = []
    score = 0
    city = get_random_city()
    return jsonify({"city": city})

@app.route('/check', methods=['POST'])
def check():
    global score
    data = request.json
    city = data['city']
    
    if city in locations and city not in chosen_cities:
        chosen_cities.append(city)
        score += 1
        x, y, _, info = locations[city]
        
        if len(chosen_cities) == 10:
            return jsonify({"result": "انتهت اللعبة!", "score": score})
        
        return jsonify({"result": "صح ✅", "info": info, "new_city": get_random_city(), "score": score})
    else:
        return jsonify({"result": "خطأ ❌", "score": score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
