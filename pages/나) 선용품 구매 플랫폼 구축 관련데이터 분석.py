import streamlit as st
st.set_page_config(layout='wide')
st.image('img/나).png')
st.markdown(
    '''
        ##### 1. 위 이미지와 같이, 현재 부산에는 *해외선사 및 외국인 선원들을 위한 선용품 구매 플랫폼이 없는 상황*임.
        ##### 2. 오프라인 방식의 선용품 관련 기관이 있지만, 판매품목이 대부분 로프, 튜브 등으로 구성되어 있음.
        ##### 3. 따라서, 외국인 선원을 위한 __온라인 선용품 구매플랫폼 구축이 필요__하다고 판단했으며 필요한 과업들을 선정하고 데이터 분석을 진행했음.
        ##### 4. 선용품 카테고리 분석  
        * __년간 선용품 품목별 추이를 분석__하여 __인기 품목 Top 4를 선정__
        * 해당 데이터를 기반으로 온라인 선용품 구매플랫폼 구축시 판매할 상품관련 품목선정에 참고할 수 있음
        ##### 5. 기업 리스트 분석
        * 선용품 구매 플랫폼 구축 완료 후 선정된 __Top 4 품목을 유통/판매 할 수 있는 기업을 소싱하는데 참고__하기 위해 정보 수집
        ##### 6.워드 클라우드
        * 소싱한 기업에서 __품목별로 키워드를 시각화__함으로써 __자사 메케팅 및 제품 개발에 참고__할 수 있음
    '''
)
