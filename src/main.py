from typing import Optional
import base64

import fitz
import streamlit as st

from restoration import joseon_restoration_page
from translation import joseon_translation_page

# 이미지 파일명을 기반으로 조건문을 만들어 진행
# 준비되지 않은 파일명이 들어올 경우, OCR 이 안된다 등의 경고 메시지를 만들어두면 좋을 듯

def get_pdf_page_base64(path: str, page: int = 0, dpi: int = 150) -> str:
    """PDF 특정 페이지를 PNG Base64 문자열로 반환"""
    doc = fitz.open(path)
    p = doc.load_page(page)
    pix = p.get_pixmap(dpi=dpi, alpha=False, colorspace=fitz.csRGB)
    img_bytes = pix.tobytes("png")
    doc.close()
    return base64.b64encode(img_bytes).decode("utf-8")


def show_pdf_as_images(
    path: str,
    *,
    title: Optional[str] = None,
    page: Optional[int] = 1,
    dpi: int = 240,
    use_container_width: bool = True,
    max_width_px: Optional[int] = None,
) -> None:
    if title:
        st.subheader(title)

    doc = fitz.open(path)

    def _render_page(pno: int) -> bytes:
        p = doc.load_page(pno)
        pix = p.get_pixmap(dpi=dpi, alpha=False, colorspace=fitz.csRGB)
        return pix.tobytes("png")

    def _show(png_bytes: bytes) -> None:
        if use_container_width:
            st.image(png_bytes, use_container_width=True)
        else:
            if max_width_px is None:
                st.image(png_bytes)
            else:
                st.image(png_bytes, width=max_width_px)

    if page is None:
        for pno in range(doc.page_count):
            _show(_render_page(pno))
    else:
        pno = max(0, min(doc.page_count - 1, page - 1))
        _show(_render_page(pno))

    doc.close()


st.set_page_config(page_title="Joseon Historical Documents Research", layout="wide")


def sidebar_tabs() -> str:
    st.sidebar.markdown(
        """
        <style>
        /* 브랜드 */
        .ari-brand{
            font-weight: 900;
            font-size: 22px;
            letter-spacing: -0.2px;
            margin: 6px 0 2px 0;
            line-height: 1.25;
            background: linear-gradient(120deg, #1E50A3, #2960b4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .ari-sub{
            color: #64748b;
            font-size: 14px;
            margin: 0 0 14px 0;
            font-weight: 500;
        }

        div[role="radiogroup"] {
            width: 100%;
        }

        /* radio를 탭처럼 보이게 */
        div.stElementContainer.element-container {
            width: 100%;
        }
        div[role="radiogroup"] > label {
            border: 1px solid rgba(137, 197, 213, 0.4);
            border-radius: 12px;
            padding: 10px 12px;
            margin: 6px 0;
            background: #ffffff;
            transition: 120ms ease-in-out;
            box-shadow: 0 2px 4px -2px rgba(0, 0, 0, 0.02);
            color: #1e293b;
            width: 100%;
            text-align: center !important;
            box-sizing: border-box;
        }
        div[role="radiogroup"] > label > .st-b8 {
            width: 100%;
            padding-left: 0;
        }
        div[role="radiogroup"] > label:hover {
            background: rgba(137, 197, 213, 0.1);
            transform: translateY(-1px);
            border-color: #1E50A3;
        }

        /* 라디오 동그라미 숨기기 */
        div[role="radiogroup"] > label > div:first-child{
            display: none !important;
        }

        /* 선택된 탭 강조 */
        div[role="radiogroup"] label:has(input[aria-checked="true"]) {
            background: rgba(137, 197, 213, 0.15) !important;
            border: 1px solid #1E50A3 !important;
        }
        div[role="radiogroup"] label:has(input[aria-checked="true"]) span {
            color: #1E50A3 !important;
        }

        /* label 내부 텍스트 */
        div[role="radiogroup"] > label span{
            font-weight: 700;
            font-size: 14.5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
        <div class="ari-brand">조선 고문서 연구</div>
        <div class="ari-sub">DAMI Lab</div>
        <style> .st-emotion-cache-pa57uv > img{border-radius:0;} </style>
        """,
        unsafe_allow_html=True,
    )

    page = st.sidebar.radio(
        "Menu",
        ["소개", "조선 고문서 복원 연구", "조선 고문서 번역 연구"],
        label_visibility="collapsed",
        index=0,
    )

    st.sidebar.markdown("---")

    # Logo Images
    logos = st.sidebar.container(gap="medium")
    with logos:
        st.image("fig/kangwon.png", use_container_width=True)
        st.image("fig/DAMI_LOGO.svg", use_container_width=True)

    st.sidebar.markdown(
        '<div style="font-size: 0.85rem; color: rgba(49, 51, 63, 0.6);">ⓒ DAMI Lab</div>',
        unsafe_allow_html=True,
    )
    return page


