## *Before Project* 
 - Task : 검색 엔진 고도화를 위한 자연어 처리
 - Dataset : 자사 데이터
 >##### Now
 >* 현 검색엔진은 <Strong>Meilisearch</Strong>를 사용, 검색 <Strong>인덱스 생성 시 형태소 분석을 처리하지 않고</Strong> 토크나이징 된 상태로 인덱스를 생성
 >>
 >##### To do
 >* 검색엔진의 한국어 전용 형태소 분석 기능 적용
 >* 한의계 도메인 단어사전 구축 및 단어사전 활용을 통한 검색엔진 성능 비교
 >* 추가로 검색엔진의 성능을 높일 수 있을 만한 방법을 강구

---
## 1. 문제 정의 및 요구 사항
 - 단어 사이 공백의 부재 시 검색 불가
 > <Strong>ex. 필립스500W전구 (검색 X)
 > -> 필립스 500W 전구 (검색 O)</Strong>

 - 특정 복합 명사를 검색 시 각 명사의 결과물이 포함되도록 요구
 > <Strong>ex. 맥문동초 (검색 시)
 > 현재 : 맥문동초
 > 개선 : 맥문동초, 맥문동</Strong>

##### 참고 사항
 > <Strong> 1. Meilisearch의 형태소 분석기 : Charabia -> Charabia의 일본어 specialized segmentation : lindera (Rust 기반의 형태소 분석기)</Strong>
 > <Strong> 2. mecab에 도메인 단어 사전으로 구축한 형태소 사전 추가 가능</Strong>

---
## 2. EDA 및 해결 방법 모색

#### Data
<strong>

 1. 자사 데이터 내 Description 및 검색에 불필요한 Index가 다수 존재

 2. 특정 자사 제품에는 표기가 되어 있음 (검색 결과 시 우선 반영 가능)

</strong>

<br>

#### Library

<strong>

 1. 검색엔진을 빌드하기 위해서는 총 4개의 라이브러리의 수정이 필요
 >* Meilisearch
 >* Milli
 >* Charabia
 >* Lindera


 2. 검색엔진에서 제공하는 유용한 기능이 존재 (추가적인 설정으로 성능 향상)
 >* 검색 우선 순위 반영
 >* 검색 가능한 Index 설정 가능
 >* 유사어 설정
 >* 불용어 처리


</strong>


---
## 3. 전략 수립

#### Baseline
##### 1) Lindera의 Mecab 단어사전에 Build된 단어사전 적용
##### 2) Charabia내 한국어용 Tokenizer Build(Lindera 사용)
##### 3) 개선한 라이브러리를 연결한 검색엔진 Build

<br>

#### More
##### 1) 도메인 단어사전 보강
##### 2) 검색엔진 자체 설정을 통한 성능 개선
##### 3) 타 검색엔진과 성능 비교
---
## 4. 수행

#### 과정
##### 1) Lindera의 단어사전 구축 및 적용
![Lindera](https://user-images.githubusercontent.com/94242504/208913170-50dddd15-0da1-4202-812d-03b8a3b61d9d.jpg)

##### 2) Charabia의 한국어 Tokenizer 파일 생성 및 빌드
![charabia](https://user-images.githubusercontent.com/94242504/208912985-c2912ee6-29ab-4a16-a763-a6536a19493e.jpg)

##### 3) 적용한 라이브러리 간 Build
![all](https://user-images.githubusercontent.com/94242504/208913377-0235ed5e-6f25-41c2-80f3-9b572be889f8.jpg)

##### 4) 조사 및 관사 등 불용어 처리
##### 5) 검색 대상의 Index 조정
##### 6) 검색 우선순위 조정 (Ranking Rule)

---
## 5. 결론

#### 성과
##### 1) Rust로 구성된 검색엔진 오픈소스에 한국어 형태소 분석 적용
##### 2) OCR 및 한의학 사이트를 통한 도메인 단어사전 구축 및 단어사전 적용

<br>

#### 깨달은 점
##### 1) 형태소 분석의 부작용 발생
> 형태소 분석을 통하여 사전 미등재 단어나 가중치가 낮은 단어들은 모두 형태소 단위로 Pre-fix 검색 <br> <strong>* 단어 검색 결과(단어 포함) : [양격산] -> [양격] or [산]</strong>
##### 2) 단어사전을 적용함에 있어 효과를 보는 단어와 악역향을 끼치는 단어를 인지
> [십전대보탕 -> 십전+대보+탕]이라는 복합명사이나 [십전대보탕]이라는 단어 전체가 없으면 검색 불가

<br>

#### 개선할 점
##### 1) 기업의 사용 방향성에 따라 적절한 토의를 거쳐 단어사전 등재 및 제외가 필요
##### 2) 한의학 용어와 유사한 불용어 단어에 대한 고민이 필요
---
###  • Meilisearch Info
 - 최대 단어 : 10개 단어
 - 최대 길이 : 65536
 - 영어, 중국어 및 일본어와 같이 공백을 단어 구분자로 사용하는 언어의 토큰화
 - 오타 허용 : 오타와 맞춤법 오류를 이해
 - Tokenizer (charabia) : https://github.com/meilisearch/charabia/blob/main/CONTRIBUTING.md
 - Tokenizer's release process(for 
 internel team only) as <Strong>Semantic Versioning Convention</Strong>
 https://semver.org/lang/ko

 ### • 참고자료
 - IR 검색엔진 강의 : https://web.stanford.edu/class/cs276/
 - IR 블로그 : http://www.kwangsiklee.com/2017/12/%EA%B2%80%EC%83%89%EC%97%94%EC%A7%84%EC%9D%98-%EA%B8%B0%EB%B3%B8/
 - BM 25 : https://littlefoxdiary.tistory.com/12
