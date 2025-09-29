import streamlit as st

# ------------------------------
# MBTI → 직업 추천 (고등학생용)
# Streamlit Cloud에서 바로 실행 가능한 단일 파일
# 외부 라이브러리 설치 없이 동작 (표준 라이브러리 + streamlit)
# ------------------------------

st.set_page_config(page_title="MBTI 직업 추천", page_icon="🎯", layout="centered")

# 간단한 스타일링
st.markdown(
    """
    <style>
      .big-title {font-size: 2rem; font-weight: 800;}
      .tag {display:inline-block; padding:4px 10px; border-radius:999px; background:#f1f5f9; margin-right:6px; font-size:0.85rem}
      .card {border-radius:16px; padding:18px; background:#ffffff; border:1px solid #e5e7eb}
      .soft {color:#64748b}
    </style>
    """,
    unsafe_allow_html=True,
)

# 데이터 정의
MBTI_TYPES = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ",
]

CAREER_DB = {
    "ISTJ": {
        "traits": ["체계적", "책임감", "신뢰도 높음"],
        "careers": [
            ("공무원", "규정과 절차 기반의 안정적 업무"),
            ("회계사", "정확한 수치 관리와 자료 검증"),
            ("품질관리 엔지니어", "표준 준수·검사·개선 활동")
        ],
    },
    "ISFJ": {
        "traits": ["배려", "성실", "실용적"],
        "careers": [
            ("간호사", "세심한 보살핌과 팀워크"),
            ("초등교사", "기초 학습 지도와 돌봄"),
            ("치위생사", "정확·깨끗함·대인 서비스")
        ],
    },
    "INFJ": {
        "traits": ["통찰", "가치지향", "깊은 공감"],
        "careers": [
            ("상담심리사", "개인의 성장 지원"),
            ("사회복지 기획자", "사회적 임팩트 설계"),
            ("콘텐츠 기획자", "의미 중심 스토리텔링")
        ],
    },
    "INTJ": {
        "traits": ["전략", "분석", "독립성"],
        "careers": [
            ("데이터 사이언티스트", "모델링·문제 해결"),
            ("전략기획", "장기 로드맵 설계"),
            ("연구원", "가설 검증·실험 설계")
        ],
    },
    "ISTP": {
        "traits": ["문제해결", "현실감각", "차분함"],
        "careers": [
            ("기계 엔지니어", "설계·정비·최적화"),
            ("응급구조/소방", "실전 상황 대처"),
            ("드론 정비/운용", "정밀 조작·유지보수")
        ],
    },
    "ISFP": {
        "traits": ["감성", "온화", "실용적 창의"],
        "careers": [
            ("그래픽 디자이너", "감각적 시각 표현"),
            ("플로리스트", "섬세한 미적 구성"),
            ("치과기공사", "정밀 수작업")
        ],
    },
    "INFP": {
        "traits": ["이상", "진정성", "창작 성향"],
        "careers": [
            ("작가/에디터", "글로 메시지 전하기"),
            ("임상심리사", "내면 탐색과 회복 지원"),
            ("UX 리서처", "사용자 공감·문제 정의")
        ],
    },
    "INTP": {
        "traits": ["호기심", "논리", "아이디어"],
        "careers": [
            ("소프트웨어 엔지니어", "추상→구현"),
            ("기초과학 연구원", "이론 탐구"),
            ("특허전문가", "발명 분석·문서화")
        ],
    },
    "ESTP": {
        "traits": ["활동적", "현장력", "결단"],
        "careers": [
            ("영업/세일즈", "대면 설득·성과 지향"),
            ("스포츠 트레이너", "즉각 피드백·동기부여"),
            ("응급구조사", "현장 판단·실행")
        ],
    },
    "ESFP": {
        "traits": ["사교성", "에너지", "감각"],
        "careers": [
            ("이벤트 플래너", "현장 운영·연출"),
            ("방송/공연 스태프", "팀워크·현장감"),
            ("뷰티 아티스트", "트렌드·표현")
        ],
    },
    "ENFP": {
        "traits": ["열정", "창의", "사람 중심"],
        "careers": [
            ("마케터", "아이디어·캠페인 설계"),
            ("사회혁신/비영리 기획", "의미·임팩트"),
            ("프로덕트 매니저(초기)", "문제 발견·조율")
        ],
    },
    "ENTP": {
        "traits": ["도전", "토론", "발명"],
        "careers": [
            ("스타트업 창업가", "새로운 가치 창출"),
            ("전략컨설턴트", "비즈니스 문제 해결"),
            ("UX 디자이너", "실험적 프로토타이핑")
        ],
    },
    "ESTJ": {
        "traits": ["조직화", "리더십", "실행"],
        "careers": [
            ("프로젝트 매니저", "목표-일정-성과 관리"),
            ("군 장교", "규율·지휘"),
            ("생산관리", "공정 최적화")
        ],
    },
    "ESFJ": {
        "traits": ["협력", "배려", "실무 능력"],
        "careers": [
            ("학교행정/학사담당", "조정·지원"),
            ("HR 매니저", "조직 문화·채용"),
            ("병원 코디네이터", "대면 서비스")
        ],
    },
    "ENFJ": {
        "traits": ["리더십", "동기부여", "커뮤니케이션"],
        "careers": [
            ("교사", "학습 설계·코칭"),
            ("커뮤니티 매니저", "집단 성장 촉진"),
            ("HRD/교육기획", "교육 프로그램 설계")
        ],
    },
    "ENTJ": {
        "traits": ["비전", "결단", "조직 설계"],
        "careers": [
            ("경영컨설턴트", "전사 전략·변화관리"),
            ("투자/VC", "사업 분석·의사결정"),
            ("기술 PM", "스케일업·로드맵")
        ],
    },
}

