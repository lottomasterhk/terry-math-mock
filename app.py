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
grade = st.radio("請選擇你嘅年級：", ["中一 (Form 1)", "中二 (Form 2)", "中三 (Form 3)"], index=1, horizontal=True)

st.markdown("---")

user_answers = {}
correct_answers = {}
question_topics = {}

# 🔴 關鍵修復：呢度由原本寫死嘅 "中三 1st Term Test" 改為動態變數，完美跟隨你所選年級與考試階段！
st.subheader(f"✍️ 第二步：{grade} {exam_stage} 校本真題級實戰快測")
st.markdown(f"請認真完成以下精選實戰試題：")

# ==================== 嚴格巢疊條件判斷 (避免混亂) ====================

# -------------------- 中一 (Form 1) --------------------
if grade == "中一 (Form 1)":
    if "1st Term Test" in exam_stage:
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
            1: "有向數與數線大小比較 (Directed Numbers)", 2: "指數記數法與質因數分解 (Indices & Prime Factorization)",
            3: "應用題與速度距離計算 (Word Problems & Speed/Distance)", 4: "整除性與因數倍数 (Divisibility Tests)",
            5: "簡易方程應用題 (Simple Equations)", 6: "有向數嘅實際應用與平均數 (Application of Directed Numbers)",
            7: "H.C.F. 與 L.C.M. 綜合運算 (H.C.F. & L.C.M.)", 8: "有向數加減運算 (Operations of Directed Numbers)",
            9: "數列規律與一般項 (Number Sequences)", 10: "代數與年齡應用題 (Algebraic Word Problems)"
        }

    elif "1st Exam" in exam_stage:
        q1 = st.radio("1. How many negative integers are there between -5.5 and 1.5?", ("A) 4", "B) 5", "C) 6", "D) 7"), key="f1_ex1_q1")
        q2 = st.radio("2. Which of the following is/are divisible by both 3 and 8?\n\nI. 32 606 312\n\nII. 46 237 512\n\nIII. 98 243 604", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f1_ex1_q2")
        safe_image("images/f1_ex1_q3.png", width=525)
        q3 = st.radio("3. In the figure, the 1st pattern consists of 3 dots. For any positive integer n, the (n + 1)th pattern is formed by adding 3 dots to the nth pattern. Find the number of dots in the 7th pattern.", ("A) 15", "B) 18", "C) 21", "D) 24"), key="f1_ex1_q3")
        q4 = st.radio("4. 600 oranges and 400 apples were sold in a shop yesterday. Today, the number of oranges sold decreases by 10% while the number of apples sold increases by 15%. Find the percentage change in the total number of oranges and apples sold.", ("A) -10%", "B) 0%", "C) +5%", "D) +15%"), key="f1_ex1_q4")
        q5 = st.radio("5. The cost price of a car is $2 500. Its marked price is 60% higher than its cost price. If the car is sold at a profit of 20%, find the discount per cent.", ("A) 25%", "B) 33%", "C) 40%", "D) 80%"), key="f1_ex1_q5")
        q6 = st.radio("6. If the general term of a sequence is an = 3(n - 1)^2, find the product of the second term and the fourth term of the sequence.", ("A) 27", "B) 30", "C) 81", "D) 243"), key="f1_ex1_q6")
        q7 = st.radio("7. The height of Vincent is 135 cm. Issac is 20% taller than Vincent, while Andy is 20% shorter than Issac. Which of the following is/are true?\n\nI. Issac's height is above 160 cm.\n\nII. Vincent is as tall as Andy.\n\nIII. All of them are at least 130 cm tall.", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f1_ex1_q7")
        safe_image("images/f1_ex1_q8.png", width=390)
        q8 = st.radio("8. Figure A shows a chocolate bar in the shape of a right triangular prism. Andy melts it to make a rectangular chocolate bar as shown in Figure B. Find the total surface area of the chocolate bar in Figure B.", ("A) 44 cm²", "B) 68 cm²", "C) 92 cm²", "D) 132 cm²"), key="f1_ex1_q8")
        q9 = st.radio("9. There are 25 questions in a test. 4 marks are awarded for each correct answer and 1 mark is deducted for a wrong answer or an unanswered question. If Susan scores 60 marks in the test, how many correct answers does she get?", ("A) 15", "B) 16", "C) 17", "D) 18"), key="f1_ex1_q9")
        q10 = st.radio("10. The marked price of a comb is $45, which is 25% higher than the selling price. Find the discount per cent.", ("A) 20%", "B) 25%", "C) 36%", "D) 75%"), key="f1_ex1_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "B) 5", 2: "B) II only", 3: "C) 21", 4: "B) 0%", 5: "A) 25%",
            6: "C) 81", 7: "A) I only", 8: "C) 92 cm²", 9: "C) 17", 10: "A) 20%"
        }
        question_topics = {
            1: "有向數範圍與整數概念 (Negative Integers)", 2: "綜合整除性判定 (Divisibility Rules)",
            3: "圖形規律與點數計算 (Patterns & Sequences)", 4: "百分比增減與總量變化 (Percentage Changes)",
            5: "營利、標價與折扣計算 (Marked Price & Discount)", 6: "一般項與數列計算 (General Terms of Sequences)",
            7: "連鎖百分比應用 (Percentage Applications)", 8: "立體圖形體積與表面面積 (Prisms & Surface Area)",
            9: "多變量應用題與方程組 (Word Problems / Simultaneous Equations)", 10: "標價與售價百分比倒算 (Discounts & Percentages)"
        }

    elif "2nd Term Test" in exam_stage:
        safe_image("images/f1_t2_q1.png", width=525)
        q1 = st.radio("1. Refer to the figures A, B, C, D and E as shown.\n\nWhich of the following statements is/are true?\n\nI. Figures C, D and E are equiangular polygons.\n\nII. There is only one regular polygon.\n\nIII. Only figures A, B and C are concave polygons.", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f1_t2_q1")
        q2 = st.radio("2. The total surface area of a right prism is 960 cm² and the total area of its lateral faces is 880 cm². Find the base area of the prism.", ("A) 10 cm²", "B) 20 cm²", "C) 30 cm²", "D) 40 cm²"), key="f1_t2_q2")
        safe_image("images/f1_t2_q3.png", width=390)
        q3 = st.radio("3. It is given that ABEF, GHI and DEH are straight lines. Find the area of the polygon ABCDEFGHI in the figure.", ("A) 161 cm²", "B) 575 cm²", "C) 671 cm²", "D) 767 cm²"), key="f1_t2_q3")
        safe_image("images/f1_t2_q4.png", width=390)
        q4 = st.radio("4. In the figure, ABEH, CBDG, ADF and CEF are straight lines. Find a + b + c + d + e.", ("A) 150°", "B) 180°", "C) 270°", "D) 360°"), key="f1_t2_q4")
        safe_image("images/f1_t2_q5.png", width=390)
        q5 = st.radio("5. Find the area of the quadrilateral ABCD in a rectangular coordinate plane in the figure, given A(-2,3), B(-3,1), C(-2,-4), D(2,1).", ("A) 17.5 sq. units", "B) 18 sq. units", "C) 24.5 sq. units", "D) 35 sq. units"), key="f1_t2_q5")
        q6 = st.radio("6. In a rectangular coordinate plane, P(k, 3) is rotated about the origin O through 180° to a point Q, then Q is translated 10 units to the left to a point R such that R is vertically below P. Find k.", ("A) -12", "B) -10", "C) -6", "D) -5"), key="f1_t2_q6")
        safe_image("images/f1_t2_q7.png", width=390)
        q7 = st.radio("7. In the figure, PQRS is a parallelogram. Given P(0, 8), Q(8, 9), R(5, -3). Find the coordinates of S.", ("A) (-3, -4)", "B) (-3, -3)", "C) (-2, -4)", "D) (-2, -3)"), key="f1_t2_q7")
        q8 = st.radio("8. Suppose a point P(3, 7) undergoes the following transformations respectively. Which of the following transformation can form the same image?\n\nI. Reflect in the y-axis.\n\nII. Translate 6 units to the left.\n\nIII. Rotate anticlockwise about the origin O through 90°.", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f1_t2_q8")
        safe_image("images/f1_t2_q9.png", width=390)
        q9 = st.radio("9. In a rectangular coordinate plane, B(-3, 2) is the image of A(2, 3) after transformations. Which of the following may be the transformation(s) involved?\n\nI. Translate 5 units to the left and then 1 unit downwards.\n\nII. Reflect in the y-axis.\n\nIII. Rotate anticlockwise about the origin O through 90°.", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f1_t2_q9")
        safe_image("images/f1_t2_q10.png", width=390)
        q10 = st.radio("10. In the figure, BCF and CDE are straight lines. Find x.", ("A) 90°", "B) 100°", "C) 110°", "D) 130°"), key="f1_t2_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "D) II and III only", 2: "D) 40 cm²", 3: "B) 575 cm²", 4: "B) 180°", 5: "A) 17.5 sq. units",
            6: "B) -10", 7: "A) (-3, -4)", 8: "B) I and III only", 9: "C) I and III only", 10: "C) 110°"
        }
        question_topics = {
            1: "多邊形認識 (Polygons: Convex & Concave)", 2: "直棱柱表面面積計算 (Prisms Surface Area)",
            3: "複合圖形面積計算 (Composite Areas)", 4: "多邊形內角與外角 (Angles of Polygons)",
            5: "坐標平面幾何與圖形面積 (Coordinate Geometry & Areas)", 6: "坐標平移與旋轉變換 (Transformations in Coordinate Plane)",
            7: "平行四邊形坐標幾何 (Parallelograms in Coordinates)", 8: "坐標平面幾何變換 (Geometric Transformations)",
            9: "複合坐標變換 (Compound Coordinate Transformations)", 10: "直線角與三角形內角 (Angles and Lines)"
        }

    else:
        q1 = st.radio("1. The total surface area of a square prism is 192 cm² and its width is 4 cm. Find the height of the square prism.", ("A) 6 cm", "B) 8 cm", "C) 10 cm", "D) 12 cm"), key="f1_fin_q1")
        q2 = st.radio("2. P(-3, 7), Q(0, k) and R(6, 1) are the vertices of a triangle in a rectangular coordinate plane where 1 < k < 7. If the area of ΔPQR is 9 square units, find k.", ("A) 2", "B) 3", "C) 4", "D) 6"), key="f1_fin_q2")
        safe_image("images/f1_fin_q3.png", width=390)
        q3 = st.radio("3. The figure below shows a trapezium PQRS where PS // QR. T is a point on PS. PR and TQ intersect at N. It is given that the lengths of PT, TS and QR are 4 cm, 2 cm and 8 cm respectively and the areas of ΔPNT and ΔQNR are 4 cm² and 16 cm² respectively. Find the area of the quadrilateral STNR.", ("A) 10 cm²", "B) 12 cm²", "C) 13 cm²", "D) 14 cm²"), key="f1_fin_q3")
        q4 = st.radio("4. Anna divides the following data into 7 groups and constructs a frequency distribution table. If the first group is 0 - 9, what is the frequency of the last group in the table?\n\n8, 28, 54, 50, 60, 22, 34, 14, 55, 12\n14, 28, 6, 12, 15, 59, 66, 29, 4, 64", ("A) 1", "B) 2", "C) 3", "D) 4"), key="f1_fin_q4")
        q5 = st.radio("5. 0.014 916 25 =", ("A) 0.015 (correct to the nearest integer)", "B) 0.015 (correct to 2 decimal places)", "C) 0.014 91 (correct to 5 decimal places)", "D) 0.014 916 (correct to 6 decimal places)"), key="f1_fin_q5")
        safe_image("images/f1_fin_q6.png", width=390)
        q6 = st.radio("6. The broken line graphs below show the profits of shop A and shop B in the first half of 2019.\n\nIn how many months is the profit of shop A lower than that of shop B?", ("A) 2", "B) 3", "C) 4", "D) 5"), key="f1_fin_q6")
        q7 = st.radio("7. Determine whether the following are discrete data or continuous data?\n\nI. The daily rainfalls of city A in July.\n\nII. The number of rainy days of city A in 2019.", ("A) continuous data / discrete data", "B) continuous data / continuous data", "C) discrete data / discrete data", "D) discrete data / continuous data"), key="f1_fin_q7")
        safe_image("images/f1_fin_q8.png", width=390)
        q8 = st.radio("8. In the figure, ADB is a straight line. Which of the following must be true?", ("A) ΔABC ~ ΔACD (3 sides proportional)", "B) ΔABC ~ ΔACD (ratio of 2 sides, inc. ∠)", "C) ΔABC ~ ΔCBD (3 sides proportional)", "D) ΔABC ~ ΔCBD (ratio of 2 sides, inc. ∠)"), key="f1_fin_q8")
        safe_image("images/f1_fin_q9.png", width=390)
        q9 = st.radio("9. Refer to the figure. Which of the following must be true?\n\nI. ΔQPR ≅ ΔSRP\n\nII. x = 5\n\nIII. y = 20°", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f1_fin_q9")
        safe_image("images/f1_fin_q10.png", width=390)
        q10 = st.radio("10. Which of the following must be true?", ("A) ΔABC ≅ ΔDEF (SSA)", "B) ΔABC ≅ ΔDEF (SAS)", "C) ΔABC ≅ ΔPQR (SAS)", "D) None of the above"), key="f1_fin_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "C) 10 cm", 2: "B) 3", 3: "D) 14 cm²", 4: "C) 3", 5: "D) 0.014 916 (correct to 6 decimal places)",
            6: "B) 3", 7: "A) continuous data / discrete data", 8: "D) ΔABC ~ ΔCBD (ratio of 2 sides, inc. ∠)", 9: "D) I, II and III", 10: "C) ΔABC ≅ ΔPQR (SAS)"
        }
        question_topics = {
            1: "正方棱柱體積與表面積 (Square Prisms)", 2: "坐標平面三角形面積反算 (Triangle Areas in Coordinates)",
            3: "相似三角形與梯形面積比例 (Similar Triangles & Trapeziums)", 4: "頻數分佈表與數據整理 (Frequency Distributions)",
            5: "有效數字與四捨五入 (Significant Figures & Rounding)", 6: "折線圖數據分析 (Broken Line Graphs)",
            7: "離散數據與連續數據辨別 (Discrete vs Continuous Data)", 8: "相似三角形判定 (Similar Triangles)",
            9: "全等三角形與幾何推論 (Congruent Triangles)", 10: "三角形全等條件辨別 (Conditions for Triangle Congruence)"
        }


