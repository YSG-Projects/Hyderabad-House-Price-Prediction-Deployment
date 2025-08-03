# 🏠 House Price Predictor - Hyderabad

A machine learning web application that predicts the **house price in Hyderabad** based on various input features such as area type, number of bedrooms, location, size, and more.

The model is trained using real estate data and deployed using **Flask**, making it easy to interact with via a web interface.

---

## 🚀 Features

- Interactive web UI built with **HTML + Flask**
- Machine Learning model trained using **GridSearchCV**
- Trained model serialized using **joblib**
- Predict house prices in Hyderabad in real-time
- Ready for deployment on **Render**, **Railway**, or **Streamlit Cloud**

---

## 🧠 Machine Learning Workflow

- Exploratory Data Analysis (EDA)
- Data cleaning and feature engineering
- Encoding categorical variables
- Feature selection
- Train-test split
- Model tuning with **GridSearchCV**
- Final model saved as `house_price_model.pkl`

---

## 🗂️ Folder Structure

house-price-predictor/
│
├── app.py # Flask backend app
├── house_price_model.pkl # Trained ML model
├── train_model.ipynb # Notebook for training & tuning
│
├── data/
│ └── hyderabad_house_prices.csv
│
├── templates/
│ ├── home.html # Input form
│ └── result.html # Result page
│
├── static/ # Optional: CSS/images if any
│
├── Procfile # For Render/Railway deployment
├── requirements.txt # Python dependencies
└── README.md

yaml
Copy
Edit

---

## 💻 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/house-price-predictor.git
   cd house-price-predictor
Create virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
python app.py
Open in browser
Visit http://127.0.0.1:5000 to access the app.

🌍 Deployment
Option 1: Render
Create a new Web Service.

Connect your GitHub repo.

Set the build command (if needed): pip install -r requirements.txt

Set the start command: python app.py

Option 2: Railway, Streamlit Cloud, or Heroku (similar setup)
📦 Requirements
Make sure these are in your requirements.txt:

nginx
Copy
Edit
flask
numpy
pandas
scikit-learn
joblib
To generate it:

bash
Copy
Edit
pip freeze > requirements.txt
✨ Future Improvements
Add interactive maps for location selection

Improve UI/UX with Bootstrap or Tailwind

Support multiple cities (Bangalore, Mumbai, etc.)

Add user authentication for profile-based history

🙌 Acknowledgements
Hyderabad Housing Data from Kaggle

Scikit-learn for ML tools

Flask for backend