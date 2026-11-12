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

# 頁面頂部品牌視覺宣傳標題 (對應 Poster 風格)
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
grade = st.radio("請選擇你嘅年級：", ["中一 (Form 1)", "中二 (Form 2)", "中三 (Form 3)"], index=1, horizontal=True)

st.markdown("---")

# 動態判斷：根據選擇顯示唔同嘅 10 題快測
if "1st Term Test" in exam_stage:
    st.subheader("✍️ 第二步：中二 1st Term Test 校本真題級 10 題快測")
    st.markdown("請認真完成以下 10 題精選實戰試題：")
    
    q1 = st.radio("1. The height of a door is measured as 2.00 m, correct to the nearest 0.05 m. Find the percentage error.", ("A) 1.25%", "B) 2.5%", "C) 12.5%", "D) 25%"))
    q2 = st.radio("2. If y = 29.4 (correct to 3 significant figures), find the range of values of y.", ("A) 29.3 < y ≤ 29.5", "B) 29.3 ≤ y < 29.5", "C) 29.35 < y ≤ 29.45", "D) 29.35 ≤ y < 29.45"))
    q3 = st.radio("3. Find the degree of the expansion of (x^2 + 2x + 4)(y - 2).", ("A) 1", "B) 2", "C) 3", "D) 4"))
    q4 = st.radio("4. If (x - p)(x + 5) - 7q ≡ x^2 + 6x - q - 1, then q =", ("A) -6", "B) -1", "C) 1", "D) 6"))
    q5 = st.radio("5. Which of the following are NOT identities?\nI. 1/x - 1 = (1 - x)/x\nII. (x + 1)^2 = x^2 + 1\nIII. (ax + b)(x - b) = ax^2 - b^2", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"))
    q6 = st.radio("6. (-4^50)^4 (1/64)^100 =", ("A) -1", "B) 4^100", "C) 1 / (4^100)", "D) -1 / (4^200)"))
    q7 = st.radio("7. If a ≠ 0 and a ≠ 1, then (a^(n+1) - a^(n-1)) / (a^n - a^(n-1)) =", ("A) 2", "B) a", "C) a + 1", "D) a - 1"))
    q8 = st.radio("8. Simplify [3 / (m - 1)] - [2 / (m + 1)] =", ("A) 1 / (m - 1)", "B) 1 / (m + 1)", "C) (m + 5) / (m^2 - 1)", "D) (m - 5) / (m^2 - 1)"))
    q9 = st.radio("9. Simplify [ (3a^2 + 6ab) / (a^2 + 2ab - ab - 2b^2) ] × [ (4a - 4b) / (9a^2) ] =", ("A) 4 / (3a)", "B) 4a / 3", "C) 4(a + 2b) / [3a(a^2 + ab - 2b^2)]", "D) 4a(a + 2b) / [3(a^2 + ab - 2b^2)]"))
    q10 = st.radio("10. If x^2 + y^2 = m and x + y = n, then xy =", ("A) (1/2)(n^2 - m)", "B) n^2 - m", "C) n^2 - m/2", "D) (n^2)/2 - m"))

else:
    st.subheader("✍️ 第二步：中二 1st Exam (上學期考試) 校本真題級 10 題快測")
    st.markdown("請認真完成以下 10 題精選上學期實戰試題：")
    
    q1 = st.radio("1. The thickness of a dictionary is measured as 4.0 cm, correct to the nearest 0.5 cm. Find the actual range of values of x.", ("A) 3.5 ≤ x < 4.5", "B) 3.5 < x < 4.5", "C) 3.75 ≤ x < 4.25", "D) 3.75 < x < 4.25"))
    q2 = st.radio("2. Which of the following is not a polynomial?", ("A) 5x - 3y", "B) 5xy - 3", "C) x/5 - y/3", "D) 5x - 3/y"))
    q3 = st.radio("3. Given V = (2πR) / T. If R = 8 and V = 5π, find the value of T.", ("A) 0.8", "B) 1.6", "C) 3.2", "D) 4"))
    q4 = st.radio("4. Factorize completely: ax - cx - ay - bx + cy + by =", ("A) (x + y)(a + b - c)", "B) (x + y)(a - b - c)", "C) (x - y)(a + b - c)", "D) (x - y)(a - b - c)"))
    q5 = st.radio("5. The graph of 4x + ay = 18 passes through P(6, -3). Which of the following points lies on the graph?", ("A) (-3, -6)", "B) (-1, -11)", "C) (1, 7)", "D) (7, -2)"))
    q6 = st.radio("6. Solve the simultaneous equations: x + y - 8 = (3x)/4 + 10 - y = 0", ("A) (316/37, -20/37)", "B) (324/37, -28/37)", "C) (-8/7, 64/7)", "D) (-72/7, 16/7)"))
    q7 = st.radio("7. In the geometric figure where AED and BEC are straight lines with angle EDC = x, z = exterior angle, which of the following must be true?", ("A) x = y", "B) x + y = 90°", "C) z = x + y", "D) x + y + z = 180°"))
    q8 = st.radio("8. In the figure where PQT and PRS are straight lines with internal angles a, b, c, d, e, which of the following angle relationships must be true?", ("A) a = b - c", "B) c + e = 180°", "C) a + b = c + e", "D) c + d + e = 180° + b"))
    q9 = st.radio("9. In the figure where CDE is a straight line and x + y = 90°, which of the following statements must be true?\nI. AB // CE\nII. AC ⊥ AD\nIII. x = y", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"))
    q10 = st.radio("10. Based on the ice cream flavor pie charts (Shop A: Chocolate 40%, Peach 24%, Mango 16%, Strawberry 12%, Almond 8%; Shop B: Mango 40%, Peach 22%, Chocolate 20%, Strawberry 10%, Almond 8%), which of the following must be correct?\nI. Number of customers voting peach in A > B\nII. Peach flavor is more popular than strawberry in both shops\nIII. Percentages of customers voting almond in shop A and B are the same", ("A) I only", "B) III only", "C) I and II only", "D) II and III only"))

st.markdown("---")

# 提交按鈕與結果預測運算
submit_btn = st.button("🚀 立即生成我的 Mock 考試預測報告！", type="primary")

if submit_btn:
    score = 0
    if "1st Term Test" in exam_stage:
        if "A" in q1: score += 1
        if "D" in q2: score += 1
        if "C" in q3: score += 1
        if "A" in q4: score += 1
        if "C" in q5: score += 1
        if "C" in q6: score += 1
        if "C" in q7: score += 1
        if "C" in q8: score += 1
        if "A" in q9: score += 1
        if "A" in q10: score += 1
    else:
        if "C" in q1: score += 1
        if "D" in q2: score += 1
        if "C" in q3: score += 1
        if "D" in q4: score += 1
        if "D" in q5: score += 1
        if "A" in q6: score += 1
        if "D" in q7: score += 1
        if "D" in q8: score += 1
        if "D" in q9: score += 1
        if "D" in q10: score += 1
    
    predicted_score = score * 10
    if predicted_score < 30: 
        predicted_score = 35
        
    st.balloons()
    
    # 改用深藍色底卡片 + 亮黃色字體，保證 100% 唔會再有白字盲點！
    st.markdown(f"""
    <div style="background-color: #0f2744; border: 2px solid #f39c12; padding: 18px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
        <span style="color: #ffeb3b !important; font-size: 18px; font-weight: bold; display: block;">
            🎉 評估完成！你目前在 {exam_stage} ({grade}) 的表現如下：
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="預測 Mock 考試分數", value=f"{predicted_score} 分 / 100分")
    with col2:
        if predicted_score >= 80:
            grade_level = "Level 5 或以上 (奪 A 級別 🏆)"
        elif predicted_score >= 60:
            grade_level = "Level 4 (進步空間大 📈)"
        else:
            grade_level = "需加把勁，盡快執好根基 ⚠️"
        st.metric(label="評級水準", value=grade_level)
        
    st.markdown("### 🔍 Terry Sir 的專業分析與建議：")
    if score >= 8:
        st.markdown(f"🌟 **太棒了！** 你對中二 **{exam_stage}** 嘅核心考點掌握得極之出色，絕對具備全班奪 A 嘅實力！")
    elif score >= 5:
        st.markdown(f"💪 **表現唔錯，但仍有進步空間！** 你大部分觀念清晰，但有少部分題目仲有盲點。只要做多幾次「拆局」訓練，好快可以衝上 80 分以上！")
    else:
        st.markdown(f"⚠️ **你需要即刻正視盲點喇！** 目前喺 **{exam_stage}** 嘅基礎出現咗唔少漏洞，如果唔盡快由淺入深執好底層邏輯，到正式考試好容易因為緊張失準。建議盡快搵 Terry Sir 幫你重塑數學根基！")

# 品牌宣傳區與 Facebook 專頁聯結
st.markdown("---")
st.markdown("### 🌟 關於 Terry Sir 數學專科教室")
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1);">
    <p style="color: #ffffff !important; font-size: 15px; line-height: 1.6;">
        Terry Sir (香港中文大學數學系畢業)，擁有 26 年一線教學經驗。我們不只教公式，更擅長運用 <b>NLP 心理引導技巧</b> 幫孩子解開數學心結，由根基打起，重拾自信奪 A！
    </p>
    <p style="margin-top: 10px;">
        👉 歡迎瀏覽我們的 <a href="https://www.facebook.com/terrysir" target="_blank" style="color: #f39c12; font-weight: bold; text-decoration: underline;">Facebook 專頁</a> 了解更多學生成績分享與實戰心得！
    </p>
</div>
""", unsafe_allow_html=True)

# WhatsApp 預約試課按鈕 ($150/1hr)
whatsapp_url = "https://api.whatsapp.com/send/?phone=85292861189&text=Hello+Terry+Sir%2C+%E6%88%91%E5%89%9B%E5%89%9B%E5%96%BA%E7%B6%B2%E4%B8%8A%E5%AE%8C%E6%88%90%E4%B8%AD%E4%BA%8CMock%E6%B8%AC%E8%A9%A6%EF%BC%8C%E6%83%B3%E9%A0%90%E7%B4%84+%24150%2F1%E5%B0%8F%E6%99%82%E8%A9%A6%E8%AA%B2%E8%A9%B3%E6%83%85%EF%BC%81&type=phone_number&app_absent=0"
st.markdown(f"""
<div style="text-align: center; margin-top: 25px;">
    <a href="{whatsapp_url}" target="_blank">
        <button style="background-color: #25D366; color: white; padding: 14px 28px; font-size: 18px; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
            📱 立即 WhatsApp 聯絡 Terry Sir 預約試課 ($150/1hr)
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #cbd5e0 !important;'>© 2026 中大數學 - Terry Sir - 初中數學專科. All Rights Reserved.</p>", unsafe_allow_html=True)
