import streamlit as st
import os

# 網頁基本設定 (頁面標題與佈局)
st.set_page_config(
    page_title="Terry Sir | 中大數學專科教室",
    page_icon="📐",
    layout="centered"
)

# 注入自定義 CSS：優化排版、美化選項卡片，確保所有文字清晰完美
st.markdown("""
<style>
    /* 全局背景與字體顏色、統一字體系列 (Sans-serif) 確保所有字體完全一致 */
    .stApp {
        background: linear-gradient(135deg, #0b1d3a 0%, #061124 100%);
        color: #ffffff !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
    }
    
    /* 確保所有標題、副標題、文字強制為白色，字體家族一致 */
    h1, h2, h3, h4, h5, h6, p, label, span, div {
        color: #ffffff !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
    }
    
    /* 讓所有 radio 按鈕入面嘅選項文字清晰顯示、字體加大至 16px、行距拉開 */
    .stRadio label p {
        color: #ffffff !important;
        font-size: 16px !important;
        line-height: 1.6 !important;
    }
    
    /* 區塊卡片化 (Container Card) 加強邊框與深色半透明背景，令選項極易閱讀 */
    .stRadio > div {
        background-color: rgba(255, 255, 255, 0.06) !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        margin-bottom: 15px;
    }
    
    /* 單一完美 Streamlit Primary 按鈕：強制 32px 字體、置中、兩行、去除多餘外框 */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%) !important;
        color: white !important;
        font-size: 32px !important;
        font-weight: 800 !important;
        text-align: center !important;
        padding: 22px 24px !important;
        border-radius: 12px !important;
        border: 2px solid rgba(255, 255, 255, 0.5) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5) !important;
        line-height: 1.4 !important;
        white-space: pre-wrap !important;
        height: auto !important;
    }
    div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(90deg, #2a5298 100%, #3a7bd5 100%) !important;
        border-color: #f39c12 !important;
    }
</style>
""", unsafe_allow_html=True)

# 輔助函式：安全載入圖片
def safe_image(img_path, width=390):
    if os.path.exists(img_path):
        st.image(img_path, width=width)

