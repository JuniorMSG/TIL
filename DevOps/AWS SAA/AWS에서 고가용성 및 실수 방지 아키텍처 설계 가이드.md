## 문제 요약 (511)

- **현재 아키텍처**:
    - Amazon RDS DB 인스턴스 1개
    - 수동으로 프로비저닝된 EC2 인스턴스 2개 (단일 가용 영역)
- **문제점**:
    - 직원이 DB 인스턴스를 삭제하여 24시간 장애 발생
- **목표**:
    - 환경의 **전반적인 안정성** 극대화

---

## 정답 및 해설

### **정답: B**
> **DB 인스턴스를 다중 AZ로 업데이트하고 삭제 방지를 활성화합니다. Application Load Balancer 뒤에 EC2 인스턴스를 배치하고 여러 가용 영역에 걸쳐 EC2 Auto Scaling 그룹에서 실행합니다.**

#### **이유**
- **RDS 다중 AZ**:
    - 장애 시 자동 페일오버로 고가용성 보장
    - **삭제 방지** 기능 활성화로 실수로 인한 삭제 방지
- **EC2 Auto Scaling 그룹 & 여러 AZ**:
    - 여러 가용 영역에 인스턴스를 분산시켜 AZ 장애에도 서비스 지속 가능
    - Auto Scaling으로 인스턴스 장애 시 자동 대체
- **Application Load Balancer**:
    - 여러 EC2 인스턴스에 트래픽 분산, 무중단 서비스 제공

#### **핵심 포인트**
- **고가용성(HA)**와 **실수 방지**를 모두 달성하는 유일한 옵션

---

### **오답 해설**

- **A**: EC2 인스턴스가 여전히 한 곳에만 있고, Auto Scaling이나 Load Balancer가 없어 장애 대응 불가
- **C**: Lambda와 API Gateway는 기존 구조와 맞지 않고, DB를 2개 두고 동시 쓰기는 데이터 정합성에 심각한 문제 발생
- **D**: 스팟 인스턴스는 예고 없이 중지될 수 있어 안정성에 적합하지 않음

---

## 기억해두면 좋은 영어 표현

- **"Update the DB instance to Multi-AZ and enable deletion protection. Deploy EC2 instances in an Auto Scaling group across multiple Availability Zones behind an Application Load Balancer."**  
  (DB 인스턴스를 다중 AZ로 업데이트하고 삭제 방지를 활성화하세요. 여러 가용 영역에 걸쳐 Auto Scaling 그룹에서 EC2 인스턴스를 실행하고 Application Load Balancer 뒤에 배치하세요.)

---

## 영어로 질문하기

**한글 질문:**  
애플리케이션 인프라의 안정성을 극대화하려면 어떤 AWS 아키텍처를 적용해야 하나요?

**영어 표현:**  
What AWS architecture should I implement to maximize the reliability of my application infrastructure?

---
