import io
import PIL
import base64
import numpy as np
import gc

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


def predict(base64string):
    images_to_predict = []
    image_data = base64.b64decode(base64string)
    img = PIL.Image.open(io.BytesIO(image_data))
    img = img.resize((64, 64))
    img = image.img_to_array(img)
    img = img/255
    images_to_predict.append(img)
    array_of_images_to_predict = np.array(images_to_predict)

    model = load_model('model_1.h5')

    predictions = model.predict(array_of_images_to_predict)
    class_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    prediction_labels = class_names[np.argmax(predictions)]

    letter_predicted = prediction_labels[0]
    print(f'## Prediction from image received: {letter_predicted} ##')

    gc.collect()

    return letter_predicted
