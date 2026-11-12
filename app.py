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
唔好再盲目死背公式！透過以下嘅 **中二 1st Term Test 實戰模擬試卷**（共 10 題），即刻預測你喺學校考試嘅 **Mock 預測分數**，精準找出你嘅失分盲點！
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
grade = st.radio("請選擇你嘅年級：", ["中一 (Form 1)", "中二 (Form 2)", "中三 (Form 3)"], index=1, horizontal=True)

st.markdown("---")
st.subheader("✍️ 第二步：中二 1st Term Test 全真 10 題 MC 能力快測")
st.markdown("請認真完成以下 10 題精選試題：")

# Q1: 誤差
q1 = st.radio(
    "1. The height of a door is measured as 2.00 m, correct to the nearest 0.05 m. Find the percentage error.",
    ("A) 1.25%", "B) 2.5%", "C) 12.5%", "D) 25%")
)

# Q2: 範圍
q2 = st.radio(
    "2. If y = 29.4 (correct to 3 significant figures), find the range of values of y.",
    ("A) 29.3 < y <= 29.5", "B) 29.3 <= y < 29.5", "C) 29.35 < y <= 29.45", "D) 29.35 <= y < 29.45")
)

# Q3: 展開式次數 (Degree)
q3 = st.radio(
    "3. Find the degree of the expansion of (x^2 + 2x + 4)(y - 2).",
    ("A) 1", "B) 2", "C) 3", "D) 4")
)

# Q4: 恆等式與比較係數
q4 = st.radio(
    "4. If (x - p)(x + 5) - 7q ≡ x^2 + 6x - q - 1, then q =",
    ("A) -6", "B) -1", "C) 1", "D) 6")
)

# Q5: 唔係恆等式
q5 = st.radio(
    "5. Which of the following are NOT identities?\nI. 1/x - 1 = (1 - x)/x\nII. (x + 1)^2 = x^2 + 1\nIII. (ax + b)(x - b) = ax^2 - b^2",
    ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III")
)

# Q6: 指數定律 (-4^50)
q6 = st.radio(
    "6. (-4^50)^4 (1/64)^100 =",
    ("A) -1", "B) 4^100", "C) 1 / (4^100)", "D) -1 / (4^200)")
)

# Q7: 指數定律 (x^n)
q7 = st.radio(
    "7. If a ≠ 0 and a ≠ 1, then (a^(n+1) - a^(n-1)) / (a^n - a^(n-1)) =",
    ("A) 2", "B) a", "C) a + 1", "D) a - 1")
)

# Q8: 代數分式化簡 (減法)
q8 = st.radio(
    "8. Simplify [3 / (m - 1)] - [2 / (m + 1)] =",
    ("A) 1 / (m - 1)", "B) 1 / (m + 1)", "C) (m + 5) / (m^2 - 1)", "D) (m - 5) / (m^2 - 1)")
)

# Q9: 代數分式化簡 (乘法)
q9 = st.radio(
    "9. Simplify [ (3a^2 + 6ab) / (a^2 + 2ab - ab - 2b^2) ] × [ (4a - 4b) / (9a^2) ] =",
    ("A) 4 / (3a)", "B) 4a / 3", "C) 4(a + 2b) / [3a(a^2 + ab - 2b^2)]", "D) 4a(a + 2b) / [3(a^2 + ab - 2b^2)]")
)

# Q10: 聯立方程與代數關係
q10 = st.radio(
    "10. If x^2 + y^2 = m and x + y = n, then xy =",
    ("A) (1/2)(n^2 - m)", "B) n^2 - m", "C) n^2 - m/2", "D) (n^2)/2 - m")
)

st.markdown("---")

# 提交按鈕與結果預測運算
if st.button("🚀 立即生成我的中二 Mock 考試預測報告！", type="primary"):
    # 標準答案對應 (根據題目 PDF 標準答案：Q1:A, Q2:D, Q3:C, Q4:A, Q5:C, Q6:C, Q7:C, Q8:C, Q9:A, Q10:A)
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
    
    # 根據 10 題對幾多黎換算 100 分制預測分數
    predicted_score = score * 10
    if predicted_score < 30: predicted_score = 35 # 最低底線
        
    st.balloons() # 慶祝特效
    
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
        st.markdown("💪 **表現唔錯，但仍有進步空間！** 你大部分觀念清晰，但有少部分題目（例如代數分式化簡或指數轉換）仲有盲點。只要做多幾次「拆局」訓練，好快可以衝上 80 分以上！")
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
st.markdown("<p style='text-align: center; color: gray;'>© 2026 中大數學 - Terry Sir - 初中數學專科. All Rights Reserved.</p>", unsafe_allow_html=True)
