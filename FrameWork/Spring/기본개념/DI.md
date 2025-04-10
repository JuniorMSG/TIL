## **DI (Dependency Injection, 의존성 주입)**

DI(Dependency Injection)는 객체 간의 의존성을 외부에서 주입해주는 설계 패턴입니다. 이는 IoC(Inversion of Control, 제어의 역전)를 구현하는 주요 방법 중 하나로, 객체가 스스로 의존성을 생성하지 않고, 외부에서 필요한 의존성을 주입받도록 합니다.

의존성 주입은 객체 간의 결합도를 낮추고, 코드의 유연성과 테스트 용이성을 높이는 데 매우 중요한 역할을 합니다. 아래에서 DI의 개념, 유형, 동작 방식, 장점, 그리고 예제를 통해 자세히 설명하겠습니다.

---

## **1. DI의 정의**
DI는 객체가 다른 객체에 의존할 때, 의존성을 직접 생성하거나 관리하지 않고 외부에서 주입받는 방식입니다. 이를 통해 객체 간의 결합도를 낮추고 유지보수를 용이하게 합니다.

### **1.1 전통적인 방식**
의존성을 직접 생성하는 방식입니다.

```java
public class Service {
    private Repository repository;

    public Service() {
        this.repository = new Repository(); // 직접 의존성 생성
    }
}
```

위 코드에서는 `Service` 클래스가 `Repository` 객체를 직접 생성하기 때문에 두 클래스가 강하게 결합되어 있습니다.

---

### **1.2 DI 방식**
의존성을 외부에서 주입받는 방식입니다.

```java
public class Service {
    private final Repository repository;

    public Service(Repository repository) { // 의존성 주입
        this.repository = repository;
    }
}
```

이 방식에서는 `Repository` 객체를 외부에서 전달받기 때문에 두 클래스 간의 결합도가 낮아집니다.

---

## **2. DI의 동작 방식**
DI는 **스프링 컨테이너**가 객체를 생성하고, 의존성을 주입하는 방식으로 동작합니다. 다음은 DI의 주요 동작 과정입니다:

1. **스프링 컨테이너 초기화**:
  - XML, Java Config, 또는 애너테이션 기반 설정을 읽고, 객체(빈)를 생성합니다.

2. **의존성 주입**:
  - 생성자, 세터 메서드, 또는 필드에 의존성을 주입합니다.

3. **빈 제공**:
  - 주입된 의존성을 가진 객체를 애플리케이션에 제공합니다.

---

## **3. DI의 유형**
스프링에서 DI는 의존성을 주입하는 방식에 따라 다음과 같이 분류됩니다:

### **3.1 생성자 주입 (Constructor Injection)**
- 생성자를 통해 의존성을 주입합니다.
- 의존성이 필수적일 때 사용합니다.
- 의존성이 주입되지 않으면 객체를 생성할 수 없으므로, 필수 의존성을 보장합니다.

```java
@Component
public class Service {
    private final Repository repository;

    @Autowired
    public Service(Repository repository) { // 생성자 주입
        this.repository = repository;
    }
}
```

#### **장점**:
- `final` 키워드를 사용할 수 있어 불변성을 보장합니다.
- 모든 의존성을 명확히 표시합니다.

---

### **3.2 세터 주입 (Setter Injection)**
- 세터 메서드를 통해 의존성을 주입합니다.
- 선택적인 의존성을 처리할 때 유용합니다.

```java
@Component
public class Service {
    private Repository repository;

    @Autowired
    public void setRepository(Repository repository) { // 세터 주입
        this.repository = repository;
    }
}
```

#### **장점**:
- 선택적인 의존성을 처리할 수 있습니다.
- 객체 생성 후 의존성을 설정할 수 있습니다.

#### **단점**:
- 필수 의존성을 보장할 수 없습니다.

---

### **3.3 필드 주입 (Field Injection)**
- 필드에 직접 의존성을 주입합니다.
- 간단한 코드 작성이 가능하지만, 테스트나 유지보수에 어려움이 있을 수 있습니다.