def home_page() -> None:
    st.markdown(
        """
        <style>
        .main-hero-title {
            font-size: 48px;
            font-weight: 900;
            background: linear-gradient(120deg, #1E50A3, #2960b4, #123e85);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
            margin-bottom: 24px;
            line-height: 1.1;
        }
        </style>
        <div class="main-hero-title">조선 고문서 연구</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")

    col_ari, col_herit = st.columns([1, 1], gap="large")

    from textwrap import dedent

    import streamlit.components.v1 as components

    card_css = dedent(
        """
        <style>
        html, body { margin: 0; padding: 0; }

        .card-wrap {
            width: 100%;
            font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
        }

        .card {
            width: 100%;
            box-sizing: border-box;
            border: 1px solid rgba(137, 197, 213, 0.4);
            border-top: 4px solid #1E50A3;
            border-radius: 18px;
            padding: 22px 22px 18px 22px;   /* 여백 ↑ */
            background: #ffffff;
            box-shadow: 0 4px 12px rgba(30, 80, 163, 0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px -3px rgba(30, 80, 163, 0.08);
            border-color: rgba(30, 80, 163, 0.4);
        }

        /* 타이틀/서브타이틀 폰트 ↑ */
        .title {
            font-size: 28px;               /* 22 -> 26 */
            font-weight: 900;
            letter-spacing: -0.02em;
            margin: 0 0 10px 0;
            color: #1E50A3;
        }

        .subtitle {
            font-size: 16.5px;             /* 14.5 -> 16.5 */
            line-height: 1.75;             /* 1.65 -> 1.75 */
            margin: 0 0 14px 0;
            color: #64748b;
        }

        /* 칩 폰트/패딩 ↑ */
        .chips { display:flex; flex-wrap:wrap; gap:10px; margin: 12px 0 8px 0; }
        .chip {
            border: none;
            border-radius: 999px;
            padding: 8px 14px;             /* ↑ */
            font-size: 14.5px;             /* 13 -> 14.5 */
            font-weight: 800;
            background: #FF9696;
            color: #ffffff;
            box-shadow: 0 2px 6px rgba(255, 150, 150, 0.4);
        }

        /* 박스/리스트 폰트 ↑ */
        .grid { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:12px; }
        .box {
            border: 1px solid rgba(137, 197, 213, 0.4);
            border-radius: 16px;
            padding: 14px;                 /* 12 -> 14 */
            background: #ffffff;
            box-shadow: 0 2px 4px rgba(30, 80, 163, 0.02);
        }
        .box h4 {
            margin: 0 0 8px 0;
            font-size: 15.5px;             /* 14 -> 15.5 */
            font-weight: 900;
            color: #1E50A3;
        }
        .box ul { margin: 8px 0 0 18px; padding: 0; }
        .box li {
            font-size: 15.5px;             /* 13.2 -> 14.5 */
            line-height: 1.75;
            color: #1e293b;
        }

        .divider { height:1px; background: rgba(137, 197, 213, 0.4); margin: 16px 0 14px 0; }

        .steps { display:flex; gap:12px; }
        .step {
            flex-grow: 1;
            border: 1px solid rgba(137, 197, 213, 0.4);
            border-radius: 16px;
            padding: 14px;                 /* 12 -> 14 */
            background: #ffffff;
            box-shadow: 0 2px 4px rgba(30, 80, 163, 0.02);
        }
        .step .k {
            font-size: 12.5px;             /* 12 -> 12.5 */
            font-weight: 900;
            color: #FF9696;
            margin-bottom: 8px;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }
        .step .t {
            font-size: 16px;               /* 14 -> 16 */
            font-weight: 900;
            color: #1E50A3;
            margin-bottom: 6px;
        }
        .step .d {
            font-size: 14.5px;             /* 13 -> 14.5 */
            line-height: 1.7;
            color: #1e293b;
        }


        @media (max-width: 900px) {
            .grid { grid-template-columns:1fr; }
            .steps { grid-template-columns:1fr; }
        }
        </style>
        """
    )

    # PDF 페이지를 Base64로 변환 (해상도 적절히 조절)
    ari_b64 = get_pdf_page_base64("fig/ari_method.pdf", page=0, dpi=200)
    herit_b64 = get_pdf_page_base64("fig/herit_method.pdf", page=0, dpi=200)

    ari_html = dedent(
        f"""
    {card_css}
    <div class="card-wrap">
      <div class="card">
        <div class="title">
        ARI <span style="font-size: 0.78em; font-weight: bolder; opacity: 0.95;">(조선 고문서 복원 AI)</span>
        </div>
        <!-- Method Image Inserted Here -->
        
        <img src="data:image/png;base64,{ari_b64}" style="width: 100%; 

            height: 350px; 

            object-fit: contain; 

            background: #ffffff; 

            border-radius: 8px; 

            margin-bottom: 16px; 

            border: 1px solid rgba(0,0,0,0.05);" />
        <div class="subtitle">
            ARI는 조선시대 고문헌의 훼손 한자(□, ◆ 등)를 복원하도록 학습된 RAG 기반 LLM 복원 모델입니다.
        </div>

        <div class="chips">
          <div class="chip">관련 문헌 기반 RAG</div>
          <div class="chip">개체명 복원</div>
          <div class="chip">상위 2개 복원 후보 제공</div>
        </div>

        <div class="grid">
          <div class="box">
            <h4>핵심 아이디어</h4>
            <ul>
              <li>훼손 문서와 문맥적으로 유사한 사료를 검색 및 참조하여 복원 정확도를 극대화했습니다.</li>
              <li>인명, 지명, 관직, 연호 등 개체명 복원에 강점을 갖도록 설계하였습니다.</li>
              <li>문서 내 문맥과 외부 지식을 유기적으로 활용하여 개체명뿐만 아니라 일반 훼손 한자 복원 전반의 범용성을 확보했습니다.</li>
            </ul>
          </div>
          <div class="box">
            <h4>출력 형태</h4>
            <ul>
              <li>단일 정답이 아닌 상위 후보들을 순위로 제시해 전문가 검토가 용이합니다.</li>
              <li>상위 2개의 복원 후보를 제공하여 전문가들의 탐색 비용과 복원 소요 시간을 절감할 수 있습니다.</li>
            </ul>
          </div>
        </div>

        <div class="divider"></div>

        <div class="steps" style="display: flex; gap: 12px; align-items: stretch;">
          
          <div class="step" style="flex: 1; display: flex; flex-direction: column;">
            <div class="k">Step 1</div>
            <div class="t">이미지 입력</div>
            <div class="d">훼손 문서의 이미지에서 OCR 텍스트를 확보합니다.</div>
          </div>

          <div class="step" style="flex: 1; display: flex; flex-direction: column;">
            <div class="k">Step 2</div>
            <div class="t">관련 문서 검색</div>
            <div class="d">유사도 검색으로 훼손 문서와 유사한 문서들을 가져옵니다.</div>
          </div>

          <div class="step" style="flex: 1; display: flex; flex-direction: column;">
            <div class="k">Step 3</div>
            <div class="t">복원 후보 제공</div>
            <div class="d">훼손 문서와 관련 문서들을 입력으로 ARI가 상위 2개의 후보를 제공합니다.</div>
          </div>
      </div>
    </div>
    """
    )

    herit_html = dedent(
        f"""
    {card_css}
    <div class="card-wrap">
      <div class="card">
        <div class="title">
        HERIT <span style="font-size: 0.78em; font-weight: bolder; opacity: 0.95;">(고문서 번역 특화 AI)</span>
        </div>
        <!-- Method Image Inserted Here -->
        <img src="data:image/png;base64,{herit_b64}" style="width: 100%; 

            height: 350px; 

            object-fit: contain; 

            background: #ffffff; 

            border-radius: 8px; 

            margin-bottom: 16px; 

            border: 1px solid rgba(0,0,0,0.05);" />
        <div class="subtitle">
          HERIT은 조선왕조실록·승정원일기 등 고문헌 원문을 영어로 번역하도록 학습된 번역 모델입니다.
        </div>

        <div class="chips">
          <div class="chip">RAG 기반 데이터 증강</div>
          <div class="chip">Proposer-Fuser</div>
          <div class="chip">시대 편향 완화</div>
        </div>

        <div class="grid">
          <div class="box">
            <h4>핵심 아이디어</h4>
            <ul>
              <li>고문서의 한자-영문 병렬데이터 부족을 데이터 증강으로 보완하여 시대 편향을 줄이고 번역 성능을 높혔습니다. 데이터는 다음과 같이 증강되었으며, 이를 통해 모델 번역 성능의 준수함을 보장했습니다.</li>
              <ul>
                <li>용어집, RAG를 통한 외부 지식을 활용으로, 인명·지명 등의 번역 정확도와 문맥 이해도를 향상시켰습니다.</li>
                <li>다양한 시대의 문서를 포함하여, 특정 시대에 치우치지 않는 번역 모델을 구축했습니다.</li>
              </ul>
            </ul>
          </div>
          <div class="box">
            <h4>출력 형태</h4>
            <ul>
              <li>HERIT과 Gemini를 활용하여 원문에 대한 번역을 제공합니다.</li>
            </ul>
          </div>
        </div>

        <div class="divider"></div>

        <div class="steps">
          <div class="step"><div class="k">Step 1</div><div class="t">입력</div><div class="d">원문 또는 OCR 텍스트를 입력합니다.</div></div>
          <div class="step"><div class="k">Step 2</div><div class="t">정리</div><div class="d">최종 번역을 생성하고, 타 모델과 비교합니다.</div></div>
        </div>
      </div>
    </div>
    """
    )

    with col_ari:
        components.html(ari_html, height=1130)

    with col_herit:
        components.html(herit_html,height=1130)

def main() -> None:
    page = sidebar_tabs()

    if page == "소개":
        home_page()
    elif page == "조선 고문서 복원 연구":
        joseon_restoration_page()
    else:
        joseon_translation_page()


if __name__ == "__main__":
    main()
