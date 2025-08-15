#Import libraries
import numpy as np
import pandas as pd
import gradio as gr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#Load dataset
df = pd.read_csv("https://drive.google.com/uc?id=1uhnWwwvC3tMdnCfb4b-iJvODvBaOev4t")

#Features
features = ['bedrooms', 'bathrooms', 'size_sqft', 'floor', 'building_age_yrs',
            'has_roofdeck', 'has_elevator', 'has_gym']

X = df[features]
y = df['rent']

#Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LinearRegression()
model.fit(X_train, y_train)

def predict_rent(bd, bth, sz, fl, age, rf, elv, gm):
    """
    Predicts apartment rent based on user-provided details and
    returns the predicted rent along with model evaluation metrics.

    Parameters:
    bd  (float) : Number of bedrooms
    bth (float) : Number of bathrooms
    sz  (float) : Apartment size in square feet
    fl  (float) : Floor number
    age (float) : Building age in years
    rf  (str)   : "Yes"/"No" indicating if the building has a roofdeck
    elv (str)   : "Yes"/"No" indicating if the building has an elevator
    gm  (str)   : "Yes"/"No" indicating if the building has a gym

    Returns:
    tuple:
        predicted_rent_str (str) - Predicted rent in USD
        rmse_str (str)           - Root Mean Square Error of the model
        mean_rent_str (str)      - Average rent in the test dataset
        error_pct_str (str)      - Percentage error relative to mean rent
        r2_str (str)             - R² score (model fit quality)
    """

    #Convert Yes/No answers into numeric 1/0 for the model
    rf = 1 if rf == "Yes" else 0
    elv = 1 if elv == "Yes" else 0
    gm = 1 if gm == "Yes" else 0

    #Package user inputs into a DataFrame to match the model's input structure
    client_apartment = pd.DataFrame(
        [[bd, bth, sz, fl, age, rf, elv, gm]],
        columns=features
    )

    #Predict rent for the provided apartment details
    prediction = model.predict(client_apartment)[0]

    #Evaluate the trained model using the test dataset
    y_pred = model.predict(X_test)                  # Model predictions for test set
    mean_rent = y_test.mean()                        # Mean rent in test set
    rmse = np.sqrt(mean_squared_error(y_test, y_pred)) # Root Mean Square Error
    r2 = r2_score(y_test, y_pred)                    # R² score (fit quality)

    #Return formatted results
    return (
        f"{prediction:.2f} USD",          # Predicted rent
        f"{rmse:.2f}",                    # RMSE value
        f"{mean_rent:.2f}",                # Mean rent
        f"{100 * rmse / mean_rent:.2f}%",  # Percentage error
        f"{r2:.4f}"                        # R² score
    )

#Gradio interface
with gr.Blocks() as iface:
    gr.Markdown("## 🏠 Apartment Rent Predictor")
    gr.Markdown("Enter apartment details to predict rent and view model performance.")

    # First row: basic apartment details
    with gr.Row():
        bd = gr.Number(label="Bedrooms")
        bth = gr.Number(label="Bathrooms")
        sz = gr.Number(label="Size (sqft)")
        fl = gr.Number(label="Floor")

    # Second row: building features
    with gr.Row():
        age = gr.Number(label="Age (yrs)")
        rf = gr.Radio(["Yes", "No"], label="Roofdeck?")
        elv = gr.Radio(["Yes", "No"], label="Elevator?")
        gm = gr.Radio(["Yes", "No"], label="Gym?")

    # Predicted rent row
    gr.Markdown("### 💰 Predicted Rent")
    predicted = gr.Textbox(
        label="Predicted Rent (USD)",
        interactive=False,
        elem_id="predicted-rent-box"
    )

    # Evaluation metrics section
    gr.Markdown("### 📊 Evaluation Metrics")
    with gr.Row():
        rmse_out = gr.Textbox(label="RMSE", interactive=False)
        mean_out = gr.Textbox(label="Mean Rent", interactive=False)
        err_pct_out = gr.Textbox(label="% Error", interactive=False)
        r2_out = gr.Textbox(label="R² Score", interactive=False)

    # Prediction button
    predict_btn = gr.Button("Predict Rent", variant="primary")

    # Connect button to function
    predict_btn.click(
        fn=predict_rent,
        inputs=[bd, bth, sz, fl, age, rf, elv, gm],
        outputs=[predicted, rmse_out, mean_out, err_pct_out, r2_out]
    )

# Add custom CSS for bigger predicted rent output
iface.css = """
#predicted-rent-box textarea {
    font-size: 1.5em;
    font-weight: bold;
    color: green;
}
"""

iface.launch()