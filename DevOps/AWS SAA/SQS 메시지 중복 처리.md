### 문제 요약

- **여러 EC2 인스턴스에서 애플리케이션 운영**
- **Amazon SQS 큐에서 메시지 수신**
- **Amazon RDS 테이블에 기록**
- **큐에서 메시지 삭제**
- **RDS에 중복 레코드 발생 (SQS 큐에는 중복 메시지 없음)**
- **메시지가 한 번만 처리되도록 보장 필요**

---

## 선택지 요약

| 옵션    | 설명                                                 |
|-------|----------------------------------------------------|
| **A** | CreateQueue API로 새 큐 생성                            |
| **B** | AddPermission API로 적절한 권한 추가                       |
| **C** | ReceiveMessage API로 적절한 대기 시간(wait time) 설정        |
| **D** | ChangeMessageVisibility API로 visibility timeout 증가 |

---

## 요구사항 vs 선택지 비교표

| 요구사항             | A (CreateQueue) | B (AddPermission) | C (ReceiveMessage) | D (ChangeVisibility) |
|------------------|:---------------:|:-----------------:|:------------------:|:--------------------:|
| 중복 메시지 방지        |        ❌        |         ❌         |         ❌          |          ✅           |
| 메시지 한 번만 처리 보장   |        ❌        |         ❌         |         ❌          |          ✅           |
| SQS/RDS와 직접적 연관성 |        ❌        |         ❌         |         ❌          |          ✅           |
| 실질적 문제 해결        |        ❌        |         ❌         |         ❌          |          ✅           |

---

## 해설

### **A. CreateQueue API로 새 큐 생성**

- 새 큐를 만든다고 중복 메시지 문제가 해결되지 않음

### **B. AddPermission API로 권한 추가**

- 권한 문제와는 무관

### **C. ReceiveMessage API로 대기 시간 설정**

- 메시지 수신 대기 시간(wait time)은 중복 처리와 직접적 관련 없음

### **D. ChangeMessageVisibility API로 visibility timeout 증가** (문제 정답)

- 메시지의 visibility timeout이 짧으면, 작업 중 장애가 발생해 메시지가 삭제되지 않을 수 있음
- 이 경우 메시지가 다시 다른 인스턴스에서 처리되어 중복 기록 발생
- visibility timeout을 늘리면, 메시지가 한 번만 처리될 확률이 높아짐
- [AWS 공식 문서 참고](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html)

---

## 결론

- **정답: D (ChangeMessageVisibility API로 visibility timeout 증가)**
    - 메시지 처리 중 장애 시, 메시지가 다시 나타나 중복 처리되는 것을 방지하기 위함
    - visibility timeout 내에 메시지를 반드시 삭제하도록 구현해야 함

---

## 기억해두면 좋은 영어 표현

- **"To guarantee that messages are processed only once, you should increase the visibility timeout
  so that the message is not available to other consumers until processing and deletion are
  complete."**
    - (메시지가 한 번만 처리되도록 보장하려면, 메시지 처리 및 삭제가 완료될 때까지 다른 소비자에게 메시지가 보이지 않도록 visibility timeout을 늘려야
      합니다.)

---

## 영어로 질문하기 예시

**한글:**  
SQS 메시지가 중복 처리되는 것을 방지하려면 visibility timeout을 조정하는 것이 맞나요?

**영어:**  
Is adjusting the visibility timeout the correct way to prevent duplicate processing of SQS messages?

---

이 양식으로 계속 정리해드릴 수 있습니다.  
다른 문제나 추가 요청 있으시면 언제든 말씀해 주세요!