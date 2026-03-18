from typing import Dict
import streamlit as st
import time
import random

def get_mock_ocr_text(filename: str) -> str:
    """파일명에 따라 모의 OCR 텍스트를 반환합니다."""
    if "ilseongnok" in filename.lower():
        # 일성록 예시 (정조 1년)
        return (
            "予 詣 景慕宮 展拜。\n"
            "是日, 予 詣 眞殿 展拜。\n"
            "藥房 提調 徐命善, 此 承旨 李在簡 等 請 對。\n"
            "上 引見 藥房 提調 命善 · 副提調 鄭民始 · 假注書 朴天行 · 記事官 洪承億 · 金炳德, 入 侍。"
        )
    elif "seungjeongwon" in filename.lower():
        # 승정원일기 예시
        return (
            "○ 辛卯 十一月 二十日 未時, 上 御 重熙堂。\n"
            "召見 大臣 備局 堂上。\n"
            "領議政 金左根, 右議政 趙斗淳, 行 左承旨 金世均, 假注書 李寅承, 記事官 洪承億 · 金炳德, 各 持 請對 擧案, 入 侍。"
        )
    elif "어사한" in filename or "eosoahan" in filename.lower():
        return "宥魚思漢, 京外從便."
    elif "방자" in filename or "bangja" in filename.lower():
        return "宜給宣飯及房子, 炊飯, 汲水人等."
    elif "임진왜란" in filename or "imjin" in filename.lower():
        return "倭賊大擧入寇, 陷釜山鎭, 僉使鄭潑戰死; 陷東萊府, 府使宋象賢死之."
    else:
        # 기본 예시 (천자문 앞부분)
        return (
            "天地玄黃 (천지현황) : 하늘은 검고 땅은 누르며\n"
            "宇宙洪荒 (우주홍황) : 우주는 넓고 거치니라\n"
            "日月盈昃 (일월영측) : 해와 달은 차고 기울며\n"
            "辰宿列張 (진숙열장) : 별들은 넓게 펴져 있도다"
        )

def get_mock_translation_text(filename: str) -> Dict[str, str]:
    """파일명에 따라 모의 번역 텍스트를 반환합니다."""
    if "어사한" in filename or "eosoahan" in filename.lower():
        return {
            "gemini": "Yu Yu thought of Han, and the capital and outer areas followed suit.",
            "herit": "The king pardoned Eo Sahan and allowed him to reside in a place of his choice outside the capital."
        }
    elif "방자" in filename or "bangja" in filename.lower():
        return {
            "gemini": "It is appropriate to provide meals, a house, and servants for cooking and fetching water.",
            "herit": "We should provide them with meals, female palace servants, cooks, and water carriers."
        }
    elif "임진왜란" in filename or "imjin" in filename.lower():
        return {
            "gemini": "The Japanese invaders launched a major incursion, capturing Busan Jin, where Admiral Jeong Pal died in battle. They then captured Dongnae-bu, where Governor Song Sang-hyeon died.",
            "herit": "Japanese pirates invaded in large numbers, captured Busan Garrison, and killed Second Commander Jeong Bal in battle. They also captured Dongnae Prefecture and killed Magistrate Song Sanghyeon."
        }
    else:
        return {
            "gemini": "dkdk",
            "herit": "dldl"
        }

