# CNN_XRAY_Classifier

# Lung Condition Prediction

This project is a web application for predicting lung conditions from chest X-ray images using a deep learning model. The application can classify the images into three categories: COVID-19 infected lungs, pneumonia infected lungs, and normal lungs.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Contributing](#contributing)

## Features

- Upload chest X-ray images for analysis.
- Predict lung conditions using a pre-trained deep learning model.
- Display the prediction result on the web page.

## Demo

You can try the live demo of the application [here](#).

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/lung-condition-prediction.git
    cd lung-condition-prediction
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download the pre-trained model:**

    - Place your pre-trained `model.h5` file in the project root directory.

## Usage

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

2. **Open your web browser and go to:**

    ```
    http://127.0.0.1:3000/
    ```

3. **Upload a chest X-ray image and get the prediction result.**

## Model

The deep learning model used in this project is a pre-trained model designed to classify chest X-ray images into three categories:
- COVID-19 infected lungs
- Pneumonia infected lungs
- Normal lungs

Ensure your `model.h5` file is properly trained and placed in the project root directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.
