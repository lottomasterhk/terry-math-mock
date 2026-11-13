import streamlit as st
import os

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
        background: linear-gradient(90deg, #2a5298 100%, #3a7bd5 100%) !important;
        border-color: #f39c12 !important;
    }
</style>
""", unsafe_allow_html=True)

# 輔助函式：安全載入圖片（已全面放大 50%）
def safe_image(img_path, width=390):
    if os.path.exists(img_path):
        st.image(img_path, width=width)

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
grade = st.radio("請選擇你嘅年級：", ["中一 (Form 1)", "中二 (Form 2)", "中三 (Form 3)"], index=2, horizontal=True)

st.markdown("---")

user_answers = {}
correct_answers = {}
question_topics = {}

# ==================== 中一 (Form 1) ====================
if "中一" in grade:
    if "1st Term Test" in exam_stage:
        st.subheader("✍️ 第二步：中一 1st Term Test 校本真題級 10 題快測")
        q1 = st.radio("1. Arrange the following numbers in descending order: +3, +1/2, -2.5, 0, -3/4, +1.2", ("A) +3 > +1.2 > +1/2 > 0 > -3/4 > -2.5", "B) +3 > +1/2 > +1.2 > 0 > -3/4 > -2.5", "C) +3 > +1.2 > +1/2 > 0 > -2.5 > -3/4", "D) -2.5 > -3/4 > 0 > +1/2 > +1.2 > +3"), key="f1_t1_q1")
        q2 = st.radio("2. Which of the following expressions gives a result of 756?", ("A) 2^2 × 3^2 × 7", "B) 2^3 × 3^2 × 7", "C) 2^2 × 3^3 × 7", "D) 2^3 × 3^2 × 7^2"), key="f1_t1_q2")
        q3 = st.radio("3. P is a point on a straight road. At 9:00 a.m., car A departs from P and travels at a speed of t km/h. At 9:30 a.m., car B departs from P and travels in the opposite direction of car A. The speed of car B is 2/3 of the speed of car A. Find the distance between the two cars at 11:00 a.m..", ("A) (2/3)t km", "B) t km", "C) 3t km", "D) (10/3)t km"), key="f1_t1_q3")
        q4 = st.radio("4. Which of the following numbers is not divisible by 6?", ("A) 1 444 584", "B) 2 476 326", "C) 3 440 976", "D) 4 585 348"), key="f1_t1_q4")
        q5 = st.radio("5. Alan buys some $1.7 stamps and $2.4 stamps for $46. It is given that the number of $1.7 stamps is 15 more than that of $2.4 stamps. Find the number of $1.7 stamps.", ("A) 20", "B) 23", "C) 30", "D) 35"), key="f1_t1_q5")
        q6 = st.radio("6. The passing mark of an examination is 55 marks. Suppose +1 mark represents 1 mark higher than the passing mark. Adrian, Bill and Carman get +20 marks, -8 marks and +6 marks in the examination respectively. Which of the following are true?\n\nI. Adrian's score is 75.\n\nII. Their total score is 18.\n\nIII. They get +6 marks on average.", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f1_t1_q6")
        q7 = st.radio("7. Which of the following are correct?\n\nI. The product of 420 and 525 is 2^2 × 3^2 × 5^3 × 7^2.\n\nII. The H.C.F. of 420 and 525 is 105.\n\nIII. The L.C.M. of 420 and 525 is 2 100.", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f1_t1_q7")
        q8 = st.radio("8. The pocket money of Kate, Elvis and Ayden are increased by $90, decreased by $110 and increased by $85 respectively. Their total pocket money is", ("A) decreased by $105.", "B) increased by $95.", "C) increased by $65.", "D) decreased by $65"), key="f1_t1_q8")
        q9 = st.radio("9. Consider the following sequence:\n\n1, 3, 7, 13, ...\n\nFor any positive integer n, the (n + 1)th term is greater than the nth term by 2n. Find the 6th term.", ("A) 21", "B) 25", "C) 31", "D) 43"), key="f1_t1_q9")
        q10 = st.radio("10. Harry's mother is m years old now. 5 years ago, Harry's age was 2/5 of his mother's age. How old is Harry now?", ("A) m - 5", "B) (2/5)m + 5", "C) (2/5)(m - 5)", "D) (2/5)(m - 5) + 5"), key="f1_t1_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "A) +3 > +1.2 > +1/2 > 0 > -3/4 > -2.5", 2: "C) 2^2 × 3^3 × 7", 3: "C) 3t km",
            4: "D) 4 585 348", 5: "A) 20", 6: "B) I and III only", 7: "D) I, II and III",
            8: "C) increased by $65.", 9: "C) 31", 10: "D) (2/5)(m - 5) + 5"
        }
        question_topics = {
            1: "有向數與數線大小比較", 2: "指數記數法與質因數分解", 3: "應用題與速度距離計算",
            4: "整除性與因數倍數", 5: "簡易方程應用題", 6: "有向數實際應用與平均數",
            7: "H.C.F. 與 L.C.M. 綜合運算", 8: "有向數加減運算", 9: "數列規律與一般項", 10: "代數與年齡應用題"
        }
    elif "1st Exam" in exam_stage:
        st.subheader("✍️ 第二步：中一 1st Exam 校本真題級 10 題快測")
        # 佔位
    elif "2nd Term Test" in exam_stage:
        st.subheader("✍️ 第二步：中一 2nd Term Test 校本真題級 10 題快測")
    else:
        st.subheader("✍️ 第二步：中一 2nd Exam 校本真題級 10 題快測")

# ==================== 中二 (Form 2) ====================
elif "中二" in grade:
    if "1st Term Test" in exam_stage:
        st.subheader("✍️ 第二步：中二 1st Term Test 校本真題級 10 題快測")
        q1 = st.radio("1. The height of a door is measured as 2.00 m, correct to the nearest 0.05 m. Find the percentage error.", ("A) 1.25%", "B) 2.5%", "C) 12.5%", "D) 25%"), key="f2_t1_q1")
        q2 = st.radio("2. If y = 29.4 (correct to 3 significant figures), find the range of values of y.", ("A) 29.3 < y ≤ 29.5", "B) 29.3 ≤ y < 29.5", "C) 29.35 < y ≤ 29.45", "D) 29.35 ≤ y < 29.45"), key="f2_t1_q2")
        q3 = st.radio("3. Find the degree of the expansion of (x^2 + 2x + 4)(y - 2).", ("A) 1", "B) 2", "C) 3", "D) 4"), key="f2_t1_q3")
        q4 = st.radio("4. If p and q are constants such that (x - p)(x + 5) - 7q ≡ x^2 + 6x - q - 1, then q =", ("A) -6", "B) -1", "C) 1", "D) 6"), key="f2_t1_q4")
        q5 = st.radio("5. Which of the following are NOT identities?\n\nI. 1/x - 1 = (1 - x)/x\n\nII. (x + 1)^2 = x^2 + 1\n\nIII. (ax + b)(x - b) = ax^2 - b^2", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f2_t1_q5")
        q6 = st.radio("6. (-4^50)^4 (1/64)^100 =", ("A) -1", "B) 4^100", "C) 1 / (4^100)", "D) -1 / (4^200)"), key="f2_t1_q6")
        q7 = st.radio("7. If a ≠ 0 and a ≠ 1, then (a^(n+1) - a^(n-1)) / (a^n - a^(n-1)) =", ("A) 2", "B) a", "C) a + 1", "D) a - 1"), key="f2_t1_q7")
        q8 = st.radio("8. Simplify [3 / (m - 1)] - [2 / (m + 1)] .", ("A) 1 / (m - 1)", "B) 1 / (m + 1)", "C) (m + 5) / (m^2 - 1)", "D) (m - 5) / (m^2 - 1)"), key="f2_t1_q8")
        q9 = st.radio("9. Simplify [ (3a^2 + 6ab) / (a^2 + 2ab - ab - 2b^2) ] × [ (4a - 4b) / (9a^2) ] .", ("A) 4 / (3a)", "B) 4a / 3", "C) 4(a + 2b) / [3a(a^2 + ab - 2b^2)]", "D) 4a(a + 2b) / [3(a^2 + ab - 2b^2)]"), key="f2_t1_q9")
        q10 = st.radio("10. If x^2 + y^2 = m and x + y = n, then xy =", ("A) (1/2)(n^2 - m)", "B) n^2 - m", "C) n^2 - m/2", "D) (n^2)/2 - m"), key="f2_t1_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "A) 1.25%", 2: "D) 29.35 ≤ y < 29.45", 3: "C) 3", 4: "D) 6", 5: "C) II and III only",
            6: "C) 1 / (4^100)", 7: "C) a + 1", 8: "C) (m + 5) / (m^2 - 1)", 9: "A) 4 / (3a)", 10: "A) (1/2)(n^2 - m)"
        }
        question_topics = {
            1: "誤差與百分誤差計算", 2: "有效數字與數值範圍", 3: "多項式展開與次方次數",
            4: "恆等式系數比較法", 5: "恆等式概念辨別", 6: "指數定律與化簡",
            7: "指數化簡與分式運算", 8: "分式加減法運算", 9: "分式乘法與因式分解", 10: "代數恆等式"
        }
    elif "1st Exam" in exam_stage:
        st.subheader("✍️ 第二步：中二 1st Exam 校本真題級 10 題快測")
    elif "2nd Term Test" in exam_stage:
        st.subheader("✍️ 第二步：中二 2nd Term Test 校本真題級 10 題快測")
    else:
        st.subheader("✍️ 第二步：中二 2nd Exam 校本真題級 10 題快測")

# ==================== 中三 (Form 3) ====================
else:
    if "1st Term Test" in exam_stage:
        st.subheader("✍️ 第二步：中三 1st Term Test (第一次測驗) 校本真題級 10 題快測")
        st.markdown("請完成以下 10 題真正對應 Word 檔 `F.3_1sttermtest_4.docx` 的實戰試題[cite: 8]：")
        
        safe_image("images/f3_t1_q13.png", width=390)
        q1 = st.radio("1. (對應試題13) $10010100011100_2 =$ ", ("A) 37 × 2^8 + 28.", "B) 37 × 2^8 + 56.", "C) 37 × 2^9 + 28.", "D) 37 × 2^9 + 56."), key="f3_t1_q1")
        
        safe_image("images/f3_t1_q14.png", width=390)
        q2 = st.radio("2. (對應試題14) $9 × 2^{10} + 6 × 2^9 + 2^3 - 7 =$ ", ("A) 101100010000_2", "B) 110010000100_2", "C) 1011000001111_2", "D) 1100000000001_2"), key="f3_t1_q2")
        
        q3 = st.radio("3. (對應試題15) Arrange the three numbers $1101100_2$, $105_{10}$ and $1101110_2$ in ascending order.", ("A) 1101110_2 < 105_10 < 1101100_2", "B) 1101100_2 < 105_10 < 1101110_2", "C) 105_10 < 1101110_2 < 1101100_2", "D) 105_10 < 1101100_2 < 1101110_2"), key="f3_t1_q3")
        
        safe_image("images/f3_t1_q16.png", width=390)
        q4 = st.radio("4. (對應試題16) A sum of $35 000 is deposited for 40 months at an interest rate of 3% p.a. compounded every four months. Find the interest, correct to the nearest dollar.", ("A) $1 180", "B) $2 715", "C) $3 662", "D) $4 966"), key="f3_t1_q4")
        
        safe_image("images/f3_t1_q18.png", width=390)
        q5 = st.radio("5. (對應試題18) If the base of a triangle is increased by 20% and its height is decreased by m% such that its area will decrease by 4%. Find m.", ("A) 10/3", "B) 20", "C) 24", "D) 80"), key="f3_t1_q5")
        
        safe_image("images/f3_t1_q19.png", width=390)
        q6 = st.radio("6. (對應試題19) $(25^{2048} \cdot 2^{2076}) / 5^{2020} =$ ", ("A) 50^4124 / 5^2020", "B) 25^56 · 2^2076", "C) 10^2076", "D) 10^2104"), key="f3_t1_q6")
        
        safe_image("images/f3_t1_q20.png", width=390)
        q7 = st.radio("7. (對應試題20) Mr Cheung takes out a loan at an interest rate of 20% p.a. compounded quarterly for 2 years. If he has to pay an interest of $4 000, find the amount he needs to repay, correct to nearest dollar.", ("A) $8 378", "B) $8 619", "C) $9 091", "D) $12 378"), key="f3_t1_q7")
        
        safe_image("images/f3_t1_q12.png", width=390)
        q8 = st.radio("8. (對應試題12) There are 20 questions in a test. For each correct answer m marks, for each wrong/unanswered n marks deducted. 10 correct = 20 marks, 15 correct = 60 marks. Find n.", ("A) 2", "B) 3", "C) 4", "D) 5"), key="f3_t1_q8")
        
        safe_image("images/f3_t1_q13b.png", width=390)
        q9 = st.radio("9. (對應試題13) If $-x^2 + kx + 10$ can be factorized where k is an integer, possible values of k: I. -5, II. -3, III. 9", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f3_t1_q9")
        
        safe_image("images/f3_t1_q14b.png", width=390)
        q10 = st.radio("10. (對應試題14) Factorize $-8x^2 - 28xy + 60y^2$.", ("A) (x - 5y)(2x + 3y)", "B) (x + 5y)(2x - 3y)", "C) -4(x - 5y)(2x + 3y)", "D) -4(x + 5y)(2x - 3y)"), key="f3_t1_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "A) 37 × 2^8 + 28.", 2: "D) 1100000000001_2", 3: "D) 105_10 < 1101100_2 < 1101110_2", 4: "C) $3 662", 5: "C) 24",
            6: "C) 10^2076", 7: "D) $12 378", 8: "B) 3", 9: "D) II and III only", 10: "D) -4(x + 5y)(2x - 3y)"
        }
        question_topics = {
            1: "二進制數與代數轉換", 2: "二進制數加減運算", 3: "不同進位制數值大小比較",
            4: "複利息與存款利息計算", 5: "百分比變化與面積應用", 6: "指數律與底數化簡",
            7: "貸款複利息與還款額計算", 8: "聯立方程應用題", 9: "二次多項式因式分解可能性", 10: "高級多項式因式分解"
        }

    elif "1st Exam" in exam_stage:
        st.subheader("✍️ 第二步：中三 1st Exam 校本真題級 10 題快測")
    elif "2nd Term Test" in exam_stage:
        st.subheader("✍️ 第二步：中三 2nd Term Test 校本真題級 10 題快測")
    else:
        st.subheader("✍️ 第二步：中三 2nd Exam 校本真題級 10 題快測")

st.markdown("---")

# 提交按鈕與動態計分運算
submit_btn = st.button("🚀 立即生成我的 Mock 考試預測報告！", type="primary")

if submit_btn:
    score = 0
    wrong_topics = []
    
    for q_num, correct_ans in correct_answers.items():
        if q_num in user_answers:
            if user_answers[q_num] == correct_ans:
                score += 1
            else:
                if q_num in question_topics:
                    wrong_topics.append(question_topics[q_num])
            
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
        analysis_text = f"🌟 **太棒了！** 你對 **{grade} - {exam_stage}** 嘅核心考點掌握得極之出色，絕對具備全班奪 A 嘅實力！繼續保持高水準發揮！"
    elif predicted_score >= 60:
        grade_level = "Level 4 (進步空間大 📈)"
        analysis_text = f"💡 **表現唔錯！** 你對 **{grade} - {exam_stage}** 有一定基礎，但部分進階題型仲有失手。只要針對錯題課題加強練習，好快就可以衝上 Level 5！"
    else:
        grade_level = "需加一把勁，盡快執好根基 ⚠️"
        analysis_text = f"⚠️ **需要注意！** 你在 **{grade} - {exam_stage}** 暴露出唔少根基漏洞。建議針對下方列出嘅失分弱項，盡快透過專科指導重頭鞏固起！"
        
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
        
    st.markdown("### 🔍 專業分析與建議：")
    st.markdown(analysis_text)
    
    if wrong_topics:
        st.markdown("### ⚠️ 需要加強溫習嘅弱項課題 (錯題診斷)：")
        st.markdown("以下係你今次測驗中需要重點重溫嘅數學課題：")
        for topic_item in wrong_topics:
            st.markdown(f"- ❌ {topic_item}")
    else:
        st.markdown("### 🎯 弱項診斷：")
        st.markdown("🏆 **完美滿分！** 你喺今次測驗中所有題目全部答對，冇任何失分弱項，請繼續保持！")

# 品牌宣傳區與 Facebook 專頁聯結
st.markdown("---")
st.markdown(f"### 🌟 關於 [Terry Sir 數學專科教室](https://www.facebook.com/terrysir)")
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1);">
    <p style="color: #ffffff !important; font-size: 15px; line-height: 1.6;">
        Terry Sir (香港中文大學數學系畢業)，擁有 26 年一線教學經驗。我們不只教公式，更擅長運用 <b>🧠 NLP 心理引導技巧</b> 幫孩子解開數學心結，由根基打起，重拾自信奪 A！
    </p>
    <p style="margin-top: 10px;">
        👉 歡迎瀏覽我們的 <a href="https://www.facebook.com/terrysir" target="_blank" style="color: #f39c12; font-weight: bold; text-decoration: underline;">Facebook 專頁</a> 了解更多學生成績分享與實戰心得！
    </p>
</div>
""", unsafe_allow_html=True)

# 經典綠色 WhatsApp 預約試課按鈕
whatsapp_url = "https://api.whatsapp.com/send/?phone=85292861189&text=Hello+Terry+Sir%2C+%E6%88%91%E5%89%9B%E5%89%9B%E5%96%BA%E7%B6%B2%E4%B8%8A%E5%AE%8C%E6%88%91初中Mock考試，想預約+%24150%2F1小時試課！&type=phone_number&app_absent=0"
st.markdown(f"""
<div style="text-align: center; margin-top: 25px;">
    <a href="{whatsapp_url}" target="_blank">
        <button style="background: linear-gradient(135deg, #25D366 0%, #128C7E 100%); color: white; padding: 14px 28px; font-size: 18px; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; box-shadow: 0 4px 15px rgba(0,0,0,0.3); width: 100%; transition: 0.3s;">
            📱 立即 WhatsApp 聯絡 Terry Sir 預約試課 ($150/1hr)
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #cbd5e0 !important;'>© 2026 中大數學 - <a href='https://www.facebook.com/terrysir' target='_blank' style='color: #f39c12; text-decoration: none;'>Terry Sir</a> - 中學數學專科. All Rights Reserved.</p>", 
    unsafe_allow_html=True
)
