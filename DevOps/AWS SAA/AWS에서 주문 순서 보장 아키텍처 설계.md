# AWS에서 주문 순서 보장 아키텍처 설계

## 문제 요약

- **상황:**
    - 전자상거래 웹 애플리케이션이 AWS에서 운영됨
    - 새로운 주문 정보는 Amazon API Gateway REST API로 전송됨
    - **주문이 들어온 순서대로** 처리되어야 함

---

## 선택지 비교

| 옵션    | 아키텍처 구성                               | 순서 보장 | 적합성           |
|-------|---------------------------------------|-------|---------------|
| **A** | API Gateway → SNS → Lambda            | ❌     | SNS는 순서 보장 X  |
| **B** | API Gateway → SQS **FIFO** 큐 → Lambda | ✅     | FIFO로 순서 보장   |
| **C** | API Gateway Authorizer로 요청 차단         | ❌     | 비현실적/불필요      |
| **D** | API Gateway → SQS **표준** 큐 → Lambda   | ❌     | 표준 큐는 순서 보장 X |

---

## 해설

- **Amazon SQS FIFO(First-In-First-Out) Queue**
    - 메시지가 도착한 순서를 **정확히 보장**합니다.
    - API Gateway와 통합하여 주문 정보를 SQS FIFO 큐에 넣고, Lambda로 처리하면 **주문 접수 순서대로** 안정적으로 처리할 수 있습니다.

- **SNS, SQS 표준 큐**
    - 높은 처리량에는 적합하지만, 메시지 순서 보장이 필요할 때는 부적합합니다.

---

## 결론

- **정답: B**
    - API Gateway → SQS FIFO 큐 → Lambda  
      이 구조를 사용하면 주문이 들어온 순서대로 처리할 수 있습니다.

---

## 기억해두면 좋은 영어 표현

- **"To guarantee the order of processing, use an Amazon SQS FIFO queue, which preserves the exact
  order of message delivery."**  
  (처리 순서를 보장하려면, 메시지 전달 순서를 정확히 유지하는 Amazon SQS FIFO 큐를 사용하세요.)

---

## 영어로 질문하기 예시

**한글:**  
AWS에서 주문을 받은 순서대로 처리하려면 어떻게 해야 하나요?

**영어:**  
How can I ensure that orders are processed in the exact order they are received on AWS?

---

## 이직/실무 팁

- FIFO 큐는 **순서 보장**과 **중복 방지** 기능이 필수적인 워크로드에 적합합니다.
- 표준 큐와 달리 처리량 제한이 있으므로, 대용량 트래픽에는 사전 용량 계획이 필요합니다.

---