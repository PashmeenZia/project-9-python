# 🎓 Project 9: Build a Python Website in 15 mins with Streamlit 🚀

import streamlit as st
import pandas as pd
import random

# Page Configuration
st.set_page_config(page_title="🎓 Student Data Generator", layout="wide")

# Custom CSS to ensure button text is visible
st.markdown(
    """
    <style>
    .stDownloadButton > button {
        display: block !important;
        visibility: visible !important;
        color: white !important;
        font-size: 16px !important;
        font-weight: bold !important;
        background-color: #4CAF50 !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Student CSV File Generator")

# Sample student data
names = ["Ali", "Alisha", "Madiha", "Nazia", "Eshaal", "Fiza", "Nadia", "Sadaf", "Zainab", "Ayesha", "Umaima", "Izhaan", "Sara", "Fatima", "Iqra", "Marium"]
students = []
for i in range(1, 16):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C", "D", "E", "F"]),
        "Marks": random.randint(40, 100)
    }
    students.append(student)

df = pd.DataFrame(students)

# 🎯 Random Student Highlight
random_student = random.choice(students)
st.info(f"⭐ Featured Student: **{random_student['Name']}** (Grade: {random_student['Grade']}, Marks: {random_student['Marks']})")

# 📜 Filter Students by Grade (Including 'All' Option)
selected_grade = st.selectbox("📌 Filter by Grade", ["All"] + sorted(df["Grade"].unique()))
if selected_grade != "All":
    df = df[df["Grade"] == selected_grade]

st.subheader("📜 Generated Students Data")
st.dataframe(df)  # ✅ Your original dataframe display

# 📊 Marks Distribution Visualization
st.subheader("📊 Marks Distribution")
st.bar_chart(df["Marks"])

# 🔽 Download CSV (Button Click -> Show Balloons 🎈)
st.subheader("📂 Download Student Data")
st.write("📥 Click the button below to download the student data as a CSV file.")

csv_file = df.to_csv(index=False).encode('utf-8-sig')

# Download Button with Balloons on Click
download_clicked = st.download_button(label="⬇️ Download CSV File", data=csv_file, file_name="students.csv", mime="text/csv")

# 🎈 Show balloons only when button is clicked
if download_clicked:
    st.balloons()

# 🎉 Success Message
st.success("✅ Students Record Generated Successfully! 🎊")
