from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# قائمة المدن مع إحداثياتها
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

# اختيار مدينة عشوائية لسؤال المستخدم
import random
def get_new_city():
    return random.choice(list(locations.keys()))

current_city = get_new_city()

@app.route('/')
def index():
    return render_template('index.html', city=current_city, locations=locations)

@app.route('/check', methods=['POST'])
def check_location():
    global current_city
    data = request.json
    x, y = data['x'], data['y']
    city_x, city_y = locations[current_city]
    
    correct = abs(x - city_x) <= 15 and abs(y - city_y) <= 15  # هامش الخطأ 15 بكسل
    
    if correct:
        current_city = get_new_city()
    
    return jsonify({"correct": correct, "new_city": current_city})

if __name__ == '__main__':
    app.run(debug=True)
