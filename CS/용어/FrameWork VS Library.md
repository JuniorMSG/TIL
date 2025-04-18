## Framework
    개발할 때 자주 사용되는 기능을 한꺼번에 제공해 개발 효율의 향상을 목표하는 소프트웨어 환경
    프레임워크는 전체적인 흐름을 스스로가 가지고 있고 개발자가 필요한 코드를 짜 넣어서 사용합니다. 

    애플리케이션 개발 시 필수적인 코드, 알고리즘, DB 연동과 같은 기능들을 위해 어느 정도 뼈대(Frame)를 제공
    사용자는 코드를 작성하여 애플리케이션을 개발합니다. 
    앱/서버 등의 구동, 메모리 관리, 이벤트 루프 등의 공통된 부분은 프레임워크가 관리하며, 
    사용자는 프레임워크가 정해준 방식대로 클래스, 메서드들을 구현하면 됩니다.

### 특징
    1. 제어의 역전(IOC) 개념이 적용된 대표적인 기술입니다.
    2. 공통적인 개발환경을 제공합니다.
    3. 개발할 수 있는 범위가 정해져 있다.
    

### 예시
    Python 서버 개발에 사용되는 Django, Flask, faseapi
    자바 기반의 JSP를 위한 프레임 워크 Struts (넘 오
    Java로 서버 개발에 사용되는 MVC패턴을 이용하는 Spring
    루비로 작성된 MVC패턴을 이용하는 Ruby on Rails
    JavaScript 기반의 express.js
    웹 개발에 사용되는 Angular, Vue.js등

## Library and module 
    재사용 가능한 코드의 집합.
    모듈이 프로그램을 구성하는 작은 부품의 느낌이라면, 
    라이브러리는 자주 사용 되는 로직을 잘 정리한 집합 느낌이다.

    표현상으로 치면 모듈은 업무 기능단위?
    라이브러리는 특정 기능단위랄까?..

    회원가입 모듈이라고 하고 회원가입 라이브러리라고는 잘 안하는 느낌이릴까
    음 정확하게 구분이 안되기 때문에 거의 비슷한 것 같다.
    

### 특징
    1. 라이브러리는 개발자가 전체적인 코드의 흐름에서 직접 제어하며 사용하는 것 입니다.
    2. 자주 사용하는 로직들을 재사용하기 편리하도록 만들어 놓은 코드의 집합
    3. 내가만든 클래스도 하나의 라이브러리가 될 수 있습니다.

### 예시
    Node.js에서 npm으로 설치한 모듈
    HTML의 클라이언트 사이드 조작을 단순화하는 JQuery
    웹에서 사용자 인터페이스 개발에 사용되는 React.js (라이브러리구나?)
    내가만든 클래스도 하나의 라이브러리가 될 수 있다.
![image](https://user-images.githubusercontent.com/22822369/186444271-583c3a3b-b02d-4f85-9965-9cf74999d0c7.png)
 
## API 
    application programming interface
    응용 프로그램에서 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어 할 수 있게 만든 인터페이스.

    API는 정의 및 프로토콜 집합을 사용하여 두 소프트웨어 구성 요소가 서로 통신할 수 있게 하는 메커니즘

    API의 맥락에서 애플리케이션이라는 단어는 고유한 기능을 가진 모든 소프트웨어를 나타냅니다. 
    인터페이스는 두 애플리케이션 간의 서비스 계약이라고 할 수 있습니다.

### 특징
    1. 다른 프로그램과 연결 해주는 다리
    2. 구현이 아닌 제어를 담당
    3. API를 조합해 원하는 프로그램을 만들 수 있다. 
    
### Ref
    https://aws.amazon.com/ko/what-is/api/



## 요약? 
    프레임워크는 틀이고
    라이브러리 & 모듈은 개발자가 틀안에서 개발하는 도구고
    module은 무언가 특정한 기능을 수행하는 하나의 덩어리고
    API는 그 덩어리에 통신할 수 있고 서로간의 규약을 정해서 뭔가 하면 API가 된다.

    
### 회원가입이라면.
    FrameWork : 스프링이라는 틀에서 개발한 회원가입 어플리케이션이 있는데
    Module : 회원가입을 책임지는 모듈이 있으며 해당 모듈에선 다양한 라이브러리를 호출해서 사용한다. 
    Library : 그안에는 비밀번호를 조건을 체크하는 라이브러리등 다양한 라이브러리가 있고.
    API : 회원가입에 대해서 통신하고 규약이 정해진 API가 있어서 해당 API에 규약대로 데이터를 전달하면 회원가입이 된다!..
    라고 생각하면 대충은 맞지 않나 싶다.
    
![image](https://user-images.githubusercontent.com/22822369/186456929-218fe31a-e2aa-40d1-a000-2f94c6476969.png)
