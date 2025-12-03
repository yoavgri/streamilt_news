
import streamlit as st
import datetime
import pandas as pd
import random

# 1. הגדרת עמוד בסיסית
st.set_page_config(
    page_title="Streamlit News",
    page_icon="📰",
    layout="wide"
)

# 2. פונקציה ליצירת נתונים מדומים (במציאות זה יוחלף ב-API כמו NewsAPI)
def get_fake_news():
    categories = ["טכנולוגיה", "ספורט", "פיננסים", "עולם"]
    articles = [
        {
            "title": "הבינה המלאכותית כובשת את העולם",
            "category": "טכנולוגיה",
            "author": "דני דיגיטל",
            "date": datetime.date(2023, 11, 1),
            "image": "https://picsum.photos/400/200?random=1",
            "summary": "התפתחויות חדשות בתחום ה-LLM משנות את הדרך בה אנו עובדים...",
            "content": "כאן יופיע התוכן המלא של הכתבה. הבינה המלאכותית ממשיכה להפתיע..."
        },
        {
            "title": "מניית הטכנולוגיה הגדולה צונחת",
            "category": "פיננסים",
            "author": "רונית רווחים",
            "date": datetime.date(2023, 11, 2),
            "image": "https://picsum.photos/400/200?random=2",
            "summary": "לאחר פרסום הדו''חות הרבעוניים, המשקיעים מגיבים בחשש.",
            "content": "השוק הגיב בירידות שערים חדות לאחר שהחברה פספסה את תחזית הרווח..."
        },
        {
            "title": "שיא חדש בריצת 100 מטר",
            "category": "ספורט",
            "author": "יוסי ספרינט",
            "date": datetime.date(2023, 11, 3),
            "image": "https://picsum.photos/400/200?random=3",
            "summary": "האצן האלמוני הפתיע את כולם בתחרות הבינלאומית.",
            "content": "באירוע מרגש באצטדיון הלאומי, נשבר שיא בן עשור..."
        },
        {
            "title": "השקת מכשיר הסמארטפון החדש",
            "category": "טכנולוגיה",
            "author": "גדי גאדג'ט",
            "date": datetime.date(2023, 11, 4),
            "image": "https://picsum.photos/400/200?random=4",
            "summary": "האם המצלמה החדשה באמת משנה את כללי המשחק?",
            "content": "החברה השיקה את דגם הפרו שלה הכולל עדשת זום חדשנית..."
        },
        {
            "title": "משבר האקלים: ועידה בינלאומית",
            "category": "עולם",
            "author": "אדם טבע",
            "date": datetime.date(2023, 11, 5),
            "image": "https://picsum.photos/400/200?random=5",
            "summary": "מנהיגי העולם מתכנסים לדון בעתיד כדור הארץ.",
            "content": "הועידה תתמקד בפתרונות אנרגיה ירוקה והפחתת פליטות..."
        }
    ]
    return pd.DataFrame(articles)

# טעינת הנתונים
df = get_fake_news()

# 3. בניית סרגל הצד (Sidebar)
with st.sidebar:
    st.title("🔍 סינון וניווט")
    
    # סינון לפי קטגוריה
    category_filter = st.multiselect(
        "בחר קטגוריות:",
        options=df["category"].unique(),
        default=df["category"].unique()
    )
    
    st.markdown("---")
    st.write("פותח באמצעות Python & Streamlit")

# 4. איזור ראשי - כותרת וחיפוש
st.title("📰  אתר החדשות ועדכונים שוטפים")
st.caption("אתר חדשות דינאמי לדוגמה")

# שורת חיפוש
search_query = st.text_input("חפש כותרת או תוכן...", "")

# 5. לוגיקה של סינון
filtered_df = df[df["category"].isin(category_filter)]

if search_query:
    filtered_df = filtered_df[
        filtered_df["title"].str.contains(search_query, case=False) |
        filtered_df["summary"].str.contains(search_query, case=False)
    ]

# 6. הצגת הכתבות
st.markdown("---")

if filtered_df.empty:
    st.warning("לא נמצאו כתבות התואמות את החיפוש שלך.")
else:
    # לולאה שעוברת על הכתבות ומציגה אותן
    for index, row in filtered_df.iterrows():
        # יצירת קונטיינר לכל כתבה כדי לשמור על סדר
        with st.container():
            col1, col2 = st.columns([1, 3]) # יחס של 1 ל-3 בין תמונה לטקסט
            
            with col1:
                st.image(row["image"], use_container_width=True)
            
            with col2:
                st.subheader(f"{row['title']}")
                # תגיות קטנות מעל הטקסט
                st.markdown(f"**{row['category']}** | 🗓️ {row['date']} | ✍️ {row['author']}")
                st.write(row["summary"])
                
                # כפתור "קרא עוד" שנפתח (Expander)
                with st.expander("קרא עוד"):
                    st.write(row["content"])
            
            st.markdown("---") # קו מפריד בין כתבות



