from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"  # مفتاح التشفير للجلسة

# قائمة المدن والمحافظات مع الإحداثيات والمعلومات
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
    "الناصرة": (404, 127, "city", "مشهورة بكنيسة البشارة"),
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
    correct = city in locations
    
    if correct:
        session['score'] += 1  # زيادة السكور
        info = locations[city][3]  # جلب المعلومات عن المدينة
    else:
        info = "إجابة خاطئة! حاول مرة أخرى."
    
    return jsonify({
        "result": "صح ✅" if correct else "خطأ ❌",
        "new_city": get_random_city() if correct else city,
        "score": session['score'],
        "info": info
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
