# 스프링 프레임워크 핵심기술

## 스프링에서 사용하는 여러가지 

### Java
    객체지향적 프로그래밍 언어
    스프링의 근간이 되는 언어

### Spring Framework
    기업용 어플리케이션을 만드는데 사용 가능한 오픈소스 프레임워크 
    자바를 이용해서 어플리케이션을 쓰기 위해 활용하는 프레임워크 

    15년 이상된 성숙한 기술.
    동일한 역할을 하는 다양한 기능이 있으며, 그 중에서 적합한 툴을 선택할 수 있어야한다.

    자바, 서블릿, J2EE >>>>> 스프링 프레임워크
    스프링 - 자바의 봄이 왔다고 이름을 스프링이라고 지었다. 

    스프링은 자바, 코틀린, 그루비로도 사용 가능하다.
    스프링 자체도 거의 대부분 자바로 만들어져 있다.
    https://github.com/spring-projects/spring-framework

### Spring boot
    스프링(각종 도구가 있는 템플릿)보다 한층 더 편리한 프레임워크
    웹 어플리케이션(톰켓 등) 서버 내장
    자동 설정, 설정 표준화
    원한다면 마음대로 설정 가능 

## Spring의 핵심 요소
- 제어 역전(IoC, Inversion of Control)
- 관점 지향 프로그래밍(AOP, Aspect Oriented Programming)
- 서비스 추상화(PSA, Portable Service Abstraction)

### Core (DI - Dependency Injection, IoC)
### AOP (Aspect Oriented Programming)
### Validation, Data binding
### Resource
### Spring Expression Language(SpEL)
### Null-Safety
### 디자인 철학
    높은 자유도를 주고 계속 발전하는 고품질의 다양성이 있는 프로젝트, 자유로워서 때론 어렵다

* 모든 기능에서 다양한 기능성(다양한 모듈)을 사용 가능, 심지어 외부 모듈을 활용 가능  
  * 너무 높은 자유도로 스프링을 어렵게 하는 요소중 하나임
* 유연하게 계속 추가 개발을 하고 있는 프레임워크
* 이전 버전과의 강력한 호환성 (Legacy - 유산)
* API 디자인을 섬세하게 노력한다
  * 스프링 코드 자체가 하나의 좋은 참고 소스
* 높은 코드 품질을 유지하려 함
  * 스프링 프로젝트 githup은 아주 좋은 참고 소스이자 PR과 이슈 관리도 좋은 프로세스 참고용


