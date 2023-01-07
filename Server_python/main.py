import pickle
from flask_cors import CORS, cross_origin
from flask import Flask
import os
from load_model import detect_from_video
from load_model import detect_from_image

#CONSTANTS
PATH_GUESS = 'image_to_guess/'
PATH_DETECTED = 'image_detected/'

# Khởi tạo Flask
app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def detect():
    with open('data.pkl', 'rb') as file:
        # Sử dụng hàm pickle.load() để đọc dữ liệu từ file và gán vào biến data
        data = pickle.load(file)
        return data

# Hàm xử lý request
@app.route("/", methods=['GET'])
@cross_origin(origin='*')
def home_page():
    return detect()

#test route api
@app.route('/detect_from_image')
def detect_image():
	image_guess = PATH_GUESS + 'di_thang_9.png'
	image_out = PATH_DETECTED + 'di_thang_9.png'
	guess = detect_from_image(image_guess, image_out)
	print(guess)
	return guess


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

    








