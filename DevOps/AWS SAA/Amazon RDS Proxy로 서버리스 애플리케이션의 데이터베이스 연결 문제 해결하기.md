## 문제 요약 (552)

- **상황**: 서버리스 애플리케이션이 Amazon RDS를 사용
- **문제점**: 갑작스러운 트래픽 증가 시 DB 연결이 자주 열리고 닫혀서 오류 및 연결 부족 발생
- **요구사항**:
    - **코드 변경 없이** 해결
    - 항상 확장 가능하고 가용성 높게 유지

---

## 정답 및 해설

### **정답: C**
> **서버리스 애플리케이션과 Amazon RDS 간에 Amazon RDS 프록시를 배포합니다.**

#### **이유**
- **Amazon RDS Proxy**는 데이터베이스 연결을 풀링(pooling)하여, 서버리스 환경에서 빈번하게 발생하는 연결/해제 문제를 해결합니다.
- **자동 연결 관리**로, 갑작스러운 트래픽 증가에도 DB 연결 수를 효율적으로 관리하여 오류와 연결 부족을 방지합니다.
- **애플리케이션 코드 변경 없이** 프록시만 추가하면 적용 가능.
- **가용성 및 확장성**도 향상됨.

---

### **오답 해설**

- **A (최대 연결 수 증가)**: 연결 수를 늘려도 풀링이 없으면 서버리스 환경에서는 여전히 문제가 발생.
- **B (DB 인스턴스 크기 증가)**: 인스턴스 크기를 늘려도 연결 관리 문제가 해결되지 않음.
- **D (예약 인스턴스 구매)**: 비용 최적화에는 도움되나, 연결 및 가용성 문제는 해결하지 못함.

---


## 기억해두면 좋은 영어 표현

- **"Deploy Amazon RDS Proxy between your serverless application and Amazon RDS to efficiently manage database connections and improve scalability and availability, without code changes."**  
  (코드 변경 없이 서버리스 애플리케이션과 RDS 사이에 RDS Proxy를 배포해 데이터베이스 연결을 효율적으로 관리하고 확장성과 가용성을 향상시키세요.)

---

## 영어로 질문하기

**한글 질문:**  
코드 변경 없이 서버리스 애플리케이션과 RDS 간의 연결 부족 문제를 해결하려면 어떻게 해야 하나요?

**영어 표현:**  
How can I resolve database connection exhaustion issues between a serverless application and Amazon RDS without changing the application code?

---

이직이나 실무에 도움이 될 만한 추가 정보가 필요하면 언제든 말씀해 주세요!