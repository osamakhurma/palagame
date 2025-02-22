from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# قائمة المدن والمحافظات مع الإحداثيات بناءً على الصورة 700x700
locations = {
    "الخليل": (347, 346, "governorate"),
    "بيت لحم": (396, 299, "city"),
    "القدس": (399, 279, "city"),
    "أريحا": (430, 239, "city"),
    "رام الله": (380, 236, "governorate"),
    "نابلس": (390, 190, "governorate"),  # تم تعديل الموقع
    "بئر السبع": (280, 416, "governorate"),
    "رفح": (205, 401, "city"),
    "غزة": (206, 363, "city"),
    "يافا": (309, 211, "city"),
    "الرملة": (326, 249, "city"),
    "طبريا": (444, 115, "city"),
    "بيسان": (443, 162, "city"),
    "حيفا": (336, 103, "city"),
    "عكا": (360, 77, "city"),
    "صفد": (441, 64, "city"),
    "جنين": (390, 160, "city"),  # تم تعديل الموقع
    "الناصرة": (404, 127, "city")
}

def get_random_city():
    return random.choice(list(locations.keys()))

@app.route('/')
def index():
    city = get_random_city()
    return render_template('index.html', city=city, locations=locations)

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    city = data['city']
    correct_x, correct_y, _ = locations[city]

    return jsonify({"result": "صح ✅", "new_city": get_random_city()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
