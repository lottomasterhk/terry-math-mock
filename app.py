import streamlit as st

# 網頁基本設定 (頁面標題與佈局)
st.set_page_config(
    page_title="Terry Sir | 中大數學專科教室",
    page_icon="📐",
    layout="centered"
)

# 注入自定義 CSS (完美還原 Poster 嘅深藍高科技、金藍配色、圓角膠囊與專業 Mood)
st.markdown("""
<style>
    /* 全局背景與字體顏色 */
    .stApp {
        background: linear-gradient(135deg, #0b1d3a 0%, #061124 100%);
        color: #ffffff;
    }
    
    /* 標題與文字美化 */
    h1, h2, h3 {
        color: #ffffff !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* 區塊卡片化 (Container Card) */
    .css-1r6slb0, .stRadio > div {
        background-color: rgba(255, 255, 255, 0.03);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* 按鈕美化：極靚嘅漸變金藍按鈕 */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 14px 24px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #2a5298 0%, #3a7bd5 100%);
        border-color: #f39c12;
    }
    
    /* 選擇框與下拉選單美化 */
    .stSelectbox, .stRadio {
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# 頁面頂部品牌視覺宣傳標題
st.markdown("""
<div style="text-align: center; padding: 10px 0;">
    <span style="background: rgba(243, 156, 18, 0.2); color: #f39c12; padding: 6px 16px; border-radius: 20px; font-size: 14px; font-weight: bold; border: 1px solid rgba(243, 156, 18, 0.4);">
        🧠 NLP 心理引導 × 中大數學專業培訓
    </span>
    <h1 style="margin-top: 15px; font-size: 32px; font-weight: 800;">【中大數學】Terry Sir - 初中數學專科教室</h1>
    <p style="color: #a0aec0; font-size: 16px; max-width: 650px; margin: 0 auto;">
        核心理念：不只教公式，用 NLP 心理引導幫孩子解開數學心結，由根基打起，重拾信心奪 A！ ✨
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# 選擇學年階段與年級
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
st.subheader("✍️ 第二步：中二 1st Term Test 全真 10 題 MC 能力快測")
st.markdown("請認真完成以下 10 題精選實戰試題：")

# 10 題精選中二 MC
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

st.markdown("---")

# 提交按鈕與結果預測運算
if st.button("🚀 立即生成我的中二 Mock 考試預測報告！", type="primary"):
    score = 0
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
    
    predicted_score = score * 10
    if predicted_score < 30: predicted_score = 35
        
    st.balloons()
    
    st.success(f"🎉 評估完成！你目前在 **{exam_stage} ({grade})** 的表現如下：")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="預測 Mock 考試分數", value=f"{predicted_score} 分 / 100分")
    with col2:
        grade_level = "Level 5 或以上 (奪 A 級別 🏆)" if predicted_score >= 80 else "Level 4 (進步空間大 📈)" if predicted_score >= 60 else "需加一把勁，盡快執好根基 ⚠️"
        st.metric(label="評級水準", value=grade_level)
        
    st.markdown("### 🔍 Terry Sir 的專業分析與建議：")
    if score >= 8:
        st.markdown("🌟 **太棒了！** 你對中二上學期嘅代數展開、指數定律、恆等式同誤差掌握得極之出色，絕對具備全班奪 A 嘅實力！")
    elif score >= 5:
        st.markdown("💪 **表現唔錯，但仍有進步空間！** 你大部分觀念清晰，但有少部分題目仲有盲點。只要做多幾次「拆局」訓練，好快可以衝上 80 分以上！")
    else:
        st.markdown("⚠️ **你需要即刻正視盲點喇！** 目前嘅基礎出現咗唔少漏洞，如果唔盡快由淺入深執好底層邏輯，到正式考試好容易因為緊張失準。建議盡快搵 Terry Sir 幫你重塑數學根基！")
        
    st.markdown("---")
    st.markdown("### 🚀 想將分數再推高？即刻搵 Terry Sir 幫你「拆局」！")
    st.markdown("唔想每次溫書都盲目死背？想學識用 NLP 心法同高效系統化筆記輕鬆拿高分？")
    
    # WhatsApp 按鈕連結
    whatsapp_url = "https://wa.me/85292861189?text=Hello%20Terry%20Sir,%20我剛剛喺網上完成中二Mock測試，想預約 $400/1小時試課詳情！"
    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="{whatsapp_url}" target="_blank">
            <button style="background-color: #25D366; color: white; padding: 12px 24px; font-size: 18px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
                📱 立即 WhatsApp 聯絡 Terry Sir 預約試課 ($400/1hr)
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #a0aec0;'>© 2026 中大數學 - Terry Sir - 初中數學專科. All Rights Reserved.</p>", unsafe_allow_html=True)
