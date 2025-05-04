import streamlit as st
import pandas as pd
import joblib

def main():
    st.set_page_config(page_title="College Graduation Predictor", layout="centered")
    st.title("🎓 Predicting Higher Education Outcomes")
    st.markdown("Use this tool to estimate the likelihood that an individual will graduate from college based on demographic and socioeconomic factors.")

    model = joblib.load("model.pkl")

    # Box-like layout for inputs (not collapsible)
    st.markdown("### Personal & Demographic Information")
    with st.container(border=True):
        col1, col2 = st.columns(2)

        with col1:
            nchild = st.selectbox("Number of Children", options=["0", "1", "2", "3", "4", "5+"], index=0)
            nchild = 5 if nchild == "5+" else int(nchild)

            marriage_status = st.selectbox("Marital Status", ["Single", "Previously Married", "Married"])
            bpl_us = st.selectbox("Born in United States?", ["Yes", "No"])

        with col2:
            speakeng_level = st.selectbox(
                "English Proficiency", [
                    "Speaks only English", "Speaks very well", "Speaks well",
                    "Speaks but not well", "Does not speak English"
                ]
            )
            race = st.selectbox("Race", [
                "Asian or Pacific Islander", "Biracial", "Black/African American", "Other", "White"
            ])
            state = st.selectbox("State of Residence", [
                'Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware',
                'District of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa',
                'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota',
                'Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
                'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon',
                'Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah',
                'Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming'
            ])

    # Encode values
    speakeng_map = {
        "Speaks only English": 0,
        "Speaks very well": 1,
        "Speaks well": 2,
        "Speaks but not well": 3,
        "Does not speak English": 4
    }
    speakeng_encoded = speakeng_map[speakeng_level]

    input_dict = {
        "NCHILD_CLEANED": nchild,
        "SPEAKENG_ENCODED": speakeng_encoded,
        "SimplifiedRace_Asian or Pacific Islander": race == "Asian or Pacific Islander",
        "SimplifiedRace_Biracial": race == "Biracial",
        "SimplifiedRace_Black/African American": race == "Black/African American",
        "SimplifiedRace_Other": race == "Other",
        "SimplifiedRace_White": race == "White",
        "MARST_Simplified_Previously Married": marriage_status == "Previously Married",
        "MARST_Simplified_Single": marriage_status == "Single",
        "BPL_Simplified_United States": bpl_us == "Yes"
    }

    # One-hot encoding for state
    for s in [
        'Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware',
        'District of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa',
        'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota',
        'Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
        'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon',
        'Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah',
        'Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming'
    ]:
        input_dict[f"STATEFIP_{s}"] = (state == s)

    input_df = pd.DataFrame([input_dict])

    # Prediction button
    if st.button("Predict"):
        prob = model.predict_proba(input_df)[0][1]
        prediction = "Yes" if prob >= 0.5 else "No"

        col1, col2 = st.columns(2)
        with col1:
            st.metric("🎓 Prediction", prediction)
        with col2:
            st.metric("📊 Probability of Graduation", f"{prob:.2%}")

if __name__ == "__main__":
    main()
