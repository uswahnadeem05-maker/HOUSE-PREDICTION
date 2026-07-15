<div align="center">

# 🏠 Pakistan House Price Predictor

**AI-powered real estate valuation tool trained on 100,000+ real property listings across Pakistan.**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Try_it_Now-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://house-prediction-gdcamhhfs9bjr9zhgfbtfd.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/uswahnadeem05-maker/HOUSE-PREDICTION)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

</div>

---

## 📖 Overview

This project predicts house prices across Pakistan using machine learning, trained on real listings sourced from Zameen.com — Pakistan's largest property portal. Built as part of a Data Analytics Internship at **CodeAlpha**, it combines data cleaning, exploratory analysis, model training, and AI integration into a single deployed web app.

## ✨ Features

| Feature | Description |
|---|---|
| 🔮 **Instant Prediction** | Get a price estimate in seconds based on city, area, bedrooms, bathrooms, and location |
| 📊 **Price Range** | Confidence interval from the model's tree ensemble, not just a single guess |
| 🏘️ **Similar Listings** | Real comparable properties pulled directly from the dataset |
| 🤖 **AI Assistant** | Chat with a Gemini-powered assistant about Pakistani real estate |
| 📈 **Data Explorer** | Interactive charts on pricing trends, city comparisons, and property types |

## 🖥️ Preview

<img width="860" height="371" alt="house str 2" src="https://github.com/user-attachments/assets/0e155d7d-956f-4630-8d0b-664552fc77cb" />
<img width="767" height="262" alt="house str 1" src="https://github.com/user-attachments/assets/2fc283ca-183c-4689-a295-854669128620" />

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/-Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/-Gemini_API-8E75B2?style=flat-square&logo=google&logoColor=white)

## 📊 Data & Model

- **Source:** 168,446 real property listings from Zameen.com
- **Cleaning:** Filtered to "For Sale" listings, removed price outliers, unified mixed area units (Marla/Kanal), log-transformed skewed price and area distributions
- **Final dataset:** 89,642 clean listings (House & Flat only)
- **Model:** Random Forest Regressor (compact, 50 trees — optimized for deployment)
- **Performance:**

| Model | R² Score |
|---|---|
| Linear Regression | 0.66 |
| **Random Forest** | **0.92** |

## 📁 Project Structure

PS C:\Users\User\Downloads\HOUSE PREDICTION> dir house_price_model.pkl Directory: C:\Users\User\Downloads\HOUSE PREDICTION Mode LastWriteTime Length Name ---- -------------

pasted

Found it! Right there in your output:

fatal: The current branch main has no upstream branch.
This is the actual problem — all 3 of your commits saved locally just fine, but none of them actually pushed to GitHub, because Git didn't know which remote branch to push to. Every git push silently failed with this error, and it's easy to miss scrolling past it. That's why GitHub kept showing the old files.

Fix: One command
powershell
git push --set-upstream origin main
This tells Git "push to the main branch on origin (GitHub), and remember this connection for all future pushes." After running this once, plain git push will work correctly from now on.

Verify it worked
powershell
git log -3
Then check GitHub directly: github.com/uswahnadeem05-maker/HOUSE-PREDICTION/blob/main/requirements.txt

It should now show:

numpy==2.2.6
scikit-learn==1.7.2
Then reboot Streamlit Cloud
Go to your app on share.streamlit.io
Click "⋮" → Reboot app
Run that one push command now — this should finally get everything synced.

Why is it taking so much times for streamlit it just processing and processing


Diagnosed performance bottlenecks and devised optimization strategies
Diagnosed performance bottlenecks and devised optimization strategies
A few reasons this can take a while, and what to check:

1. First deploy is always the slowest
Streamlit Cloud has to install all your libraries from scratch (pandas, scikit-learn, numpy, streamlit, etc.) — this alone can take 3-5+ minutes on a fresh deploy, especially with pinned versions that may need to compile.

2. Your CSV (49MB) loads on every app start
Since pd.read_csv("zameen-updated.csv") runs when the app first loads, and it's ~168,000 rows, this adds real time to startup — though this alone shouldn't take more than 10-20 seconds.

3. Model loading (6.6MB) is fast, not the bottleneck

What to check right now
1. Look at the build logs directly
On your Streamlit Cloud app page, click "Manage app" (bottom right) — this shows live logs of exactly what it's doing (installing packages, running your script, etc.). This tells you if it's stuck vs. just genuinely slow.

