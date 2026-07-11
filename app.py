import gradio as gr
import joblib
import numpy as np
import pandas as pd
import os
from dotenv import load_dotenv
from google import genai

# ---- Load everything once ----
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

model = joblib.load('house_price_model.pkl')
le_city = joblib.load('city_encoder.pkl')
le_type = joblib.load('property_type_encoder.pkl')

df = pd.read_csv("zameen-updated.csv")
df = df[(df['purpose'] == 'For Sale') & (df['price'] > 100000) &
        (df['bedrooms'] > 0) & (df['baths'] > 0) &
        (df['property_type'].isin(['House', 'Flat']))].copy()


# ---- Prediction logic ----
def predict_price(city, property_type, area_marla, bedrooms, baths, latitude, longitude):
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

    result_html = f"""
    <div style="background: linear-gradient(135deg, #FDF2F8, #ECFDF5); border-radius: 16px; padding: 28px; text-align: center; border: 1px solid #F3D8E8;">
        <p style="font-size: 14px; color: #6B7280; margin: 0; text-transform: uppercase; letter-spacing: 1px;">Estimated Price</p>
        <p style="font-size: 40px; font-weight: 800; color: #E11D48; margin: 8px 0;">PKR {predicted_price:,.0f}</p>
        <p style="font-size: 15px; color: #6B7280; margin: 0;">Likely Range: PKR {lower:,.0f} — PKR {upper:,.0f}</p>
    </div>
    """
    return result_html


def similar_listings(city, bedrooms, baths):
    similar = df[(df['city'] == city) & (df['bedrooms'].between(bedrooms - 1, bedrooms + 1))].copy()
    if len(similar) == 0:
        return pd.DataFrame(columns=['location', 'city', 'price', 'bedrooms', 'baths', 'area'])
    similar['area_diff'] = abs(similar['baths'] - baths)
    similar = similar.sort_values('area_diff').head(5)
    return similar[['location', 'city', 'price', 'bedrooms', 'baths', 'area']]


def full_predict(city, property_type, area_marla, bedrooms, baths, latitude, longitude):
    result_html = predict_price(city, property_type, area_marla, bedrooms, baths, latitude, longitude)
    listings = similar_listings(city, bedrooms, baths)
    return result_html, listings


# ---- AI Chat ----
def chat_with_ai(message, history):
    prompt = f"Answer this question about Pakistani real estate, briefly and helpfully: {message}"
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text


# ---- Chart data ----
property_counts = df["property_type"].value_counts().reset_index()
property_counts.columns = ["property_type", "count"]

city_counts = df["city"].value_counts().head(10).reset_index()
city_counts.columns = ["city", "count"]

df["log_price"] = np.log1p(df["price"])

city_avg_price = df.groupby("city")["price"].mean().sort_values(ascending=False).head(10).reset_index()
city_avg_price.columns = ["city", "avg_price"]

bedroom_avg = df[df["bedrooms"] <= 10].groupby("bedrooms")["price"].mean().reset_index()
bedroom_avg.columns = ["bedrooms", "avg_price"]

