from tensorflow.keras.models import load_model
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import io

model = load_model('model.h5')

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    image_file = request.files["image"]
    image = load_img(io.BytesIO(image_file.read()), target_size=(256, 256))  # Ensure target size matches model input
    image = img_to_array(image)
    image = image / 255.0
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)  # Expand dimensions to match the model input

    pred = model.predict(image)
    pred = np.argmax(pred, axis=1)

    result = "Could not classify the image"  # Default message

    if pred[0] == 0:  # Check pred[0] instead of pred
        result = 'covid-19 infected lungs'
    elif pred[0] == 1:
        result = "pneumonia infected lungs"
    elif pred[0] == 2:
        result = "normal lungs" 
        
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
