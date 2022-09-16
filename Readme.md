## *Before Project* 
 - 검색 엔진 고도화를 위한 자연어 처리
 - Dataset : 자사 마켓 데이터
 - 요구사항 : 형태소 분석, 한의계 도메인 단어사전(유의어, 불용어 처리 등) 구축
 >##### 현행
 >* 현 검색엔진은 <Strong>Meilisearch</Strong>를 사용, 검색 인덱스 생성 시 형태소 분석을 처리하지 않고 토크나이징 된 상태로 인덱스를 생성
 >>
 >##### To do
 >* 한의계 도메인 단어사전 구축 및 단어사전 활용을 통한 검색엔진 성능 비교
 >* 추가로 검색엔진의 성능을 높일 수 있을 만한 방법을 강구
 - 질문 사항
 >* 현재 사용하고 있는 검색 엔진과 Tokenizer
 >* 도메인 단어사전의 활용 방법 (사측에서 제작하여 활용하고자 하는 방향)

## 1. 문제 정의
 - 단어 사이 공백의 부재 시 검색의 성능 저하 발생
 > <Strong>ex. 필립스500W전구 -> 필립스 500W 전구</Strong>

#### 진행 절차
 > <Strong> 1. Meilisearch의 이해 (API가 어떻게 검색을 하는지, API의 Tokenizer가 어떤 방식으로 토큰화 하는지 등)</Strong>

##### 참고 사항
 > <Strong> 1. Meilisearch의 형태소 분석기 : Charabia -> Charabia의 일본어 specialized segmentation : lindera (Rust 기반의 형태소 분석기)</Strong>
 > <Strong> 2. mecab에 도메인 단어 사전으로 구축한 형태소 사전 추가 가능</Strong>

## 2. EDA
 --

## 3. 문제 해결 방법 탐색 및 전략 수립


## 4. 실험 결과 분석 및 해석


## 5. 결론


## 데모 제작

## Meilisearch (Appendix)
 - 최대 단어 : 10개 단어
 - 최대 길이 : 65536
 - 영어, 중국어 및 일본어와 같이 공백을 단어 구분자로 사용하는 언어의 토큰화
 - 오타 허용 : 오타와 맞춤법 오류를 이해
 - Tokenizer (charabia) : https://github.com/meilisearch/charabia/blob/main/CONTRIBUTING.md
 - Tokenizer's release process(for 
 internel team only) as <Strong>Semantic Versioning Convention</Strong>
 https://semver.org/lang/ko

 ## Q&A (Appendix)
 - 메디스트림 : 검색 엔진 또는 AI 솔루션에 업데이트를 해야함
 - 키워드를 추출해서 매칭하여 검색 하는 것이 최종 목표
 - IR 검색엔진 강의 : https://web.stanford.edu/class/cs276/
 - IR 블로그 : http://www.kwangsiklee.com/2017/12/%EA%B2%80%EC%83%89%EC%97%94%EC%A7%84%EC%9D%98-%EA%B8%B0%EB%B3%B8/
 - BM 25 : https://littlefoxdiary.tistory.com/12