import streamlit as st

# 網頁基本設定
st.set_page_config(
    page_title="Terry Sir | 初中數學 Mock Exam 預測系統",
    page_icon="📐",
    layout="centered"
)

# 頁面標題與簡介
st.title("📐 Terry Sir【中大數學】初中數學 Mock 預測系統")
st.markdown("""
歡迎來到由中大數學系畢業、26年一線教學經驗嘅 **Terry Sir** 專屬數學評估平台！ 👨‍🏫✨  
唔好再盲目死背公式！透過以下嘅 1st Term Test 實戰測試，即刻預測你喺學校考試嘅 **Mock 預測分數**，精準找出你嘅失分盲點！
""")

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
grade = st.radio("請選擇你嘅年級：", ["中一 (Form 1)", "中二 (Form 2)", "中三 (Form 3)"], horizontal=True)

st.markdown("---")
st.subheader("✍️ 第二步：1st Term Test 實戰精選能力快測")
st.markdown("請認真回答以下 5 條精選試題：")

# 題目 1 (誤差 Percentage Error)
q1 = st.radio(
    "題目 1 (誤差)：The height of a door is measured as 2.00 m, correct to the nearest 0.05 m. Find the percentage error.",
    ("A) 1.25%", "B) 2.5%", "C) 12.5%", "D) 25%")
)

# 題目 2 (有效數字與範圍 Significant Figures / Range)
q2 = st.radio(
    "題目 2 (數值範圍)：If y = 29.4 (correct to 3 significant figures), find the range of values of y.",
    ("A) 29.3 < y <= 29.5", "B) 29.3 <= y < 29.5", "C) 29.35 < y <= 29.45", "D) 29.35 <= y < 29.45")
)

# 題目 3 (恆等式與比較係數 Identities)
q3 = st.radio(
    "題目 3 (恆等式)：If (x - p)(x + 5) - 7q ≡ x^2 + 6x - q - 1, then q =",
    ("A) -6", "B) -1", "C) 1", "D) 6")
)

# 題目 4 (指數定律 Laws of Indices)
q4 = st.radio(
    "題目 4 (指數定律)：(-4^50)^4 (1/64)^100 =",
    ("A) -1", "B) 4^100", "C) 1 / (4^100)", "D) -1 / (4^200)")
)

# 題目 5 (代數分式化簡 Algebraic Fractions)
q5 = st.radio(
    "題目 5 (分式化簡)：Simplify [3 / (m - 1)] - [2 / (m + 1)] =",
    ("A) 1 / (m - 1)", "B) 1 / (m + 1)", "C) (m + 5) / (m^2 - 1)", "D) (m - 5) / (m^2 - 1)")
)

st.markdown("---")

# 提交按鈕與結果預測運算
if st.button("🚀 立即生成我的 Mock 考試預測報告！", type="primary"):
    # 正確答案對應：Q1: A, Q2: D, Q3: A, Q4: C (視乎選定標準，此處為示範邏輯), Q5: C
    score = 0
    if "A" in q1: score += 1
    if "D" in q2: score += 1
    if "A" in q3: score += 1
    if "C" in q4: score += 1
    if "C" in q5: score += 1
    
    # 根據答對題數 (滿分5題) 換算 100 分制預測分數
    predicted_score = 35 + (score * 13) if score > 0 else 30
    if score == 5:
        predicted_score = 92  # 全對高分
        
    st.balloons() # 慶祝特效
    
    st.success(f"🎉 評估完成！你目前在 **{exam_stage} ({grade})** 的表現如下：")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="預測 Mock 考試分數", value=f"{predicted_score} 分 / 100分")
    with col2:
        grade_level = "Level 5 或以上 (奪 A 級別 🏆)" if predicted_score >= 75 else "Level 4 (進步空間大 📈)" if predicted_score >= 60 else "需加一把勁，盡快執好根基 ⚠️"
        st.metric(label="評級水準", value=grade_level)
        
    st.markdown("### 🔍 Terry Sir 的專業分析與建議：")
    if score >= 4:
        st.markdown("🌟 **太棒了！** 你對初中代數、誤差同指數定律嘅基本功掌握得非常好，完全具備衝擊全班頭幾名嘅實力！只要繼續保持，穩陣奪 A 絕對冇問題！")
    elif score >= 3:
        st.markdown("💪 **表現唔錯，但仍有進步空間！** 你大部分概念都清晰，但有少部分細微盲點（例如符號或括號展開）。只要適當做多啲「拆局」訓練，好快可以推上 80 分以上！")
    else:
        st.markdown("⚠️ **你需要即刻注意喇！** 目前嘅基礎出現咗明顯漏洞，如果唔盡快執好底層邏輯，到正式考試好容易因為緊張而失準。建議盡快搵 Terry Sir 幫你重塑數學根基！")
        
    st.markdown("---")
    st.markdown("### 🚀 想將分數再推高？即刻搵 Terry Sir 幫你「拆局」！")
    st.markdown("唔想每次溫書都盲目死背？想學識用 NLP 心法同高效系統化筆記輕鬆拿高分？")
    
    # WhatsApp 按鈕連結
    whatsapp_url = "https://wa.me/85292861189?text=Hello%20Terry%20Sir,%20我剛剛喺網上 Mock 測試做咗，想預約 $400/1小時試課詳情！"
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
st.markdown("<p style='text-align: center; color: gray;'>© 2026 中大數學 - Terry Sir - 初中數學專科. All Rights Reserved.</p>", unsafe_allow_html=True)
