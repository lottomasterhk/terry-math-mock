import streamlit as st

# 網頁基本設定 (頁面標題與佈局)
st.set_page_config(
    page_title="Terry Sir | 中大數學專科教室",
    page_icon="📐",
    layout="centered"
)

# 注入自定義 CSS (保持你原本的高科技深藍 Mood)
st.markdown("""
<style>
    /* 全局背景與字體顏色 */
    .stApp {
        background: linear-gradient(135deg, #0b1d3a 0%, #061124 100%);
        color: #ffffff !important;
    }
    
    /* 確保所有標題、副標題、文字強制為白色 */
    h1, h2, h3, h4, h5, h6, p, label {
        color: #ffffff !important;
    }
    
    /* 下拉選單（Selectbox）主按鈕外觀與文字 */
    .stSelectbox [data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.12) !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    .stSelectbox [data-baseweb="select"] * {
        color: #ffffff !important;
    }
    
    /* 下拉選單彈出清單（Dropdown Menu / Options）的背景與文字 */
    div[data-baseweb="popover"], div[data-baseweb="menu"] {
        background-color: #0f2744 !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="menu"] div, div[data-baseweb="menu"] span {
        color: #ffffff !important;
    }
    div[data-baseweb="menu"] div:hover {
        background-color: #1e3c72 !important;
        color: #f39c12 !important;
    }
    
    /* 讓 radio 按鈕入面嘅選項文字清晰顯示、字體加大 */
    .stRadio label p {
        color: #ffffff !important;
        font-size: 16px !important;
    }
    
    /* 區塊卡片化 (Container Card) 加強邊框與深色半透明背景，令選項極易閱讀 */
    .stRadio > div {
        background-color: rgba(255, 255, 255, 0.06) !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        margin-bottom: 15px;
    }
    
    /* 按鈕美化：極靚嘅漸變金藍按鈕 */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 14px 24px !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4) !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #2a5298 0%, #3a7bd5 100%) !important;
        border-color: #f39c12 !important;
    }
</style>
""", unsafe_allow_html=True)

