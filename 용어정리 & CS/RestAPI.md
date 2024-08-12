## 1. API란
    Application Programming Interface(애플리케이션 프로그램 인터페이스)
    요청과 응답을 사용하여 두 애플리케이션이 서로 통신하는 방법이며...
    라이브러리도 API의 일종이며 
    URL로 통신하면 RestAPI

## 2. RestAPI
    Rest(Representational State Transfer) API로 URL(Uniform Resource Identifier)로 통신하는 API를 지칭하며 
    자원(Resource)을 의미(Representation)로 구분하여 그 상태를 전달함

[LINK => 5분만에 제대로 설계하는 REST API](https://www.youtube.com/watch?v=4DxHX95Lq2U)

### 작성 규칙
1. 동사를 사용하지 않는다.  (명사를 통한 리소스 식별)
2. HTTP헤더에 데이터 포맷 포함
3. GET 메소드를 통해 값을 변경하지 말고 PUT, POST, DELETE등의 메소드들을 이용해 상태를 변경 해야한다
4. 서브 URL 표현식을 통해 세부 표현
    1. API 내부에 다른 리소스와 관계가 있을때 서브 리소스 표현으로 그 관계를 표시한다.
5. HTTP 응답 상태 코드를 사용한다.

### 작성 방법

| 명령어    | 종류     | HTTP Method |
|--------|--------|-------------|
| Create | 데이터 생성 | POST        |
| Read   | 데이터 조회 | GET         |
| Update | 데이터 수정 | PUT / PATCH |
| Delete | 데이터 삭제 | DELETE      |

### 작성 예시

    고양이에 대한 정보를 제공하는 API를 설계한다면..
    설계할 때 고양이 데이터를 추가하거나 삭제할 수 있는 API를 구현하고자 하면..

| Method | URL        | DESC                    |
|--------|------------|-------------------------|
| GET    | /cats      | 고양이 전체에 대한 데이터를 불러온다    |
| GET    | /cats/{id} | id에 해당하는 고양이 데이터를 불러온다. |
| POST   | /cats/{id} | 고양이 데이터를 생성한다.          |
| PUT    | /cats/{id} | 고양이 데이터를 수정한다.          |
| DELETE | /cats/{id} | 고양이 데이터를 삭제한다.          |


### Reference
* 신박하게 잘 설명한 영상이 있길래... [API](https://www.youtube.com/watch?v=em7HOGu01ro)