2. How long has it actually been?

Under 5 minutes: normal, just wait
10+ minutes with no progress in logs: likely actually stuck, needs a manual reboot
If it seems truly stuck
Click "⋮" menu → Reboot app
If that doesn't help, try Delete app and redeploy fresh — sometimes a clean deploy resolves weird stuck states better than rebooting
Check the "Manage app" logs first — paste me what it shows (especially the last few lines) and I can tell you if it's actually progressing or genuinely frozen.

UTC     ] Logs for house-prediction-gdcamhhfs9bjr9zhgfbtfd.streamlit.app/
────────────────────────────────────────────────────────────────────────────────────────
[22:41:32] 🚀 Starting up repository: 'house-prediction', branch: 'main', main module: 'app.py'
[22:41:32] 🐙 Cloning repository...
[22:41:34] 🐙 Cloning into '/mount/src/house-prediction'...
[22:41:34] 🐙 Cloned repository!
[22:41:34] 🐙 Pulling code changes from Github...
[22:41:35] 📦 Processing dependencies...

──────────────────────────────────────── uv ───────────────────────────────────────────

Using uv pip install.
Using Python 3.14.6 environment at /home/adminuser/venv
Resolved 64 packages in 748ms
[23:27:11] 🐍 Python dependencies were installed from /mount/src/house-prediction/requirements.txt using uv.
[23:27:13] 📦 Processed dependencies!
[23:27:17] 🐙 Pulling code changes from Github...
[23:27:18] 📦 Processing dependencies...
[23:27:18] 📦 Processed dependencies!
[23:27:20] 🔄 Updated app!
[23:27:20] 🐙 Pulling code changes from Github...
[23:27:21] 📦 Processing dependencies...
[23:27:21] 📦 Processed dependencies!
[23:27:23] 🔄 Updated app!
[23:27:23] 🐙 Pulling code changes from Github...
[23:27:24] 📦 Processing dependencies...
[23:27:24] 📦 Processed dependencies!
[23:27:27] 🔄 Updated app!
[23:27:27] 🐙 Pulling code changes from Github...
[23:27:27] 📦 Processing dependencies...
[23:27:27] 📦 Processed dependencies!
[23:27:30] 🔄 Updated app!
[23:27:30] 🐙 Pulling code changes from Github...
[23:27:30] 📦 Processing dependencies...
[23:27:30] 📦 Processed dependencies!
[23:27:33] 🔄 Updated app!

Show more

Identified Python version incompatibility causing deployment loop
Identified Python version incompatibility causing deployment loop
Found the real issue — look at this line:

Using Python 3.14.6 environment
Python 3.14 is brand new and likely doesn't have pre-built installer packages ("wheels") yet for your pinned numpy==2.2.6 and scikit-learn==1.7.2. When there's no pre-built version available, pip has to compile these libraries from source code on the server — which is extremely slow (this is likely why it took ~45 minutes between "Processing dependencies" and finishing).

Fix: Force Streamlit Cloud to use a stable, older Python version
Create a new file called runtime.txt in your project folder with this content:

python-3.11
This tells Streamlit Cloud to use Python 3.11 instead of 3.14 — a much more stable, widely-supported version with pre-built packages for everything in your requirements.txt, avoiding slow compilation entirely.

