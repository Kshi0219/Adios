import streamlit as st
import numpy as np
st.image('img/나).png')
st.markdown(
    '''
        ### 1. 위 이미지 내용 중 여행/숙박 코스 추천서비스 관련하여, 해당 서비스 대상을\n \t### 해외 선사에 탑승한 외국인 선원으로 선정하였음.
        ##### 2. 외국인 선원의 체류시간 파악을 위해 가-2) 화물처리실적-체류시간 상관분석 을 위해 수집한 부산항 체류시간 데이터를 활용함.
    '''
)
st.image('img/time_combined.png',caption='이미지:년도별 평균체류시간, describe')
st.markdown('''
                ##### 3. 년도별 체류시간의 집계를 위해, 데이터 전처리 후 describe() 함수를 적용하여 최소/최대/평균 체류시간을 분석했음.
                ##### 4. __평균 체류시간은 84시간(3일 12시간), 최소 9시간__이라는 것을 파악하였고, 이에 따라 __부산 신항 주변을 기준으로 7시간 코스, 3일 코스__를 짰음.
                ##### 5. 코스 시각화를 위해 맛집, 관광지, 숙박 관련 데이터를 __크롤링 후 Google API를 활용하여 장소별 위도/경도 파악__후 다-1, 다-2,다-3과 같이 시각화를 진행했음
                ##### 6. 5번 과정을 거쳐 __OSMNX 라이브러리를 활용__하여 다-4) 와 같이 체류시간별 코스를 시각화하였음.
            ''')