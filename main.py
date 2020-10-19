from flask import Flask, render_template, Response, request, jsonify
from Prediction import predict

app = Flask(__name__)


@app.route('/')
def camera():
    return render_template('index.html')


@app.route('/image', methods=['GET', 'POST'])
def signup():
    incoming_pkg = request.get_json()
    img_b64_str_encoded = str(incoming_pkg['imgBase64'])
    image_array = img_b64_str_encoded.split(',')
    image = image_array[len(image_array) - 1]
    app.logger.info("Processing and Predicting Which Digit ...")
    prediction = predict(image)

    return jsonify(response=prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