# 頁面頂部品牌視覺宣傳標題
st.markdown("""
<div style="text-align: center; padding: 10px 0;">
    <h1 style="margin-top: 5px; font-size: 30px; font-weight: 800; color: #ffffff !important;">【中大數學】Terry Sir - 初中數學專科教室</h1>
    <p style="color: #cbd5e0 !important; font-size: 15px; max-width: 650px; margin: 0 auto;">
        核心理念：不只教公式，用 NLP 心理引導幫孩子解開數學心結，由根基打起，重拾信心奪 A！ ✨
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==================== 引流挑戰心態吸睛文案 (Lead Magnet 區) ====================
st.markdown("""
<div style="background: linear-gradient(135deg, rgba(243, 156, 18, 0.15) 0%, rgba(30, 60, 114, 0.4) 100%); border: 2px solid #f39c12; padding: 22px; border-radius: 14px; margin-bottom: 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.4);">
    <h3 style="color: #ffeb3b !important; margin-top: 0; font-size: 22px; font-weight: 800;">🔥 【挑戰 10 題校本真題，測出你真實嘅數學「斤兩」！】</h3>
    <p style="color: #ffffff !important; font-size: 16px; line-height: 1.6; margin-bottom: 12px;">
        同學、家長你好！數學科成日溫到懷疑人生？唔好淨係靠估！與其估自己識唔識，不如直接接受呢個挑戰，用中一至中三<b>全港校本級 10 題實戰真題</b>嚟驗證你嘅真實實力。
    </p>
    <p style="color: #cbd5e0 !important; font-size: 15px; line-height: 1.5; margin-bottom: 0;">
        💡 <b>夠膽就即刻挑戰，睇下自己離 Level 5 奪 A 仲差幾遠！</b> 如果發現有盲點唔緊要，因為呢度就係你逆轉勝嘅起點。立即開始下方的測試！👇
    </p>
</div>
""", unsafe_allow_html=True)

# 第一步：先揀年級，再揀考試階段
st.subheader("📌 第一步：選擇你的年級與考試階段")
grade = st.radio("請選擇你嘅年級：", ["中一 (Form 1)", "中二 (Form 2)", "中三 (Form 3)"], index=2, horizontal=True)

exam_stage = st.radio(
    "請選擇考試階段：",
    [
        "1st Term Test (第一次測驗)", 
        "1st Exam (上學期考試)", 
        "2nd Term Test (第二次測驗)", 
        "2nd Exam (下學期考試 / Final)"
    ],
    index=3,
    horizontal=False
)

st.markdown("---")

user_answers = {}
correct_answers = {}
question_topics = {}

# 標題輸出
st.subheader(f"✍️ 第二步：{grade} {exam_stage} 校本真題級 10 題快測")
st.markdown(f"請認真完成以下精選實戰試題：")

# ==================== 嚴格雙重條件判定 (完整覆蓋所有年級與階段) ====================

# ----------------------------------------------------
# 1. 中一 (Form 1)
# ----------------------------------------------------
if grade == "中一 (Form 1)" and "1st Term Test" in exam_stage:
    f_half = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1</span><span style='display:block; padding-top:1px;'>2</span></span>"
    f_3_4 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>3</span><span style='display:block; padding-top:1px;'>4</span></span>"
    f_2_3 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>2</span><span style='display:block; padding-top:1px;'>3</span></span>"
    f_10_3 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>10</span><span style='display:block; padding-top:1px;'>3</span></span>"
    f_2_5 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>2</span><span style='display:block; padding-top:1px;'>5</span></span>"

    st.markdown(f"1. Arrange the following numbers in descending order: +3, {f_half}, -2.5, 0, -{f_3_4}, +1.2", unsafe_allow_html=True)
    q1_choice = st.radio("請選擇第 1 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": f"A) +3 > +1.2 > 1/2 > 0 > -3/4 > -2.5",
        "B": f"B) +3 > 1/2 > +1.2 > 0 > -3/4 > -2.5",
        "C": f"C) +3 > +1.2 > 1/2 > 0 > -2.5 > -3/4",
        "D": f"D) -2.5 > -3/4 > 0 > 1/2 > +1.2 > +3"
    }[x], key="f1_t1_q1_ans", label_visibility="collapsed")
    q1_mapping = {"A": f"A) +3 > +1.2 > {f_half} > 0 > -{f_3_4} > -2.5", "B": f"B) +3 > {f_half} > +1.2 > 0 > -{f_3_4} > -2.5", "C": f"C) +3 > +1.2 > {f_half} > 0 > -2.5 > -{f_3_4}", "D": f"D) -2.5 > -{f_3_4} > 0 > {f_half} > +1.2 > +3"}
    q1 = q1_mapping[q1_choice]

    q2 = st.radio("2. Which of the following expressions gives a result of 756?", ("A) 2² × 3² × 7", "B) 2³ × 3² × 7", "C) 2² × 3³ × 7", "D) 2³ × 3² × 7²"), key="f1_t1_q2")
    
    st.markdown(f"3. P is a point on a straight road. At 9:00 a.m., car A departs from P and travels at a speed of t km/h. At 9:30 a.m., car B departs from P and travels in the opposite direction of car A. The speed of car B is {f_2_3} of the speed of car A. Find the distance between the two cars at 11:00 a.m.", unsafe_allow_html=True)
    q3_choice = st.radio("請選擇第 3 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": "A) (2/3)t km",
        "B": "B) t km",
        "C": "C) 3t km",
        "D": "D) (10/3)t km"
    }[x], key="f1_t1_q3_ans", label_visibility="collapsed")
    q3_mapping = {"A": f"A) ({f_2_3})t km", "B": "B) t km", "C": "C) 3t km", "D": f"D) ({f_10_3})t km"}
    q3 = q3_mapping[q3_choice]

    q4 = st.radio("4. Which of the following numbers is not divisible by 6?", ("A) 1,444,584", "B) 2,476,326", "C) 3,440,976", "D) 4,585,348"), key="f1_t1_q4")
    q5 = st.radio("5. Alan buys some $1.7 stamps and $2.4 stamps for $46. It is given that the number of $1.7 stamps is 15 more than that of $2.4 stamps. Find the number of $1.7 stamps.", ("A) 20", "B) 23", "C) 30", "D) 35"), key="f1_t1_q5")
    q6 = st.radio("6. The passing mark of an examination is 55 marks. Suppose +1 mark represents 1 mark higher than the passing mark. Adrian, Bill and Carman get +20 marks, -8 marks and +6 marks in the examination respectively. Which of the following are true?\n\nI. Adrian's score is 75.\n\nII. Their total score is 18.\n\nIII. They get +6 marks on average.", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f1_t1_q6")
    q7 = st.radio("7. Which of the following are correct?\n\nI. The product of 420 and 525 is 2² × 3² × 5³ × 7².\n\nII. The H.C.F. of 420 and 525 is 105.\n\nIII. The L.C.M. of 420 and 525 is 2,100.", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f1_t1_q7")
    q8 = st.radio("8. The pocket money of Kate, Elvis and Ayden are increased by $90, decreased by $110 and increased by $85 respectively. Their total pocket money is", ("A) decreased by $105.", "B) increased by $95.", "C) increased by $65.", "D) decreased by $65"), key="f1_t1_q8")
    q9 = st.radio("9. Consider the following sequence: 1, 3, 7, 13, ... For any positive integer n, the (n + 1)-th term is greater than the n-th term by 2n. Find the 6th term.", ("A) 21", "B) 25", "C) 31", "D) 43"), key="f1_t1_q9")
    
    st.markdown(f"10. Harry's mother is m years old now. 5 years ago, Harry's age was {f_2_5} of his mother's age. How old is Harry now?", unsafe_allow_html=True)
    q10_choice = st.radio("請選擇第 10 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": "A) m - 5",
        "B": "B) (2/5)m + 5",
        "C": "C) (2/5)(m - 5)",
        "D": "D) (2/5)(m - 5) + 5"
    }[x], key="f1_t1_q10_ans", label_visibility="collapsed")
    q10_mapping = {"A": "A) m - 5", "B": f"B) ({f_2_5})m + 5", "C": f"C) ({f_2_5})(m - 5)", "D": f"D) ({f_2_5})(m - 5) + 5"}
    q10 = q10_mapping[q10_choice]

    user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
    correct_answers = {
        1: f"A) +3 > +1.2 > {f_half} > 0 > -{f_3_4} > -2.5", 2: "C) 2² × 3³ × 7", 3: "C) 3t km",
        4: "D) 4,585,348", 5: "A) 20", 6: "B) I and III only", 7: "D) I, II and III",
        8: "C) increased by $65.", 9: "C) 31", 10: f"D) ({f_2_5})(m - 5) + 5"
    }
    question_topics = {
        1: "有向數與數線大小比較 (Directed Numbers)", 2: "指數記數法與質因數分解 (Indices & Prime Factorization)",
        3: "應用題與速度距離計算 (Word Problems & Speed/Distance)", 4: "整除性與因數倍数 (Divisibility Tests)",
        5: "簡易方程應用題 (Simple Equations)", 6: "有向數嘅實際應用與平均數 (Application of Directed Numbers)",
        7: "H.C.F. 與 L.C.M. 綜合運算 (H.C.F. & L.C.M.)", 8: "有向數加減運算 (Operations of Directed Numbers)",
        9: "數列規律與一般項 (Number Sequences)", 10: "代數與年齡應用題 (Algebraic Word Problems)"
    }

elif grade == "中一 (Form 1)" and "1st Exam" in exam_stage:
    q1 = st.radio("1. How many negative integers are there between -5.5 and 1.5?", ("A) 4", "B) 5", "C) 6", "D) 7"), key="f1_ex1_q1")
    q2 = st.radio("2. Which of the following is/are divisible by both 3 and 8?\n\nI. 32,606,312\n\nII. 46,237,512\n\nIII. 98,243,604", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f1_ex1_q2")
    safe_image("images/f1_ex1_q3.png", width=525)
    q3 = st.radio("3. In the figure, the 1st pattern consists of 3 dots. For any positive integer n, the (n + 1)-th pattern is formed by adding 3 dots to the n-th pattern. Find the number of dots in the 7th pattern.", ("A) 15", "B) 18", "C) 21", "D) 24"), key="f1_ex1_q3")
    q4 = st.radio("4. 600 oranges and 400 apples were sold in a shop yesterday. Today, the number of oranges sold decreases by 10% while the number of apples sold increases by 15%. Find the percentage change in the total number of oranges and apples sold.", ("A) -10%", "B) 0%", "C) +5%", "D) +15%"), key="f1_ex1_q4")
    q5 = st.radio("5. The cost price of a car is $2,500. Its marked price is 60% higher than its cost price. If the car is sold at a profit of 20%, find the discount per cent.", ("A) 25%", "B) 33%", "C) 40%", "D) 80%"), key="f1_ex1_q5")
    q6 = st.radio("6. If the general term of a sequence is a_n = 3(n - 1)², find the product of the second term and the fourth term of the sequence.", ("A) 27", "B) 30", "C) 81", "D) 243"), key="f1_ex1_q6")
    q7 = st.radio("7. The height of Vincent is 135 cm. Issac is 20% taller than Vincent, while Andy is 20% shorter than Issac. Which of the following are true?\n\nI. Issac's height is above 160 cm.\n\nII. Vincent is as tall as Andy.\n\nIII. All of them are at least 130 cm tall.", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f1_ex1_q7")
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

elif grade == "中一 (Form 1)" and "2nd Term Test" in exam_stage:
    safe_image("images/f1_t2_q1.png", width=525)
    q1 = st.radio("1. Refer to the figures A, B, C, D and E as shown.\n\nWhich of the following statements are true?\n\nI. Figures C, D and E are equiangular polygons.\n\nII. There is only one regular polygon.\n\nIII. Only figures A, B and C are concave polygons.", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f1_t2_q1")
    q2 = st.radio("2. The total surface area of a right prism is 960 cm² and the total area of its lateral faces is 880 cm². Find the base area of the prism.", ("A) 10 cm²", "B) 20 cm²", "C) 30 cm²", "D) 40 cm²"), key="f1_t2_q2")
    safe_image("images/f1_t2_q3.png", width=390)
    q3 = st.radio("3. It is given that ABEF, GHI and DEH are straight lines. Find the area of the polygon ABCDEFGHI in the figure.", ("A) 161 cm²", "B) 575 cm²", "C) 671 cm²", "D) 767 cm²"), key="f1_t2_q3")
    safe_image("images/f1_t2_q4.png", width=390)
    q4 = st.radio("4. In the figure, ABEH, CBDG, ADF and CEF are straight lines. Find a + b + c + d + e.", ("A) 150°", "B) 180°", "C) 270°", "D) 360°"), key="f1_t2_q4")
    safe_image("images/f1_t2_q5.png", width=390)
    q5 = st.radio("5. Find the area of the quadrilateral ABCD in a rectangular coordinate plane in the figure, given A(-2, 3), B(-3, 1), C(-2, -4), D(2, 1).", ("A) 17.5 sq. units", "B) 18 sq. units", "C) 24.5 sq. units", "D) 35 sq. units"), key="f1_t2_q5")
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
        6: "D) -5", 7: "A) (-3, -4)", 8: "A) I and II only", 9: "C) I and III only", 10: "A) 90°"
    }
    question_topics = {
        1: "多邊形認識 (Polygons: Convex & Concave)", 2: "直棱柱表面面積計算 (Prisms Surface Area)",
        3: "複合圖形面積計算 (Composite Areas)", 4: "多邊形內角與外角 (Angles of Polygons)",
        5: "坐標平面幾何與圖形面積 (Coordinate Geometry & Areas)", 6: "坐標平移與旋轉變換 (Transformations in Coordinate Plane)",
        7: "平行四邊形坐標幾何 (Parallelograms in Coordinates)", 8: "坐標平面幾何變換 (Geometric Transformations)",
        9: "複合坐標變換 (Compound Coordinate Transformations)", 10: "直線角與三角形內角 (Angles and Lines)"
    }

elif grade == "中一 (Form 1)" and "2nd Exam" in exam_stage:
    q1 = st.radio("1. The total surface area of a square prism is 192 cm² and its width is 4 cm. Find the height of the square prism.", ("A) 6 cm", "B) 8 cm", "C) 10 cm", "D) 12 cm"), key="f1_fin_q1")
    q2 = st.radio("2. P(-3, 7), Q(0, k) and R(6, 1) are the vertices of a triangle in a rectangular coordinate plane where 1 < k < 7. If the area of triangle PQR is 9 square units, find k.", ("A) 2", "B) 3", "C) 4", "D) 6"), key="f1_fin_q2")
    safe_image("images/f1_fin_q3.png", width=390)
    q3 = st.radio("3. The figure below shows a trapezium PQRS where PS || QR. T is a point on PS. PR and TQ intersect at N. It is given that the lengths of PT, TS and QR are 4 cm, 2 cm and 8 cm respectively and the areas of triangle PNT and triangle QNR are 4 cm² and 16 cm² respectively. Find the area of the quadrilateral STNR.", ("A) 10 cm²", "B) 12 cm²", "C) 13 cm²", "D) 14 cm²"), key="f1_fin_q3")
    q4 = st.radio("4. Anna divides the following data into 7 groups and constructs a frequency distribution table. If the first group is 0 - 9, what is the frequency of the last group in the table?\n\n8, 28, 54, 50, 60, 22, 34, 14, 55, 12\n\n14, 28, 6, 12, 15, 59, 66, 29, 4, 64", ("A) 1", "B) 2", "C) 3", "D) 4"), key="f1_fin_q4")
    q5 = st.radio("5. 0.01491625 =", ("A) 0.015 (correct to the nearest integer)", "B) 0.015 (correct to 2 decimal places)", "C) 0.01491 (correct to 5 decimal places)", "D) 0.014916 (correct to 6 decimal places)"), key="f1_fin_q5")
    safe_image("images/f1_fin_q6.png", width=390)
    q6 = st.radio("6. The broken line graphs below show the profits of shop A and shop B in the first half of 2019.\n\nIn how many months is the profit of shop A lower than that of shop B?", ("A) 2", "B) 3", "C) 4", "D) 5"), key="f1_fin_q6")
    q7 = st.radio("7. Determine whether the following are discrete data or continuous data?\n\nI. The daily rainfalls of city A in July.\n\nII. The number of rainy days of city A in 2019.", ("A) continuous data / discrete data", "B) continuous data / continuous data", "C) discrete data / discrete data", "D) discrete data / continuous data"), key="f1_fin_q7")
    safe_image("images/f1_fin_q8.png", width=390)
    q8 = st.radio("8. In the figure, ADB is a straight line. Which of the following must be true?", (
        "A) △ABC ~ △ACD (3 sides proportional)", 
        "B) △ABC ~ △ACD (ratio of 2 sides, inc. angle)", 
        "C) △ABC ~ △CBD (3 sides proportional)", 
        "D) △ABC ~ △CBD (ratio of 2 sides, inc. angle)"
    ), format_func=lambda x: {
        "A) △ABC ~ △ACD (3 sides proportional)": "A) $\\triangle ABC \\sim \\triangle ACD$ (3 sides proportional)",
        "B) △ABC ~ △ACD (ratio of 2 sides, inc. angle)": "B) $\\triangle ABC \\sim \\triangle ACD$ (ratio of 2 sides, inc. angle)",
        "C) △ABC ~ △CBD (3 sides proportional)": "C) $\\triangle ABC \\sim \\triangle CBD$ (3 sides proportional)",
        "D) △ABC ~ △CBD (ratio of 2 sides, inc. angle)": "D) $\\triangle ABC \\sim \\triangle CBD$ (ratio of 2 sides, inc. angle)"
    }[x], key="f1_fin_q8")
    safe_image("images/f1_fin_q9.png", width=390)
    q9 = st.radio("9. Refer to the figure. Which of the following must be true?\n\nI. △QPR ≅ △SRP\n\nII. x = 5\n\nIII. y = 20°", (
        "A) I and II only", 
        "B) I and III only", 
        "C) II and III only", 
        "D) I, II and III"
    ), format_func=lambda x: {
        "A) I and II only": "A) I and II only ($\\triangle QPR \\cong \\triangle SRP$)",
        "B) I and III only": "B) I and III only",
        "C) II and III only": "C) II and III only",
        "D) I, II and III": "D) I, II and III"
    }[x], key="f1_fin_q9")
    safe_image("images/f1_fin_q10.png", width=390)
    q10 = st.radio("10. Which of the following must be true?", (
        "A) △ABC ≅ △DEF (SSA)", 
        "B) △ABC ≅ △DEF (SAS)", 
        "C) △ABC ≅ △PQR (SAS)", 
        "D) None of the above"
    ), format_func=lambda x: {
        "A) △ABC ≅ △DEF (SSA)": "A) $\\triangle ABC \\cong \\triangle DEF$ (SSA)",
        "B) △ABC ≅ △DEF (SAS)": "B) $\\triangle ABC \\cong \\triangle DEF$ (SAS)",
        "C) △ABC ≅ △PQR (SAS)": "C) $\\triangle ABC \\cong \\triangle PQR$ (SAS)",
        "D) None of the above": "D) None of the above"
    }[x], key="f1_fin_q10")

    user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
    correct_answers = {
        1: "C) 10 cm", 2: "B) 3", 3: "D) 14 cm²", 4: "C) 3", 5: "D) 0.014916 (correct to 6 decimal places)",
        6: "B) 3", 7: "A) continuous data / discrete data", 8: "B) △ABC ~ △ACD (ratio of 2 sides, inc. angle)", 9: "A) I and II only", 10: "D) None of the above"
    }
    question_topics = {
        1: "正方棱柱體積與表面積 (Square Prisms)", 2: "坐標平面三角形面積反算 (Triangle Areas in Coordinates)",
        3: "相似三角形與梯形面積比例 (Similar Triangles & Trapeziums)", 4: "頻數分佈表與數據整理 (Frequency Distributions)",
        5: "有效數字與四捨五入 (Significant Figures & Rounding)", 6: "折線圖數據分析 (Broken Line Graphs)",
        7: "離散數據與連續數據辨別 (Discrete vs Continuous Data)", 8: "相似三角形判定 (Similar Triangles)",
        9: "全等三角形與幾何推論 (Congruent Triangles)", 10: "三角形全等條件辨別 (Conditions for Triangle Congruence)"
    }


# ----------------------------------------------------
# 2. 中二 (Form 2)
# ----------------------------------------------------
elif grade == "中二 (Form 2)" and "1st Term Test" in exam_stage:
    f_1_x = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1</span><span style='display:block; padding-top:1px;'>x</span></span>"
    f_1_minus_x_x = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1 - x</span><span style='display:block; padding-top:1px;'>x</span></span>"
    f_1_m_1 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1</span><span style='display:block; padding-top:1px;'>m - 1</span></span>"
    f_1_m_1_alt = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1</span><span style='display:block; padding-top:1px;'>m + 1</span></span>"
    f_m_5_sq = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>m + 5</span><span style='display:block; padding-top:1px;'>m² - 1</span></span>"
    f_m_5_neg = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>m - 5</span><span style='display:block; padding-top:1px;'>m² - 1</span></span>"
    f_half = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1</span><span style='display:block; padding-top:1px;'>2</span></span>"

    q1 = st.radio("1. The height of a door is measured as 2.00 m, correct to the nearest 0.05 m. Find the percentage error.", ("A) 1.25%", "B) 2.5%", "C) 12.5%", "D) 25%"), key="f2_t1_q1")
    q2 = st.radio("2. If y = 29.4 (correct to 3 significant figures), find the range of values of y.", ("A) 29.3 < y <= 29.5", "B) 29.3 <= y < 29.5", "C) 29.35 < y <= 29.45", "D) 29.35 <= y < 29.45"), key="f2_t1_q2")
    q3 = st.radio("3. Find the degree of the expansion of (x² + 2x + 4)(y - 2).", ("A) 1", "B) 2", "C) 3", "D) 4"), key="f2_t1_q3")
    q4 = st.radio("4. If p and q are constants such that (x - p)(x + 5) - 7q = x² + 6x - q - 1, then q =", ("A) -6", "B) -1", "C) 1", "D) 6"), key="f2_t1_q4")
    
    st.markdown(f"5. Which of the following are NOT identities?\n\nI. ({f_1_x}) - 1 = {f_1_minus_x_x}\n\nII. (x + 1)² = x² + 1\n\nIII. (ax + b)(x - b) = ax² - b²", unsafe_allow_html=True)
    q5 = st.radio("5.", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f2_t1_q5", label_visibility="collapsed")
    
    f_minus_4_50_4 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'>(-4<sup>50</sup>)<sup>4</sup></span>"
    f_fraction_inner = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1</span><span style='display:block; padding-top:1px;'>64</span></span>"
    f_1_64_100 = f"<span style='display:inline-block; vertical-align:middle; text-align:center;'>( {f_fraction_inner} )<sup>100</sup></span>"
    st.markdown(f"6. {f_minus_4_50_4} × {f_1_64_100} =", unsafe_allow_html=True)
    q6 = st.radio("6.", ("A) -1.", "B) 4¹⁰⁰.", "C) 1 / 4¹⁰⁰.", "D) -1 / 4²⁰⁰."), key="f2_t1_q6", label_visibility="collapsed")
    q7 = st.radio("7. If a ≠ 0 and a ≠ 1, then (aⁿ⁺¹ - aⁿ⁻¹) / (aⁿ - aⁿ⁻¹) =", ("A) 2", "B) a", "C) a + 1", "D) a - 1"), key="f2_t1_q7")
    
    f_3_m_1 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>3</span><span style='display:block; padding-top:1px;'>m - 1</span></span>"
    f_2_m_1 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>2</span><span style='display:block; padding-top:1px;'>m + 1</span></span>"
    st.markdown(f"8. Simplify {f_3_m_1} - {f_2_m_1}.", unsafe_allow_html=True)
    q8_choice = st.radio("請選擇第 8 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": "A) 1 / (m - 1)",
        "B": "B) 1 / (m + 1)",
        "C": "C) (m + 5) / (m² - 1)",
        "D": "D) (m - 5) / (m² - 1)"
    }[x], key="f2_t1_q8_ans", label_visibility="collapsed")
    q8_mapping = {"A": f"A) {f_1_m_1}", "B": f"B) {f_1_m_1_alt}", "C": f"C) {f_m_5_sq}", "D": f"D) {f_m_5_neg}"}
    q8 = q8_mapping[q8_choice]

    f_frac_1 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>3<i>a</i>² + 6<i>ab</i></span><span style='display:block; padding-top:1px;'><i>a</i>² + 2<i>ab</i> - <i>ab</i> - 2<i>b</i>²</span></span>"
    f_frac_2 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>4<i>a</i> - 4<i>b</i></span><span style='display:block; padding-top:1px;'>9<i>a</i>²</span></span>"
    st.markdown(f"9. Simplify {f_frac_1} × {f_frac_2}.", unsafe_allow_html=True)
    q9 = st.radio("9.", ("A) 4 / (3a)", "B) 4a / 3", "C) 4(a + 2b) / 3a(a² + ab - 2b²)", "D) 4a(a + 2b) / 3(a² + ab - 2b²)"), key="f2_t1_q9", label_visibility="collapsed")
    st.markdown("10. If x² + y² = m and x + y = n, then xy =", unsafe_allow_html=True)
    q10_choice = st.radio("請選擇第 10 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": "A) (1/2)(n² - m)",
        "B": "B) n² - m",
        "C": "C) n² - m/2",
        "D": "D) (n²)/2 - m"
    }[x], key="f2_t1_q10_ans", label_visibility="collapsed")
    q10_mapping = {"A": f"A) ({f_half})(n² - m)", "B": "B) n² - m", "C": "C) n² - m/2", "D": f"D) ({f_half})n² - m"}
    q10 = q10_mapping[q10_choice]

    user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
    correct_answers = {
        1: "A) 1.25%", 2: "D) 29.35 <= y < 29.45", 3: "C) 3", 4: "C) 1", 5: "C) II and III only",
        6: "C) 1 / 4¹⁰⁰.", 7: "C) a + 1", 8: f"C) {f_m_5_sq}", 9: "A) 4 / (3a)", 10: f"A) ({f_half})(n² - m)"
    }
    question_topics = {
        1: "誤差與百分誤差計算 (Percentage Errors)", 2: "有效數字與數值範圍 (Significant Figures & Ranges)",
        3: "多項式展開與次方次數 (Polynomial Expansions & Degrees)", 4: "恆等式系數比較法 (Polynomial Identities)",
        5: "恆等式概念辨別 (Identities vs Equations)", 6: "指數定律與化簡 (Laws of Indices)",
        7: "指數化簡與分式運算 (Algebraic Fractions with Indices)", 8: "分式加減法運算 (Addition/Subtraction of Rational Expressions)",
        9: "分式乘法與因式分解 (Multiplication of Algebraic Fractions)", 10: "代數恆等式與完全平方公式 (Algebraic Identities & Formulas)"
    }

elif grade == "中二 (Form 2)" and "1st Exam" in exam_stage:
    q1 = st.radio("1. The thickness of a dictionary is measured as 4.0 cm, correct to the nearest 0.5 cm. Let x cm be the actual thickness of the dictionary. Find the range of values of x.", ("A) 3.5 <= x < 4.5", "B) 3.5 < x < 4.5", "C) 3.75 <= x < 4.25", "D) 3.75 < x < 4.25"), key="f2_ex1_q1")
    q2 = st.radio("2. Which of the following is not a polynomial?", ("A) 5x - 3y", "B) 5xy - 3", "C) x/5 - y/3", "D) 5x - 3/y"), key="f2_ex1_q2")
    q3 = st.radio("3. It is given that V = (2πR)/T. If R = 8 and V = 5π, find the value of T.", ("A) 0.8", "B) 1.6", "C) 3.2", "D) 4"), key="f2_ex1_q3")
    q4 = st.radio("4. Factorize completely: ax - cx - ay - bx + cy + by =", ("A) (x + y)(a + b - c)", "B) (x + y)(a - b - c)", "C) (x - y)(a + b - c)", "D) (x - y)(a - b - c)"), key="f2_ex1_q4")
    q5 = st.radio("5. The graph of the equation 4x + ay = 18 passes through P(6, -3), where a is a constant. Which of the following points lies on the graph of the given equation?", ("A) (-3,-6)", "B) (-1,-11)", "C) (1,7)", "D) (7,-2)"), key="f2_ex1_q5")
    q6 = st.radio("6. Solve the simultaneous equations x + y - 8 = (3x)/4 + 10 - y = 0.", ("A) (316/37, -20/37)", "B) (324/37, -28/37)", "C) (-8/7, 64/7)", "D) (-72/7, 16/7)"), key="f2_ex1_q6")
    safe_image("images/f2_ex1_q7.png", width=390)
    q7 = st.radio("7. In the figure, AED and BEC are straight lines. Which of the following must be true?", ("A) x = y", "B) x + y = 90°", "C) z = x + y", "D) x + y + z = 180°"), key="f2_ex1_q7")
    safe_image("images/f2_ex1_q8.png", width=390)
    q8 = st.radio("8. In the figure, PQT and PRS are straight lines. Which of the following must be true?", ("A) a = b - c", "B) c + e = 180°", "C) a + b = c + e", "D) c + d + e = 180° + b"), key="f2_ex1_q8")
    safe_image("images/f2_ex1_q9.png", width=390)
    q9 = st.radio("9. In the figure, CDE is a straight line and x + y = 90°. Which of the following must be true?\n\nI. AB || CE\n\nII. AC ⊥ AD\n\nIII. x = y", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f2_ex1_q9")
    safe_image("images/f2_ex1_q10.png", width=585)
    q10 = st.radio("10. The pie charts below show the favourite flavours of ice cream voted by customers of shop A and shop B respectively.\n\nWhich of the following must be correct?\n\nI. The number of customers of shop A who vote peach flavour is more than that of shop B.\n\nII. In both shop A and shop B, peach flavour is more popular than strawberry flavour.\n\nIII. The percentages of customers who vote almond flavour in shop A and shop B are the same.", ("A) I only", "B) III only", "C) I and II only", "D) II and III only"), key="f2_ex1_q10")

    user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
    correct_answers = {
        1: "C) 3.75 <= x < 4.25", 2: "D) 5x - 3/y", 3: "C) 3.2", 4: "D) (x - y)(a - b - c)", 5: "C) (1,7)",
        6: "C) (-8/7, 64/7)", 7: "D) x + y + z = 180°", 8: "D) c + d + e = 180° + b", 9: "A) I and II only", 10: "D) II and III only"
    }
    question_topics = {
        1: "量度極限與誤差範圍 (Measurement Limits & Limits of Accuracy)", 2: "多項式概念與辨別 (Polynomial Concepts)",
        3: "公式換算與主項變換 (Formula Manipulation)", 4: "進階因式分解技巧 (Advanced Factorization)",
        5: "直線方程與坐標代入 (Linear Equations & Graphs)", 6: "二元一次方程組求解 (Simultaneous Linear Equations)",
        7: "直線與角關係 (Angles and Lines)", 8: "三角形外角與內角和 (Exterior Angle Theorem of Triangles)",
        9: "平行線與垂直線性質 (Parallel & Perpendicular Lines)", 10: "扇形圖與百分比誤區 (Pie Charts & Statistical Misconceptions)"
    }

elif grade == "中二 (Form 2)" and "2nd Term Test" in exam_stage:
    f_5_13 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>5</span><span style='display:block; padding-top:1px;'>13</span></span>"
    f_4_3 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>4</span><span style='display:block; padding-top:1px;'>3</span></span>"
    f_13_5 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>13</span><span style='display:block; padding-top:1px;'>5</span></span>"
    f_5_8 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>5</span><span style='display:block; padding-top:1px;'>8</span></span>"
    f_4x_3y_3x_5y = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>4<i>x</i> + 3<i>y</i></span><span style='display:block; padding-top:1px;'>3<i>x</i> + 5<i>y</i></span></span>"
    f_3x_y_x_3y = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>3<i>x</i> + <i>y</i></span><span style='display:block; padding-top:1px;'><i>x</i> + 3<i>y</i></span></span>"

    st.markdown(f"1. If x and y are non-zero numbers such that {f_4x_3y_3x_5y} = {f_5_8}, then {f_3x_y_x_3y} =", unsafe_allow_html=True)
    q1_choice = st.radio("請選擇第 1 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": "A) 13/5",
        "B": "B) 1",
        "C": "C) 4/3",
        "D": "D) 5/13"
    }[x], key="f2_t2_q1_ans", label_visibility="collapsed")
    q1_mapping = {"A": f"A) {f_13_5}", "B": "B) 1", "C": f"C) {f_4_3}", "D": f"D) {f_5_13}"}
    q1 = q1_mapping[q1_choice]

    q2 = st.radio("2. Suppose 10 Swiss Francs dollars (CHF) are equivalent to 89 H.K. dollars (HKD) and 10 U.S. dollars (USD) are equivalent to 78 HKD. How many USD can 546 CHF be changed to?", ("A) 478 USD", "B) 623 USD", "C) 1271 USD", "D) 2173 USD"), key="f2_t2_q2")
    q3 = st.radio("3. If 3 pipes are used to fill a swimming pool in 1.5 hour, how much time can be saved by using 5 pipes instead? Assume that all the pipes discharge at the same rate.", ("A) 10 minutes", "B) 24 minutes", "C) 36 minutes", "D) 54 minutes"), key="f2_t2_q3")
    q4 = st.radio("4. Joe has brought some candies for his students who pass the term test. If 84 students pass, each of the students can have 7 candies. How many students pass the term test if each of them can have 3 candies?", ("A) 4", "B) 36", "C) 196", "D) 252"), key="f2_t2_q4")
    
    st.markdown("5. If 0.75x = y and 2z = 7y, where x, y and z are non-zero numbers, find (2x + y) : (y + z).", unsafe_allow_html=True)
    q5_choice = st.radio("請選擇第 5 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": "A) 22 : 27",
        "B": "B) 21 : 25",
        "C": "C) 10 : 9",
        "D": "D) 37 : 27"
    }[x], key="f2_t2_q5_ans", label_visibility="collapsed")
    q5_mapping = {"A": "A) 22 : 27", "B": "B) 21 : 25", "C": "C) 10 : 9", "D": "D) 37 : 27"}
    q5 = q5_mapping[q5_choice]

    q6 = st.radio("6. If each exterior angle of a regular n-sided polygon is 15°, which of the following are true?\n\nI. The value of n is 24.\n\nII. The ratio of the size of each interior angle of the polygon to that of each exterior angle is 12 : 1.\n\nIII. The sum of the interior angles of the polygon is 3960°.", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f2_t2_q6")
    safe_image("images/f2_t2_q7.png", width=390)
    q7 = st.radio("7. In the figure, AED and CGD are straight lines, and ABCD ~ EFGD. Find x.", ("A) 6", "B) 7", "C) 8", "D) 9"), key="f2_t2_q7")
    safe_image("images/f2_t2_q8.png", width=390)
    q8 = st.radio("8. In the figure, PQRS is a quadrilateral. The diagonals PR and QS intersect at T. It is given that $\\angle PSQ = \\angle SPR$ and $\\angle PQS = \\angle SRP$. Which of the following must be true?\n\nI. $\\triangle QPS \\cong \\triangle RSP$\n\nII. $\\triangle PTS \\sim \\triangle QTR$\n\nIII. $PS \\parallel QR$", (
        "A) I and II only", 
        "B) I and III only", 
        "C) II and III only", 
        "D) I, II and III"
    ), format_func=lambda x: {
        "A) I and II only": "A) I and II only",
        "B) I and III only": "B) I and III only",
        "C) II and III only": "C) II and III only",
        "D) I, II and III": "D) I, II and III"
    }[x], key="f2_t2_q8")
    safe_image("images/f2_t2_q9.png", width=390)
    q9 = st.radio("9. In the figure, ABC and FED are straight lines, where AB = BC = DE = EF. It is given that AC || FD and AF || CD. Which of the following must be true?\n\nI. $\\triangle ABF \\cong \\triangle EFB$\n\nII. $\\triangle EFB \\cong \\triangle EDB$\n\nIII. $\\triangle CBD \\cong \\triangle ABF$", (
        "A) I and III only", 
        "B) I only", 
        "C) II only", 
        "D) II and III only"
    ), format_func=lambda x: {
        "A) I and III only": "A) I and III only",
        "B) I only": "B) I only",
        "C) II only": "C) II only",
        "D) II and III only": "D) II and III only"
    }[x], key="f2_t2_q9")
    safe_image("images/f2_t2_q10.png", width=390)
    q10 = st.radio("10. In the figure, ABCD is a square and triangle CED is an equilateral triangle. If DE = DG and DG || EF, find x.", ("A) 34°", "B) 36°", "C) 39°", "D) 41°"), key="f2_t2_q10")

    user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
    correct_answers = {
        1: f"D) {f_5_13}", 2: "B) 623 USD", 3: "C) 36 minutes", 4: "C) 196", 5: "A) 22 : 27",
        6: "B) I and III only", 7: "C) 8", 8: "D) I, II and III", 9: "B) I only", 10: "D) 41°"
    }
    question_topics = {
        1: "比與率及分式代數化簡 (Ratios & Fractions)", 2: "外幣找換與比例應用 (Currency Conversions)",
        3: "正比例與反比例應用題 (Direct & Inverse Proportions)", 4: "變分與極端比例應用 (Variation & Proportions)",
        5: "連比運算與化簡 (Chain Ratios)", 6: "多邊形內角外角綜合計算 (Polygon Angle Properties)",
        7: "相似圖形與邊長比例 (Similar Figures & Ratios)", 8: "相似三角形與全等三角形綜合 (Similar & Congruent Triangles)",
        9: "圖形全等與平行線性質 (Congruence & Parallel Lines)", 10: "正方形與等邊三角形幾何綜合 (Squares & Equilateral Triangles)"
    }

elif grade == "中二 (Form 2)" and "2nd Exam" in exam_stage:
    q1 = st.radio("1. Which of the following is/are rational number(s)?\n\nI. √(2²)\n\nII. π\n\nIII. 0.3", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f2_fin_q1")
    q2 = st.radio("2. The scale of a map is 1 : 200,000. If the distance between two lighthouses on the map is 5.23 cm, find the actual distance between the two lighthouses.", ("A) 2.46 km", "B) 2.62 km", "C) 10.46 km", "D) 10.62 km"), key="f2_fin_q2")
    q3 = st.radio("3. Which of the following circles has the longest radius?", ("A) A circle with area 5 cm²", "B) A circle with circumference 4 cm", "C) A circle with diameter 3 cm", "D) A circle with radius 1 cm"), key="f2_fin_q3")
    safe_image("images/f2_fin_q4.png", width=390)
    q4 = st.radio("4. In the figure, the length of the line segment joining A and G is", ("A) 19", "B) 23", "C) 25", "D) 30"), key="f2_fin_q4")
    q5 = st.radio("5. A square and an isosceles triangle have the same perimeter 100 cm. If the base of the isosceles triangle is 18 cm, how much greater is the area of the square comparing to that of the isosceles triangle?", ("A) 256 cm²", "B) 265 cm²", "C) 440.5 cm²", "D) 445 cm²"), key="f2_fin_q5")
    q6 = st.radio("6. If each interior angle of a regular n-sided polygon is 157.5°, which of the following are true?\n\nI. The value of n is 16.\n\nII. The sum of the interior angle of the polygon is 2520°.\n\nIII. The ratio of the size of each interior angle to that of each exterior angle is 6:1.", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f2_fin_q6")
    safe_image("images/f2_fin_q7.png", width=390)
    
    q7 = st.radio("7. In the figure, ABCDEFGHI is a regular nonagon. Which of the following are true?\n\nI. $\\triangle ABC \\cong \\triangle EDC$\n\nII. $AC \\perp CE$\n\nIII. $\\angle AEF = 80^\\circ$", (
        "A) I and II only", 
        "B) I and III only", 
        "C) II and III only", 
        "D) I, II and III"
    ), format_func=lambda x: {
        "A) I and II only": "A) I and II only",
        "B) I and III only": "B) I and III only",
        "C) II and III only": "C) II and III only",
        "D) I, II and III": "D) I, II and III"
    }[x], key="f2_fin_q7")

    safe_image("images/f2_fin_q8.png", width=390)
    
    f_mr_nr_title = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>MR</span><span style='display:block; padding-top:1px;'>NR</span></span>"
    st.markdown(f"8. In the figure, PQRS is a rectangle and PMNS is a straight line. Find {f_mr_nr_title}.", unsafe_allow_html=True)
    
    f_cos_beta_sin_alpha = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>cos β</span><span style='display:block; padding-top:1px;'>sin α</span></span>"
    f_sin_beta_cos_alpha = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>sin β</span><span style='display:block; padding-top:1px;'>cos α</span></span>"
    
    q8_choice = st.radio("請選擇第 8 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": "A) cos β / sin α",
        "B": "B) sin β / cos α",
        "C": "C) sin α cos β",
        "D": "D) cos α sin β"
    }[x], key="f2_fin_q8_ans", label_visibility="collapsed")
    
    q8_mapping = {
        "A": f"A) {f_cos_beta_sin_alpha}", 
        "B": f"B) {f_sin_beta_cos_alpha}", 
        "C": "C) sin α cos β", 
        "D": "D) cos α sin β"
    }
    q8 = q8_mapping[q8_choice]

    q9 = st.radio("9. Two right cylinders P and Q have the same height. It is given that the ratio of base radii of cylinders P and Q is 1 : 2. The ratio of the base radius of P to the height of P is 1 : 3. The ratio of the total surface area of P to Q is", ("A) 1 : 2", "B) 2 : 5", "C) 4 : 7", "D) 7 : 16"), key="f2_fin_q9")
    safe_image("images/f2_fin_q10.png", width=390)
    q10 = st.radio("10. In the figure, PQRST is a regular pentagon. QT =", ("A) 2x", "B) 2x sin 54°", "C) 2 cos 54°", "D) 2x tan 54°"), key="f2_fin_q10")

    user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
    
    correct_answers = {
        1: "C) I and III only", 
        2: "C) 10.46 km", 
        3: "C) A circle with diameter 3 cm", 
        4: "C) 25", 
        5: "B) 265 cm²", 
        6: "A) I and II only", 
        7: "B) I and III only", 
        8: f"A) {f_cos_beta_sin_alpha}", 
        9: "C) 4 : 7", 
        10: "B) 2x sin 54°"
    }
    question_topics = {
        1: "有理數與無理數概念 (Rational & Irrational Numbers)", 2: "地圖比例尺與實際距離換算 (Map Scales & Actual Distances)",
        3: "圓面積、周界與半徑關係 (Circle Areas and Circumference)", 4: "直角坐標系與距離公式 (Coordinate Geometry & Distance Formula)",
        5: "平面圖形面積綜合計算 (Areas of Polygons & Triangles)", 6: "正多邊形內角外角性質 (Properties of Regular Polygons)",
        7: "正九邊形與全等圖形綜合 (Regular Nonagons & Congruence)", 8: "三角比（正弦、餘弦）應用 (Trigonometric Ratios: Sin & Cos)",
        9: "相似形與體積表面面積比例 (Mensuration: Cylinders & Ratios)", 10: "正五邊形與三角比應用 (Regular Pentagons & Trig)"
    }


# ----------------------------------------------------
# 3. 中三 (Form 3)
# ----------------------------------------------------
elif grade == "中三 (Form 3)" and "1st Term Test" in exam_stage:
    q1 = st.radio("1. 10010100011100₂ =", ("A) 37 × 2⁸ + 28.", "B) 37 × 2⁸ + 56.", "C) 37 × 2⁹ + 28.", "D) 37 × 2⁹ + 56."), key="f3_t1_q1")
    q2 = st.radio("2. 9 × 2¹⁰ + 6 × 2⁹ + 2³ - 7 =", ("A) 101100010000₂", "B) 110010000100₂", "C) 1011000001111₂", "D) 1100000000001₂"), key="f3_t1_q2")
    q3 = st.radio("3. Arrange the three numbers 1101100₂, 105₁₀ and 1101110₂ in ascending order.", ("A) 1101110₂ < 105₁₀ < 1101100₂", "B) 1101100₂ < 105₁₀ < 1101110₂", "C) 105₁₀ < 1101110₂ < 1101100₂", "D) 105₁₀ < 1101100₂ < 1101110₂"), key="f3_t1_q3")
    q4 = st.radio("4. A sum of $35,000 is deposited for 40 months at an interest rate of 3% p.a. compounded every four months. Find the interest, correct to the nearest dollar.", ("A) $1,180", "B) $2,715", "C) $3,662", "D) $4,966"), key="f3_t1_q4")
    
    f_10_3 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>10</span><span style='display:block; padding-top:1px;'>3</span></span>"
    st.markdown("5. If the base of a triangle is increased by 20% and its height is decreased by m% such that its area will decrease by 4%. Find m.", unsafe_allow_html=True)
    q5_choice = st.radio("請選擇第 5 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": "A) 10/3",
        "B": "B) 20",
        "C": "C) 24",
        "D": "D) 80"
    }[x], key="f3_t1_q5_ans", label_visibility="collapsed")
    q5_mapping = {"A": f"A) {f_10_3}", "B": "B) 20", "C": "C) 24", "D": "D) 80"}
    q5 = q5_mapping[q5_choice]

    q6 = st.radio("6. (25²⁰⁴⁸ × 2²⁰⁷⁶) / 5²⁰²⁰ =", ("A) 50⁴¹²⁴ / 5²⁰²⁰", "B) 25⁵⁶ × 2²⁰⁷⁶", "C) 10²⁰⁷⁶", "D) 10²¹⁰⁴"), key="f3_t1_q6")
    q7 = st.radio("7. Mr Cheung takes out a loan at an interest rate of 20% p.a. compounded quarterly for 2 years. If he has to pay an interest of $4,000, find the amount he needs to repay, correct to nearest dollar.", ("A) $8,378", "B) $8,619", "C) $9,091", "D) $12,378"), key="f3_t1_q7")
    
    q8 = st.radio(
        "8. There are 20 questions in a test. For each question answered correct, m marks will be given. For each unanswered question or wrongly answered question, n marks will be deducted. If 10 questions are answered correctly, a student will get 20 marks. If 15 questions are answered correctly, a student will get 60 marks. Find n.", 
        ("A) 2", "B) 3", "C) 4", "D) 5"), 
        key="f3_t1_q8"
    )
    
    q9 = st.radio("9. If -x² + kx + 10 can be factorized where k is an integer, which of the following is/are possible value(s) of k?\n\nI. -5\n\nII. -3\n\nIII. 9", ("A) I only", "B) II only", "C) I and III only", "D) II and III only"), key="f3_t1_q9")
    q10 = st.radio("10. Factorize -8x² - 28xy + 60y².", ("A) (x - 5y)(2x + 3y)", "B) (x + 5y)(2x - 3y)", "C) -4(x - 5y)(2x + 3y)", "D) -4(x + 5y)(2x - 3y)"), key="f3_t1_q10")

    user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
    correct_answers = {
        1: "A) 37 × 2⁸ + 28.", 
        2: "D) 1100000000001₂", 
        3: "D) 105₁₀ < 1101100₂ < 1101110₂", 
        4: "C) $3,662", 
        5: "B) 20", 
        6: "C) 10²⁰⁷⁶", 
        7: "D) $12,378", 
        8: "B) 3", 
        9: "D) II and III only", 
        10: "D) -4(x + 5y)(2x - 3y)"
    }
    question_topics = {
        1: "二進制數與代數轉換 (Binary Numbers)", 2: "二進制數加減運算 (Binary Arithmetic)",
        3: "不同進位制數值大小比較 (Number Bases Comparison)", 4: "複利息與存款利息計算 (Compound Interest)",
        5: "百分比變化與面積應用 (Percentage Change in Area)", 6: "指數律與底數化簡 (Laws of Indices)",
        7: "貸款複利息與還款額計算 (Loans & Compound Interest)", 8: "聯立方程應用題 (Simultaneous Equations)",
        9: "二次多項式因式分解可能性 (Factorization of Quadratics)", 10: "高級多項式因式分解 (Advanced Factorization)"
    }

elif grade == "中三 (Form 3)" and "1st Exam" in exam_stage:
    f_1_3123 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1</span><span style='display:block; padding-top:1px;'>3¹²³</span></span>"
    f_9_16 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>9</span><span style='display:block; padding-top:1px;'>16</span></span>"
    f_1_12 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1</span><span style='display:block; padding-top:1px;'>12</span></span>"
    f_1_6 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1</span><span style='display:block; padding-top:1px;'>6</span></span>"
    f_1_4 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1</span><span style='display:block; padding-top:1px;'>4</span></span>"
    f_1_3 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>1</span><span style='display:block; padding-top:1px;'>3</span></span>"
    f_a_5 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>a</span><span style='display:block; padding-top:1px;'>5</span></span>"
    f_8_3x_5 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>8 - 3x</span><span style='display:block; padding-top:1px;'>5</span></span>"
    f_5_2x_2 = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'>5 + 2x</span><span style='display:block; padding-top:1px;'>2</span></span>"

    f_q5_expr = "<span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'><i>x</i>² - 9<i>y</i>²</span><span style='display:block; padding-top:1px;'><i>y</i>⁴</span></span> ÷ <span style='display:inline-block; vertical-align:middle; text-align:center;'><span style='display:block; border-bottom:1px solid white; padding-bottom:1px;'><i>x</i> + 3<i>y</i></span><span style='display:block; padding-top:1px;'><i>y</i>²</span></span>"

    st.markdown("1. 3²⁴⁶ × 9⁻¹²³ =", unsafe_allow_html=True)
    q1_choice = st.radio("請選擇第 1 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": "A) 1.",
        "B": "B) -1.",
        "C": "C) 3¹²³.",
        "D": "D) 1 / (3¹²³)."
    }[x], key="f3_ex1_q1_ans", label_visibility="collapsed")
    q1_mapping = {"A": "A) 1.", "B": "B) -1.", "C": "C) 3¹²³.", "D": f"D) {f_1_3123}."}
    q1 = q1_mapping[q1_choice]

    st.markdown(f"2. Find the smallest integer a satisfying {f_a_5} - 1 > -4.", unsafe_allow_html=True)
    q2_choice = st.radio("請選擇第 2 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": "A) -24",
        "B": "B) -15",
        "C": "C) -14",
        "D": "D) -3"
    }[x], key="f3_ex1_q2_ans", label_visibility="collapsed")
    q2_mapping = {"A": "A) -24", "B": "B) -15", "C": "C) -14", "D": "D) -3"}
    q2 = q2_mapping[q2_choice]
    
    st.markdown(f"3. Solve the inequality {f_8_3x_5} ≥ {f_5_2x_2}.", unsafe_allow_html=True)
    q3_choice = st.radio("請選擇第 3 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": f"A) x <= -9/16",
        "B": f"B) x <= 9/16",
        "C": f"C) x >= -9/16",
        "D": f"D) x >= 9/16"
    }[x], key="f3_ex1_q3_ans", label_visibility="collapsed")
    q3_mapping = {
        "A": f"A) x <= -{f_9_16}", 
        "B": f"B) x <= {f_9_16}", 
        "C": f"C) x >= -{f_9_16}", 
        "D": f"D) x >= {f_9_16}"
    }
    q3 = q3_mapping[q3_choice]

    q4 = st.radio("4. If the growth rate of a value is 10% per month, and its value after 1 year is 2,125, find the original value correct to 3 significant figures.", ("A) 193", "B) 677", "C) 989", "D) 1,920"), key="f3_ex1_q4")
    
    st.markdown(f"5. {f_q5_expr} =", unsafe_allow_html=True)
    q5 = st.radio("請選擇第 5 題答案：", ("A) (x + 3y) / y⁶", "B) (x - 9y) / y⁶", "C) (x - 3y) / y²", "D) (x - 9y) / y²"), key="f3_ex1_q5", label_visibility="collapsed")
    
    safe_image("images/f3_ex1_q6.png", width=585)
    q6 = st.radio("6. In the figure, QS and RS are angle bisectors of triangle PQR. Find $\\angle QSR$.", ("A) 100°", "B) 120°", "C) 125°", "D) 130°"), key="f3_ex1_q6")
    
    st.markdown("7. Both Isaac and Andy want to buy a radiator. Isaac chooses a radiator among brands A, B, C and D at random, while Andy chooses a radiator among brands A, B and C at random. Find the probability that they choose the same brand.", unsafe_allow_html=True)
    q7_choice = st.radio("請選擇第 7 題答案：", ("A", "B", "C", "D"), format_func=lambda x: {
        "A": "A) 1/12",
        "B": "B) 1/6",
        "C": "C) 1/4",
        "D": "D) 1/3"
    }[x], key="f3_ex1_q7_ans", label_visibility="collapsed")
    q7_mapping = {"A": f"A) {f_1_12}", "B": f"B) {f_1_6}", "C": f"C) {f_1_4}", "D": f"D) {f_1_3}"}
    q7 = q7_mapping[q7_choice]

    safe_image("images/f3_ex1_q8.png", width=390)
    q8 = st.radio("8. A bag contains 3 red cards, 2 green cards and 15 yellow cards. In a game, a card is randomly drawn from the bag and the corresponding score will be given according to the table.", ("A) 9.25", "B) 11.5", "C) 13.25", "D) 15"), key="f3_ex1_q8")
    
    safe_image("images/f3_ex1_q9.png", width=585)
    q9 = st.radio("9. The prices of items sold in a supermarket are as follows: Shower gel $41, Oats $37, Chocolate bar $28, Hand sanitizer $33, Potato chips $26. The prices of all items are increased by 10% and then decreased by $2. Find the mean of the adjusted price of the above items.", ("A) $33.0", "B) $33.7", "C) $34.1", "D) $34.3"), key="f3_ex1_q9")
    
    safe_image("images/f3_ex1_q10.png", width=390)
    q10 = st.radio("10. In the figure, APB and AQC are straight lines. If AQ = 26, PQ = 10, QC = 22 and PB = 28, which of the following must be true?", ("A) BC is an altitude of triangle ABC.", "B) BQ is an angle bisector of triangle ABC.", "C) PC is a median of triangle ABC.", "D) PQ is a perpendicular bisector of triangle ABC."), key="f3_ex1_q10")

    user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
    correct_answers = {
        1: "A) 1.", 
        2: "C) -14", 
        3: f"A) x <= -{f_9_16}", 
        4: "B) 677", 
        5: "C) (x - 3y) / y²",
        6: "D) 130°", 
        7: f"C) {f_1_4}", 
        8: "A) 9.25", 
        9: "D) $34.3", 
        10: "A) BC is an altitude of triangle ABC."
    }
    question_topics = {
        1: "指數定律與化簡 (Laws of Indices)", 
        2: "一元一次不等式應用 (Linear Inequalities)", 
        3: "代數不等式求解 (Solving Inequalities)", 
        4: "複利息與增長率計算 (Growth Rate & Compound Interest)", 
        5: "分式化簡與因式分解 (Algebraic Fractions)", 
        6: "三角形內角與角平分線 (Angle Bisectors of Triangles)", 
        7: "獨立事件概率計算 (Probability of Independent Events)", 
        8: "數學期望值計算 (Expected Value)", 
        9: "平均數與百分比調整 (Means & Percentage Adjustments)", 
        10: "相似三角形與幾何推論 (Geometry Proofs & Similar Triangles)"
    }

elif grade == "中三 (Form 3)" and "2nd Term Test" in exam_stage:
    # ----------------------------------------------------
    # 第 1 題維持
    # ----------------------------------------------------
    safe_image("images/f3_t2_q1.png", width=390)
    q1 = st.radio(
        "1. The figure shows the sector OAB. The radius of the sector is 9 cm and the angle of sector is 280°. If it is folded into a hollow circular cone, find the base radius of the cone.", 
        ("A) 4.5 cm", "B) 7 cm", "C) 9 cm", "D) 14 cm"), 
        key="f3_t2_q1"
    )
    
    # 第 2 題維持
    safe_image("images/f3_t2_q2.png", width=390)
    q2 = st.radio(
        "2. In the figure, the slopes of the straight lines L₁, L₂ and L₃ are m₁, m₂ and m₃ respectively. Which of the following must be correct?", 
        ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), 
        key="f3_t2_q2"
    )
    
    # 第 3 題維持
    safe_image("images/f3_t2_q3.png", width=390)
    q3 = st.radio(
        "3. Mr Choi drives along an inclined road PQ at a speed of 36 km/h for 2 hours. If the horizontal distance he has travelled is 68 km, find the gradient of PQ in the form of 1 : n, where n is correct to the nearest integer.", 
        ("A) 1 : 2", "B) 1 : 3", "C) 1 : 4", "D) 1 : 5"), 
        key="f3_t2_q3"
    )
    
    # 第 4 題維持
    safe_image("images/f3_t2_q4.png", width=390)
    q4 = st.radio(
        "4. If tan θ = √k / 2 where θ is acute, find sin θ × cos θ.", 
        ("A) 2k / (k + 4)", "B) (k + 4) / 2k", "C) (k + 4) / 2√k ", "D) 2√k / (k + 4) "), 
        key="f3_t2_q4"
    )

    # 第 5 題維持
    safe_image("images/f3_t2_q5.png", width=390)
    q5 = st.radio(
        "5. A sheep walks 12 m due south from tree A to tree B, then walks 25 m due east to tree C and finally walks 29 m due north to tree D. Find the compass bearing of D from A, correct to the nearest degree.", 
        ("A) S34°W", "B) S56°W", "C) N34°E", "D) N56°E"), 
        key="f3_t2_q5"
    )
    
    # 第 6 題維持
    safe_image("images/f3_t2_q6.png", width=390)
    q6 = st.radio(
        "6. The three points A(-2, -6), B(3, c) and C(23, 14) are collinear. Find c.", 
        ("A) -2", "B) -1", "C) 1", "D) 2"), 
        key="f3_t2_q6"
    )

    # 第 7 題維持
    safe_image("images/f3_t2_q7.png", width=390)
    q7 = st.radio(
        "7. A(-6, -1), B(b, -13), C(-2, b - 5) and E(-1, -9) are four given points. If AE // BC, find the value of b.", 
        ("A) -8", "B) -2", "C) 2", "D) 8"), 
        key="f3_t2_q7"
    )
    
    # 第 8 題維持
    safe_image("images/f3_t2_q8.png", width=390)
    q8 = st.radio(
        "8. The ratio of the base radius of a right circular cylinder to the base radius of a right circular cone is 6 : 5 while the ratio of the volume of the circular cylinder to the volume of the circular cone is 18 : 5. If the height of the circular cylinder is 5 cm, then the height of the circular cone is", 
        ("A) 6 cm.", "B) 7 cm.", "C) 8 cm.", "D) 9 cm."), 
        key="f3_t2_q8"
    )
    
    # 第 9 題維持
    safe_image("images/f3_t2_q9.png", width=585)
    q9 = st.radio("9. Which of the following are identities?\n\nI. sin²θ - cos²θ = 1 - 2cos²θ\n\nII. sin²θ + (cos θ)/(tan θ) = 1/sin θ\n\nIII. sin²θ × tan(90° - θ) = sin θ × cos θ", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f3_t2_q9")
    
    # 第 10 題維持
    safe_image("images/f3_t2_q10.png", width=390)
    q10 = st.radio(
        "10. Denote the origin by O. The coordinates of the point A are (22, 0). Let B be a point lying on the negative y-axis such that the x-coordinate of the incentre of ΔOAB is 4. Find the area of ΔOAB correct to 3 significant figures.", 
        ("A) 99.0 sq. units", "B) 113 sq. units", "C) 161 sq. units", "D) 322 sq. units"), 
        key="f3_t2_q10"
    )

    user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
    correct_answers = {
        1: "B) 7 cm", 
        2: "A) I and II only", 
        3: "B) 1 : 3", 
        4: "D) 2√k / (k + 4) ", 
        5: "D) N56°E",
        6: "A) -2", 
        7: "D) 8", 
        8: "A) 6 cm.",
        9: "B) I and III only", 
        10: "B) 113 sq. units"
    }
    question_topics = {
        1: "圓錐與扇形展開關係 (Sectors & Circular Cones)", 
        2: "直角坐標系中直線斜率分析 (Slopes of Straight Lines)",
        3: "斜坡梯度與距離換算 (Gradients & Distances)", 
        4: "三角比代數化簡 (Trigonometric Ratios & Surds)",
        5: "方向角與向量應用 (Bearings & Distances)", 
        6: "共線三點與斜率相等 (Collinear Points)",
        7: "平行線與坐標幾何斜率 (Parallel Lines & Slopes)", 
        8: "圓柱與圓錐體積比例關係 (Volumes of Cylinders & Cones)",
        9: "進階三角恆等式驗證 (Advanced Trigonometric Identities)", 
        10: "坐標幾何與三角形內心面積 (Coordinate Geometry & Incentres)"
    }

else:
    safe_image("images/f3_fin_q1.png", width=390)
    q1 = st.radio("1. The figure shows sector OAB. The radius of the sector is 9 cm and the angle of sector is  $\\angle = 280^\\circ$. If it is folded into a hollow circular cone, find base radius of the cone.", ("A) 4.5 cm", "B) 7 cm", "C) 9 cm", "D) 14 cm"), key="f3_fin_q1")
    safe_image("images/f3_fin_q2.png", width=390)
    q2 = st.radio("2. In the figure, the slopes of the straight lines L₁, L₂ and L₃ are m₁, m₂ and m₃ respectively. Which of the following must be correct?\n\nI. m₂ < 0\n\nII. m₃ > 0\n\nIII. m₂ > m₁", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f3_fin_q2")
    safe_image("images/f3_fin_q3.png", width=390)
    q3 = st.radio("3. Mr Choi drives along an inclined road PQ at a speed of 36 km/h for 2 hours. If the horizontal distance he has travelled is 68 km, find the gradient of PQ in the form of 1 : n, where n is correct to the nearest integer.", ("A) 1 : 2", "B) 1 : 3", "C) 1 : 4", "D) 1 : 5"), key="f3_fin_q3")
    safe_image("images/f3_fin_q4.png", width=390)
    q4 = st.radio("4. If tan θ = √k / 2 where θ is acute, find sin θ × cos θ.", ("A) 2k / (k + 4)", "B) (k + 4) / 2k", "C) (k + 4) / 2√k", "D) 2√k / (k + 4) "), key="f3_fin_q4")
    safe_image("images/f3_fin_q5.png", width=390)
    q5 = st.radio("5. A sheep walks 12 m due south from tree A to tree B, then walks 25 m due east to tree C and finally walks 29 m due north to tree D. Find the compass bearing of D from A, correct to the nearest degree.", ("A) S34°W", "B) S56°W", "C) N34°E", "D) N56°E"), key="f3_fin_q5")
    safe_image("images/f3_fin_q6.png", width=390)
    q6 = st.radio("6. The three points A(-2, -6), B(3, c) and C(23, 14) are collinear. Find c.", ("A) -2", "B) -1", "C) 1", "D) 2"), key="f3_fin_q6")
    safe_image("images/f3_fin_q7.png", width=390)
    q7 = st.radio("7. A(-6, -1), B(b, -13), C(-2, b - 5) and E(-1, -9) are four given points. If AE // BC, find the value of b.", ("A) -8", "B) -2", "C) 2", "D) 8"), key="f3_fin_q7")
    safe_image("images/f3_fin_q8.png", width=390)
    q8 = st.radio("8. The ratio of the base radius of a right circular cylinder to the base radius if a right circular cone is 6 : 5 while the ratio of volume of the the circular cylinder to the volume of the circular cone is 18 : 5. If the height of the circular cylinder is 5 cm, then the height of the circular cone is", ("A) 6 cm.", "B) 7 cm.", "C) 8 cm.", "D) 9 cm."), key="f3_fin_q8")
    safe_image("images/f3_fin_q9.png", width=390)
    q9 = st.radio("9. Which of the following are identities?\n\nI. sin²θ - cos²θ = 1 - 2cos²θ\n\nII. sin²θ + (cos θ)/(tan θ) = 1/sin θ\n\nIII. sin²θ × tan(90° - θ) = sin θ × cos θ", ("A) I and II only", "B) I and III only", "C) II and III only", "D) I, II and III"), key="f3_fin_q9")
    safe_image("images/f3_fin_q10.png", width=390)
    q10 = st.radio("10. Denote the origin by O. The coordinates of the point A are (22, 0). Let B be a point lying on the negative y-axis such that the x-coordinate of the incentre of ΔOAB is 4. Find the area of ΔOAB correct to 3 significant figures.", ("A) 99.0 sq. units", "B) 113 sq. units", "C) 161 sq. units", "D) 322 sq. units"), key="f3_fin_q10")

    user_answers = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}
    correct_answers = {
        1: "B) 7 cm", 2: "A) I and II only", 3: "B) 1 : 3", 4: "D) 2√k / (k + 4) ", 5: "D) N56°E",
        6: "A) -2", 7: "D) 8", 8: "A) 6 cm.", 9: "B) I and III only", 10: "A) 6 cm."
    }
    question_topics = {
        1: "圓錐與扇形展開關係 (Sectors & Circular Cones)", 2: "直角坐標系中直線斜率分析 (Slopes of Straight Lines)",
        3: "斜坡梯度與距離換算 (Gradients & Distances)", 4: "三角比代數化簡 (Trigonometric Ratios & Surds)",
        5: "方向角與向量應用 (Bearings & Distances)", 6: "共線三點與斜率相等 (Collinear Points)",
        7: "平行線與坐標幾何斜率 (Parallel Lines & Slopes)", 8: "圓柱與圓錐體積比例關係 (Volumes of Cylinders & Cones)",
        9: "進階三角恆等式驗證 (Advanced Trigonometric Identities)", 10: "幾何體積綜合應用 (Mensuration & Volumes)"
    }


# ==================== 單一原生按鈕 (32px，乾淨俐落) ====================
submit_clicked = st.button("🚀 按此立即提交\n並生成我的 Mock 考試預測報告！", type="primary")

if submit_clicked:
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

# 品牌宣傳區與 [Terry Sir 數學專科教室](https://www.facebook.com/terrysir) 專頁聯結
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
    "<p style='text-align: center; color: #cbd50 !important;'>© 2026 中大數學 - <a href='https://www.facebook.com/terrysir' target='_blank' style='color: #f39c12; text-decoration: none;'>Terry Sir</a> - 中學數學專科. All Rights Reserved.</p>", 
    unsafe_allow_html=True
)
