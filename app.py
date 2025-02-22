from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"  # مفتاح التشفير للجلسة

# قائمة المدن والمحافظات مع الإحداثيات بناءً على الصورة 700x700
locations = {
    "الخليل": (347, 346, "governorate"),
    "بيت لحم": (396, 299, "city"),
    "القدس": (399, 279, "city"),
    "أريحا": (430, 239, "city"),
    "رام الله": (380, 236, "governorate"),
    "نابلس": (390, 190, "governorate"),
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
    "جنين": (390, 160, "city"),
    "الناصرة": (404, 127, "city")
}

def get_random_city():
    return random.choice(list(locations.keys()))

@app.route('/')
def index():
    session['score'] = 0  # إعادة تعيين السكور عند بدء اللعبة
    city = get_random_city()
    return render_template('index.html', city=city, locations=locations, score=session['score'])

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    city = data['city']
    
    if city in locations:  # إذا الجواب صحيح
        session['score'] += 1  # زيادة السكور
    
    return jsonify({"result": "صح ✅", "new_city": get_random_city(), "score": session['score']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
