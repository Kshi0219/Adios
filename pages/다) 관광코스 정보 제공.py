import streamlit as st
st.image('img/나).png',caption='체류시간.describe()')
st.markdown(
    '''
        ### 1. 위 이미지 내용 중 여행/숙박 코스 추천서비스 관련하여, 해당 서비스 대상을 해외 선사에 탑승한 외국인 선원으로 선정하였음.
        ### 2. 외국인 선원의 체류시간 파악을 위해 가-2) 화물처리실적-체류시간 상관분석 을 위해 수집한 부산항 체류시간 데이터를 활용함.
    '''
)
st.image('img/stayed_time_describe.png',caption='이미지:describe')
st.markdown('''### 3. 년도별 체류시간의 집계를 위해, 데이터 전처리 후 describe() 함수를 적용하여 최소/최대/평균 체류시간을 분석했음.''')