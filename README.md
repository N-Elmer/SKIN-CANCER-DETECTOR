# SKIN-CANCER-DETECTOR
SKIN CANCER 🔬🧪DETECTION SYSTEM

SKIN-CANCER-DETECTOR is a web application that detects malignant and benign skin cancer. It leverages computer vision and image recognition techniques to determine if a patient has skin cancer or not. The application offers a friendly and intuitive web interface for users who are non technical to easily use the AI.

## Folder Structure

📂 SKIN-CANCER-DETECTOR
   
   |
   
   ├── 📄 README.md
   
   ├── 📂 datasets
   
   │   ├── 📂 test
   
   │   │   ├── 📂 benign

   │   │   ├── 📂 malignant
   
   │   ├── 📂 train

   │   │   ├── 📂 benign

   │   │   ├── 📂 malignant
   
   ├── 📂 model
   
   │   ├── 📄 saved_model.h5
   
   ├── 📂 uploads
   
   ├── 📂 static
   
   │   ├── 📂 css
   
   │   │   └── 📄 styles.css

   │   ├── 📂 images
   
   │   │   └── 📄 header-image.jpg
   
   │   ├── 📂 js
   
   │   │   └── 📄 script.js
   
   │   └── 📄 favicon.ico
   
   ├── 📂 templates

   │   ├── 📄 index.html
   
   │   └── 📄 result.html
   
   ├── 📄 CancerDetector.ipynb
   
   ├── 📄 app.py
   
   └── 📄 requirements.txt

The project folder structure consists of the following files and folders:

- 📄 README.md: This file contains the documentation and information about the FOOT-FORECASTER web application, including how to use it and any additional details.

- 📂 data: This folder contains the data files used for preprocessing and training the machine learning models.

- 📂 models: This folder contains the trained machine learning model in the form of an h5 file named `saved_model.h5`.

- 📂 static: This folder contains the static assets used in the web application, including CSS files, JavaScript files, and a favicon.ico file.

   - 📂 css: This subfolder contains the CSS stylesheets used for styling the web application, specifically the `styles.css` file.

   - 📂 js: This subfolder contains the JavaScript files used for the web application's functionality, including the `script.js` files.

- 📂 templates: This folder contains the HTML templates used for rendering the web pages, specifically the `index.html` and the `result.html` file.

- 📄 CancerDetector.ipynb: This Jupyter Notebook file is used for training machine learning models for the image detection.

- 📄 app.py: This file contains the Flask microservice backend for the FOOT-FORECASTER web application. It includes the machine learning model and handles the data requests and responses.

- 📄 requirements.txt: This file lists the project's dependencies and their versions for easy installation.

## Usage

To use the SKIN-CANCER-DETECTOR web application, follow these steps:

1. Clone or download this project repository.

2. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

3. Open the `CancerDetector.ipynb` notebook and execute it to train the machine learning models.

4. Run the Flask microservice backend by executing the following command:

   ```
   python app.py
   ```

5. Open a web browser and access the SKIN-CANCER-DETECTOR web application by navigating to `http://localhost:5000`.

6. Using the upload button on the web user interface, upload an image you wish to test for cancer.

7. View the test results on the results page.

## Code Explanation

The SKIN-CANCER-DETECTOR web application is implemented using HTML, CSS, JavaScript and Flask. Here's a breakdown of the different components:

- **JavaScript**: This file handles the interactivity of the web application, including attaching event listeners, updating the user interface on user input.

- **Flask**: The Flask microservice backend is implemented in the `app.py` file. It handles the routing and data requests for the web application.

## Troubleshooting

If you encounter any issues or errors while using the SKIN-CANCER-DETECTOR web application, consider the following:

- Double-check that all the necessary files and folders are present in the correct locations, as described in the folder structure section.

- Ensure that you have Python installed on your system, and the required dependencies are installed by running `pip install -r requirements.txt`.

- Verify that the data files are located in the `datasets` folder.

- If you encounter any issues with the machine learning models, make sure you have successfully preprocessed the data and trained the models using the provided Jupyter Notebook files (`CancerDetector.ipynb`).

- If the Flask microservice backend fails to run, check that there are no errors in the `app.py` file and that the required dependencies are installed.

If the problem persists, feel free to open an issue in the GitHub repository for further assistance.

---

This README file provides an overview of the FOOT-FORECASTER web application, its folder structure, usage instructions, code explanation, and troubleshooting tips. Use it as a guide to understand and utilize the SKIN-CANCER-DETECTOR app.
