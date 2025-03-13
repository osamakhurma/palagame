from flask import Flask, render_template, request, jsonify
import random
import os
from PIL import Image  # للتأكد من أبعاد الصورة

app = Flask(__name__, static_folder='.')

# البيانات الخاصة بالمحافظات والمدن (مخزنة محليًا)
provinces = [
    {"name": "حيفا", "x": 238, "y": 139},
    {"name": "عكا", "x": 257, "y": 114},
    {"name": "يافا", "x": 199, "y": 312},
    {"name": "غزة", "x": 143, "y": 422},
    {"name": "رفح", "x": 108, "y": 479},
    {"name": "بئر السبع", "x": 200, "y": 489},
    {"name": "صفد", "x": 337, "y": 100},
    {"name": "طبريا", "x": 343, "y": 152},
    {"name": "بيسان", "x": 338, "y": 201},
    {"name": "الناصرة", "x": 295, "y": 161},
]

cities = [
    {"name": "جنين", "x": 302, "y": 206},
    {"name": "نابلس", "x": 294, "y": 261},
    {"name": "أريحا", "x": 326, "y": 349},
    {"name": "رام الله", "x": 282, "y": 345},
    {"name": "القدس", "x": 286, "y": 370},
    {"name": "بيت لحم", "x": 281, "y": 385},
    {"name": "الخليل", "x": 248, "y": 425},
]

# تتبع المرحلة الحالية وعدد الإجابات الصحيحة
current_stage = "provinces"  # أولًا المحافظات
score = 0
questions = []

# دالة للتحقق من أبعاد الصورة
def check_image_dimensions(image_path, expected_width, expected_height):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            if width != expected_width or height != expected_height:
                print(f"تحذير: أبعاد الصورة غير صحيحة! المتوقع: {expected_width}x{expected_height}, الفعلي: {width}x{height}")
            else:
                print("أبعاد الصورة صحيحة.")
    except Exception as e:
        print(f"خطأ في فتح الصورة: {e}")

# تحقق من أبعاد الصورة عند بدء التشغيل
check_image_dimensions("213.png", 486, 900)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_question', methods=['GET'])
def get_question():
    global current_stage, score, questions
    
    if current_stage == "provinces":
        data = provinces
    else:
        data = cities
    
    if len(questions) == 0:
        questions = random.sample(data, len(data))
    
    question = questions.pop()
    
    # إرسال الإحداثيات بشكل دقيق
    return jsonify({
        "name": question["name"],
        "x": question["x"],
        "y": question["y"]
    })

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    global score, current_stage
    
    data = request.json
    correct_x = int(data['correct_x'])
    correct_y = int(data['correct_y'])
    user_x = int(data['user_x'])
    user_y = int(data['user_y'])
    
    distance = ((correct_x - user_x) ** 2 + (correct_y - user_y) ** 2) ** 0.5
    if distance < 20:
        score += 1
    
    if score == 5 and current_stage == "provinces":
        current_stage = "cities"
        score = 0
        return jsonify({"message": "مبروك! انتقلت إلى مرحلة المدن."})
    elif score == 10 and current_stage == "cities":
        return jsonify({"message": "مبروك! أنهيت اللعبة!"})
    
    return jsonify({"score": score})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