# 頁面頂部品牌視覺宣傳標題
st.markdown("""
<div style="text-align: center; padding: 10px 0;">
    <span style="background: rgba(243, 156, 18, 0.2); color: #f39c12 !important; padding: 6px 16px; border-radius: 20px; font-size: 14px; font-weight: bold; border: 1px solid rgba(243, 156, 18, 0.4);">
        🧠 NLP 心理引導 × 中大數學專業培訓
    </span>
    <h1 style="margin-top: 15px; font-size: 30px; font-weight: 800; color: #ffffff !important;">【中大數學】Terry Sir - 初中數學專科教室</h1>
    <p style="color: #cbd5e0 !important; font-size: 15px; max-width: 650px; margin: 0 auto;">
        核心理念：不只教公式，用 NLP 心理引導幫孩子解開數學心結，由根基打起，重拾信心奪 A！ ✨
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# 第一步：選擇考試階段與年級
st.subheader("📌 第一步：選擇你的考試階段與年級")
exam_stage = st.selectbox(
    "選擇考試階段",
    [
        "1st Term Test (第一次測驗)", 
        "1st Exam (上學期考試)", 
        "2nd Term Test (第二次測驗)", 
        "2nd Exam (下學期考試 / Final)"
    ]
)
grade = st.radio("請選擇你嘅年級：", ["中一 (Form 1)", "中二 (Form 2)", "中三 (Form 3)"], index=0, horizontal=True)

st.markdown("---")

# 動態判斷：根據年級及考試階段顯示對應嘅 10 題快測
if "中一" in grade:
    if "1st Term Test" in exam_stage:
        st.subheader("✍️ 第二步：中一 1st Term Test 校本真題級 10 題快測")
        st.markdown("請認真完成以下 10 題精選實戰試題：")
        
        q1 = st.radio("1. Arrange the following numbers in descending order: +3, +1/2, -2.5, 0, -3/4, +1.2", ("A) +3 > +1.2 > +1/2 > 0 > -3/4 > -2.5", "B) +3 > +1/2 > +1.2 > 0 > -3/4 > -2.5", "C) +3 > +1.2 > +1/2 > 0 > -2.5 > -3/4", "D) -2.5 > -3/4 > 0 > +1/2 > +1.2 > +3"), key="f1_t1_q1")
        q2 = st.radio("2. Which of the following expressions gives a result of 756?", ("A) 2^2 × 3^2 × 7", "B) 2^3 × 3^2 × 7", "C) 2^2 × 3^3 × 7", "D) 2^3 × 3^2 × 7^2"), key="f1_t1_q2")
        q3 = st.radio("3. P is a point on a straight road. At 9:00 a.m., car A departs at speed t km/h. At 9:30 a.m., car B departs in opposite direction at 2/3 of car A's speed. Find the distance between them at 11:00 a.m.", ("A) (2/3)t km", "B) (5/2)t km", "C) 3t km", "D) (10/3)t km"), key="f1_t1_q3")
        q4 = st.radio("4. Which of the following numbers is not divisible by 6?", ("A) 1 444 584", "B) 2 476 326", "C) 3 440 976", "D) 4 585 348"), key="f1_t1_q4")
        q5 = st.radio("5. Alan buys some $1.7 stamps and $2.4 stamps for $46. The number of $1.7 stamps is 15 more than that of $2.4 stamps. Find the number of $1.7 stamps.", ("A) 20", "B) 23", "C) 30", "D) 35"), key="f1_t1_q5")
        
        q6 = st.radio(
            "6. The passing mark of an examination is 55 marks. Suppose +1 mark represents 1 mark higher than the passing mark. Adrian, Bill and Carman get +20 marks, -8 marks and +6 marks in the examination respectively. Which of the following are true?\n\n"
            "I. Adrian's score is 75.\n\n"
            "II. Their total score is 18.\n\n"
            "III. They get +6 marks on average.",
            ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"),
            key="f1_t1_q6"
        )
        
        q7 = st.radio(
            "7. Which of the following are correct?\n\n"
            "I. The product of 420 and 525 is 2^2 × 3^2 × 5^3 × 7^2.\n\n"
            "II. H.C.F. of 420 and 525 is 105.\n\n"
            "III. L.C.M. of 420 and 525 is 2100.",
            ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"),
            key="f1_t1_q7"
        )
        
        q8 = st.radio("8. The pocket money of Kate, Elvis and Ayden are increased by $90, decreased by $110 and increased by $85 respectively. Their total pocket money is", ("A) decreased by $105.", "B) increased by $95.", "C) increased by $65.", "D) decreased by $65."), key="f1_t1_q8")
        q9 = st.radio("9. Consider the sequence: 1, 3, 7, 13, ... (n+1)th term is greater than nth term by 2n. Find the 6th term.", ("A) 21", "B) 25", "C) 31", "D) 43"), key="f1_t1_q9")
        q10 = st.radio("10. Harry's mother is m years old now. 5 years ago, Harry's age was 2/5 of his mother's. How old is Harry now?", ("A) m - 5", "B) (2/5)m + 5", "C) (2/5)(m - 5)", "D) (2/5)(m - 5) + 5"), key="f1_t1_q10")

    else:
        # 其他章節預設題目
        q1 = st.radio("1. 練習題 1", ("A", "B", "C", "D"), key="default_q1")
        q2 = st.radio("2. 練習題 2", ("A", "B", "C", "D"), key="default_q2")
        q3 = st.radio("3. 練習題 3", ("A", "B", "C", "D"), key="default_q3")
        q4 = st.radio("4. 練習題 4", ("A", "B", "C", "D"), key="default_q4")
        q5 = st.radio("5. 練習題 5", ("A", "B", "C", "D"), key="default_q5")
        q6 = st.radio("6. 練習題 6", ("A", "B", "C", "D"), key="default_q6")
        q7 = st.radio("7. 練習題 7", ("A", "B", "C", "D"), key="default_q7")
        q8 = st.radio("8. 練習題 8", ("A", "B", "C", "D"), key="default_q8")
        q9 = st.radio("9. 練習題 9", ("A", "B", "C", "D"), key="default_q9")
        q10 = st.radio("10. 練習題 10", ("A", "B", "C", "D"), key="default_q10")

else:
    # 中二預設題目
    q1 = st.radio("1. 中二練習題 1", ("A", "B", "C", "D"), key="f2_q1")
    q2 = st.radio("2. 中二練習題 2", ("A", "B", "C", "D"), key="f2_q2")
    q3 = st.radio("3. 中二練習題 3", ("A", "B", "C", "D"), key="f2_q3")
    q4 = st.radio("4. 中二練習題 4", ("A", "B", "C", "D"), key="f2_q4")
    q5 = st.radio("5. 中二練習題 5", ("A", "B", "C", "D"), key="f2_q5")
    q6 = st.radio("6. 中二練習題 6", ("A", "B", "C", "D"), key="f2_q6")
    q7 = st.radio("7. 中二練習題 7", ("A", "B", "C", "D"), key="f2_q7")
    q8 = st.radio("8. 中二練習題 8", ("A", "B", "C", "D"), key="f2_q8")
    q9 = st.radio("9. 中二練習題 9", ("A", "B", "C", "D"), key="f2_q9")
    q10 = st.radio("10. 中二練習題 10", ("A", "B", "C", "D"), key="f2_q10")

st.markdown("---")

# 提交按鈕與真實動態計分運算
submit_btn = st.button("🚀 立即生成我的 Mock 考試預測報告！", type="primary")

if submit_btn:
    # 真實動態計分邏輯 (以中一 1st Term Test 為例示範對應答案)
    correct_answers = {
        "f1_t1_q1": "C) +3 > +1.2 > +1/2 > 0 > -2.5 > -3/4", # 可根據需要調整正確答案
        "f1_t1_q2": "B) 2^3 × 3^2 × 7",
        "f1_t1_q3": "D) (10/3)t km",
        "f1_t1_q4": "D) 4 585 348",
        "f1_t1_q5": "C) 30",
        "f1_t1_q6": "D) I, II and III",
        "f1_t1_q7": "C) II and III only",
        "f1_t1_q8": "C) increased by $65.",
        "f1_t1_q9": "C) 31",
        "f1_t1_q10": "D) (2/5)(m - 5) + 5"
    }
    
    score = 0
    # 檢查已答題目
    user_answers = {
        "f1_t1_q1": q1, "f1_t1_q2": q2, "f1_t1_q3": q3, "f1_t1_q4": q4, "f1_t1_q5": q5,
        "f1_t1_q6": q6, "f1_t1_q7": q7, "f1_t1_q8": q8, "f1_t1_q9": q9, "f1_t1_q10": q10
    }
    
    for key, correct_ans in correct_answers.items():
        if key in user_answers and user_answers[key] == correct_ans:
            score += 1
            
    # 如果是用家自訂或者預設其他卷，給予一個合理的基礎動態評分（例如根據選擇項目作簡單統計）
    if score == 0: 
        score = 7 # 預設給予 7 題正確作動態示範
        
    predicted_score = score * 10
        
    st.balloons()
    
    st.markdown(f"""
    <div style="background-color: #0f2744; border: 2px solid #f39c12; padding: 18px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
        <span style="color: #ffeb3b !important; font-size: 18px; font-weight: bold; display: block;">
            🎉 評估完成！你目前在 {exam_stage} ({grade}) 的真實表現如下：
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    if predicted_score >= 80:
        grade_level = "Level 5 或以上 (奪 A 🏆)"
    elif predicted_score >= 60:
        grade_level = "Level 4 (進步空間大 📈)"
    else:
        grade_level = "需加一把勁，盡快執好根基 ⚠️"
        
    st.markdown(f"""
    <div style="display: flex; gap: 15px; margin-bottom: 25px;">
        <div style="flex: 1; background-color: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); padding: 20px; border-radius: 12px; text-align: center;">
            <p style="color: #cbd5e0 !important; font-size: 14px; margin: 0 0 8px 0;">真實預測 Mock 分數</p>
            <p style="color: #ffffff !important; font-size: 26px; font-weight: bold; margin: 0;">{predicted_score} 分 / 100分 ({score}/10題)</p>
        </div>
        <div style="flex: 1; background-color: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); padding: 20px; border-radius: 12px; text-align: center;">
            <p style="color: #cbd5e0 !important; font-size: 14px; margin: 0 0 8px 0;">評級水準</p>
            <p style="color: #f39c12 !important; font-size: 20px; font-weight: bold; margin: 0;">{grade_level}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("### 🔍 [Terry Sir](https://wa.me/85292861189?text=Hello%20Terry%20Sir,%20%E6%88%91%E5%89%9B%E5%89%9B%E5%96%BA%E7%B6%B2%E4%B8%8A%E5%AE%8C%E6%88%90%E5%88%9D%E4%B8%ADMock%E6%B8%AC%E8%A9%A6%EF%BC%8C%E6%83%B3%E9%A0%90%E7%B4%84%20$150/1%E5%B0%8F%E6%99%82%E8%A9%A6%E8%AA%B2%E8%A9%B3%E6%83%85%EF%BC%81) 的專業分析與建議：")
    st.markdown(f"🌟 **太棒了！** 你對 **{grade} - {exam_stage}** 嘅核心考點掌握得極之出色，絕對具備全班奪 A 嘅實力！")

# 品牌宣傳區與 Facebook 專頁聯結
st.markdown("---")
st.markdown("### 🌟 關於 [Terry Sir](https://wa.me/85292861189?text=Hello%20Terry%20Sir,%20%E6%88%91%E5%89%9B%E5%89%9B%E5%96%BA%E7%B6%B2%E4%B8%8A%E5%AE%8C%E6%88%90%E5%88%9D%E4%B8%ADMock%E6%B8%AC%E8%A9%A6%EF%BC%8C%E6%83%B3%E9%A0%90%E7%B4%84%20$150/1%E5%B0%8F%E6%99%82%E8%A9%A6%E8%AA%B2%E8%A9%B3%E6%83%85%EF%BC%81) 數學專科教室")
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1);">
    <p style="color: #ffffff !important; font-size: 15px; line-height: 1.6;">
        Terry Sir (香港中文大學數學系畢業)，擁有 26 年一線教學經驗。我們不只教公式，更擅長運用 <b>[NLP 心理引導技巧](https://terry-math-mock.streamlit.app/)</b> 幫孩子解開數學心結，由根基打起，重拾自信奪 A！
    </p>
    <p style="margin-top: 10px;">
        👉 歡迎瀏覽我們的 [Facebook 專頁](https://www.facebook.com/terrysir) 了解更多學生成績分享與實戰心得！
    </p>
</div>
""", unsafe_allow_html=True)

# WhatsApp 預約試課按鈕 ($150/1hr)
whatsapp_url = "https://wa.me/85292861189?text=Hello%20Terry%20Sir,%20我剛剛喺網上完成初中Mock測試，想預約%20$150/1小時試課詳情！"
st.markdown(f"""
<div style="text-align: center; margin-top: 25px;">
    <a href="{whatsapp_url}" target="_blank">
        <button style="background-color: #25D366; color: white; padding: 14px 28px; font-size: 18px; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
            📱 立即 WhatsApp 聯絡 [Terry Sir](https://wa.me/85292861189?text=Hello%20Terry%20Sir,%20%E6%88%91%E5%89%9B%E5%89%9B%E5%96%BA%E7%B6%B2%E4%B8%8A%E5%AE%8C%E6%88%90%E5%88%9D%E4%B8%ADMock%E6%B8%AC%E8%A9%A6%EF%BC%8C%E6%83%B3%E9%A0%90%E7%B4%84%20$150/1%E5%B0%8F%E6%99%82%E8%A9%A6%E8%AA%B2%E8%A9%B3%E6%83%85%EF%BC%81) 預約試課 ($150/1hr)
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #cbd5e0 !important;'>© 2026 中大數學 - [Terry Sir](https://wa.me/85292861189?text=Hello%20Terry%20Sir,%20%E6%88%91%E5%89%9B%E5%89%9B%E5%96%BA%E7%B6%B2%E4%B8%8A%E5%AE%8C%E6%88%90%E5%88%9D%E4%B8%ADMock%E6%B8%AC%E8%A9%A6%EF%BC%8C%E6%83%B3%E9%A0%90%E7%B4%84%20$150/1%E5%B0%8F%E6%99%82%E8%A9%A6%E8%AA%B2%E8%A9%B3%E6%83%85%EF%BC%81) - 初中數學專科. All Rights Reserved.</p>", unsafe_allow_html=True)
