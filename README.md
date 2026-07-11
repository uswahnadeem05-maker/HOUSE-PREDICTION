<div align="center">

# 🏠 Pakistan House Price Predictor

**AI-powered real estate valuation tool trained on 100,000+ real property listings across Pakistan.**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Try_it_Now-10B981?style=for-the-badge)](https://huggingface.co/spaces/uswahnadeem05-maker/pakistan-house-price-predictor)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/uswahnadeem05-maker/HOUSE-PREDICTION)
[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

</div>

---

## 📖 Overview
]
This project predicts house prices across Pakistan using machine learning, trained on real listings scraped from Zameen.com — Pakistan's largest property portal. Built as part of a Data Analytics Internship at **CodeAlpha**, it combines data cleaning, exploratory analysis, model training, and AI integration into a single deployed web app.

## ✨ Features

| Feature | Description |
|---|---|
| 🔮 **Instant Prediction** | Get a price estimate in seconds based on city, area, bedrooms, bathrooms, and location |
| 📊 **Price Range** | Confidence interval from the model's tree ensemble, not just a single guess |
| 🏘️ **Similar Listings** | Real comparable properties pulled directly from the dataset |
| 🤖 **AI Assistant** | Chat with a Gemini-powered assistant about Pakistani real estate |
| 📈 **Data Explorer** | Interactive charts on pricing trends, city comparisons, and property types |

## 🖥️ Preview

<img width="853" height="404" alt="HPUSE PRED PI  2" src="https://github.com/user-attachments/assets/67d54751-6604-460b-9243-cbbb63c39ae3" />
<img width="860" height="374" alt="HPUSE PRED PIC 1" src="https://github.com/user-attachments/assets/bf71e60c-36bb-4cad-84f4-20000abcad98" />

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/-Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Gradio](https://img.shields.io/badge/-Gradio-FF7C00?style=flat-square)
![Gemini](https://img.shields.io/badge/-Gemini_API-8E75B2?style=flat-square&logo=google&logoColor=white)

## 📊 Data & Model

- **Source:** 168,446 real property listings from Zameen.com
- **Cleaning:** Filtered to "For Sale" listings, removed price outliers, unified mixed area units (Marla/Kanal), log-transformed skewed price and area distributions
- **Final dataset:** 89,642 clean listings (House & Flat only)
- **Model:** Random Forest Regressor (100 trees)
- **Performance:**

| Model | R² Score |
|---|---|
| Linear Regression | 0.66 |
| **Random Forest** | **0.92** |

## 📁 Project Structure

HOUSE-PREDICTION/
├── app.py                      # Gradio web application
├── house_prediction.ipynb      # Data cleaning, EDA & model training
├── city_encoder.pkl            # Saved city label encoder
├── property_type_encoder.pkl   # Saved property type label encoder
├── requirements.txt
├── SETUP.md                    # Full setup instructions
└── README.md

> **Note:** `house_price_model.pkl` and `zameen-updated.csv` are excluded from this repo due to GitHub's file size limits. See [SETUP.md](SETUP.md) to regenerate them locally.

## 🚀 Quick Start

```bash
git clone https://github.com/uswahnadeem05-maker/HOUSE-PREDICTION.git
cd HOUSE-PREDICTION
pip install -r requirements.txt
python app.py
```

Full setup details (including dataset download and API key setup) are in [SETUP.md](SETUP.md).

## 💡 Key Insights

- Pakistani house prices are heavily right-skewed — a small number of luxury properties (up to PKR 2 billion) distort raw price distributions, requiring log transformation for reliable modeling
- **Area** and **city** are the strongest predictors of price
- Random Forest significantly outperforms Linear Regression (66% → 92% R²) due to non-linear pricing patterns in real estate

## 🎓 About This Project

Built as part of the **CodeAlpha Data Analytics Internship**, covering:
- ✅ Exploratory Data Analysis
- ✅ Data Visualization
- ✅ Machine Learning Model Development
- ✅ AI Integration & Deployment

## 👤 Author

**Uswah Nadeem**
Computational Finance Student, NED University of Engineering & Technology
[GitHub](https://github.com/uswahnadeem05-maker)

---

<div align="center">

⭐ If you found this project interesting, consider giving it a star!

</div>
