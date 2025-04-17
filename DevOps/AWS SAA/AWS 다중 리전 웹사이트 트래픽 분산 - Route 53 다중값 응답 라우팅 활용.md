## 문제 요약 (836)

- **상황**: 두 개의 AWS 리전에 Auto Scaling 그룹을 사용하여 웹 사이트 운영
- **요구사항**:
    - 두 지역에 트래픽 분산 (성장 및 재해 복구 목적)
    - **비정상인 지역에는 트래픽이 가지 않아야 함** (헬스 체크 필요)
    - 데이터베이스 필요 없음

---

## 정답 및 해설

### **정답: B**

> **Amazon Route 53 다중값 응답 라우팅 정책 (Multivalue Answer Routing Policy)**

#### **이유**

- **Route 53 다중값 응답 라우팅**은 여러 지역의 리소스(예: EC2 인스턴스, Load Balancer 등)에 트래픽을 분산시킬 수 있으며, 각 엔드포인트의 상태(헬스
  체크)를 기반으로 비정상 리소스를 응답에서 제외합니다.
- 즉, 한 지역이 장애가 나면 자동으로 정상 지역으로만 트래픽이 분산됩니다.
- 글로벌 트래픽 분산과 장애 복구(Disaster Recovery)에 적합합니다.

---

### **오답 해설**

#### A. Route 53 단순 라우팅 정책

- 단일 엔드포인트만 응답하므로 다중 지역 분산 불가

#### C, D. 한 지역의 Application Load Balancer에 두 지역의 리소스 등록

- Application Load Balancer(ALB)는 **리전 간 리소스 등록이 불가**함
- ALB는 같은 리전 내의 리소스만 대상으로 할 수 있음

---

## 기억해두면 좋은 영어 표현

- **"Route 53 Multivalue Answer Routing can distribute traffic across multiple AWS regions and only
  routes to healthy endpoints."**  
  (Route 53 다중값 응답 라우팅은 여러 AWS 리전에 트래픽을 분산시키며, 정상 엔드포인트로만 라우팅합니다.)

---

## 영어로 질문하기

**한글 질문:**  
AWS에서 두 리전에 웹사이트를 배포하고, 비정상 리전으로 트래픽이 가지 않게 하려면 어떤 Route 53 정책을 써야 하나요?

**영어 표현:**  
Which Route 53 routing policy should I use to distribute traffic across two AWS regions and avoid
sending traffic to unhealthy regions?

---

추가 질문 있으면 언제든 말씀해 주세요!