SUBJECT_TIPS = {
    # 각 유형에 어울리는 고등학교 과목·활동 힌트 (학생 친화 요약)
    "분석형(NT)": ["수학Ⅱ/미적분", "물리학Ⅰ·Ⅱ", "정보/프로그래밍", "과학탐구 보고서"],
    "현장형(ST)": ["공학일반", "과학탐구실험", "지구과학Ⅰ", "안전/응급 교육 봉사"],
    "공감형(NF)": ["사회/윤리", "심리학 관련 독서", "동아리 멘토링", "봉사·캠페인"],
    "실용형(SF)": ["가정·보건", "미술/디자인", "생명과학Ⅰ", "현장체험·포트폴리오"],
}

# 도우미 함수

def group_of(mbti: str) -> str:
    # 간단 그룹: 마지막 두 글자 기준 + N/S, T/F
    n = "N" in mbti
    t = "T" in mbti
    sfx = ("NT" if (n and t) else ("NF" if (n and not t) else ("ST" if (not n and t) else "SF")))
    return sfx

# 헤더
st.markdown('<div class="big-title">🎯 MBTI 기반 직업 추천 (고등학생용)</div>', unsafe_allow_html=True)
st.write("\n")

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("**👉 내 MBTI를 선택하세요**")
with col2:
    st.markdown("**🧭 참고:** 결과는 *진로 탐색의 출발점*이에요. 확정 답이 아니라 *단서*예요!")

user_type = st.selectbox("MBTI 선택", MBTI_TYPES, index=MBTI_TYPES.index("ENFP"))

if user_type:
    data = CAREER_DB[user_type]
    tags = " ".join([f"<span class='tag'>#{t}</span>" for t in data["traits"]])

    st.markdown(f"<div class='card'>"
                f"<h3>💼 추천 직업 Top 3 — <code>{user_type}</code></h3>"
                f"<div class='soft'>특징: {tags}</div>"
                f"</div>", unsafe_allow_html=True)

    st.write("")

    for i, (job, why) in enumerate(data["careers"], start=1):
        st.markdown(
            f"""
            <div class='card'>
              <h4>{i}. {job} {'✨' if i==1 else ('🚀' if i==2 else '🌿')}</h4>
              <div class='soft'>이 유형과 잘 맞는 이유: {why}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    grp = group_of(user_type)
    tips = SUBJECT_TIPS.get({
        "NT": "분석형(NT)",
        "NF": "공감형(NF)",
        "ST": "현장형(ST)",
        "SF": "실용형(SF)",
    }[grp], [])

    with st.expander("📘 과목·활동 힌트 (고1~고3)"):
        st.markdown(
            """
            - 📚 **추천 과목/활동**: {tips}
            - 📝 **작은 미션**: 관심 직업 1개를 고르고, 학교 활동·독서·대회·동아리에서 *당장 할 수 있는 1가지*를 정해보세요.
            - 🧠 **핵심 태도**: 결과보다 **과정 기록**(노트/포트폴리오)이 진로 스토리를 만듭니다.
            """.format(tips=", ".join(tips))
        )

# 하단 안내
st.markdown("---")
with st.container():
    st.markdown(
        """
        🧩 **주의사항**
        - MBTI는 성격 경향을 *간단히* 보는 도구예요. 모든 사람은 상황에 따라 다양하게 행동할 수 있어요.
        - 더 깊은 탐색을 위해서는 **홀랜드 검사(RIASEC)**, **적성/흥미 검사**, **현장 체험**을 함께 고려해 보세요.
        - 필요하면 담임/진로 상담 선생님과 꼭 상의하세요. 🙌
        """
    )

# 사이드바: 빠른 안내
with st.sidebar:
    st.markdown("## 🧭 사용법")
    st.write("1) MBTI 선택 → 2) 추천 직업 읽기 → 3) 과목·활동 힌트 확인")
    st.write("\n")
    st.markdown("**Tip**: 마음이 끌리는 직업이 있다면, 학교 활동과 연결해 *작은 실험*을 해보세요!")

# 앱 실행 안내 (로컬)
if __name__ == "__main__":
    # Streamlit은 'streamlit run app.py' 형태로 실행됩니다.
    # 여기서는 별도 실행 로직이 필요 없습니다.
    pass
