## ruby on rails
    레일즈는 웹 사이트를 만들기 위한 하나의 틀 (FrameWork)
    ruby 프로그래밍 언어로 이루어진 오픈소스 웹 프레임워크로
    강력하고 탄탄한 웹 어플리케이션을 빠르게 개발 할 수 있도록 해준다.
![image](https://user-images.githubusercontent.com/22822369/186697368-246e01c2-bac4-43bc-8200-e37e8869e542.png)

### 특징
    프론트 + 백엔드 웹 프레임워크다. 
    
    MVC (Models Views Controller)
    CoC (Convention over Configuration)
    DRY (Don't Repeat Yourself)
    ORM (Object Relational Mapping)

### 장점
    1. 사람들이 사용하는 언어와 비슷해서, 초보자들이 배우기 쉽다.   Python이랑 비슷하다.
    2. 개발하기 편리하다: 다양한 Gem (라이브러리)을 통해 기능을 빠르게 구현할 수 있으며, 
       데이터베이스 작업할 때 엑티브레코드 패턴을 적용한 ORM을 도입하여 편리하게 구현할 수 있다. 
       또한, 내장된 라이브러리로 초기 일회성 설정으로 자동 배포가 가능하다.
    3. 확장성과 이식성이 높다: 루비를 지원하는 OS라면 추가 작업 없이 프로그램이 실행될 수 있다. 
       유지보수에 쓰이는 비용과 시간을 절약해주며, 파이썬이나 JavaScript 등 다른 언어로 개발된 라이브러리를 Ruby 위에 쉽게 구현 가능할 수 있다.
    4. MVC 아키텍처: MVC 패턴에 익숙한 개발자는 레일즈를 쉽게 다룰 수 있다

### 단점 
    1. 인터프리터 언어는 명령문 별로 코드 구문을 실행하기 때문에 컴파일러(Java, C)를 사용하는 언어에 비해 속도가 느리다.
       높은 메모리 소비와 느린 가비지 콜렉션(garbage collection)으로 속도가 느리다.
    2. 국내 사용률이 낮다.
    3. 이미 구현된 라이브러리와 프레임워크로 빠른 개발이 가능하지만, 유니크한 설계로 다시 커스터마이징을 하기에는 어려움이 있다.

## MVC Architecture
    스프링이랑 똑같은 MVC를 사용한다.
    Models Views Controller

### Models
    1. 비즈니스 로직
    2. 데이터 및 데이터 베이스에 대한 작업
### Views
    1. 사용자 요청에 대한 결과물 표현
    2. 화면에 표출되는 방식에 대한 로직과 데이터를 다룸
    3. 눈에 보이는 부분을 만들어줌
### Controller
    1. 모델과 뷰를 연결시켜줌
    2. 사용자의 입력을 받아 Model을 조작함.
    3. 데이터의 흐름을 제어한다.

## 적용된 개념 ? 이념?
### CoC
    Convention over Configuration
    기본 디자인 패러다임    
    개발자가 내려야 할 결정을 줄여주고 
    파일 설정등에 쓰는 시간을 줄여주고 코딩에 집중 할 수 있도록 해준다. 

### DRY
    Don't Repeat Yourself 
    코드에 반복성을 줄이기 위한 소프트웨어 이론
    더 쉽게 관리하고 확장 할 수 있게되고 버그를 줄일 수 있다.

### ORM
    Object Relational Mapping
    데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법 
    레일즈는 직접 SQL 문을 사용해서 데이터를 가져오지 않고, ActiveRecords라는 ORM 프레임워크를 사용해서 데이터를 조작한다.


## rails 설치
    gem update --system
    gem install rails --no-document
    gem install tzinfo
    gem install ffi
    npm install --global yarn

    원하는 디렉토리로 이동한후
    rails new 프로젝트명
![image](https://user-images.githubusercontent.com/22822369/186462068-a5a92c19-cf94-4c61-b985-c170eb88ab3e.png)  
![image](https://user-images.githubusercontent.com/22822369/186462628-236e12c8-dece-462d-99dc-9651cbb1e4a8.png)

### 기동
    rails -s
    rails server

### 실행완료
![image](https://user-images.githubusercontent.com/22822369/186692504-a27baba5-8795-46eb-8b5c-acecb8041b47.png)
![image](https://user-images.githubusercontent.com/22822369/186692679-1f045a90-dcd2-44fe-b409-be8a9e7a46ab.png)


## reference
https://guides.rubyonrails.org/index.html  
https://rubykr.github.io/rails_guides/getting_started.html  
https://kbs4674.tistory.com/6  
https://freemoa-blog.com/903  