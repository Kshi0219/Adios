import streamlit as st
st.markdown(
    '''
    ##### 초기가설
    __”부산항 수출〮입 물동량이 증가한다면, 입항한 외국인 선원들의 체류시간 또한 증가할 것이다.”__
    ##### 가설검증
    __[가설] 물동량이 증가하면 화물처리물동량 또한 증가할 것이다.__
    * 수집데이터 : 년간 부산항 물동량, 년간 부산항 화물처리량
    * 상관분석 결과 : 0.999 양의 상관관계로 __물동량이 증가하면 화물처리량도 증가함.__
    * 가-1) 물동량 - 화물 처리실적 상관분석 참고 요망.<br>
    __[가설] 화물처리물동량이 증가하면 체류시간 또한 증가할 것이다.__
    * 수집데이터 : 년간 부산항 물동량, 년간 부산항 화물처리량.
    * 상관분석 결과 : 0.493 양의 상관관계로 __화물처리량이 증가하면 해외 선박/선원의 체류시간도 증가함.__
    * 가-2) 화물 처리실적 - 체류시간 상관분석 참고 요망
    __년간 부산항 입/출항 선원수__
    * 시각화 그래프 : 년간 부산항 입/출항 선원수.
    * 시각화 그래프 : 년,월별 화물처리실적, 체류시간 추이.
    * 해석 : 년간 부산항 입/출항 선원수 그래프 추이는 년,월별 화물처리실적, 체류시간 추이를 따라가는것으로 예상할 수 있음.
    * 부산항만공사 체인포탈에서 제공하는 '년간 부산항 입/출항 선원수'관련 데이터 기간이 2009~2021년까지의 데이터를 제공.
    ##### 결론
        * 부산항 물동량이 증가됨에 따라 화물처리량 또한 증가되고, 입출항 해외 선원수 또한 함께 증가됨.
        * 이는 부산항만공사에서 해외 선박소속의 선원들을 대상으로한 서비스를 기획하고 시행할 수 있는 명분으로 작용할 수 있음.
'''
)