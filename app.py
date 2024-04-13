import os
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
saved_model_path = 'model/saved_model.h5'

def load_or_train_model():
    if os.path.exists(saved_model_path):
        model = load_model(saved_model_path)
    else:
        # Preprocess the images and labels
        image_size = (128, 128)
        batch_size = 32

        train_folder = 'datasets/train'
        test_folder = 'datasets/test'

        train_data_generator = ImageDataGenerator(rescale=1./255)
        test_data_generator = ImageDataGenerator(rescale=1./255)

        train_generator = train_data_generator.flow_from_directory(
            train_folder,
            target_size=image_size,
            batch_size=batch_size,
            class_mode='binary'
        )

        test_generator = test_data_generator.flow_from_directory(
            test_folder,
            target_size=image_size,
            batch_size=batch_size,
            class_mode='binary',
            shuffle=False
        )

        # Build the model
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)))
        model.add(MaxPooling2D((2, 2)))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Conv2D(128, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        # Train the model
        epochs = 10

        history = model.fit(
            train_generator,
            steps_per_epoch=len(train_generator),
            epochs=epochs,
            validation_data=test_generator,
            validation_steps=len(test_generator)
        )

        # Save the trained model
        model.save(saved_model_path)

    return model

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(filepath)

        # Load or train the model
        model = load_or_train_model()

        # Preprocess the uploaded image
        image_size = (128, 128)
        image = Image.open(filepath)
        image = image.resize(image_size)
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)

        # Run the model inference
        prediction = model.predict(image)[0][0] * 100
        prediction = round(prediction, 2)

        # Render the result on the HTML page
        return render_template('result.html', prediction=prediction)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)