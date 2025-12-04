## 1. 프로젝트 개요
- 주제: 기획직무 채용공고 데이터 수집 및 기획자 역량 분석
- 목표: 기획자에게 요구되는 역량, 기술스택, 자격요건, 역할 키워드를 데이터화

## 2. 프로젝트 목적
- 기획 직무에 필요한 역량과 트렌드 파악, 데이터 기반 커리어 가이드 구축
- 지원 공고를 편하게 보고 싶은지 / 기획 직무를 분석하고 싶은지

## 3. 데이터 수집 계획
    1) 수집 대상:

        사람인
        https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&cat_kewd=2205%2C1635%2C1649        
        
        원티드
        https://www.wanted.co.kr/wdlist/507?country=kr&job_sort=job.popularity_order&years=-1&locations=all&selected=565&selected=559

        잡코리아
        https://www.jobkorea.co.kr/recruit/joblist?menucode=duty


    2) 수집 방법:
       Selenium

    3) 수집 범위:
        검색키워드: ‘기획’, ‘서비스 기획’, ‘PM’, ‘AI기획', '웹기획', '앱기획'
    
    4) 수집 항목:
        회사명, 채용일자, 신입/경력여부, 직무설명(직무소개), 주요업무(담당업무, 이런 업무를 해요), 자격요건(이런 분들을 찾고 있어요), 우대사항(이런 분이면 더 좋아요), 기술스택(툴, 이런 기술이 필요해요)
        

## 4. 코드 설계
    1) 기능목록 적기
    - 원티드 : 스크롤, 상세페이지 열기 필요 -> selenium 활용
    - 잡코리아 : 홈페이지 지원 / 즉시지원 구분 필요 -> selenium 활용
    - 사람인 : 레이아웃 별 구분 필요 -> selenium 활용