# -------------------- 中二 (Form 2) --------------------
elif grade == "中二 (Form 2)":
    if "1st Term Test" in exam_stage:
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
            1: "誤差與百分誤差計算 (Percentage Errors)", 2: "有效數字與數值範圍 (Significant Figures & Ranges)",
            3: "多項式展開與次方次數 (Polynomial Expansions & Degrees)", 4: "恆等式系數比較法 (Polynomial Identities)",
            5: "恆等式概念辨別 (Identities vs Equations)", 6: "指數定律與化簡 (Laws of Indices)",
            7: "指數化簡與分式運算 (Algebraic Fractions with Indices)", 8: "分式加減法運算 (Addition/Subtraction of Rational Expressions)",
            9: "分式乘法與因式分解 (Multiplication of Algebraic Fractions)", 10: "代數恆等式與完全平方公式 (Algebraic Identities & Formulas)"
        }

    elif "1st Exam" in exam_stage:
        q1 = st.radio("1. The thickness of a dictionary is measured as 4.0 cm, correct to the nearest 0.5 cm. Let x cm be the actual thickness of the dictionary. Find the range of values of x.", ("A) 3.5 ≤ x < 4.5", "B) 3.5 < x < 4.5", "C) 3.75 ≤ x < 4.25", "D) 3.75 < x < 4.25"), key="f2_ex1_q1")
        q2 = st.radio("2. Which of the following is not a polynomial?", ("A) 5x - 3y", "B) 5xy - 3", "C) x/5 - y/3", "D) 5x - 3/y"), key="f2_ex1_q2")
        q3 = st.radio("3. It is given that V = (2πR) / T. If R = 8 and V = 5π, find the value of T.", ("A) 0.8", "B) 1.6", "C) 3.2", "D) 4"), key="f2_ex1_q3")
        q4 = st.radio("4. Factorize completely: ax - cx - ay - bx + cy + by =", ("A) (x + y)(a + b - c)", "B) (x + y)(a - b - c)", "C) (x - y)(a + b - c)", "D) (x - y)(a - b - c)"), key="f2_ex1_q4")
        q5 = st.radio("5. The graph of the equation 4x + ay = 18 passes through P(6, -3), where a is a constant. Which of the following points lies on the graph of the given equation?", ("A) (-3,-6)", "B) (-1,-11)", "C) (1,7)", "D) (7,-2)"), key="f2_ex1_q5")
        q6 = st.radio("6. Solve the simultaneous equations x + y - 8 = (3x)/4 + 10 - y = 0 .", ("A) (316/37, -20/37)", "B) (324/37, -28/37)", "C) (-8/7, 64/7)", "D) (-72/7, 16/7)"), key="f2_ex1_q6")
        safe_image("images/f2_ex1_q7.png", width=390)
        q7 = st.radio("7. In the figure, AED and BEC are straight lines. Which of the following must be true?", ("A) x = y", "B) x + y = 90°", "C) z = x + y", "D) x + y + z = 180°"), key="f2_ex1_q7")
        safe_image("images/f2_ex1_q8.png", width=390)
        q8 = st.radio("8. In the figure, PQT and PRS are straight lines. Which of the following must be true?", ("A) a = b - c", "B) c + e = 180°", "C) a + b = c + e", "D) c + d + e = 180° + b"), key="f2_ex1_q8")
        safe_image("images/f2_ex1_q9.png", width=390)
        q9 = st.radio("9. In the figure, CDE is a straight line and x + y = 90°. Which of the following must be true?\n\nI. AB // CE\n\nII. AC ⊥ AD\n\nIII. x = y", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f2_ex1_q9")
        safe_image("images/f2_ex1_q10.png", width=390)
        q10 = st.radio("10. The pie charts below show the favourite flavours of ice cream voted by customers of shop A and shop B respectively.\n\nWhich of the following must be correct?\n\nI. The number of customers of shop A who vote peach flavour is more than that of shop B.\n\nII. In both shop A and shop B, peach flavour is more popular than strawberry flavour.\n\nIII. The percentages of customers who vote almond flavour in shop A and shop B are the same.", ("A) I only", "B) III only", "C) I and II only", "D) II and III only"), key="f2_ex1_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "C) 3.75 ≤ x < 4.25", 2: "D) 5x - 3/y", 3: "D) 4", 4: "D) (x - y)(a - b - c)", 5: "C) (1,7)",
            6: "C) (-8/7, 64/7)", 7: "C) z = x + y", 8: "C) a + b = c + e", 9: "A) I and II only", 10: "D) II and III only"
        }
        question_topics = {
            1: "量度極限與誤差範圍 (Measurement Limits & Limits of Accuracy)", 2: "多項式概念與辨別 (Polynomial Concepts)",
            3: "公式換算與主項變換 (Formula Manipulation)", 4: "進階因式分解技巧 (Advanced Factorization)",
            5: "直線方程與坐標代入 (Linear Equations & Graphs)", 6: "二元一次方程組求解 (Simultaneous Linear Equations)",
            7: "直線與角關係 (Angles and Lines)", 8: "三角形外角與內角和 (Exterior Angle Theorem of Triangles)",
            9: "平行線與垂直線性質 (Parallel & Perpendicular Lines)", 10: "扇形圖與百分比誤區 (Pie Charts & Statistical Misconceptions)"
        }

    elif "2nd Term Test" in exam_stage:
        q1 = st.radio("1. If x and y are non-zero numbers such that (4x + 3y)/(3x + 5y) = 5/8, then (3x + y)/(x + 3y) =", ("A) 5/13", "B) 1.", "C) 4/3", "D) 13/5"), key="f2_t2_q1")
        q2 = st.radio("2. Suppose 10 Swiss Francs dollars (CHF) are equivalent to 89 H.K. dollars (HKD) and 10 U.S. dollars (USD) are equivalent to 78 HKD. How many USD can 546 CHF be changed to?", ("A) 478 USD", "B) 623 USD", "C) 1271 USD", "D) 2173 USD"), key="f2_t2_q2")
        q3 = st.radio("3. If 3 pipes are used to fill a swimming pool in 1.5 hour, how much time can be saved by using 5 pipes instead? Assume that all the pipes discharge at the same rate.", ("A) 10 minutes", "B) 24 minutes", "C) 36 minutes", "D) 54 minutes"), key="f2_t2_q3")
        q4 = st.radio("4. Joe has brought some candies for his students who pass the term test. If 84 students pass, each of the students can have 7 candies. How many students pass the term test if each of them can have 3 candies?", ("A) 4", "B) 36", "C) 196", "D) 252"), key="f2_t2_q4")
        q5 = st.radio("5. If 0.75x = y and 2z = 7y, where x, y and z are non-zero numbers, find (2x + y) : (y + z).", ("A) 22 : 27", "B) 21 : 25", "C) 10 : 9", "D) 37 : 27"), key="f2_t2_q5")
        q6 = st.radio("6. If each exterior angle of a regular n-sided polygon is 15°, which of the following are true ?\n\nI. The value of n is 24.\n\nII. The ratio of the size of each interior angle of the polygon to that of each exterior angle is 12 : 1.\n\nIII. The sum of the interior angles of the polygon is 3960°.", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f2_t2_q6")
        safe_image("images/f2_t2_q7.png", width=390)
        q7 = st.radio("7. In the figure, AED and CGD are straight lines, and ABCD ~ EFGD. Find x.", ("A) 6", "B) 7", "C) 8", "D) 9"), key="f2_t2_q7")
        safe_image("images/f2_t2_q8.png", width=390)
        q8 = st.radio("8. In the figure, PQRS is a quadrilateral. The diagonals PR and QS intersect at T. It is given that ∠PSQ = ∠SPR and ∠PQS = ∠SRP. Which of the following must be true?\n\nI. Deduce ΔQPS ≅ ΔRSP\n\nII. ΔPTS ~ ΔQTR\n\nIII. PS // QR", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f2_t2_q8")
        safe_image("images/f2_t2_q9.png", width=390)
        q9 = st.radio("9. In the figure, ABC and FED are straight lines, where AB = BC = DE = EF. It is given that AC // FD and AF // CD. Which of the following must be true?\n\nI. ΔABF ≅ ΔEFB\n\nII. ΔEFB ≅ ΔEDB\n\nIII. ΔCBD ≅ ΔABF", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f2_t2_q9")
        safe_image("images/f2_t2_q10.png", width=390)
        q10 = st.radio("10. In the figure, ABCD is a square and ΔCED is an equilateral triangle. If DE = DG and DG // EF, find x.", ("A) 34°", "B) 36°", "C) 39°", "D) 41°"), key="f2_t2_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "D) 13/5", 2: "B) 623 USD", 3: "C) 36 minutes", 4: "D) 252", 5: "B) 21 : 25",
            6: "B) I and III only", 7: "D) 9", 8: "D) I, II and III", 9: "C) I and III only", 10: "B) 36°"
        }
        question_topics = {
            1: "比與率及分式代數化簡 (Ratios & Fractions)", 2: "外幣找換與比例應用 (Currency Conversions)",
            3: "正比例與反比例應用題 (Direct & Inverse Proportions)", 4: "變分與極端比例應用 (Variation & Proportions)",
            5: "連比運算與化簡 (Chain Ratios)", 6: "多邊形內角外角綜合計算 (Polygon Angle Properties)",
            7: "相似圖形與邊長比例 (Similar Figures & Ratios)", 8: "相似三角形與全等三角形綜合 (Similar & Congruent Triangles)",
            9: "圖形全等與平行線性質 (Congruence & Parallel Lines)", 10: "正方形與等邊三角形幾何綜合 (Squares & Equilateral Triangles)"
        }

    else:
        q1 = st.radio("1. Which of the following is/are rational number(s)?\n\nI. √(2^2)\n\nII. π\n\nIII. 0.3", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f2_fin_q1")
        q2 = st.radio("2. The scale of a map is 1 : 200 000. If the distance between two lighthouses on the map is 5.23 cm, find the actual distance between the two lighthouses.", ("A) 2.46 km", "B) 2.62 km", "C) 10.46 km", "D) 10.62 km"), key="f2_fin_q2")
        q3 = st.radio("3. Which of the following circles has the longest radius?", ("A) A circle with area 5 cm²", "B) A circle with circumference 4 cm", "C) A circle with diameter 3 cm", "D) A circle with radius 1 cm"), key="f2_fin_q3")
        safe_image("images/f2_fin_q4.png", width=390)
        q4 = st.radio("4. In the figure, the length of the line segment joining A and G is", ("A) 19", "B) 23", "C) 25", "D) 30"), key="f2_fin_q4")
        q5 = st.radio("5. A square and an isosceles triangle have the same perimeter 100 cm. If the base of the isosceles triangle is 18 cm, how much greater is the area of the square comparing to that of the isosceles triangle?", ("A) 256 cm²", "B) 265 cm²", "C) 440.5 cm²", "D) 445 cm²"), key="f2_fin_q5")
        q6 = st.radio("6. If each interior angle of a regular n-sided polygon is 157.5°, which of the following are true?\n\nI. The value of n is 16.\n\nII. The sum of the interior angle of the polygon is 2520°.\n\nIII. The ratio of the size of each interior angle to that of each exterior angle is 6:1.", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f2_fin_q6")
        safe_image("images/f2_fin_q7.png", width=390)
        q7 = st.radio("7. In the figure, ABCDEFGHI is a regular nonagon. Which of the following are true?\n\nI. ΔABC ≅ ΔEDC\n\nII. AC ⊥ CE\n\nIII. ∠AEF = 80°", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f2_fin_q7")
        safe_image("images/f2_fin_q8.png", width=390)
        q8 = st.radio("8. In the figure, PQRS is a rectangle and PMNS is a straight line. Find cos β / sin α .", ("A) MR / NR", "B) sin β", "C) cos α", "D) sin α cos β"), key="f2_fin_q8")
        q9 = st.radio("9. Two right cylinders P and Q have the same height. It is given that the ratio of the base radii of cylinders P and Q is 1:2. The ratio of the base radius of P to the height of P is 1:3. The ratio of the total surface area of P to Q is", ("A) 1:2", "B) 2:5", "C) 4:7", "D) 7:16"), key="f2_fin_q9")
        safe_image("images/f2_fin_q10.png", width=390)
        q10 = st.radio("10. In the figure, PQRST is a regular pentagon. QT =", ("A) 2x", "B) 2x sin 54°", "C) 2 cos 54°", "D) 2x tan 54°"), key="f2_fin_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "C) I and III only", 2: "C) 10.46 km", 3: "A) A circle with area 5 cm²", 4: "C) 25", 5: "D) 445 cm²",
            6: "D) I, II and III", 7: "D) I, II and III", 8: "A) MR / NR", 9: "D) 7:16", 10: "B) 2x sin 54°"
        }
        question_topics = {
            1: "有理數與無理數概念 (Rational & Irrational Numbers)", 2: "地圖比例尺與實際距離換算 (Map Scales & Actual Distances)",
            3: "圓面積、周界與半徑關係 (Circle Areas and Circumference)", 4: "直角坐標系與距離公式 (Coordinate Geometry & Distance Formula)",
            5: "平面圖形面積綜合計算 (Areas of Polygons & Triangles)", 6: "正多邊形內角外角性質 (Properties of Regular Polygons)",
            7: "正九邊形與全等圖形綜合 (Regular Nonagons & Congruence)", 8: "三角比（正弦、餘弦）應用 (Trigonometric Ratios: Sin & Cos)",
            9: "相似形與體積表面面積比例 (Mensuration: Cylinders & Ratios)", 10: "正五邊形與三角比應用 (Regular Pentagons & Trig)"
        }


