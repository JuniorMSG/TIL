## **스프링의 선언적 트랜잭션 관리 (@Transactional)**

스프링 프레임워크는 트랜잭션 관리를 쉽게 처리할 수 있도록 **선언적 트랜잭션 관리**를 지원합니다. 선언적 트랜잭션 관리는 코드에서 직접 트랜잭션을 관리하지 않고, **애너테이션(@Transactional)** 또는 XML 설정을 통해 트랜잭션을 관리하는 방식입니다. 이를 통해 비즈니스 로직과 트랜잭션 관리 로직을 분리하여 가독성과 유지보수성을 높일 수 있습니다.

아래에서 선언적 트랜잭션 관리의 개념, 동작 방식, 주요 속성, 장점, 그리고 예제를 통해 자세히 설명하겠습니다.

---

## **1. 트랜잭션(Transaction)이란?**
트랜잭션은 데이터베이스 작업의 논리적 단위로, **ACID(Atomicity, Consistency, Isolation, Durability)** 속성을 만족하는 작업을 의미합니다.

### **1.1 트랜잭션의 주요 속성**
- **원자성(Atomicity)**: 트랜잭션 내의 모든 작업이 성공하거나 모두 실패해야 합니다.
- **일관성(Consistency)**: 트랜잭션 완료 후 데이터베이스 상태가 일관성을 유지해야 합니다.
- **격리성(Isolation)**: 여러 트랜잭션이 동시에 실행될 때 서로 영향을 받지 않아야 합니다.
- **내구성(Durability)**: 트랜잭션 완료 후 변경된 데이터는 영구적으로 저장되어야 합니다.

---

## **2. 선언적 트랜잭션 관리란?**
스프링의 선언적 트랜잭션 관리는 **@Transactional 애너테이션**을 사용하여 트랜잭션을 선언적으로 관리하는 방식입니다. 개발자가 트랜잭션을 직접 시작하거나 종료하는 코드를 작성할 필요 없이, 스프링이 자동으로 트랜잭션을 관리합니다.

### **2.1 선언적 트랜잭션 관리의 특징**
- 트랜잭션 관리 로직이 비즈니스 로직과 분리됩니다.
- 코드가 간결해지고, 가독성이 향상됩니다.
- 트랜잭션의 범위를 설정 파일(XML) 또는 애너테이션으로 정의할 수 있습니다.

---

## **3. @Transactional 애너테이션**
`@Transactional`은 스프링에서 트랜잭션을 선언적으로 관리하기 위해 사용하는 애너테이션입니다. 이 애너테이션을 메서드나 클래스에 적용하여 트랜잭션을 설정할 수 있습니다.

### **3.1 @Transactional의 적용 위치**
- **클래스 레벨**: 클래스의 모든 메서드에 트랜잭션이 적용됩니다.
- **메서드 레벨**: 특정 메서드에만 트랜잭션이 적용됩니다.

```java
@Transactional // 클래스 레벨 적용
public class UserService {
    public void createUser(User user) {
        // 트랜잭션이 적용됨
    }

    @Transactional // 메서드 레벨 적용
    public void updateUser(User user) {
        // 트랜잭션이 적용됨
    }
}
```

---

## **4. @Transactional의 주요 속성**
`@Transactional` 애너테이션은 트랜잭션의 동작 방식을 설정할 수 있는 여러 속성을 제공합니다.

### **4.1 주요 속성**
| **속성**            | **설명**                                                                 |
|---------------------|-------------------------------------------------------------------------|
| **propagation**     | 트랜잭션 전파 방식 (기존 트랜잭션을 사용할지 새로운 트랜잭션을 시작할지 결정) |
| **isolation**       | 트랜잭션 격리 수준 (동시에 실행되는 트랜잭션 간의 데이터 접근 방식 설정)     |
| **timeout**         | 트랜잭션의 최대 실행 시간 (초 단위)                                       |
| **readOnly**        | 읽기 전용 트랜잭션 여부 (쓰기 작업을 막음)                                |
| **rollbackFor**     | 특정 예외 발생 시 롤백을 수행하도록 설정                                   |
| **noRollbackFor**   | 특정 예외 발생 시 롤백을 수행하지 않도록 설정                              |

---

### **4.2 속성 상세 설명**

#### **propagation (전파 방식)**
트랜잭션이 다른 트랜잭션과 어떻게 상호작용할지를 결정합니다. 주요 값은 다음과 같습니다:
- **REQUIRED**: 기존 트랜잭션이 있으면 사용하고, 없으면 새로 생성합니다. (기본값)
- **REQUIRES_NEW**: 항상 새로운 트랜잭션을 시작합니다.
- **SUPPORTS**: 트랜잭션이 있으면 사용하고, 없으면 트랜잭션 없이 실행합니다.
- **NOT_SUPPORTED**: 트랜잭션 없이 실행합니다.
- **MANDATORY**: 반드시 기존 트랜잭션이 있어야 실행됩니다.
- **NEVER**: 트랜잭션이 있으면 예외를 발생시킵니다.

