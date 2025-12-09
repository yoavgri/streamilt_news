import streamlit as st
import pandas as pd
from google import genai
import os

# 1. הגדרת ה-Client
CLIENT_KEY_NAME = "GEMINI_API_KEY"
client = genai.Client(api_key=st.secrets["AIzaSyB3tnzqdnEn3QH3jzFDYMkH8IAXDpFnqTo"]) # השתמש ב-st.secrets לאבטחה

# 2. קבלת פרמטרים מ-URL של Tableau
if 'filter_value' in st.query_params:
    filter_value = st.query_params['filter_value']
    st.write(f"נתונים שנבחרו ב-Tableau עבור: **{filter_value}**")

    # שלב 3: בניית הפרומפט וקריאה ל-Gemini
    prompt = (
        f"נתח את הנתונים עבור קטגוריה '{filter_value}' (במידה ויש לך את הנתונים בפועל), "
        f"והפק תובנה עסקית קצרה וממוקדת."
    )

    if st.button('בקש תובנה מ-Gemini'):
        with st.spinner('Gemini מנתח את הנתונים...'):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                st.success("תובנת Gemini:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"שגיאה ב-Gemini API: {e}")
else:

    st.info("בחר פריט בדאשבורד Tableau כדי להתחיל ניתוח.")
