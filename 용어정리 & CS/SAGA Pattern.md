Saga 패턴은 분산 시스템에서 데이터 일관성을 유지하기 위해 사용되는 디자인 패턴입니다.  
특히 마이크로서비스 아키텍처에서 장기간 실행되는 트랜잭션을 관리하는 데 유용합니다.   
Saga 패턴은 큰 트랜잭션을 작은 독립적인 단계(서브 트랜잭션)로 나누고,   
각 단계가 성공적으로 완료되었는지 확인하며, 문제가 발생하면 보상 조치(롤백)를 통해 이전 상태로 되돌립니다.

### Saga 패턴의 개념

1. **Saga**: 하나의 비즈니스 트랜잭션을 구성하는 여러 서브 트랜잭션의 집합입니다.
2. **서브 트랜잭션**: 독립적으로 커밋될 수 있는 트랜잭션 단위입니다.
3. **보상 트랜잭션**: 서브 트랜잭션의 실패 시, 시스템을 이전 상태로 복구하기 위해 실행되는 롤백 동작입니다.

### Saga 패턴의 유형

1. **Choreography (안무형)**:
  - 각 서비스가 다음 서비스로 트랜잭션을 전달하는 이벤트 기반 접근 방식입니다.
  - 각 서비스는 자신이 해야 할 작업을 완료하고 다음 이벤트를 발행하여 다음 서비스를 호출합니다.
- 중앙 조정자가 없으며, 각 서비스가 스스로를 관리합니다.

2. **Orchestration (오케스트레이션형)**:

- 중앙 조정자가 전체 프로세스를 제어합니다.
- 조정자는 각 서비스를 호출하고, 트랜잭션의 상태를 추적하며, 실패 시 보상 트랜잭션을 호출합니다.

### Choreography 예제

```java
// OrderService.java
public class OrderService {
    @Autowired
    private ApplicationEventPublisher eventPublisher;

    public void createOrder(Order order) {
        // 주문 생성 로직
        eventPublisher.publishEvent(new OrderCreatedEvent(order));
    }
}

// PaymentService.java
@EventListener
public void handleOrderCreated(OrderCreatedEvent event) {
    // 결제 처리 로직
    if (paymentSuccess) {
        eventPublisher.publishEvent(new PaymentCompletedEvent(event.getOrder()));
    } else {
        eventPublisher.publishEvent(new PaymentFailedEvent(event.getOrder()));
    }
}

// InventoryService.java
@EventListener
public void handlePaymentCompleted(PaymentCompletedEvent event) {
    // 재고 감소 로직
}
```

### Orchestration 예제

```java
// OrderSagaOrchestrator.java
public class OrderSagaOrchestrator {
    @Autowired
    private OrderService orderService;
    @Autowired
    private PaymentService paymentService;
    @Autowired
    private InventoryService inventoryService;

    public void createOrder(Order order) {
        try {
            orderService.createOrder(order);
            paymentService.processPayment(order);
            inventoryService.updateInventory(order);
        } catch (Exception e) {
            // 보상 트랜잭션 수행
            paymentService.cancelPayment(order);
            orderService.cancelOrder(order);
        }
    }
}
```

### 장점

1. **데이터 일관성 유지**: 분산 시스템에서 데이터 일관성을 효과적으로 유지할 수 있습니다.
2. **내결함성 향상**: 보상 트랜잭션을 통해 시스템의 복구 능력을 향상시킵니다.
3. **확장성**: 각 서브 트랜잭션이 독립적으로 수행되므로, 시스템의 확장성이 높습니다.

### 단점

1. **복잡성 증가**: 트랜잭션 단계와 보상 트랜잭션을 관리해야 하므로, 시스템의 복잡성이 증가합니다.
2. **타임아웃 처리**: 장기간 실행되는 트랜잭션에서 타임아웃 처리와 관련된 문제를 해결해야 합니다.
3. **부분 실패 처리**: 부분 실패를 관리하고, 보상 트랜잭션을 적절하게 설계하는 것이 어렵습니다.

### Saga 패턴 사용 예

- **전자상거래**: 주문 생성, 결제 처리, 재고 업데이트 등.
- **여행 예약 시스템**: 항공권 예약, 호텔 예약, 렌터카 예약 등.
- **은행 거래**: 계좌 이체, 대출 승인, 지불 처리 등.