Push this
powershell
git add runtime.txt
git commit -m "Pin Python version to 3.11 for faster, stable deployment"
git push
Then delete and redeploy (don't just reboot)
Since the app seems to be stuck in a weird update loop (notice it's repeatedly "Pulling code changes" every few seconds at the bottom — that's unusual), I'd recommend:

On Streamlit Cloud, click "⋮" → Delete app
Click New app and redeploy fresh with the same settings (repo, branch, app.py, and your GEMINI_API_KEY secret)
This clean redeploy with runtime.txt in place should install much faster since Python 3.11 has ready-made packages for everything you need.


<div align="center"> # 🏠 Pakistan House Price Predictor **AI-powered real estate valuation tool trained on 100,000+ real property listings across Pakistan.** [![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Try_it_Now-10B981?style=for-the-badge)](https://huggingface.co/spaces/uswahnadeem0

pasted

can u also  change it accordingly as these are my files nowgitignore
Add requirements, compact model, and updated gitignore for deployment
12 hours ago
README.md
Create README.md
4 days ago
app.py
Add requirements, compact model, and updated gitignore for deployment
12 hours ago
city_encoder.pkl
Initial commit: Pakistan House Price Predictor
4 days ago
house_prediction.ipynb
Add requirements, compact model, and updated gitignore for deployment
12 hours ago
house_price_model.pkl
Add requirements, compact model, and updated gitignore for deployment
12 hours ago
property_type_encoder.pkl
Initial commit: Pakistan House Price Predictor
4 days ago
requirements.txt
Fix requirements.txt syntax and pin numpy/scikit-learn versions
12 hours ago
runtime.txt
Pin Python version to 3.11 for faster, stable deployment
46 minutes ago
zameen-updated.csv               and also i made the project on streamlit

Show more

Overhauled README to reflect Streamlit migration and updated project structure
Overhauled README to reflect Streamlit migration and updated project structure
Here's your updated README, reflecting Streamlit (not Gradio) and the fact that all files are now included in the repo.

markdown
<div align="center">

# 🏠 Pakistan House Price Predictor

**AI-powered real estate valuation tool trained on 100,000+ real property listings across Pakistan.**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Try_it_Now-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://house-prediction-gdcamhhfs9bjr9zhgfbtfd.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/uswahnadeem05-maker/HOUSE-PREDICTION)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

</div>

---

## 📖 Overview

This project predicts house prices across Pakistan using machine learning, trained on real listings sourced from Zameen.com — Pakistan's largest property portal. Built as part of a Data Analytics Internship at **CodeAlpha**, it combines data cleaning, exploratory analysis, model training, and AI integration into a single deployed web app.

## ✨ Features

|
 Feature 
|
 Description 
|
|
---
|
---
|
|
 🔮 
**
Instant Prediction
**
|
 Get a price estimate in seconds based on city, area, bedrooms, bathrooms, and location 
|
|
 📊 
**
Price Range
**
|
 Confidence interval from the model's tree ensemble, not just a single guess 
|
|
 🏘️ 
**
Similar Listings
**
|
 Real comparable properties pulled directly from the dataset 
|
|
 🤖 
**
AI Assistant
**
|
 Chat with a Gemini-powered assistant about Pakistani real estate 
|
|
 📈 
**
Data Explorer
**
|
 Interactive charts on pricing trends, city comparisons, and property types 
|

## 🖥️ Preview

<img width="853" height="404" alt="House Price Predictor Screenshot 1" src="https://github.com/user-attachments/assets/67d54751-6604-460b-9243-cbbb63c39ae3" />
<img width="860" height="374" alt="House Price Predictor Screenshot 2" src="https://github.com/user-attachments/assets/bf71e60c-36bb-4cad-84f4-20000abcad98" />

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/-Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/-Gemini_API-8E75B2?style=flat-square&logo=google&logoColor=white)

## 📊 Data & Model

- **Source:** 168,446 real property listings from Zameen.com
- **Cleaning:** Filtered to "For Sale" listings, removed price outliers, unified mixed area units (Marla/Kanal), log-transformed skewed price and area distributions
- **Final dataset:** 89,642 clean listings (House & Flat only)
- **Model:** Random Forest Regressor (compact, 50 trees — optimized for deployment)
- **Performance:**

|
 Model 
|
 R² Score 
|
|
---
|
---
|
|
 Linear Regression 
|
 0.66 
|
|
**
Random Forest
**
|
**
0.92
**
|

## 📁 Project Structure
HOUSE-PREDICTION/
├── app.py # Streamlit web application
├── house_prediction.ipynb # Data cleaning, EDA & model training
├── house_price_model.pkl # Trained Random Forest model
├── city_encoder.pkl # Saved city label encoder
├── property_type_encoder.pkl # Saved property type label encoder
├── zameen-updated.csv # Raw dataset (Zameen.com listings)
├── requirements.txt
├── runtime.txt # Pins Python version for deployment
├── SETUP.md # Full setup instructions
└── README.md

## 🚀 Quick Start

```bash
git clone https://github.com/uswahnadeem05-maker/HOUSE-PREDICTION.git
cd HOUSE-PREDICTION
pip install -r requirements.txt
streamlit run app.py
```

You'll also need a free Gemini API key — see [SETUP.md](SETUP.md) for full setup details.

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
