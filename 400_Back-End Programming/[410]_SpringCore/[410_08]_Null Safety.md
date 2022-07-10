# [410]. Spring
## [410_08]_Null Safety

## Null Safety
    널 안정성을 높이는 방법

- 아래와 같은 코드를 만들지 않는 방법
- 혹은 아래와 같은 널 체크를 하지 않아서 발생하는 NPE(Null Pointer Exception)을 방지하는 방법
- 완벽한 방법은 아니지만 IDE(Intellij, Eclipse)에서 경고를 표시함으로써 1차적인 문제를 방지하고, 정확한 에러 위치를 확인할 수 있도록 도움
- ☆ 보일러플레이트 코드를 제거 할 수 있다.

```java
public void method(String request) {
	if(request == null) return;

	// normal process
	System.out.println(request.toUpperCase());
}
```

---

## @NonNull Annotation

- 해당 값이나 함수 등이 Null이 아님을 나타내는 어노테이션
- org.springframework.lang.NonNull 사용

- 메서드 파라미터에 붙이는 경우 : null이라는 데이터가 들어오는 것을 사전에 방지함
![img_6.png](img_6.png)
- 프로퍼티에 붙이는 경우 : null을 저장하는 경우 경고
![img_7.png](img_7.png)
- 메서드에 붙이는 경우 : null을 리턴하는 경우 경고, 응답값을 저장하거나 활용하는 쪽도 NonNull이라고 신뢰하고 사용
![img_8.png](img_8.png)

---

## @Nullable Annotation

- ★ @NonNull과 반대로 해당 데이터가 null일 수 있음을 명시함
- 해당 어노테이션이 붙은 값을 사용하는 경우 null check를 항상 수행하도록 경고

![img_9.png](img_9.png)

---

## Null 관련 어노테이션 참고

- jetbrain(intellij 개발회사) : [https://www.jetbrains.com/help/idea/nullable-and-notnull-annotations.html](https://www.jetbrains.com/help/idea/nullable-and-notnull-annotations.html)
- lombok : [https://projectlombok.org/features/NonNull](https://projectlombok.org/features/NonNull)