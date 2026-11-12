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
唔好再盲目死背公式！透過以下嘅階段性實戰測試，即刻預測你喺學校考試嘅 **Mock 預測分數**，精準找出你嘅失分盲點！
""")

st.markdown("---")

# 選擇學年階段
st.subheader("📌 第一步：請選擇你目前準備緊嘅考試階段")
exam_stage = st.selectbox(
    "選擇考試階段",
    [
        "1st Term Test (第一次測驗)", 
        "1st Exam (上學期考試)", 
        "2nd Term Test (第二次測驗)", 
        "2nd Exam (下學期考試 / Final)"
    ]
)

# 選擇級別
grade = st.radio("請選擇你嘅年級：", ["中一 (Form 1)", "中二 (Form 2)", "中三 (Form 3)"], horizontal=True)

st.markdown("---")
st.subheader("✍️ 第二步：即時數學能力快測")
st.markdown("請回答以下 3 條精選核心題目，測試你現階段嘅實力：")

# 模擬題目 (你可以隨時根據你手上嘅題目隨時替換呢度嘅 Q1, Q2, Q3)
q1 = st.radio(
    "題目 1 (代數與展開)：化簡或展開 $(2x - y)^2$ =",
    ("A) $4x^2 - y^2$", "B) $4x^2 - 4xy + y^2$", "C) $4x^2 + y^2$", "D) $2x^2 - 2xy + y^2$")
)

q2 = st.radio(
    "題目 2 (指數定律)：化簡 $\\frac{x^5 \\times x^3}{x^2}$ =",
    ("A) $x^4$", "B) $x^6$", "C) $x^8$", "D) $x^{10}$")
)

q3 = st.radio(
    "題目 3 (因式分解)：因式分解 $9x^2 - 16y^2$ =",
    ("A) $(3x - 4y)^2$", "B) $(3x + 4y)^2$", "C) $(3x - 4y)(3x + 4y)$", "D) $(9x - 16y)(x + y)$")
)

st.markdown("---")

# 提交按鈕與結果預測運算
if st.button("🚀 立即生成我的 Mock 考試預測報告！", type="primary"):
    # 簡單計分邏輯 (正確答案分別係 B, B, C)
    score = 0
    if "B" in q1: score += 1
    if "B" in q2: score += 1
    if "C" in q3: score += 1
    
    # 根據答對題數預測分數 (滿分 100)
    predicted_score = 45 + (score * 18) if score > 0 else 40
    if score == 3:
        predicted_score = 88  # 全對就拎高分
        
    st.balloons() # 慶祝特效
    
    st.success(f"🎉 評估完成！你目前在 **{exam_stage} ({grade})** 的表現如下：")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="預測 Mock 考試分數", value=f"{predicted_score} 分 / 100分")
    with col2:
        grade_level = "Level 5 或以上 (奪 A 級別 🏆)" if predicted_score >= 75 else "Level 4 (進步空間大 📈)" if predicted_score >= 60 else "需加一把勁，盡快執好根基 ⚠️"
        st.metric(label="評級水準", value=grade_level)
        
    st.markdown("### 🔍 Terry Sir 的專業分析與建議：")
    if score == 3:
        st.markdown("🌟 **太棒了！** 你對代數展開、指數定律同因式分解嘅基本功掌握得非常好，完全具備衝擊全班頭幾名嘅實力！只要繼續保持，穩陣奪 A 絕對冇問題！")
    elif score == 2:
        st.markdown("💪 **表現唔錯，但仍有進步空間！** 你大部分概念都清晰，但有少部分細微盲點（例如符號或括號運用）。只要適當做多啲「拆局」訓練，好快可以推上 80 分以上！")
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