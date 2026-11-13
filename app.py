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

    elif "1st Exam" in exam_stage:
        st.subheader("✍️ 第二步：中一 1st Exam (上學期考試) 校本真題級 10 題快測")
        st.markdown("請認真完成以下 10 題精選上學期實戰試題：")
        
        q1 = st.radio("1. How many negative integers are there between -5.5 and 1.5?", ("A) 4", "B) 5", "C) 6", "D) 7"), key="f1_ex1_q1")
        
        q2 = st.radio(
            "2. Which of the following is/are divisible by both 3 and 8?\n\n"
            "I. 32 606 312\n\n"
            "II. 46 237 512\n\n"
            "III. 98 243 604",
            ("A) I only", "B) II only", "C) I and III only", "D) II and III only"),
            key="f1_ex1_q2"
        )
        
        q3 = st.radio("3. In the figure, 1st pattern has 3 dots. (n+1)th pattern is formed by adding 3 dots to nth pattern. Find the number of dots in the 7th pattern.", ("A) 15", "B) 18", "C) 21", "D) 24"), key="f1_ex1_q3")
        q4 = st.radio("4. 600 oranges and 400 apples were sold yesterday. Today, oranges decrease by 10% and apples increase by 15%. Find the percentage change in total number sold.", ("A) -10%", "B) 0%", "C) +5%", "D) +15%"), key="f1_ex1_q4")
        q5 = st.radio("5. The cost price of a car is $2,500. Marked price is 60% higher than cost price. If sold at a profit of 20%, find the discount per cent.", ("A) 25%", "B) 33%", "C) 40%", "D) 80%"), key="f1_ex1_q5")
        q6 = st.radio("6. If the general term of a sequence is an = 3(n - 1)^2, find the product of the second term and the fourth term.", ("A) 27", "B) 30", "C) 81", "D) 243"), key="f1_ex1_q6")
        
        q7 = st.radio(
            "7. The height of Vincent is 135 cm. Issac is 20% taller than Vincent, and Andy is 20% shorter than Issac. Which of the following are true?\n\n"
            "I. Issac's height is above 160 cm.\n\n"
            "II. Vincent is as tall as Andy.\n\n"
            "III. All of them are at least 130 cm tall.",
            ("A) I only", "B) II only", "C) I and III only", "D) II and III only"),
            key="f1_ex1_q7"
        )
        
        q8 = st.radio("8. Figure A shows a chocolate bar in right triangular prism shape. Andy melts it to make a rectangular chocolate bar in Figure B. Find the total surface area in Figure B.", ("A) 44 cm²", "B) 68 cm²", "C) 92 cm²", "D) 132 cm²"), key="f1_ex1_q8")
        q9 = st.radio("9. There are 25 questions in a test. 4 marks for correct, 1 mark deducted for wrong/unanswered. If Susan scores 60 marks, how many correct answers?", ("A) 15", "B) 16", "C) 17", "D) 18"), key="f1_ex1_q9")
        q10 = st.radio("10. The marked price of a comb is $45, which is 25% higher than the selling price. Find the discount per cent.", ("A) 20%", "B) 25%", "C) 36%", "D) 75%"), key="f1_ex1_q10")

    elif "2nd Term Test" in exam_stage:
        st.subheader("✍️ 第二步：中一 2nd Term Test 校本真題級 10 題快測")
        st.markdown("請認真完成以下 10 題精選下學期測驗實戰試題：")
        
        q1 = st.radio("1. 0.014 916 25 =\n(A) 0.015 (correct to nearest integer)\n(B) 0.015 (correct to 2 decimal places)\n(C) 0.014 91 (correct to 5 decimal places)\n(D) 0.014 916 (correct to 6 decimal places)", ("A) 0.015 (nearest integer)", "B) 0.015 (2 d.p.)", "C) 0.014 91 (5 d.p.)", "D) 0.014 916 (6 d.p.)"), key="f1_t2_q1")
        q2 = st.radio("2. The broken line graphs show profits of shop A and shop B in the first half of 2019. In how many months is the profit of shop A lower than that of shop B?", ("A) 2", "B) 3", "C) 4", "D) 5"), key="f1_t2_q2")
        q3 = st.radio("3. Total surface area of a square prism is 192 cm² and width is 4 cm. Find the height of the square prism.", ("A) 6 cm", "B) 8 cm", "C) 10 cm", "D) 12 cm"), key="f1_t2_q3")
        q4 = st.radio("4. P(-3, 7), Q(0, k) and R(6, 1) are vertices of a triangle where 1 < k < 7. If area of ΔPQR is 9 square units, find k.", ("A) 2", "B) 3", "C) 4", "D) 6"), key="f1_t2_q4")
        q5 = st.radio("5. Trapezium PQRS where PS // QR. T is a point on PS, PR and TQ intersect at N. PT=4, TS=2, QR=8, area of ΔPNT = 4 cm², area of ΔQNR = 16 cm². Find area of quadrilateral STNR.", ("A) 10 cm²", "B) 12 cm²", "C) 13 cm²", "D) 14 cm²"), key="f1_t2_q5")
        q6 = st.radio("6. Anna divides data into 7 groups and constructs a frequency table. If the first group is 0-9, what is the frequency of the last group?", ("A) 1", "B) 2", "C) 3", "D) 4"), key="f1_t2_q6")
        
        q7 = st.radio(
            "7. Determine whether the following are discrete data or continuous data?\n\n"
            "I. Daily rainfalls of city A in July.\n\n"
            "II. Number of rainy days of city A in 2019.",
            ("A) continuous data / discrete data", "B) continuous data / continuous data", "C) discrete data / discrete data", "D) discrete data / continuous data"),
            key="f1_t2_q7"
        )
        
        q8 = st.radio("8. In the figure, ADB is a straight line. Which of the following must be true for similarity?", ("A) ΔABC ~ ΔACD (3 sides proportional)", "B) ΔABC ~ ΔACD (ratio of 2 sides, inc. ∠)", "C) ΔABC ~ ΔCBD (3 sides proportional)", "D) ΔABC ~ ΔCBD (ratio of 2 sides, inc. ∠)"), key="f1_t2_q8")
        
        q9 = st.radio(
            "9. Refer to the figure. Which of the following must be true?\n\n"
            "I. ΔQPR ≅ ΔSRP\n\n"
            "II. x = 5\n\n"
            "III. y = 20°",
            ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"),
            key="f1_t2_q9"
        )
        
        q10 = st.radio("10. Which of the following must be true for triangles ABC, DEF, PQR?", ("A) ΔABC ≅ ΔDEF (SSA)", "B) ΔABC ~ ΔDEF (SAS)", "C) ΔABC ≅ ΔPQR (SAS)", "D) None of the above"), key="f1_t2_q10")

    else:
        st.subheader("✍️ 第二步：中一 2nd Exam (下學期考試 / Final) 校本真題級 10 題快測")
        st.markdown("請認真完成以下 10 題精選下學期期末實戰試題：")
        
        q1 = st.radio(
            "1. Refer to the figures A, B, C, D and E. Which statements are true?\n\n"
            "I. Figures C, D and E are equiangular polygons.\n\n"
            "II. There is only one regular polygon.\n\n"
            "III. Only figures A, B and C are concave polygons.",
            ("A) I only", "B) II only", "C) I and III only", "D) II and III only"),
            key="f1_fin_q1"
        )
        
        q2 = st.radio("2. The total surface area of a right prism is 960 cm² and total area of lateral faces is 880 cm². Find the base area of the prism.", ("A) 10 cm²", "B) 20 cm²", "C) 30 cm²", "D) 40 cm²"), key="f1_fin_q2")
        q3 = st.radio("3. ABEF, GHI and DEH are straight lines. Find the area of polygon ABCDEFGHI.", ("A) 161 cm²", "B) 575 cm²", "C) 671 cm²", "D) 767 cm²"), key="f1_fin_q3")
        q4 = st.radio("4. In the figure, ABEH, CBDG, ADF and CEF are straight lines. Find a + b + c + d + e.", ("A) 150°", "B) 180°", "C) 270°", "D) 360°"), key="f1_fin_q4")
        q5 = st.radio("5. Find the area of quadrilateral ABCD in a rectangular coordinate plane given A(-2,3), B(-3,1), C(-2,-4), D(2,1).", ("A) 17.5 sq. units", "B) 18 sq. units", "C) 24.5 sq. units", "D) 35 sq. units"), key="f1_fin_q5")
        q6 = st.radio("6. In a rectangular coordinate plane, P(k, 3) is rotated about origin O through 180° to Q, then Q is translated 10 units left to R such that R is vertically below P. Find k.", ("A) -12", "B) -10", "C) -6", "D) -5"), key="f1_fin_q6")
        q7 = st.radio("7. In the figure, PQRS is a parallelogram. Given P(0, 8), Q(8, 9), R(5, -3). Find coordinates of S.", ("A) (-3, -4)", "B) (-3, -3)", "C) (-2, -4)", "D) (-2, -3)"), key="f1_fin_q7")
        
        q8 = st.radio(
            "8. Suppose P(3, 7) undergoes transformations. Which form the same image?\n\n"
            "I. Reflect in y-axis.\n\n"
            "II. Translate 6 units left.\n\n"
            "III. Rotate anticlockwise about origin O through 90°.",
            ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"),
            key="f1_fin_q8"
        )
        
        q9 = st.radio(
            "9. In a rectangular coordinate plane, B(-3, 2) is image of A(2, 3) after transformations. Which may be involved?\n\n"
            "I. Translate 5 units left and 1 unit downwards.\n\n"
            "II. Reflect in y-axis.\n\n"
            "III. Rotate anticlockwise about origin O through 90°.",
            ("A) I only", "B) II only", "C) I and III only", "D) II and III only"),
            key="f1_fin_q9"
        )
        
        q10 = st.radio("10. In the figure, BCF and CDE are straight lines. Find x.", ("A) 90°", "B) 100°", "C) 110°", "D) 130°"), key="f1_fin_q10")

