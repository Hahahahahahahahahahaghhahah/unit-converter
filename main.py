import streamlit as st

st.title("Unit Converter")

opt = st.selectbox("Select conversion", ["Length (m ↔ ft)", "Weight (kg ↔ lb)", "Temp (C ↔ F)"])
val = st.number_input("Enter value")

if opt == "Length (m ↔ ft)":
    unit = st.radio("From", ["Meters", "Feet"])
    res = val * 3.28084 if unit == "Meters" else val / 3.28084
    st.write(f"Result: {res:.2f} {'ft' if unit == 'Meters' else 'm'}")

elif opt == "Weight (kg ↔ lb)":
    unit = st.radio("From", ["Kilograms", "Pounds"])
    res = val * 2.20462 if unit == "Kilograms" else val / 2.20462
    st.write(f"Result: {res:.2f} {'lb' if unit == 'Kilograms' else 'kg'}")

else:
    unit = st.radio("From", ["Celsius", "Fahrenheit"])
    res = (val * 9/5) + 32 if unit == "Celsius" else (val - 32) * 5/9
    st.write(f"Result: {res:.2f} {'°F' if unit == 'Celsius' else '°C'}")
