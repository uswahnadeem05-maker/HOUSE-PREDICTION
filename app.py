import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os
from google import genai

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = joblib.load('house_price_model.pkl')
le_city = joblib.load('city_encoder.pkl')
le_type = joblib.load('property_type_encoder.pkl')

df = pd.read_csv("zameen-updated.csv")
df = df[(df['purpose'] == 'For Sale') & (df['price'] > 100000) &
        (df['bedrooms'] > 0) & (df['baths'] > 0) &
        (df['property_type'].isin(['House', 'Flat']))].copy()

st.set_page_config(page_title="Pakistan House Price Predictor", page_icon="🏠", layout="wide")

st.title("🏠 Pakistan House Price Predictor")
st.write("AI-powered price estimates trained on real Zameen.com listings.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Listings", f"{len(df):,}")
col2.metric("Cities", len(le_city.classes_))
col3.metric("Model", "Random Forest")
col4.metric("Accuracy", "92%")

tab1, tab2, tab3 = st.tabs(["🔮 Predict", "📊 Explore Data", "💬 AI Assistant"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        city = st.selectbox("City", le_city.classes_)
        property_type = st.selectbox("Property Type", le_type.classes_)
        area_marla = st.number_input("Area (Marla)", min_value=1.0, max_value=500.0, value=10.0)
        bedrooms = st.number_input("Bedrooms", min_value=1, max_value=20, value=3)
        baths = st.number_input("Bathrooms", min_value=1, max_value=20, value=2)
        latitude = st.number_input("Latitude", value=33.6844, format="%.4f")
        longitude = st.number_input("Longitude", value=73.0479, format="%.4f")
        predict_clicked = st.button("Generate Price Estimate", type="primary")

    with col2:
        if predict_clicked:
            log_area = np.log1p(area_marla)
            city_encoded = le_city.transform([city])[0]
            type_encoded = le_type.transform([property_type])[0]
            input_data = pd.DataFrame(
                [[log_area, bedrooms, baths, city_encoded, type_encoded, latitude, longitude]],
                columns=['log_area', 'bedrooms', 'baths', 'city_encoded', 'property_type_encoded', 'latitude', 'longitude']
            )
            log_prediction = model.predict(input_data)[0]
            predicted_price = np.expm1(log_prediction)
            tree_preds = np.array([tree.predict(input_data)[0] for tree in model.estimators_])
            lower = np.expm1(np.percentile(tree_preds, 10))
            upper = np.expm1(np.percentile(tree_preds, 90))

            st.success(f"### Estimated Price: PKR {predicted_price:,.0f}")
            st.info(f"Likely Range: PKR {lower:,.0f} — PKR {upper:,.0f}")

            similar = df[(df['city'] == city) & (df['bedrooms'].between(bedrooms - 1, bedrooms + 1))].copy()
            similar['area_diff'] = abs(similar['baths'] - baths)
            similar = similar.sort_values('area_diff').head(5)
            st.write("**Similar Listings**")
            st.dataframe(similar[['location', 'city', 'price', 'bedrooms', 'baths', 'area']])

with tab2:
    st.subheader("Property Type Distribution")
    st.bar_chart(df["property_type"].value_counts())

    st.subheader("Top 10 Cities by Listings")
    st.bar_chart(df["city"].value_counts().head(10))

    st.subheader("Average Price by City")
    st.bar_chart(df.groupby("city")["price"].mean().sort_values(ascending=False).head(10))

with tab3:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Ask about Pakistani real estate...")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)
        with st.chat_message("assistant"):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Answer briefly about Pakistani real estate: {user_input}"
            )
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