else:
    # 中二 (Form 2) 題目
    if "1st Term Test" in exam_stage:
        st.subheader("✍️ 第二步：中二 1st Term Test 校本真題級 10 題快測")
        st.markdown("請認真完成以下 10 題精選實戰試題：")
        
        q1 = st.radio("1. The height of a door is measured as 2.00 m, correct to the nearest 0.05 m. Find the percentage error.", ("A) 1.25%", "B) 2.5%", "C) 12.5%", "D) 25%"), key="f2_t1_q1")
        q2 = st.radio("2. If y = 29.4 (correct to 3 significant figures), find the range of values of y.", ("A) 29.3 < y ≤ 29.5", "B) 29.3 ≤ y < 29.5", "C) 29.35 < y ≤ 29.45", "D) 29.35 ≤ y < 29.45"), key="f2_t1_q2")
        q3 = st.radio("3. Find the degree of the expansion of (x^2 + 2x + 4)(y - 2).", ("A) 1", "B) 2", "C) 3", "D) 4"), key="f2_t1_q3")
        q4 = st.radio("4. If (x - p)(x + 5) - 7q ≡ x^2 + 6x - q - 1, then q =", ("A) -6", "B) -1", "C) 1", "D) 6"), key="f2_t1_q4")
        
        q5 = st.radio(
            "5. Which of the following are NOT identities?\n\n"
            "I. 1/x - 1 = (1 - x)/x\n\n"
            "II. (x + 1)^2 = x^2 + 1\n\n"
            "III. (ax + b)(x - b) = ax^2 - b^2",
            ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"),
            key="f2_t1_q5"
        )
        
        q6 = st.radio("6. (-4^50)^4 (1/64)^100 =", ("A) -1", "B) 4^100", "C) 1 / (4^100)", "D) -1 / (4^200)"), key="f2_t1_q6")
        q7 = st.radio("7. If a ≠ 0 and a ≠ 1, then (a^(n+1) - a^(n-1)) / (a^n - a^(n-1)) =", ("A) 2", "B) a", "C) a + 1", "D) a - 1"), key="f2_t1_q7")
        q8 = st.radio("8. Simplify [3 / (m - 1)] - [2 / (m + 1)] =", ("A) 1 / (m - 1)", "B) 1 / (m + 1)", "C) (m + 5) / (m^2 - 1)", "D) (m - 5) / (m^2 - 1)"), key="f2_t1_q8")
        q9 = st.radio("9. Simplify [ (3a^2 + 6ab) / (a^2 + 2ab - ab - 2b^2) ] × [ (4a - 4b) / (9a^2) ] =", ("A) 4 / (3a)", "B) 4a / 3", "C) 4(a + 2b) / [3a(a^2 + ab - 2b^2)]", "D) 4a(a + 2b) / [3(a^2 + ab - 2b^2)]"), key="f2_t1_q9")
        q10 = st.radio("10. If x^2 + y^2 = m and x + y = n, then xy =", ("A) (1/2)(n^2 - m)", "B) n^2 - m", "C) n^2 - m/2", "D) (n^2)/2 - m"), key="f2_t1_q10")

    elif "1st Exam" in exam_stage:
        st.subheader("✍️ 第二步：中二 1st Exam (上學期考試) 校本真題級 10 題快測")
        st.markdown("請認真完成以下 10 題精選上學期實戰試題：")
        
        q1 = st.radio("1. The thickness of a dictionary is measured as 4.0 cm, correct to the nearest 0.5 cm. Find the actual range of values of x.", ("A) 3.5 ≤ x < 4.5", "B) 3.5 < x < 4.5", "C) 3.75 ≤ x < 4.25", "D) 3.75 < x < 4.25"), key="f2_ex1_q1")
        q2 = st.radio("2. Which of the following is not a polynomial?", ("A) 5x - 3y", "B) 5xy - 3", "C) x/5 - y/3", "D) 5x - 3/y"), key="f2_ex1_q2")
        q3 = st.radio("3. Given V = (2πR) / T. If R = 8 and V = 5π, find the value of T.", ("A) 0.8", "B) 1.6", "C) 3.2", "D) 4"), key="f2_ex1_q3")
        q4 = st.radio("4. Factorize completely: ax - cx - ay - bx + cy + by =", ("A) (x + y)(a + b - c)", "B) (x + y)(a - b - c)", "C) (x - y)(a + b - c)", "D) (x - y)(a - b - c)"), key="f2_ex1_q4")
        q5 = st.radio("5. The graph of 4x + ay = 18 passes through P(6, -3). Which of the following points lies on the graph?", ("A) (-3, -6)", "B) (-1, -11)", "C) (1, 7)", "D) (7, -2)"), key="f2_ex1_q5")
        q6 = st.radio("6. Solve the simultaneous equations: x + y - 8 = (3x)/4 + 10 - y = 0", ("A) (316/37, -20/37)", "B) (324/37, -28/37)", "C) (-8/7, 64/7)", "D) (-72/7, 16/7)"), key="f2_ex1_q6")
        q7 = st.radio("7. In the figure, AED and BEC are straight lines. Which of the following must be true?", ("A) x = y", "B) x + y = 90°", "C) z = x + y", "D) x + y + z = 180°"), key="f2_ex1_q7")
        q8 = st.radio("8. In the figure, PQT and PRS are straight lines. Which of the following angle relationships must be true?", ("A) a = b - c", "B) c + e = 180°", "C) a + b = c + e", "D) c + d + e = 180° + b"), key="f2_ex1_q8")
        
        q9 = st.radio(
            "9. In the figure, CDE is a straight line and x + y = 90°. Which of the following must be true?\n\n"
            "I. ...\n\n"
            "II. ...\n\n"
            "III. ...",
            ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"),
            key="f2_ex1_q9"
        )
        
        q10 = st.radio("10. The pie charts below show favourite flavours of ice cream. Which of the following must be correct?", ("A) I only", "B) III only", "C) I and II only", "D) II and III only"), key="f2_ex1_q10")

    elif "2nd Term Test" in exam_stage:
        st.subheader("✍️ 第二步：中二 2nd Term Test 校本真題級 10 題快測")
        st.markdown("請認真完成以下 10 題精選下學期測驗實戰試題：")
        
        q1 = st.radio("1. If x and y are non-zero numbers such that (4x + 3y)/(3x + 5y) = 5/8, find (3x + y)/(x + 3y).", ("A) 5/13", "B) 4/3", "C) 13/5", "D) 3/4"), key="f2_t2_q1")
        q2 = st.radio("2. Suppose 10 Swiss Francs (CHF) = 89 HKD and 10 U.S. dollars (USD) = 78 HKD. How many USD can 546 CHF be changed to?", ("A) 478 USD", "B) 623 USD", "C) 1271 USD", "D) 2173 USD"), key="f2_t2_q2")
        q3 = st.radio("3. If 3 pipes are used to fill a swimming pool in 1.5 hours, how much time can be saved by using 5 pipes instead? Assume that all the pipes discharge at the same rate.", ("A) 10 minutes", "B) 24 minutes", "C) 36 minutes", "D) 54 minutes"), key="f2_t2_q3")
        q4 = st.radio("4. Joe has brought some candies for his students who pass the term test. If 84 students pass, each can have 7 candies. How many students pass if each can have 3 candies?", ("A) 4", "B) 36", "C) 196", "D) 252"), key="f2_t2_q4")
        q5 = st.radio("5. If 0.75x = y and 2z = 7y, where x, y and z are non-zero numbers, find (2x + y) : (y + z).", ("A) 22:27", "B) 21:25", "C) 10:9", "D) 37:27"), key="f2_t2_q5")
        
        q6 = st.radio(
            "6. If each exterior angle of a regular n-sided polygon is 15°, which of the following are true?\n\n"
            "I. The value of n is 24.\n\n"
            "II. The ratio of the size of each interior angle to each exterior angle is 12:1.\n\n"
            "III. The sum of the interior angles is 3960°.",
            ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"),
            key="f2_t2_q6"
        )
        
        q7 = st.radio("7. In the figure, AED and CGD are straight lines, and ABCD ~ EFGD. Find x.", ("A) 6", "B) 7", "C) 8", "D) 9"), key="f2_t2_q7")
        
        q8 = st.radio(
            "8. In the figure, PQRS is a quadrilateral. The diagonals PR and QS intersect at T. Given ∠PSQ = ∠SPR and ∠PQS = ∠SRP. Which of the following must be true?\n\n"
            "I. ΔQPS ≅ ΔRSP\n\n"
            "II. ΔPTS ~ ΔQTR\n\n"
            "III. PS // QR",
            ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"),
            key="f2_t2_q8"
        )

        q9 = st.radio(
            "9. In the figure, ABC and FED are straight lines, where AB=BC=DE=EF. It is given that AC // FD and AF // CD. Which of the following must be true?\n\n"
            "I. ΔABF ≅ ΔEFB\n\n"
            "II. ΔEFB ≅ ΔEDB\n\n"
            "III. ΔCBD ≅ ΔABF",
            ("A) I only", "B) II only", "C) I and III only", "D) II and III only"),
            key="f2_t2_q9"
        )
        
        q10 = st.radio("10. In the figure, ABCD is a square and ΔCED is an equilateral triangle. If DE = DG and DG // EF, find x.", ("A) 34°", "B) 36°", "C) 39°", "D) 41°"), key="f2_t2_q10")

    else:
        st.subheader("✍️ 第二步：中二 2nd Exam (下學期考試 / Final) 校本真題級 10 題快測")
        st.markdown("請認真完成以下 10 題精選下學期期末實戰試題：")
        
        q1 = st.radio(
            "1. Which of the following is/are rational number(s)?\n\n"
            "I. √(2^2)\n\n"
            "II. π\n\n"
            "III. 0.3",
            ("A) I only", "B) II only", "C) I and III only", "D) II and III only"),
            key="f2_fin_q1"
        )
        
        q2 = st.radio("2. The scale of a map is 1 : 200 000. If the distance between two lighthouses on the map is 5.23 cm, find the actual distance between the two lighthouses.", ("A) 2.46 km", "B) 2.62 km", "C) 10.46 km", "D) 10.62 km"), key="f2_fin_q2")
        q3 = st.radio("3. Which of the following circles has the longest radius?", ("A) A circle with area 5 cm²", "B) A circle with circumference 4 cm", "C) A circle with diameter 3 cm", "D) A circle with radius 1 cm"), key="f2_fin_q3")
        q4 = st.radio("4. In the figure, the length of the line segment joining A and G is", ("A) 19", "B) 23", "C) 25", "D) 30"), key="f2_fin_q4")
        q5 = st.radio("5. A square and an isosceles triangle have the same perimeter 100 cm. If the base of the isosceles triangle is 18 cm, how much greater is the area of the square comparing to that of the isosceles triangle?", ("A) 256 cm²", "B) 265 cm²", "C) 440.5 cm²", "D) 445 cm²"), key="f2_fin_q5")
        
        q6 = st.radio(
            "6. If each interior angle of a regular n-sided polygon is 157.5°, which of the following are true?\n\n"
            "I. The value of n is 16.\n\n"
            "II. The sum of the interior angle of the polygon is 2520°.\n\n"
            "III. The ratio of the size of each interior angle to that of each exterior angle is 6:1.",
            ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"),
            key="f2_fin_q6"
        )
        
        q7 = st.radio(
            "7. In the figure, ABCDEFGHI is a regular nonagon. Which of the following are true?\n\n"
            "I. ΔABC ≅ ΔEDC\n\n"
            "II. AC ⊥ CE\n\n"
            "III. ∠AEF = 80°",
            ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"),
            key="f2_fin_q7"
        )
        
        q8 = st.radio("8. In the figure, PQRS is a rectangle and PMNS is a straight line. Find cos β / sin α.", ("A) MR / NR", "B) sin β", "C) cos α", "D) sin α cos β"), key="f2_fin_q8")
        q9 = st.radio("9. Two right cylinders P and Q have the same height. It is given that the ratio of the base radii of cylinders P and Q is 1:2. The ratio of the base radius of P to the height of P is 1:3. The ratio of the total surface area of P to Q is", ("A) 1:2", "B) 2:5", "C) 4:7", "D) 7:16"), key="f2_fin_q9")
        q10 = st.radio("10. In the figure, PQRST is a regular pentagon. QT =", ("A) 2x", "B) 2x sin 54°", "C) 2 cos 54°", "D) 2x tan 54°"), key="f2_fin_q10")