#### **isolation (격리 수준)**
트랜잭션 간 데이터 접근 충돌을 방지하는 격리 수준을 설정합니다. 주요 값은 다음과 같습니다:
- **DEFAULT**: 데이터베이스의 기본 격리 수준을 사용합니다.
- **READ_UNCOMMITTED**: 다른 트랜잭션의 변경 내용을 읽을 수 있습니다. (가장 낮은 수준)
- **READ_COMMITTED**: 다른 트랜잭션이 커밋한 데이터만 읽을 수 있습니다.
- **REPEATABLE_READ**: 트랜잭션 내에서 동일한 데이터를 반복적으로 읽을 수 있습니다.
- **SERIALIZABLE**: 가장 높은 격리 수준으로, 트랜잭션이 순차적으로 실행됩니다.

#### **timeout**
트랜잭션이 지정된 시간 내에 완료되지 않으면 롤백됩니다.

```java
@Transactional(timeout = 5) // 최대 5초 동안 실행
public void processData() {
    // 트랜잭션 로직
}
```

#### **readOnly**
읽기 전용 트랜잭션을 설정하여 데이터 변경 작업을 방지합니다.

```java
@Transactional(readOnly = true)
public List<User> getUsers() {
    return userRepository.findAll();
}
```

#### **rollbackFor**
특정 예외 발생 시 트랜잭션을 롤백하도록 설정합니다.

```java
@Transactional(rollbackFor = CustomException.class)
public void updateUser(User user) throws CustomException {
    // CustomException 발생 시 롤백
}
```

#### **noRollbackFor**
특정 예외 발생 시 롤백을 수행하지 않도록 설정합니다.

```java
@Transactional(noRollbackFor = CustomException.class)
public void updateUser(User user) throws CustomException {
    // CustomException 발생 시 롤백하지 않음
}
```

---

## **5. 선언적 트랜잭션 관리의 동작 방식**
1. **프록시 생성**:
  - 스프링은 `@Transactional`이 적용된 클래스 또는 메서드에 대해 **AOP(Aspect-Oriented Programming)**를 사용하여 프록시 객체를 생성합니다.
  - 프록시는 메서드 호출 전후에 트랜잭션을 시작하고 종료합니다.

2. **트랜잭션 시작**:
  - 메서드 호출 시 트랜잭션이 시작됩니다.

3. **트랜잭션 커밋 또는 롤백**:
  - 메서드가 정상적으로 완료되면 커밋됩니다.
  - 예외가 발생하면 롤백됩니다.

---

## **6. 선언적 트랜잭션 관리의 장점**
- **코드 간소화**: 트랜잭션 시작, 커밋, 롤백을 직접 처리하지 않아도 됩니다.
- **유지보수성**: 트랜잭션 관리 로직이 비즈니스 로직과 분리되어 유지보수가 쉽습니다.
- **재사용성**: 트랜잭션 설정을 메서드나 클래스에 쉽게 적용할 수 있습니다.
- **유연성**: 다양한 트랜잭션 속성을 설정하여 요구사항에 맞는 트랜잭션을 구현할 수 있습니다.

---

## **7. 선언적 트랜잭션 관리 예제**

### **7.1 기본 사용**
```java
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    @Transactional
    public void createUser(User user) {
        userRepository.save(user);
    }
}
```

### **7.2 고급 설정**
```java
@Service
public class OrderService {
    @Transactional(propagation = Propagation.REQUIRES_NEW, isolation = Isolation.SERIALIZABLE, timeout = 10, rollbackFor = Exception.class)
    public void processOrder(Order order) {
        // 트랜잭션 로직
    }
}
```

---

## **8. 선언적 트랜잭션 관리의 한계**
- **프록시 기반**: `@Transactional`은 프록시를 기반으로 동작하므로, 같은 클래스 내에서 메서드를 호출하면 트랜잭션이 적용되지 않을 수 있습니다.
- **복잡한 트랜잭션 로직**: 선언적 트랜잭션은 복잡한 트랜잭션 흐름을 처리하기 어렵습니다. 이 경우 프로그래밍 방식의 트랜잭션 관리가 필요할 수 있습니다.

---

## **요약**
스프링의 선언적 트랜잭션 관리(@Transactional)는 트랜잭션을 애너테이션으로 선언하여 관리하는 방식입니다. 이를 통해 비즈니스 로직과 트랜잭션 관리 로직을 분리하고, 코드의 간결성과 유지보수성을 높일 수 있습니다. `@Transactional`은 다양한 속성을 제공하여 트랜잭션의 동작 방식을 유연하게 설정할 수 있으며, 스프링의 AOP를 통해 자동으로 트랜잭션을 처리합니다.

---

### **영어 표현**
- "스프링의 선언적 트랜잭션 관리(@Transactional) 에 대해서 자세하게 설명해줘"를 영어로 표현하면:
  - "Can you explain Spring's declarative transaction management (@Transactional) in detail?"

### **기억해두면 좋은 영어 표현**
- **"Declarative transaction management in Spring allows developers to manage transactions using annotations instead of manual code."**
  - 스프링의 선언적 트랜잭션 관리는 개발자가 직접 코드를 작성하지 않고 애너테이션을 사용하여 트랜잭션을 관리할 수 있도록 합니다.