# Cyclone Path Prediction Using Deep Learning

This project implements a machine learning–based system to predict cyclone paths across different ocean basins using historical cyclone track data. Basin-specific models are trained to forecast future cyclone coordinates, and predictions are served through a Flask web application with interactive visualisation.

---

## Project Overview

Accurate cyclone path prediction is essential for disaster preparedness and risk mitigation. This project predicts future latitude and longitude positions of cyclones using historical track data recorded at six-hour intervals.

Separate models are trained for the **Indian**, **Pacific**, and **Atlantic** ocean basins to capture region-specific movement patterns and improve prediction accuracy.

---

## Models and Approach

The following models are used for cyclone path prediction:

- Long Short-Term Memory (LSTM) networks for sequential trajectory modelling  
- Support Vector Regression (SVR) as a baseline regression model  
- Gradient Boosting Regressor (GBR) for non-linear regression  

Each basin is trained independently to better model regional cyclone behaviour.

---

## Repository Structure

```
.
├── indian.py # Train models for Indian Ocean basin
├── pacific.py # Train models for Pacific Ocean basin
├── copy_of_atlantic2.py # Train models for Atlantic Ocean basin
├── prediction_indian.py # Generate predictions for Indian Ocean
├── prediction_pacific.py # Generate predictions for Pacific Ocean
├── prediction_atlantic.py # Generate predictions for Atlantic Ocean
├── app.py # Flask web application
└── README.md
```


---

## Usage

### Training Basin-Specific Models

Train cyclone path prediction models for each ocean basin using:

```bash
python indian.py
python pacific.py
python copy_of_atlantic2.py
```

Each script:
- Loads basin-specific cyclone track data
- Trains LSTM, SVR, and Gradient Boosting models
- Saves trained models for downstream prediction

### Generating Predictions

After training, generate cyclone path forecasts using:
```bash
python prediction_indian.py
python prediction_pacific.py
python prediction_atlantic.py
```

These scripts:
- Load trained basin-specific models
- Accept recent cyclone coordinates as input
- Predict future latitude and longitude positions

### Running the Web Application
Start the Flask application:
```bash
python app.py
```
The web interface allows users to:
- Select an ocean basin
- Enter cyclone coordinates
- Generate predicted cyclone paths
- Visualise predictions on an interactive map

---

## Results
The trained models learn cyclone movement patterns across different ocean basins. LSTM models capture temporal dependencies effectively, while ensemble methods improve prediction robustness. Basin-specific training improves regional forecast accuracy.

---

## Technologies Used
- Python
- TensorFlow / Keras
- scikit-learn
- Flask
- NumPy, pandas
- Heroku (deployment)

---

## Author
Sundararajan Srinivasan

GitHub: https://github.com/Sundar-1002

---