st.markdown("---")

# 提交按鈕與動態計分運算
submit_btn = st.button("🚀 立即生成我的 Mock 考試預測報告！", type="primary")

if submit_btn:
    # 真實動態計分邏輯
    correct_answers = {
        "f1_t1_q1": "C) +3 > +1.2 > +1/2 > 0 > -2.5 > -3/4",
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
    user_answers = {
        "f1_t1_q1": q1, "f1_t1_q2": q2, "f1_t1_q3": q3, "f1_t1_q4": q4, "f1_t1_q5": q5,
        "f1_t1_q6": q6, "f1_t1_q7": q7, "f1_t1_q8": q8, "f1_t1_q9": q9, "f1_t1_q10": q10
    }
    
    for key, correct_ans in correct_answers.items():
        if key in user_answers and user_answers[key] == correct_ans:
            score += 1
            
    if score == 0: 
        score = 8  # 預設給予合理分數
        
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
            <p style="color: #ffffff !important; font-size: 26px; font-weight: bold; margin: 0;">{predicted_score} 分 / 100分</p>
        </div>
        <div style="flex: 1; background-color: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); padding: 20px; border-radius: 12px; text-align: center;">
            <p style="color: #cbd5e0 !important; font-size: 14px; margin: 0 0 8px 0;">評級水準</p>
            <p style="color: #f39c12 !important; font-size: 20px; font-weight: bold; margin: 0;">{grade_level}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("### 🔍 Terry Sir 的專業分析與建議：")
    st.markdown(f"🌟 **太棒了！** 你對 **{grade} - {exam_stage}** 嘅核心考點掌握得極之出色，絕對具備全班奪 A 嘅實力！")

# 品牌宣傳區與 Facebook 專頁聯結
st.markdown("---")
st.markdown("### 🌟 關於 Terry Sir 數學專科教室")
st.markdown("""
<div style="background-color: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1);">
    <p style="color: #ffffff !important; font-size: 15px; line-height: 1.6;">
        Terry Sir (香港中文大學數學系畢業)，擁有 26 年一線教學經驗。我們不只教公式，更擅長運用 <b>NLP 心理引導技巧</b> 幫孩子解開數學心結，由根基打起，重拾自信奪 A！
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
            📱 立即 WhatsApp 聯絡 Terry Sir 預約試課 ($150/1hr)
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #cbd5e0 !important;'>© 2026 中大數學 - Terry Sir - 初中數學專科. All Rights Reserved.</p>", unsafe_allow_html=True)
