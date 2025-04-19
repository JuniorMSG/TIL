# 주문 순서 보장: AWS 기반 전자상거래 주문 처리 아키텍처

## 요약

- **상황:**
    - 한 회사가 AWS에서 전자상거래 웹 애플리케이션을 구축 중
    - 주문 정보는 Amazon API Gateway REST API로 전송됨
    - 주문이 **접수된 순서대로** 처리되어야 함

---

## 선택지 요약

| 옵션    | 설명                                      | 순서 보장 | 적합성           |
|-------|-----------------------------------------|-------|---------------|
| **A** | API Gateway → SNS → Lambda              | ❌     | SNS는 순서 보장 X  |
| **B** | API Gateway → SQS **FIFO** 대기열 → Lambda | ✅     | FIFO로 순서 보장   |
| **C** | API Gateway 권한 부여자로 모든 요청 차단            | ❌     | 비현실적/불필요      |
| **D** | API Gateway → SQS **표준** 대기열 → Lambda   | ❌     | 표준 큐는 순서 보장 X |

---

## 해설

- **Amazon SQS FIFO(First-In-First-Out) Queue**는 메시지가 들어온 순서를 정확히 보장합니다.
- SNS, SQS 표준 큐 등은 높은 처리량에는 적합하지만, **순서 보장**이 필요할 때는 적합하지 않습니다.
- SQS FIFO 큐에 메시지를 넣고, Lambda로 처리하면 **주문이 접수된 순서대로** 안전하게 처리할 수 있습니다.

---

## 결론

- **정답: B (API Gateway → SQS FIFO 대기열 → Lambda)**
    - 주문 순서 보장이 반드시 필요한 경우, SQS FIFO 큐를 사용하는 것이 가장 적합합니다.

---

## 기억해두면 좋은 영어 표현

- **"To guarantee the order of processing, use an Amazon SQS FIFO queue, which preserves the exact
  order of message delivery."**
    - (처리 순서를 보장하려면, 메시지 전달 순서를 정확히 유지하는 Amazon SQS FIFO 큐를 사용하세요.)

---

## 영어로 질문하기 예시

**한글:**  
주문이 들어온 순서대로 처리되도록 AWS에서 아키텍처를 설계하려면 어떻게 해야 하나요?

**영어:**  
How can I design an AWS architecture to ensure that orders are processed in the exact order they are
received?

---

## 추가 팁 (이직/실무)

- SQS FIFO 큐는 **순서 보장**뿐 아니라 **중복 방지(Deduplication)** 기능도 제공합니다.
- FIFO 큐는 표준 큐보다 처리량이 낮을 수 있으니, 트래픽 규모에 따라 적합성을 검토하세요.
- 아키텍처 설계 시, **순서 보장 여부**와 **처리량 요구사항**을 명확히 구분하는 것이 중요합니다.

---

이렇게 정리해두면 실무 아키텍처 설계, 면접 답변, 문서화에 모두 활용할 수 있습니다!