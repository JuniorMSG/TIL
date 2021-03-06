# 711_MSA
## 01_MSAvsMonolithic.md

# 마이크로 서비스 (Micro Service) vs 모놀리틱 (Monolithic) 구조

## 모놀리틱 (Monolithic) 구조
    하나의 서버에 서비스할 모든 애플리케이션 소스 (UI, 비즈니스 로직, DB처리 로직 등)가 존재하는 구조를 의미합니다.
    모놀리틱 구조는 처음에는 작은 서비스로 시작하거나 모듈화가 잘 되어 있어 큰 문제가 없을 수 있으나 
    오늘날과 같이 점점 많은 기능들이 요구되고 복잡한 비즈니스 서비스들이 추가되면서 모놀리틱 구조는 다양한 문제가 발생하고 있습니다.

## 모놀리틱 구조에서의 장점
    아키텍처 구조가 심플하여 관리자 용이하다
    트랜잭션 관리가 쉽다.
    애플리케이션 설계 및 테스트가 용이하다.  (애플리케이션의 복잡도가 증가하면 테스트의 복잡도가 크게 증가할 수 있다.)
 
## 모놀리틱 구조에서의 단점
    여러 서비스들이 하나의 구조에 존재하여 특정 서비스 장애 시 전체적인 장애가 발생 할 수 있다. 
    (예: Memory segmentation fault, Out Of Memory Error 등)
    여러 모듈간 의존성이 복잡해져 모듈 수정 시 다른 모든 서비스에 영향을 주어 장애를 발생 시킬 수 있다.
    애플리케이션 구조에 따라 배포/재배포 시 시간이 오래 걸릴 수 있고, 
    시스템 확장 및 Auto Scaling등에 제약이 발생 할 수 있다. (예: 단일 데이터베이스 사용에 따른 확장 제한)
         


# 마이크로 서비스 (Micro Service)
    마이크로 서비스는 서비스를 작게 나눈 것! 
    독립적으로 실행 및 배치가 가능한 작은 단위로 나누어 서비스를 제공하는 것을 뜻합니다.
    서비스와 서비스의 통신은 보통 경량 메커니즘 (HTTP, REST API, Message Queue)을 사용하고, 
    각 서비스들의 연계를 좀 더 유연하게 할 수 있도록 API Gateway 서버 기능을 적용하기도 합니다.

## 마이크로 서비스는 다음과 같은 장점을 가지고 있습니다.
    모놀리틱 구조의 복잡성을 해소할 수 있다.
    각각의 서비스별로 배포/재배포가 자유롭다.
    서비스 별로 확장이 용이하다.

## 반면 마이크로 서비스의 단점은 아래와 같습니다.
    서비스를 분해하기 위한 설계를 잘 고려해야 한다.
    각 서비스 별로 분산된 시스템으로 구성되어 많은 WEB/WAS 시스템이 증가하고 모니터링 대상도 증가하게 된다.
    서비스가 분산되어 있고, 서비스 별로 자체 데이터 저장소를 가지고 있어 데이터베이스 트랜잭션 관리가 어렵다.
    모놀리틱 구조보다 애플리케이션 테스트가 어렵다.
         