Saga 패턴은 분산 시스템에서 복잡한 트랜잭션 관리 문제를 해결하는 데 유용하지만, 그 복잡성을 관리하기 위해 n적절한 도구와 프레임워크의 지원이 필요합니다. 대표적인 Saga 패턴 지원 프레임워크로는 Axon, Camunda, Spring Boot와 같은 도구들이 있습니다.




## Choreography(안무형)와 Orchestration(오케스트레이션형)은 각각의 장 단점
특정 상황에 더 적합한 선택이 될 수 있습니다. 이 둘은 주로 마이크로서비스 아키텍처에서 서비스 간의 통신과 상호작용을 관리하는 방식입니다.

### Choreography (안무형)

**특징:**
- 각 서비스가 독립적으로 동작하며, 이벤트를 게시하고 다른 서비스는 이를 구독합니다.
- 중앙 집중화된 제어 구조가 없습니다. 서비스 간의 상호작용은 이벤트를 통해 암묵적으로 정의됩니다.
- 느슨한 결합과 높은 확장성을 제공합니다.

**장점:**
- **확장성:** 각 서비스가 독립적으로 동작하기 때문에 서비스 추가 및 제거가 비교적 용이합니다.
- **느슨한 결합:** 서비스 간의 직접적인 의존성이 낮아져, 변경이 발생해도 다른 서비스에 미치는 영향이 적습니다.
- **복잡성 감소:** 중앙 집중화된 관리가 없기 때문에, 단순한 워크플로우에서는 관리가 쉬울 수 있습니다.

**단점:**
- **디버깅 어려움:** 이벤트 기반 시스템에서는 문제 발생 시 원인을 추적하는 것이 어려울 수 있습니다.
- **복잡한 워크플로우 관리:** 복잡한 비즈니스 로직이 필요한 경우 이벤트 흐름을 관리하기 어려울 수 있습니다.
- **순서 보장 어려움:** 이벤트의 순서를 보장하는 것이 어렵기 때문에, 일부 시나리오에서는 데이터 일관성 문제가 발생할 수 있습니다.

**적합한 곳:**
- **단순한 워크플로우:** 서비스 간의 상호작용이 비교적 단순한 경우.
- **독립적인 서비스:** 서비스가 독립적으로 동작하며, 서로 간의 의존성이 낮은 경우.
- **확장성 중시:** 시스템의 확장성을 중요시하는 경우.

### Orchestration (오케스트레이션형)

**특징:**
- 중앙 집중화된 오케스트레이터(Orchestrator)가 전체 워크플로우를 제어합니다.
- 오케스트레이터가 각 서비스 호출을 조정하고 관리합니다.
- 명시적이고 중앙화된 제어 구조를 가집니다.

**장점:**
- **명확한 제어:** 중앙화된 관리 덕분에 워크플로우의 흐름을 명확히 이해하고 관리할 수 있습니다.
- **복잡한 비즈니스 로직:** 복잡한 워크플로우를 관리하기에 적합합니다.
- **디버깅 용이:** 문제 발생 시 중앙화된 로직 덕분에 디버깅이 비교적 용이합니다.
- **순서 보장:** 서비스 호출의 순서를 쉽게 관리할 수 있습니다.

**단점:**
- **단일 장애점:** 오케스트레이터가 장애가 발생하면 전체 시스템에 영향을 미칠 수 있습니다.
- **확장성 제한:** 중앙 집중화된 관리로 인해 확장성이 제한될 수 있습니다.
- **서비스 결합도:** 서비스 간의 의존성이 높아져, 하나의 서비스 변경이 다른 서비스에 영향을 줄 수 있습니다.

**적합한 곳:**
- **복잡한 워크플로우:** 복잡한 비즈니스 로직과 워크플로우를 관리해야 하는 경우.
- **일관성 중시:** 워크플로우의 일관성과 순서를 보장해야 하는 경우.
- **명확한 제어 필요:** 중앙에서 명확히 제어하고 관리해야 하는 경우.

### 결론

- **Choreography:** 서비스 간의 상호작용이 비교적 단순하고, 독립적으로 동작해야 하며, 확장성이 중요한 경우에 적합합니다.
- **Orchestration:** 복잡한 비즈니스 로직을 관리하고, 일관성과 제어가 중요한 경우에 적합합니다.

이 두 접근 방식은 상호 배타적이지 않으며, 혼합하여 사용할 수도 있습니다. 예를 들어, 일부 서비스는 Choreography를 통해 느슨하게 결합되고, 다른 서비스는 Orchestration을 통해 복잡한 워크플로우를 관리하는 방식으로 구현할 수 있습니다.