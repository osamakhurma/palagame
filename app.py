from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# قائمة المدن مع إحداثياتها الصحيحة
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
    "حيفا": (237, 139),
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_answer", methods=["POST"])
def check_answer():
    data = request.json
    city_name = data.get("city")
    x, y = data.get("x"), data.get("y")

    if city_name in cities:
        correct_x, correct_y = cities[city_name]
        tolerance = 15  # مدى قبول الخطأ في تحديد النقطة

        if abs(x - correct_x) <= tolerance and abs(y - correct_y) <= tolerance:
            return jsonify({"correct": True})
        else:
            return jsonify({"correct": False})

    return jsonify({"error": "مدينة غير معروفة"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # استخدام المنفذ من البيئة أو 5000 افتراضيًا
    app.run(host="0.0.0.0", port=port, debug=True)