def joseon_translation_page() -> None:
    # --- CSS Styling (Restoration Style) ---
    st.markdown(
        """
        <style>
        /* Base Container & Animation */
        
        .hero-title {
            font-size: 42px;
            font-weight: 900;
            background: linear-gradient(120deg, #1E50A3, #2960b4, #123e85);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
            margin-bottom: 8px;
            line-height: 1.2;
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

        /* Result Cards */
        .result-card {
            border: 1px solid rgba(137, 197, 213, 0.4);
            border-radius: 16px;
            padding: 20px;
            background: #ffffff;
            box-shadow: 0 2px 8px rgba(30, 80, 163, 0.05);
            height: 100%;
            border-top: 4px solid #1E50A3; /* Top border accent */
        }
        
        .result-card.secondary-card {
            border-top: 4px solid #FF9696; /* Second card accent color */
        }

        .result-header {
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
        
        .result-card.secondary-card .result-header {
            color: #d15656;
            border-bottom: 1px dashed rgba(255, 150, 150, 0.5);
        }

        .result-content {
            font-size: 16px;
            line-height: 1.7;
            color: #1e293b;
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

    # --- Header & KPIs ---
    st.markdown(
        '<div class="hero-title" style="font-size:48px; font-weight:800; line-height:1.1;">HERIT: Translation for Joseon Historical Documents</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="hero-sub">고문서 이미지 업로드 시, OCR을 진행하여 HERIT과 Gemini-2.5-Flash의 번역 결과를 대조 제공합니다.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="kpi-wrap">
            <div class="kpi"><p class="k">번역 파이프라인</p><p class="v">이미지 → OCR → 번역</p></div>
            <div class="kpi"><p class="k">지원 모델</p><p class="v">HERIT, Gemini-2.5-flash</p></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Step 1: 이미지 업로드 및 OCR ---
    st.markdown(
        '<p class="section-title"><span class="section-num">1)</span><span class="section-text">이미지 업로드 및 OCR</span> <span class="badge">Step 1</span></p>',
        unsafe_allow_html=True,
    )
    
    uploaded_file = st.file_uploader("이미지 파일 선택", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

    # 파일 변경 감지 및 초기화
    if uploaded_file:
        if st.session_state.get("last_trans_filename") != uploaded_file.name:
            st.session_state["trans_ocr_result"] = ""
            st.session_state.pop("trans_result", None)
            st.session_state["last_trans_filename"] = uploaded_file.name
    else:
        # 파일 제거 시 상태 초기화
        st.session_state.pop("last_trans_filename", None)
        st.session_state.pop("trans_ocr_result", None)
        st.session_state.pop("trans_result", None)

    if uploaded_file is None:
        st.info("이미지를 업로드하면 OCR 및 번역 기능을 사용할 수 있습니다.")
        st.markdown("---")
        # Step 2 Placeholder
        st.markdown(
            '<p class="section-title"><span class="section-num">2)</span><span class="section-text">번역</span> <span class="badge">Step 2</span></p>',
            unsafe_allow_html=True,
        )
        st.warning("먼저 이미지를 업로드해 주세요.")
        return

    filename = uploaded_file.name

    col1, col2 = st.columns([1, 2], gap="medium")

    with col1:
        st.markdown('<div class="panel-title">이미지 미리보기</div>', unsafe_allow_html=True)
        st.image(uploaded_file, use_container_width=True)

    with col2:
        st.markdown('<div class="panel-title">OCR 결과</div>', unsafe_allow_html=True)
        st.markdown('<div class="panel-sub">OCR 실행 후 결과를 확인할 수 있습니다.</div>', unsafe_allow_html=True)

        if st.button("OCR 실행", use_container_width=True):
            with st.spinner("OCR 분석 중..."):
                time.sleep(random.uniform(2.5, 3.5))
                st.session_state["trans_ocr_result"] = get_mock_ocr_text(filename)
                # OCR이 새로 실행되면 기존 번역 결과는 초기화
                if "trans_result" in st.session_state:
                    del st.session_state["trans_result"]
        
        ocr_text = st.session_state.get("trans_ocr_result", "")
        if ocr_text:
            st.text_area("ocr_result_area", value=ocr_text, height=20, label_visibility="collapsed")
        else:
            st.info("OCR 실행 버튼을 눌러 텍스트를 추출하세요.")

        # --- Step 2: 번역 ---
        st.markdown(
            '<p class="section-title"><span class="section-num">2)</span><span class="section-text">번역</span> <span class="badge">Step 2</span></p>',
            unsafe_allow_html=True,
        )
        
        if not ocr_text:
            st.warning("먼저 OCR을 실행하여 텍스트를 추출해 주세요.")
            return

        st.caption("추출된 텍스트를 바탕으로 AI 번역을 수행합니다.")

        if st.button("번역 실행", type="primary", use_container_width=True):
            with st.spinner("번역 생성 중..."):
                time.sleep(random.uniform(2.5, 3.5))
                st.session_state["trans_result"] = get_mock_translation_text(filename)
        
        trans_result = st.session_state.get("trans_result")
        
        if trans_result:
            st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)
            r_col1, r_col2 = st.columns(2, gap="medium")
            with r_col1:
                st.markdown(f'''
                    <div class="result-card">
                        <div class="result-header">
                            <span style="font-size: 18px;">🏛️</span> HERIT 번역
                        </div>
                        <div class="result-content">{trans_result.get("herit", "")}</div>
                    </div>
                ''', unsafe_allow_html=True)
            with r_col2:
                st.markdown(f'''
                    <div class="result-card secondary-card">
                        <div class="result-header">
                            <span style="font-size: 18px;">✨</span> Gemini-2.5-flash 번역
                        </div>
                        <div class="result-content">{trans_result.get("gemini", "")}</div>
                    </div>
                ''', unsafe_allow_html=True)