# -------------------- 中三 (Form 3) --------------------
elif grade == "中三 (Form 3)":
    if "1st Term Test" in exam_stage:
        q1 = st.radio("1. 3^246 · 9^-123 =", ("A) 1.", "B) -1.", "C) 3^123.", "D) 1 / (3^123)."), key="f3_t1_q1")
        q2 = st.radio("2. Find the smallest integer a satisfying a/5 - 1 > -4.", ("A) -24", "B) -15", "C) -14", "D) -3"), key="f3_t1_q2")
        q3 = st.radio("3. Solve the inequality (8 - 3x)/5 ≥ (5 + 2x)/2 .", ("A) x ≤ -9/16", "B) x ≤ 9/16", "C) x ≥ -9/16", "D) x ≥ 9/16"), key="f3_t1_q3")
        q4 = st.radio("4. If the growth rate of a value is 10% per month, and its value after 1 year is 2 125, find the original value correct to 3 significant figures.", ("A) 193", "B) 677", "C) 989", "D) 1920"), key="f3_t1_q4")
        q5 = st.radio("5. (x^2 - 9y^2) / y^4 ÷ (x + 3y) / y^2 =", ("A) (x + 3y) / y^6", "B) (x - 9y) / y^6", "C) (x - 3y) / y^2", "D) (x - 9y) / y^2"), key="f3_t1_q5")
        safe_image("images/f3_t1_q6.png", width=390)
        q6 = st.radio("6. In the figure, QS and RS are angle bisectors of ΔPQR. Find ∠QSR.", ("A) 100°", "B) 120°", "C) 125°", "D) 130°"), key="f3_t1_q6")
        q7 = st.radio("7. Both Isaac and Andy want to buy a radiator. Isaac chooses a radiator among brands A, B, C and D at random, while Andy chooses a radiator among brands A, B and C at random. Find the probability that they choose the same brand.", ("A) 1/12", "B) 1/6", "C) 1/4", "D) 1/3"), key="f3_t1_q7")
        safe_image("images/f3_t1_q8.png", width=390)
        q8 = st.radio("8. A bag contains 3 red cards, 2 green cards and 15 yellow cards. In a game, a card is randomly drawn from the bag and the corresponding score will be given according to the table.", ("A) 9.25", "B) 11.5", "C) 13.25", "D) 15"), key="f3_t1_q8")
        safe_image("images/f3_t1_q9.png", width=390)
        q9 = st.radio("9. The prices of items sold in a supermarket: Shower gel $41, Oats $37, Chocolate bar $28, Hand sanitizer $33, Potato chips $26. Prices are increased by 10% and then decreased by $2. Find the mean of the adjusted price.", ("A) $33.0", "B) $33.7", "C) $34.1", "D) $34.3"), key="f3_t1_q9")
        safe_image("images/f3_t1_q10.png", width=390)
        q10 = st.radio("10. In the figure, APB and AQC are straight lines. If AQ = 26, PQ = 10, QC = 22 and PB = 28, which of the following must be true?", ("A) BC is an altitude of ΔABC.", "B) BQ is an angle bisector of ΔABC.", "C) PC is a median of ΔABC.", "D) PQ is a perpendicular bisector of ΔABC."), key="f3_t1_q10")

        q11 = st.radio("11. 10010100011100₂ =", ("A) 37 × 2⁸ + 28.", "B) 37 × 2⁸ + 56.", "C) 37 × 2⁹ + 28.", "D) 37 × 2⁹ + 56."), key="f3_t1_q11")
        safe_image("images/f3_t1_q11.png", width=390)

        q12 = st.radio("12. 9 × 2¹⁰ + 6 × 2⁹ + 2³ - 7 =", ("A) 101100010000₂", "B) 110010000100₂", "C) 1011000001111₂", "D) 1100000000001₂"), key="f3_t1_q12")
        safe_image("images/f3_t1_q12.png", width=390)

        q13 = st.radio("13. Arrange the three numbers 1101100₂, 105₁₀ and 1101110₂ in ascending order.", ("A) 1101110₂ < 105₁₀ < 1101100₂", "B) 1101100₂ < 105₁₀ < 1101110₂", "C) 105₁₀ < 1101110₂ < 1101100₂", "D) 105₁₀ < 1101100₂ < 1101110₂"), key="f3_t1_q13")
        safe_image("images/f3_t1_q13.png", width=390)

        q14 = st.radio("14. A sum of $35 000 is deposited for 40 months at an interest rate of 3% p.a. compounded every four months. Find the interest, correct to the nearest dollar.", ("A) $1 180", "B) $2 715", "C) $3 662", "D) $4 966"), key="f3_t1_q14")
        safe_image("images/f3_t1_q14.png", width=390)

        q15 = st.radio("15. If the base of a triangle is increased by 20% and its height is decreased by m% such that its area will decrease by 4%. Find m.", ("A) 10/3", "B) 20", "C) 24", "D) 80"), key="f3_t1_q15")
        safe_image("images/f3_t1_q15.png", width=390)

        q16 = st.radio("16. (25²⁰⁴⁸ · 2²⁰⁷⁶) / 5²⁰²⁰ =", ("A) 50⁴¹²⁴ / 5²⁰²⁰", "B) 25⁵⁶ · 2²⁰⁷⁶", "C) 10²⁰⁷⁶", "D) 10²¹⁰⁴"), key="f3_t1_q16")
        safe_image("images/f3_t1_q16.png", width=390)

        q17 = st.radio("17. Mr Cheung takes out a loan at an interest rate of 20% p.a. compounded quarterly for 2 years. If he has to pay an interest of $4 000, find the amount he needs to repay, correct to nearest dollar.", ("A) $8 378", "B) $8 619", "C) $9 091", "D) $12 378"), key="f3_t1_q17")
        safe_image("images/f3_t1_q17.png", width=390)

        q18 = st.radio("18. There are 20 questions in a test. For each correct answer, m marks will be given. For each unanswered or wrongly answered question, n marks will be deducted. If 10 questions are answered correctly, a student will get 20 marks. If 15 questions are answered correctly, a student will get 60 marks. Find n.", ("A) 2", "B) 3", "C) 4", "D) 5"), key="f3_t1_q18")
        safe_image("images/f3_t1_q18.png", width=390)

        q19 = st.radio("19. If -x² + kx + 10 can be factored where k is an integer, which of the following is/are possible value(s) of k? I. -5, II. -3, III. 9", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f3_t1_q19")
        safe_image("images/f3_t1_q19.png", width=390)

        q20 = st.radio("20. Factorize -8x² - 28xy + 60y².", ("A) (x - 5y)(2x + 3y)", "B) (x + 5y)(2x - 3y)", "C) -4(x - 5y)(2x + 3y)", "D) -4(x + 5y)(2x - 3y)"), key="f3_t1_q20")
        safe_image("images/f3_t1_q20.png", width=390)

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20}
        correct_answers = {
            1: "A) 1.", 2: "C) -14", 3: "A) x ≤ -9/16", 4: "B) 677", 5: "C) (x - 3y) / y^2",
            6: "D) 130°", 7: "C) 1/4", 8: "A) 9.25", 9: "D) $34.3", 10: "A) BC is an altitude of ΔABC.",
            11: "A) 37 × 2⁸ + 28.", 12: "D) 1100000000001₂", 13: "D) 105₁₀ < 1101100₂ < 1101110₂", 14: "C) $3 662", 15: "C) 24",
            16: "C) 10²⁰⁷⁶", 17: "D) $12 378", 18: "B) 3", 19: "D) II and III only", 20: "D) -4(x + 5y)(2x - 3y)"
        }
        question_topics = {
            1: "指數定律與化簡 (Laws of Indices)", 2: "一元一次不等式應用 (Linear Inequalities)", 3: "代數不等式求解 (Solving Inequalities)", 4: "複利息與增長率計算 (Growth Rate & Compound Interest)", 5: "分式化簡與因式分解 (Algebraic Fractions)", 6: "三角形內角與角平分線 (Angle Bisectors of Triangles)", 7: "獨立事件概率計算 (Probability of Independent Events)", 8: "數學期望值計算 (Expected Value)", 9: "平均數與百分比調整 (Means & Percentage Adjustments)", 10: "相似三角形與幾何推論 (Geometry Proofs & Similar Triangles)",
            11: "二進制數與代數轉換 (Binary Numbers)", 12: "二進制數加減運算 (Binary Arithmetic)", 13: "不同進位制數值大小比較 (Number Bases Comparison)", 14: "複利息與存款利息計算 (Compound Interest)", 15: "百分比變化與面積應用 (Percentage Change in Area)", 16: "指數律與底數化簡 (Laws of Indices)", 17: "貸款複利息與還款額計算 (Loans & Compound Interest)", 18: "聯立方程應用題 (Simultaneous Equations)", 19: "二次多項式因式分解可能性 (Factorization of Quadratics)", 20: "高級多項式因式分解 (Advanced Factorization)"
        }

    elif "1st Exam" in exam_stage:
        safe_image("images/f3_ex1_q1.png", width=390)
        q1 = st.radio("1. 10010100011100_2 =", ("A) 37 × 2^8 + 28.", "B) 37 × 2^8 + 56.", "C) 37 × 2^9 + 28.", "D) 37 × 2^9 + 56."), key="f3_ex1_q1")
        safe_image("images/f3_ex1_q2.png", width=390)
        q2 = st.radio("2. 9 × 2^10 + 6 × 2^9 + 2^3 - 7 =", ("A) 101100010000_2", "B) 110010000100_2", "C) 1011000001111_2", "D) 1100000000001_2"), key="f3_ex1_q2")
        safe_image("images/f3_ex1_q3.png", width=390)
        q3 = st.radio("3. Arrange the three numbers 1101100_2, 105_10 and 1101110_2 in ascending order.", ("A) 1101110_2 < 105_10 < 1101100_2", "B) 1101100_2 < 105_10 < 1101110_2", "C) 105_10 < 1101110_2 < 1101100_2", "D) 105_10 < 1101100_2 < 1101110_2"), key="f3_ex1_q3")
        safe_image("images/f3_ex1_q4.png", width=390)
        q4 = st.radio("4. A sum of $35 000 is deposited for 40 months at an interest rate of 3% p.a. compounded every four months. Find the interest.", ("A) $1 180", "B) $2 715", "C) $3 662", "D) $4 966"), key="f3_ex1_q4")
        safe_image("images/f3_ex1_q5.png", width=390)
        q5 = st.radio("5. If the base of a triangle is increased by 20% and its height is decreased by m% such that its area will decrease by 4%. Find m.", ("A) 10/3", "B) 20", "C) 24", "D) 80"), key="f3_ex1_q5")
        safe_image("images/f3_ex1_q6.png", width=390)
        q6 = st.radio("6. (25^2048 · 2^2076) / 5^2020 =", ("A) 50^4124 / 5^2020", "B) 25^56 · 2^2076", "C) 10^2076", "D) 10^2104"), key="f3_ex1_q6")
        safe_image("images/f3_ex1_q7.png", width=390)
        q7 = st.radio("7. Mr Cheung takes out a loan at an interest rate of 20% p.a. compounded quarterly for 2 years. If he has to pay an interest of $4 000, find the amount he needs to repay.", ("A) $8 378", "B) $8 619", "C) $9 091", "D) $12 378"), key="f3_ex1_q7")
        safe_image("images/f3_ex1_q8.png", width=390)
        q8 = st.radio("8. There are 20 questions in a test. For each correct answer m marks, for each wrong/unanswered n marks deducted. 10 correct = 20 marks, 15 correct = 60 marks. Find n.", ("A) 2", "B) 3", "C) 4", "D) 5"), key="f3_ex1_q8")
        safe_image("images/f3_ex1_q9.png", width=390)
        q9 = st.radio("9. If -x^2 + kx + 10 can be factorized where k is an integer, possible values of k: I. -5, II. -3, III. 9", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f3_ex1_q9")
        safe_image("images/f3_ex1_q10.png", width=390)
        q10 = st.radio("10. Factorize -8x^2 - 28xy + 60y^2.", ("A) (x - 5y)(2x + 3y)", "B) (x + 5y)(2x - 3y)", "C) -4(x - 5y)(2x + 3y)", "D) -4(x + 5y)(2x - 3y)"), key="f3_ex1_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "A) 37 × 2^8 + 28.", 2: "D) 1100000000001_2", 3: "D) 105_10 < 1101100_2 < 1101110_2", 4: "C) $3 662", 5: "C) 24",
            6: "C) 10^2076", 7: "D) $12 378", 8: "B) 3", 9: "D) II and III only", 10: "D) -4(x + 5y)(2x - 3y)"
        }
        question_topics = {
            1: "二進制數與代數轉換 (Binary Numbers)", 2: "二進制數加減運算 (Binary Arithmetic)",
            3: "不同進位制數值大小比較 (Number Bases Comparison)", 4: "複利息與存款利息計算 (Compound Interest)",
            5: "百分比變化與面積應用 (Percentage Change in Area)", 6: "指數律與底數化簡 (Laws of Indices)",
            7: "貸款複利息與還款額計算 (Loans & Compound Interest)", 8: "聯立方程應用題 (Simultaneous Equations)",
            9: "二次多項式因式分解可能性 (Factorization of Quadratics)", 10: "高級多項式因式分解 (Advanced Factorization)"
        }

    elif "2nd Term Test" in exam_stage:
        safe_image("images/f3_t2_q1.png", width=390)
        q1 = st.radio("1. In the figure, ABCE is a rectangle, CDEF is a rhombus. If ∠FBC = 34°, find ∠CDE.", ("A) 64°", "B) 66°", "C) 68°", "D) 70°"), key="f3_t2_q1")
        safe_image("images/f3_t2_q2.png", width=390)
        q2 = st.radio("2. Solid consists of a right circular cone and hemisphere with common base. Height = 8 cm, slant height = 10 cm. Find total surface area.", ("A) 120π cm²", "B) 132π cm²", "C) 384π cm²", "D) 204π cm²"), key="f3_t2_q2")
        safe_image("images/f3_t2_q3.png", width=390)
        q3 = st.radio("3. Simplify cos θ / tan²(90° - θ) - 1 / sin(90° - θ) .", ("A) 0", "B) 1", "C) cos θ", "D) -cos θ"), key="f3_t2_q3")
        safe_image("images/f3_t2_q4.png", width=390)
        q4 = st.radio("4. In the figure, D is a point on AC such that BD ⊥ AC. Find AB : BC given angle A = 45° and angle C = 30°.", ("A) 1 : 2", "B) √2 : 2", "C) √2 : 4", "D) 4 : √2"), key="f3_t2_q4")
        safe_image("images/f3_t2_q5.png", width=390)
        q5 = st.radio("5. ABCDEFGH is a cuboid and EACD is a pyramid. What is the ratio of the volume of the pyramid to that of the cuboid?", ("A) 1 : 2", "B) 1 : 3", "C) 1 : 4", "D) 1 : 6"), key="f3_t2_q5")
        safe_image("images/f3_t2_q6.png", width=390)
        q6 = st.radio("6. Paul deposited $65 000 at 4% p.a. compounded quarterly. What is the difference between the interest obtained in the third year and that in the second year?", ("A) $112", "B) $2 746", "C) $2 858", "D) $5 604"), key="f3_t2_q6")
        safe_image("images/f3_t2_q7.png", width=390)
        q7 = st.radio("7. Factorize 8xy - 6x^2 - 2y^2.", ("A) -2(x - y)(4x + y)", "B) -2(3x - y)(x - y)", "C) (x - y)(4x + y)", "D) (3x - y)(x - y)"), key="f3_t2_q7")
        safe_image("images/f3_t2_q8.png", width=390)
        q8 = st.radio("8. BCDE is a parallelogram. G is mid-point of CD. AG and BE intersect at F. CB produced to A so area ΔABF : area ΔACG = 4 : 9. Area ΔABF = 12 cm², find area DEFG.", ("A) 21 cm²", "B) 27 cm²", "C) 36 cm²", "D) 42 cm²"), key="f3_t2_q8")
        safe_image("images/f3_t2_q9.png", width=390)
        q9 = st.radio("9. A(2, -17) and B(14, 3) are two given points. If M is the mid-point of AB, find the coordinates of M.", ("A) (-6, -7)", "B) (-6, -10)", "C) (8, -7)", "D) (8, 10)"), key="f3_t2_q9")
        safe_image("images/f3_t2_q10.png", width=390)
        q10 = st.radio("10. Which of the following numbers is the smallest?\n\nA. -4^-4 × 10^-10\nB. (-4)^-4 × 10^-10\nC. -0.000 000 000 000 4\nD. -3 / 12^12", ("A) A", "B) B", "C) C", "D) D"), key="f3_t2_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "C) 68°", 2: "B) 132π cm²", 3: "D) -cos θ", 4: "B) √2 : 2", 5: "D) 1 : 6",
            6: "A) $112", 7: "B) -2(3x - y)(x - y)", 8: "A) 21 cm²", 9: "C) (8, -7)", 10: "C) C"
        }
        question_topics = {
            1: "四邊形性質：矩形與菱形 (Rectangles & Rhombuses)", 2: "立體圖形：圓錐與半球表面面積 (Surface Area of Composite Solids)",
            3: "三角恆等式與轉角公式 (Trigonometric Identities)", 4: "解三角形與三角比應用 (Solution of Triangles)",
            5: "立體圖形體積比例 (Volumes of Pyramids & Cuboids)", 6: "複利息期數利息差計算 (Compound Interest Differences)",
            7: "二次多項式因式分解 (Quadratic Factorization)", 8: "平行四邊形與相似形面積比例 (Area Ratios of Similar Figures)",
            9: "坐標幾何：中點公式 (Mid-point Formula)", 10: "負指數與極小數大小比較 (Indices & Small Numbers Comparison)"
        }

    else:
        safe_image("images/f3_fin_q1.png", width=390)
        q1 = st.radio("1. The figure shows sector OAB. Radius = 9 cm, angle = 280°. Folded into a hollow circular cone, find base radius.", ("A) 4.5 cm", "B) 7 cm", "C) 9 cm", "D) 14 cm"), key="f3_fin_q1")
        safe_image("images/f3_fin_q2.png", width=390)
        q2 = st.radio("2. In the figure, slopes of L1, L2, L3 are m1, m2, m3. Which are correct? I. m2 < 0, II. m3 > 0, III. m2 > m1", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f3_fin_q2")
        safe_image("images/f3_fin_q3.png", width=390)
        q3 = st.radio("3. Mr Choi drives along an inclined road PQ at 36 km/h for 2 hours. Horizontal distance is 68 km. Find gradient of PQ in form 1 : n.", ("A) 1 : 2", "B) 1 : 3", "C) 1 : 4", "D) 1 : 5"), key="f3_fin_q3")
        safe_image("images/f3_fin_q4.png", width=390)
        q4 = st.radio("4. If tan θ = √k / 2 where θ is acute, find sin θ cos θ.", ("A) 2k / (k + 4)", "B) (k + 4) / 2k", "C) 2√k / (k + 4)", "D) 2√k / (k + 4) [variant]"), key="f3_fin_q4")
        safe_image("images/f3_fin_q5.png", width=390)
        q5 = st.radio("5. A sheep walks 12m south from A to B, 25m east to C, 29m north to D. Find compass bearing of D from A.", ("A) S34°W", "B) S56°W", "C) N34°E", "D) N56°E"), key="f3_fin_q5")
        safe_image("images/f3_fin_q6.png", width=390)
        q6 = st.radio("6. The three points A(-2, -6), B(3, c) and C(23, 14) are collinear. Find c.", ("A) -2", "B) -1", "C) 1", "D) 2"), key="f3_fin_q6")
        safe_image("images/f3_fin_q7.png", width=390)
        q7 = st.radio("7. A(-6, -1), B(b, -13), C(-2, b-5), E(-1, -9). If AE // BC, find b.", ("A) -8", "B) -2", "C) 2", "D) 8"), key="f3_fin_q7")
        safe_image("images/f3_fin_q8.png", width=390)
        q8 = st.radio("8. Ratio of base radius of cylinder to cone is 6 : 5. Ratio of volume of cylinder to cone is 18 : 5. If cylinder height is 5 cm, find cone height.", ("A) 6 cm.", "B) 7 cm.", "C) 8 cm.", "D) 9 cm."), key="f3_fin_q8")
        safe_image("images/f3_fin_q9.png", width=390)
        q9 = st.radio("9. Which of the following are identities? I. sin²θ - cos²θ = 1 - 2cos²θ, II. sin²θ + cosθ / tanθ = 1 / sinθ, III. sin²θ tan(90° - θ) = sinθ cosθ", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f3_fin_q9")
        safe_image("images/f3_fin_q10.png", width=390)
        q10 = st.radio("10. Ratio of base radius of cylinder to cone is 6 : 5... [Duplicate variant test check]", ("A) 6 cm.", "B) 7 cm.", "C) 8 cm.", "D) 9 cm."), key="f3_fin_q10")

        user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
        correct_answers = {
            1: "B) 7 cm", 2: "A) I and II only", 3: "B) 1 : 3", 4: "D) 2√k / (k + 4)", 5: "D) N56°E",
            6: "A) -2", 7: "D) 8", 8: "A) 6 cm.", 9: "B) I and III only", 10: "A) 6 cm."
        }
        question_topics = {
            1: "圓錐與扇形展開關係 (Sectors & Circular Cones)", 2: "直角坐標系中直線斜率分析 (Slopes of Straight Lines)",
            3: "斜坡梯度與距離換算 (Gradients & Distances)", 4: "三角比代數化簡 (Trigonometric Ratios & Surds)",
            5: "方向角與向量應用 (Bearings & Distances)", 6: "共線三點與斜率相等 (Collinear Points)",
            7: "平行線與坐標幾何斜率 (Parallel Lines & Slopes)", 8: "圓柱與圓錐體積比例關係 (Volumes of Cylinders & Cones)",
            9: "進階三角恆等式驗證 (Advanced Trigonometric Identities)", 10: "幾何體積綜合應用 (Mensuration & Volumes)"
        }

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
        st.mockdown("🏆 **完美滿分！** 你喺今次測驗中所有題目全部答對，冇任何失分弱項，請繼續保持！")

# 品牌宣傳區與 Facebook 專頁聯結
st.markdown("---")
st.markdown("### 🌟 關於 [Terry Sir 數學專科教室](https://www.facebook.com/terrysir)")
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
    "<p style='text-align: center; color: #cbd5e0 !important;'>© 2026 中大數學 - <a href='https://www.facebook.com/terrysir' target='_blank' style='color: #f39c12; text-text-decoration: none;'>Terry Sir</a> - 中學數學專科. All Rights Reserved.</p>", 
    unsafe_allow_html=True
)