feature_importance = pd.DataFrame({
    'feature': ['Area', 'Bedrooms', 'Bathrooms', 'City', 'Property Type', 'Latitude', 'Longitude'],
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)


# ---- Styling ----
custom_theme = gr.themes.Soft(primary_hue="rose", secondary_hue="emerald")

custom_css = """
.gradio-container { max-width: 1150px !important; margin: auto !important; }
.stat-card {
    background: white; border-radius: 14px; padding: 18px; text-align: center;
    border: 1px solid #F0F0F0; box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.stat-number { font-size: 26px; font-weight: 800; color: #E11D48; margin: 0; }
.stat-label { font-size: 13px; color: #6B7280; margin: 4px 0 0 0; }
footer { visibility: hidden; }
"""


def stat_card(number, label):
    return f"""<div class="stat-card"><p class="stat-number">{number}</p><p class="stat-label">{label}</p></div>"""


# ---- Build app ----
with gr.Blocks(title="Pakistan House Price Predictor", theme=custom_theme, css=custom_css) as demo:

    gr.HTML("""
    <div style="background: linear-gradient(135deg, #1E3A8A, #10B981); padding: 55px 30px; border-radius: 18px; text-align: center; margin-bottom: 10px;">
        <h1 style="color: white; font-size: 42px; margin: 0;">🏠 Pakistan House Price Predictor</h1>
        <p style="color: #E0F2FE; font-size: 17px; margin-top: 10px; max-width: 650px; margin-left: auto; margin-right: auto;">
            An AI-powered valuation tool trained on real Zameen.com listings — estimate property prices across Pakistan in seconds.
        </p>
    </div>
    """)

    with gr.Row():
        gr.HTML(stat_card(f"{len(df):,}", "Listings Analyzed"))
        gr.HTML(stat_card(len(le_city.classes_), "Cities Covered"))
        gr.HTML(stat_card("Random Forest", "Model Used"))
        gr.HTML(stat_card("92%", "Accuracy (R²)"))

    gr.Markdown(" ")

    with gr.Tab("🔮 Predict"):
        gr.Markdown("### Enter Property Details")
        with gr.Row():
            with gr.Column(scale=1):
                city_input = gr.Dropdown(choices=list(le_city.classes_), label="City")
                type_input = gr.Dropdown(choices=list(le_type.classes_), label="Property Type")
                area_input = gr.Number(label="Area (Marla)", value=10)
                with gr.Row():
                    bed_input = gr.Number(label="Bedrooms", value=3)
                    bath_input = gr.Number(label="Bathrooms", value=2)
                with gr.Row():
                    lat_input = gr.Number(label="Latitude", value=33.6844)
                    lon_input = gr.Number(label="Longitude", value=73.0479)
                predict_btn = gr.Button("Generate Price Estimate", variant="primary", size="lg")

            with gr.Column(scale=1):
                output_html = gr.HTML()
                gr.Markdown("#### Similar Real Listings")
                listings_table = gr.Dataframe(headers=['location', 'city', 'price', 'bedrooms', 'baths', 'area'])

        predict_btn.click(
            fn=full_predict,
            inputs=[city_input, type_input, area_input, bed_input, bath_input, lat_input, lon_input],
            outputs=[output_html, listings_table]
        )

        gr.Markdown("### What Drives This Model's Predictions")
        gr.BarPlot(feature_importance, x="feature", y="importance", title="Feature Importance", y_title="Importance Score")

    with gr.Tab("📊 Explore Data"):
        gr.Markdown("### A Look at the Data Behind This Model")
        gr.Markdown("168,000+ real property listings from across Pakistan were cleaned and analyzed to build this tool.")

        with gr.Row():
            gr.BarPlot(property_counts, x="property_type", y="count", title="Property Type Distribution")
            gr.BarPlot(city_counts, x="city", y="count", title="Top 10 Cities by Listing Count")

        with gr.Row():
            gr.BarPlot(city_avg_price, x="city", y="avg_price", title="Average Price by City (Top 10)")
            gr.LinePlot(bedroom_avg, x="bedrooms", y="avg_price", title="Average Price by Bedroom Count")

        gr.Markdown("### Sample Property Locations")
        map_sample = df.sample(min(1000, len(df)), random_state=1)[["latitude", "longitude"]].rename(
            columns={"latitude": "lat", "longitude": "lon"}
        )
        gr.Plot(value=None, visible=False)  # placeholder, map shown below
        gr.HTML(f"<p style='color:#6B7280;'>Showing a sample of {min(1000, len(df)):,} listings on the map.</p>")

    with gr.Tab("💬 AI Assistant"):
        gr.Markdown("### Ask About Pakistani Real Estate")
        gr.Markdown("Ask general questions about property pricing, trends, or what factors affect real estate value in Pakistan.")
        gr.ChatInterface(fn=chat_with_ai, type="messages")

    gr.HTML("""
    <div style="text-align:center; padding: 30px 0 10px 0; color: #9CA3AF; font-size: 13px;">
        Built with Python, scikit-learn, and Gradio · Data sourced from Zameen.com
    </div>
    """)

demo.launch()