```java
@Component
public class Service {
    @Autowired
    private Repository repository; // 필드 주입
}
```

#### **장점**:
- 코드가 간결하고, 애너테이션만으로 의존성을 주입할 수 있습니다.

#### **단점**:
- 테스트 시 Mock 객체를 주입하기 어렵습니다.
- 의존성이 숨겨져 있어 명확하지 않을 수 있습니다.

---

### **3.4 인터페이스 주입 (Interface Injection)**
- 의존성을 주입받기 위한 메서드를 인터페이스로 정의하는 방식입니다.
- 스프링에서는 잘 사용되지 않는 방식입니다.

---

## **4. DI의 장점**
DI는 개발과 유지보수를 용이하게 하고, 애플리케이션의 확장성을 높입니다.

### **4.1 느슨한 결합 (Loose Coupling)**
- 객체 간의 결합도를 낮추어, 코드 변경 시 다른 객체에 미치는 영향을 최소화합니다.

### **4.2 테스트 용이성**
- 의존성을 외부에서 주입받기 때문에 Mock 객체를 쉽게 주입하여 단위 테스트를 수행할 수 있습니다.

### **4.3 코드 재사용성**
- 의존성을 외부에서 주입받아 동일한 객체를 다양한 환경에서 재사용할 수 있습니다.

### **4.4 유지보수성**
- 의존성을 설정 정보로 관리할 수 있어, 코드 수정 없이 설정만 변경하여 다른 객체를 주입할 수 있습니다.

---

## **5. DI의 예제**

### **5.1 XML 기반 DI**
XML 파일을 사용하여 의존성을 설정합니다.

```xml
<beans xmlns="http://www.springframework.org/schema/beans">
    <bean id="repository" class="com.example.Repository"/>
    <bean id="service" class="com.example.Service">
        <constructor-arg ref="repository"/>
    </bean>
</beans>
```

---

### **5.2 Java Config 기반 DI**
Java 클래스를 사용하여 의존성을 설정합니다.

```java
@Configuration
public class AppConfig {
    @Bean
    public Repository repository() {
        return new Repository();
    }

    @Bean
    public Service service(Repository repository) {
        return new Service(repository);
    }
}
```

---

### **5.3 애너테이션 기반 DI**
애너테이션을 사용하여 의존성을 설정합니다.

```java
@Component
public class Repository {
}

@Component
public class Service {
    private final Repository repository;

    @Autowired
    public Service(Repository repository) {
        this.repository = repository;
    }
}
```

---

## **6. DI와 IoC의 차이**
- **IoC**는 객체의 생성과 의존성 관리를 개발자가 아닌 프레임워크가 담당하도록 하는 개념입니다.
- **DI**는 IoC를 구현하는 방법 중 하나로, 의존성을 외부에서 주입하는 구체적인 기술입니다.

---

## **7. DI의 한계**
- DI를 과도하게 사용하면 객체 간의 관계가 지나치게 복잡해질 수 있습니다.
- 의존성 주입이 잘못 설계되면 의존성 트리가 지나치게 깊어지는 문제가 발생할 수 있습니다.

---

## **요약**
DI(Dependency Injection)는 객체 간의 의존성을 외부에서 주입받는 설계 패턴으로, 스프링 프레임워크에서 IoC를 구현하는 핵심 메커니즘입니다. DI는 객체 간의 결합도를 낮추고, 코드의 유연성과 테스트 용이성을 높이며, 유지보수를 쉽게 만들어줍니다. 스프링에서는 생성자 주입, 세터 주입, 필드 주입을 통해 DI를 구현할 수 있습니다.

---

### **영어 표현**
- "DI (Dependency Injection) 에 대해서 자세하게 설명해줘"를 영어로 표현하면:
  - "Can you explain DI (Dependency Injection) in detail?"

### **기억해두면 좋은 영어 표현**
- **"Dependency Injection is a design pattern that allows an object to receive its dependencies from an external source rather than creating them itself."**
  - 의존성 주입은 객체가 의존성을 스스로 생성하지 않고 외부에서 주입받을 수 있도록 하는 설계 패턴입니다.