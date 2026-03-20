def joseon_restoration_page() -> None:
    import time
    import random
    from pathlib import Path

    import streamlit as st

    st.markdown(
        """
        <style>
        /* Base Container & Animation */
        
        .hero-title {
            font-size: 48px;
            font-weight: 900;
            background: linear-gradient(120deg, #1E50A3, #2960b4, #123e85);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
            margin-bottom: 8px;
            line-height: 1.1;
        }
        
        textarea {
            font-size: 20px !important;
            line-height: 1.6 !important;
        }
        
        .hero-sub {
            color: #64748b;
            font-size: 15px;
            font-weight: 500;
            margin-top: 0;
            margin-bottom: 24px;
        }

        /* Modern KPI Cards */
        .kpi-wrap {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 16px;
            margin: 12px 0 32px 0;
        }
        
        .kpi {
            border: 1px solid rgba(137, 197, 213, 0.4);
            border-radius: 20px;
            padding: 16px 20px;
            background: rgba(255, 255, 255, 0.9);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -2px rgba(0, 0, 0, 0.02);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .kpi:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(30, 80, 163, 0.08), 0 4px 6px -4px rgba(30, 80, 163, 0.04);
            border-color: rgba(30, 80, 163, 0.4);
        }
        
        .kpi .k {
            font-size: 13px;
            font-weight: 600;
            color: #1E50A3;
            opacity: 0.8;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin: 0 0 4px 0;
        }
        
        .kpi .v {
            font-size: 18px;
            font-weight: 800;
            color: #0f172a;
            margin: 0;
            letter-spacing: -0.3px;
        }

        /* Section Titles with Accent */
        p.section-title {
            display: flex;
            align-items: center;
            font-size: 28px !important;
            font-weight: 900 !important;
            color: #0f172a !important;
            letter-spacing: -0.5px !important;
            margin: 32px 0 16px 0 !important;
            padding-bottom: 12px;
            border-bottom: 2px solid rgba(137, 197, 213, 0.3);
        }
        
        .section-num {
            color: #1E50A3;
            margin-right: 12px;
        }
        
        .badge {
            display: inline-flex;
            align-items: center;
            padding: 4px 12px;
            border-radius: 9999px;
            font-size: 13px !important;
            font-weight: 700 !important;
            color: #ffffff;
            background: #89C5D5;
            margin-left: 16px;
            transform: translateY(-1px);
        }

        /* Panel Styling */
        .panel-title {
            font-size: 20px;
            font-weight: 800;
            color: #1E50A3;
            margin: 0 0 6px 0;
            letter-spacing: -0.3px;
        }
        
        .panel-sub {
            font-size: 14px;
            color: #64748b;
            margin: 0 0 16px 0;
        }

        /* Streamlit Button Overrides */
        div.stButton > button {
            border-radius: 12px;
            font-weight: 700;
            padding: 4px 24px;
            transition: all 0.2s ease;
            border: 1px solid rgba(137, 197, 213, 0.6);
            background: #ffffff;
            color: #1E50A3;
        }
        
        div.stButton > button:hover {
            border-color: #1E50A3;
            color: #1E50A3;
            background: rgba(137, 197, 213, 0.1);
        }
        
        div.stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #1E50A3, #2960b4);
            color: white;
            border: none;
            box-shadow: 0 4px 12px rgba(30, 80, 163, 0.3);
        }
        
        div.stButton > button[kind="primary"]:hover {
            background: linear-gradient(135deg, #FF9696, #ff7a7a); /* Point color on hover */
            color: white;
            box-shadow: 0 6px 16px rgba(255, 150, 150, 0.4);
            transform: translateY(-1px);
            border: none;
        }

        /* restored token highlight */
        .hl{
            color: #FF9696;
            font-weight: 950;
            background: rgba(255, 150, 150, 0.1);
            padding: 0 4px;
            border-radius: 4px;
        }

        /* ===== Candidate Cards (VIEW ONLY) ===== */
        .candidate-card{
            border: 1px solid rgba(137, 197, 213, 0.4);
            border-top: 4px solid #1E50A3;
            border-radius: 16px;
            padding: 20px;
            background: #ffffff;
            box-shadow: 0 2px 8px rgba(30, 80, 163, 0.05);
            margin-bottom: 16px;
            height: calc(100% - 16px);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .candidate-card:hover{
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 15px -3px rgba(30, 80, 163, 0.08), 0 4px 6px -4px rgba(30, 80, 163, 0.04) !important;
            border-color: rgba(30, 80, 163, 0.4) !important;
        }

        .candidate-rank{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 12px;
            font-weight: 800;
            font-size: 15px;
            color: #1E50A3;
            border-bottom: 1px dashed rgba(137, 197, 213, 0.5);
            padding-bottom: 8px;
        }
        .candidate-text{
            font-size: 22px;
            line-height: 1.8;
            color: #1e293b;
            font-weight: 600;
        }
        
        .candidate-desc{
            margin-top: 10px;
            font-size: 17px;
            line-height: 1.6;
            color: #64748b;
            font-weight: 500;
        }

        /* Alert/Info Overrides */
        div[data-testid="stAlert"] {
            border-radius: 12px;
            border: none;
            background-color: rgba(137, 197, 213, 0.15);
            color: #1E50A3;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    def uploaded_stem(u) -> str:
        try:
            return Path(u.name).stem
        except Exception:
            return ""

    def highlight_after_phrase(sentence: str, phrase: str, n: int) -> str:
        k = sentence.find(phrase)
        if k == -1:
            return sentence
        start = k + len(phrase)
        end = start + n
        if end > len(sentence):
            return sentence
        restored = sentence[start:end]
        return sentence[:start] + f'<span class="hl">{restored}</span>' + sentence[end:]


    def highlight_before_phrase(sentence: str, phrase: str, n: int) -> str:
        k = sentence.find(phrase)
        if k == -1 or k < n:
            return sentence
        start = k - n
        restored = sentence[start:k]
        return sentence[:start] + f'<span class="hl">{restored}</span>' + sentence[k:]
    st.markdown(    
        '<div class="hero-title">ARI: 조선 고문서 복원 AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-sub">조선시대 고문서의 훼손 이미지 업로드 시, 글자 인식 및 ARI 기반 복원을 진행하여 상위 복원 후보를 생성합니다.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="kpi-wrap">
            <div class="kpi"><p class="k">복원 파이프라인</p><p class="v">이미지 → 글자 인식 → 복원</p></div>
            <div class="kpi"><p class="k">결과</p><p class="v">복원 후보 리스트</p></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------------- Step 1 ----------------
    st.markdown(
        '<p class="section-title"><span class="section-num">1)</span><span class="section-text">이미지 업로드 및 글자 인식</span> <span class="badge">Step 1</span></p>',
        unsafe_allow_html=True,
    )

    uploaded = st.file_uploader(
        "조선 고문서 이미지 업로드",
        type=["png", "jpg", "jpeg", "webp"],
        key="joseon_image_uploader",
        label_visibility="collapsed",
    )
    
    if uploaded is not None:
        current_uploaded_name = uploaded.name
        previous_uploaded_name = st.session_state.get("joseon_uploaded_name")

        if previous_uploaded_name != current_uploaded_name:
            st.session_state["joseon_uploaded_name"] = current_uploaded_name
            st.session_state.pop("joseon_ocr_text", None)
            st.session_state.pop("joseon_restoration_candidates", None)
            st.session_state.pop("joseon_selected_candidate_idx", None)
            st.session_state.pop("joseon_restored_text", None)


    if uploaded is None:
        st.info("이미지를 업로드하면 인식된 텍스트 확인이 가능합니다.")
        st.markdown("---")
        st.markdown(
            '<p class="section-title"><span class="section-num">2)</span><span class="section-text">조선 고문서 복원</span> <span class="badge">Step 2</span></p>',
            unsafe_allow_html=True,
        )
        st.warning("먼저 이미지를 업로드해 주세요.")
        return

    stem = uploaded_stem(uploaded)
    is_jrs_1651_7_11 = stem == "jrs_1651-7-11_10"
    is_jrs_1650_6_11 = stem == "jrs_1650-6-11_17"
    is_jrs_1688_4_26 = stem == "jrs_1688-4-26_10"

    left, right = st.columns([0.75, 1.25], gap="small")

    with left:
        st.markdown('<div class="panel-title">이미지 미리보기</div>', unsafe_allow_html=True)
        st.image(uploaded, width=500)

    with right:
        st.markdown('<div class="panel-title">글자 인식 결과</div>', unsafe_allow_html=True)
        st.markdown('<div class="panel-sub">글자 인식 후 결과를 확인할 수 있습니다.</div>', unsafe_allow_html=True)

        c1, c2 = st.columns([1, 1])
        with c1:
            run_ocr = st.button("글자 인식 실행", use_container_width=True, key="run_ocr_btn")
        with c2:
            clear_ocr = st.button("결과 초기화", use_container_width=True, key="clear_ocr_btn")

        if clear_ocr:
            st.session_state.pop("joseon_ocr_text", None)
            st.session_state.pop("joseon_restoration_candidates", None)
            st.session_state.pop("joseon_selected_candidate_idx", None)
            st.session_state.pop("joseon_restored_text", None)

        if run_ocr:
            with st.spinner("글자 인식중..."):
                time.sleep(random.uniform(2.5, 3.5))

            if is_jrs_1651_7_11:
                st.session_state["joseon_ocr_text"] = (
                    "以式年監試覆試, 小學□禮考講試官望, 傳于南翧曰, 以有名稱."
                )
            elif is_jrs_1650_6_11:
                st.session_state["joseon_ocr_text"] = (
                    "趙壽益, 以義禁府言啓曰, 本府月令醫員金榮齡手本內, 保放罪人□廷顯身病, 更加看審, 則染病之餘, 因添病, 食飮全廢, 氣力澌盡, 比前無異云, 不得已待其差歇還囚之意, 敢啓. 傳曰, 知道."
                )
            elif is_jrs_1688_4_26:
                st.session_state["joseon_ocr_text"] = (
                    "判府事李□□上疏. 大槪, 寒疾方苦, 足病近劇, 起居之班, 不得致身, 乞削臣職, 仍治臣罪事. 入啓. 答曰, 省疏具悉卿懇。所患如此, 不得進參, 有何所傷? 至於薄略常廩, 不足過辭, 卿其安心, 勿辭領受, 亦勿待罪, 從容善. 仍傳曰, 遣史官傳諭."
                )
            else:
                st.session_state["joseon_ocr_text"] = (
                    "Internal Server Error"
                )
            st.success("글자 인식 완료")

        ocr_text = st.session_state.get("joseon_ocr_text", "")
        if ocr_text:
            st.text_area("ocr_text_area", ocr_text, height=180, label_visibility="collapsed")
        else:
            st.info("글자 인식을 진행해 주세요.")

    st.markdown("---")

    # ---------------- Step 2 ----------------
    st.markdown(
        '<p class="section-title"><span class="section-num">2)</span><span class="section-text">복원</span> <span class="badge">Step 2</span></p>',
        unsafe_allow_html=True,
    )
    st.caption("인식 결과를 입력으로 받아 ARI가 복원 후보를 생성합니다.")

    ocr_text = st.session_state.get("joseon_ocr_text", "")
    if not ocr_text:
        st.warning("먼저 글자 인식을 실행해 주세요.")
        return

    # st.markdown('<div class="panel-title">훼손 문서</div>', unsafe_allow_html=True)
    # st.text_area("damaged_from_ocr", ocr_text, height=120, label_visibility="collapsed")
    
    st.markdown('<div class="panel-title">훼손 문서</div>', unsafe_allow_html=True)
    st.text_area("damaged_from_ocr", ocr_text, height=120, label_visibility="collapsed")

    if is_jrs_1651_7_11:
        st.markdown(
            """
            <div style="
                margin-top: 8px;
                margin-bottom: 20px;
                padding: 14px 16px;
                border-radius: 12px;
                background: rgba(137, 197, 213, 0.12);
                border: 1px solid rgba(137, 197, 213, 0.35);
                color: #334155;
                font-size: 16px;
                line-height: 1.8;
            ">
                <b style="color:#1E50A3;">한국어 번역</b><br>
                정기 과거 시험의 2차 시험과 『소학』, 『□례』 등에 관한 구술시험을 담당할 시험관 후보 명단을 두고,
                왕이 남현에게 전하기를 “명성이 높고 학식이 널리 알려진 사람으로 선발하라”라고 하였다.
            </div>
            """,
            unsafe_allow_html=True,
        )

    a, b = st.columns([1, 1])
    with a:
        run_restore = st.button("복원 실행", use_container_width=True, key="run_restoration_btn")
    with b:
        reset_all = st.button("결과 초기화", use_container_width=True, key="reset_restoration_btn")

    if reset_all:
        st.session_state.pop("joseon_ocr_text", None)
        st.session_state.pop("joseon_restoration_candidates", None)
        st.session_state.pop("joseon_selected_candidate_idx", None)
        st.session_state.pop("joseon_restored_text", None)
        st.success("Session reset.")
        return

    if run_restore:
        with st.spinner("손상된 문서 복원 중..."):
            time.sleep(random.uniform(2.5, 3.5))

        if is_jrs_1651_7_11:
            st.session_state["joseon_restoration_candidates"] = [
                "以式年監試覆試, 小學家禮考講試官望, 傳于南翧曰, 以有名稱.",
                "以式年監試覆試, 小學儀禮考講試官望, 傳于南翧曰, 以有名稱.",
            ]
        elif is_jrs_1650_6_11:
            st.session_state["joseon_restoration_candidates"] = [
                "趙壽益, 以義禁府言啓曰, 本府月令醫員金榮齡手本內, 保放罪人李廷顯身病, 更加看審, 則染病之餘, 因添病, 食飮全廢, 氣力澌盡, 比前無異云, 不得已待其差歇還囚之意, 敢啓. 傳曰, 知道.",
                "趙壽益, 以義禁府言啓曰, 本府月令醫員金榮齡手本內, 保放罪人金廷顯身病, 更加看審, 則染病之餘, 因添病, 食飮全廢, 氣力澌盡, 比前無異云, 不得已待其差歇還囚之意, 敢啓. 傳曰, 知道.",
                "趙壽益, 以義禁府言啓曰, 本府月令醫員金榮齡手本內, 保放罪人柳廷顯身病, 更加看審, 則染病之餘, 因添病, 食飮全廢, 氣力澌盡, 比前無異云, 不得已待其差歇還囚之意, 敢啓. 傳曰, 知道.",
                "趙壽益, 以義禁府言啓曰, 本府月令醫員金榮齡手本內, 保放罪人趙廷顯身病, 更加看審, 則染病之餘, 因添病, 食飮全廢, 氣力澌盡, 比前無異云, 不得已待其差歇還囚之意, 敢啓. 傳曰, 知道.",
                "趙壽益, 以義禁府言啓曰, 本府月令醫員金榮齡手本內, 保放罪人申廷顯身病, 更加看審, 則染病之餘, 因添病, 食飮全廢, 氣力澌盡, 比前無異云, 不得已待其差歇還囚之意, 敢啓. 傳曰, 知道.",
                "趙壽益, 以義禁府言啓曰, 本府月令醫員金榮齡手本內, 保放罪人朴廷顯身病, 更加看審, 則染病之餘, 因添病, 食飮全廢, 氣力澌盡, 比前無異云, 不得已待其差歇還囚之意, 敢啓. 傳曰, 知道.",
                "趙壽益, 以義禁府言啓曰, 本府月令醫員金榮齡手本內, 保放罪人元廷顯身病, 更加看審, 則染病之餘, 因添病, 食飮全廢, 氣力澌盡, 比前無異云, 不得已待其差歇還囚之意, 敢啓. 傳曰, 知道.",
                "趙壽益, 以義禁府言啓曰, 本府月令醫員金榮齡手本內, 保放罪人南廷顯身病, 更加看審, 則染病之餘, 因添病, 食飮全廢, 氣力澌盡, 比前無異云, 不得已待其差歇還囚之意, 敢啓. 傳曰, 知道.",
                "趙壽益, 以義禁府言啓曰, 本府月令醫員金榮齡手本內, 保放罪人具廷顯身病, 更加看審, 則染病之餘, 因添病, 食飮全廢, 氣力澌盡, 比前無異云, 不得已待其差歇還囚之意, 敢啓. 傳曰, 知道.",
                "趙壽益, 以義禁府言啓曰, 本府月令醫員金榮齡手本內, 保放罪人洪廷顯身病, 更加看審, 則染病之餘, 因添病, 食飮全廢, 氣力澌盡, 比前無異云, 不得已待其差歇還囚之意, 敢啓. 傳曰, 知道.",
            ]
        elif is_jrs_1688_4_26:
            st.session_state["joseon_restoration_candidates"] = [
                "判府事李尙眞上疏. 大槪, 寒疾方苦, 足病近劇, 起居之班, 不得致身, 乞削臣職, 仍治臣罪事. 入啓. 答曰, 省疏具悉卿懇. 所患如此, 不得進參, 有何所傷? 至於薄略常廩, 不足過辭, 卿其安心, 勿辭領受, 亦勿待罪, 從容善攝. 仍傳曰, 遣史官傳諭.",
                "判府事李端眀上疏. 大槪, 寒疾方苦, 足病近劇, 起居之班, 不得致身, 乞削臣職, 仍治臣罪事. 入啓. 答曰, 省疏具悉卿懇. 所患如此, 不得進參, 有何所傷? 至於薄略常廩, 不足過辭, 卿其安心, 勿辭領受, 亦勿待罪, 從容善攝. 仍傳曰, 遣史官傳諭.",
                "判府事李浣眕上疏. 大槪, 寒疾方苦, 足病近劇, 起居之班, 不得致身, 乞削臣職, 仍治臣罪事. 入啓. 答曰, 省疏具悉卿懇. 所患如此, 不得進參, 有何所傷? 至於薄略常廩, 不足過辭, 卿其安心, 勿辭領受, 亦勿待罪, 從容善攝. 仍傳曰, 遣史官傳諭.",
                "判府事李世眑上疏. 大槪, 寒疾方苦, 足病近劇, 起居之班, 不得致身, 乞削臣職, 仍治臣罪事. 入啓. 答曰, 省疏具悉卿懇. 所患如此, 不得進參, 有何所傷? 至於薄略常廩, 不足過辭, 卿其安心, 勿辭領受, 亦勿待罪, 從容善攝. 仍傳曰, 遣史官傳諭.",
                "判府事李元眔上疏. 大槪, 寒疾方苦, 足病近劇, 起居之班, 不得致身, 乞削臣職, 仍治臣罪事. 入啓. 答曰, 省疏具悉卿懇. 所患如此, 不得進參, 有何所傷? 至於薄略常廩, 不足過辭, 卿其安心, 勿辭領受, 亦勿待罪, 從容善攝. 仍傳曰, 遣史官傳諭.",
                "判府事李正眰上疏. 大槪, 寒疾方苦, 足病近劇, 起居之班, 不得致身, 乞削臣職, 仍治臣罪事. 入啓. 答曰, 省疏具悉卿懇. 所患如此, 不得進參, 有何所傷? 至於薄略常廩, 不足過辭, 卿其安心, 勿辭領受, 亦勿待罪, 從容善攝. 仍傳曰, 遣史官傳諭.",
                "判府事李殷眐上疏. 大槪, 寒疾方苦, 足病近劇, 起居之班, 不得致身, 乞削臣職, 仍治臣罪事. 入啓. 答曰, 省疏具悉卿懇. 所患如此, 不得進參, 有何所傷? 至於薄略常廩, 不足過辭, 卿其安心, 勿辭領受, 亦勿待罪, 從容善攝. 仍傳曰, 遣史官傳諭.",
                "判府事李袤眘上疏. 大槪, 寒疾方苦, 足病近劇, 起居之班, 不得致身, 乞削臣職, 仍治臣罪事. 入啓. 答曰, 省疏具悉卿懇. 所患如此, 不得進參, 有何所傷? 至於薄略常廩, 不足過辭, 卿其安心, 勿辭領受, 亦勿待罪, 從容善攝. 仍傳曰, 遣史官傳諭.",
                "判府事李景眎上疏. 大槪, 寒疾方苦, 足病近劇, 起居之班, 不得致身, 乞削臣職, 仍治臣罪事. 入啓. 答曰, 省疏具悉卿懇. 所患如此, 不得進參, 有何所傷? 至於薄略常廩, 不足過辭, 卿其安心, 勿辭領受, 亦勿待罪, 從容善攝. 仍傳曰, 遣史官傳諭.",
                "判府事李蓍眽上疏. 大槪, 寒疾方苦, 足病近劇, 起居之班, 不得致身, 乞削臣職, 仍治臣罪事. 入啓. 答曰, 省疏具悉卿懇. 所患如此, 不得進參, 有何所傷? 至於薄略常廩, 不足過辭, 卿其安心, 勿辭領受, 亦勿待罪, 從容善攝. 仍傳曰, 遣史官傳諭.",
            ]
        else:
            st.session_state["joseon_restoration_candidates"] = [
                "吳益泳啓曰, 右副承旨李軒卿, 今日不爲仕進, 卽爲牌招, 何如? 傳曰, 允.",
                "尹相翊啓曰, 右副承旨李軒卿, 今日不爲仕進, 卽爲牌招, 何如? 傳曰, 允.",
                "李鍾淳啓曰, 右副承旨李軒卿, 今日不爲仕進, 卽爲牌招, 何如? 傳曰, 允.",
                "吳益泳啓曰, 右副承旨李軒卿, 今日不爲仕進, 竝卽牌招, 何如? 傳曰, 允.",
                "尹相翊啓曰, 右副承旨李軒卿, 今日不爲仕進, 竝卽牌招, 何如? 傳曰, 允.",
                "李鍾淳啓曰, 右副承旨李軒卿, 今日不爲仕進, 仍爲牌招, 何如? 傳曰, 允.",
                "吳益泳啓曰, 右副承旨李軒卿, 今日不爲仕進, 卽爲牌招, 何如? 傳曰, 可.",
                "尹相翊啓曰, 右副承旨李軒卿, 今日不爲仕進, 卽爲牌招, 何如? 傳曰, 可.",
                "李鍾淳啓曰, 右副承旨李軒卿, 今日不爲仕進, 卽爲牌招, 何如? 傳曰, 可.",
                "吳益泳啓曰, 右副承旨李軒卿, 今日不爲仕進, 卽爲牌招, 何如? 傳曰, 允. 又啓曰, 以今日例爲之, 何如? 傳曰, 允.",
            ]

        st.session_state["joseon_selected_candidate_idx"] = 0
        st.session_state["joseon_restored_text"] = st.session_state["joseon_restoration_candidates"][0]
        st.success("2개의 복원 후보가 생성되었습니다.")

    candidates = st.session_state.get("joseon_restoration_candidates", [])
    if not candidates:
        st.info("'복원 실행' 버튼을 눌러 복원 결과를 확인하세요.")
        return

    st.markdown('<div class="panel-title">복원 후보</div>', unsafe_allow_html=True)

    n = len(candidates)
    for row_start in range(0, n, 2):
        cols = st.columns(2, gap="large")

        for j in range(2):
            i = row_start + j
            if i >= n:
                break

            cand = candidates[i]
            candidate_desc = ""


            if is_jrs_1651_7_11:
                rendered = highlight_after_phrase(cand, "小學", 1)

                if i == 0:
                    candidate_desc = "『가례』로 예측함"
                elif i == 1:
                    candidate_desc = "『의례』로 예측함"

            elif is_jrs_1650_6_11:
                rendered = highlight_after_phrase(cand, "保放罪人", 1)

            elif is_jrs_1688_4_26:
                rendered = highlight_before_phrase(cand, "上疏", 2)

            else:
                rendered = cand

            with cols[j]:
                st.markdown(
                    f"""
                    <div class="candidate-card">
                        <div class="candidate-rank">{i+1}위 후보</div>
                        <div class="candidate-text">{rendered}</div>
                        <div class="candidate-desc">{candidate_desc}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
