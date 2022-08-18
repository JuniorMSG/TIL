# Annotation.

    Bean을 편하게 혹은 다른 기능을 편하게 생성 할 수 있는 방법
    어노테이션으로 인해 데이터의 유효성 검사 등을 쉽게 알 수 있고, 이와 관련한 코드가 깔끔해지게 됩니다.
    일단 어노테이션의 용도는 다양한 목적이 있지만 
    메타 데이터의 비중이 가장 크다 할 수 있습니다.

    메타-테이터(Meta-Data) : 데이터를 위한 데이터를 의미하며, 풀어 이야기하면 한 데이터에 대한 설명을 의미하는 데이터. (자신의 정보를 담고 있는 데이터)

## Spring Annotation

### @Componant
    Bean을 등록하는 가장 기본적인 단위 

### @Controller
    Spring Model, View, Controller (MVC) 모델에서
    C를 담당함.
    Controller의 주요 역할은 클라이언트 (View)단과 
    Model단의 연결을 한다.


### @RestController
    Controller + ResponseBody가 합쳐진 형태의 컨트롤러로 선언하는것