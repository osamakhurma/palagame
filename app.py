from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

# قائمة المدن الفلسطينية مع الإحداثيات الصحيحة
cities = {
    "الخليل": (249, 428),
    "بئر السبع": (198, 490),
    "رفح": (106, 477),
    "غزة": (142, 424),
    "يافا": (199, 313),
    "أريحا": (325, 349),
    "القدس": (282, 368),
    "نابلس": (293, 259),
    "جنين": (299, 207),
    "طبريا": (344, 153),
    "الناصرة": (297, 161),
    "صفد": (339, 98),
    "عكا": (258, 113),
    "حيفا": (237, 139)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    city_name = data.get("city")
    x, y = data.get("x"), data.get("y")

    if city_name in cities:
        correct_x, correct_y = cities[city_name]
        distance = ((x - correct_x) ** 2 + (y - correct_y) ** 2) ** 0.5

        if distance < 20:  # هامش خطأ بسيط
            return jsonify({"correct": True})
    
    return jsonify({"correct": False})

if __name__ == '__main__':
    app.run(debug=True)
