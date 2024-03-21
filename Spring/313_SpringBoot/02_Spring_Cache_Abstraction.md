# spring_cache
* [01. 02_Spring_Cache_Abstraction](#spring_cache_abstraction)

### Reference  

[뒤로](README.md) / [위로](#spring-boot)

## Spring_Cache_Abstraction
    Spring Cache Abstraction
    • 애플리케이션에 "투명하게(transparently)" 캐시를 넣어주는 기능
    • 메소드, 클래스에 적용 가능
    • 캐시 인프라는 스프링 부트 자동 설정으로 세팅되고, 프로퍼티로 관리 가능

### Transparently
    • 캐시가 시스템, 애플리케이션에 투명하게 자리잡는다는 말은..
    • 데이터를 통신하는 시스템 쌍방이 캐시의 존재를 모른다는 의미
    • "캐시가 있건 없건, 시스템의 기대 동작은 동일해야 한다."
    • 캐시의 목표: 오로지 "성능"
    • 캐시의 개념과 목적에 부합하는 성질이자, 조건

### 캐시를 왜 쓸까?
    반복 작업이면 고려해야한다. 
    • 잘 바뀌지 않는 정보를 외부 저장소에서 반복적으로 읽어온다면
    • 기대값이 어차피 같다면
    • 캐싱해서 성능 향상, I/O 감소

### 사용방법
    @EnableCaching 사용하면 된다.

### 캐싱에서 생각해야 하는 것들
    • 무엇을 캐시할까?
    • 얼마나 오랫동안 캐시할까?
    • 언제 캐시를 갱신할까?

### 주요기능들
    • @EnableCaching
    • @Cacheable
    • @CacheEvict
    • @CachePut

### Redis
    실무에서 가장 많이 사용하는 캐시 서버중하나.

[뒤로](README.md) / [위로](#spring-boot)



