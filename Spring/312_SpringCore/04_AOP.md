# AOP(Aspect Oriented Programming)

# 잡설
    전자정부 프레임워크나 스프링 하위버전에서는 XML 형식으로 구현되어 코드 읽기가 더 어렵다.
    스프링 부트에선 대부분 Annotation을 사용하여 사용한다.
    로깅, 페이징 관련 기능을 AOP 처리 했었는데
    훨씬 편한것 같은데 한번 만들어 봐야겠다. 
    

# 관점 지향 프로그래밍 - AOP(Aspect Oriented Programming)
    Filter, Intercepter - 프로젝트 전체 공통 부분
    AOP - 특정한 함수 호출 전이나 후에 뭔가 공통적인 처리가 필요하다.
          (로깅, 트랜잭션, 인증, 페이징등등)
    

## 장점
    * 손쉽게 공통 기능을 추가/수정/삭제 할 수 있다.
## 단점
    * 코드 분석이 어려워진다.    

## AOP의 기본 개념들

### Aspect
    특정 하나의 주제를 여러 클래스나 기능에 걸쳐서 모듈화함
    AOP 중에서 가장 많이 활용되는 부분은 @Transactional (트랜잭션 관리) 기능
    프로젝트에서 페이징, 로깅관리등에 셋팅해서 사용해봤다.

### Advice
    조언, AOP에서 실제로 적용하는 기능(로깅, 트랜잭션, 인증 등)을 뜻함

### Join point
    모듈화된 특정 기능이 실행될 수 있는 연결 포인트

### Pointcut
    Join point 중에서 해당 Aspect를 적용할 대상을 뽑을 조건식

### Target Object
    Advice가 적용될 대상 오브젝트

### AOP Proxy
    대상 오브젝트에 Aspect를 적용하는 경우 Advice를 덧붙이기 위해 하는 작업을 AOP Proxy라고 함
    주로 CGLIB(Code Generation Library, 실행 중에 실시간으로 코드를 생성하는 라이브러리) 프록시를 사용하여 프록싱 처리를 한다.

### Weaving
    Advice를 비즈니스 로직 코드에 삽입하는 것을 말함

![img_5.png](rsc/[410_04]_AOP_01.png)


## AspectJ 지원

AspectJ는 AOP를 제대로 사용하기 위해 꼭 필요한 라이브러리

기본적으로 제공되는 Spring AOP로는 다양한 기법(Pointcut 등)의 AOP를 사용할 수 없음

### Aspect의 생성

```java
package org.xyz;
import org.aspectj.lang.annotation.Aspect;

@Aspect
@Component  // Component를 붙인 것은 해당 Aspect를 스프링의 Bean으로 등록해서 사용하기 위함
public class UsefulAspect {

}
```

### Pointcut 선언

```java
package org.xyz;
import org.aspectj.lang.annotation.Aspect;

@Aspect
@Component  // Component를 붙인 것은 해당 Aspect를 스프링의 Bean으로 등록해서 사용하기 위함
public class UsefulAspect {

	@Pointcut("execution(* transfer(..))")
	private void anyOldTransfer() {}
}
```

- 해당 Aspect의 Advice(실행할 액션)이 적용될 Join point를 찾기 위한 패턴 또는 조건 생성
- 포인트 컷 표현식이라고 부름

### Pointcut 결합

```java
package org.xyz;
import org.aspectj.lang.annotation.Aspect;

@Aspect
@Component  // Component를 붙인 것은 해당 Aspect를 스프링의 Bean으로 등록해서 사용하기 위함
public class UsefulAspect {

	@Pointcut("execution(public * *(..))")
	private void anyPublicOperation() {} //public 메서드 대상 포인트 컷

	@Pointcut("within(com.xyz.myapp.trading..*)")
	private void inTrading() {} // 특정 패키지 대상 포인트 컷
	
	@Pointcut("anyPublicOperation() && inTrading()")
	private void tradingOperation() {} // 위의 두 조건을 and(&&) 조건으로 결합한 포인트 컷
}
```

---

## Advice 정의

포인트컷들을 활용하여 포인트컷의 전/후/주변에서 실행될 액션을 정의함

### Before Advice

dataAccessOperation()이라는 미리 정의된 포인트 컷의 바로 전에 doAccessCheck가 실행

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;

@Aspect
public class BeforeExample {

    @Before("com.xyz.myapp.CommonPointcuts.dataAccessOperation()")
    public void doAccessCheck() {
        // ...
    }
}
```

### After Returning Advice

dataAccessOperation()라는 미리 정의된 포인트컷에서 return이 발생된 후 실행

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.AfterReturning;

@Aspect
public class AfterReturningExample {

    @AfterReturning("com.xyz.myapp.CommonPointcuts.dataAccessOperation()")
    public void doAccessCheck() {
        // ...
    }
}
```

### Around Advice

businessService()라는 포인트컷의 전/후에 필요한 동작을 추가함