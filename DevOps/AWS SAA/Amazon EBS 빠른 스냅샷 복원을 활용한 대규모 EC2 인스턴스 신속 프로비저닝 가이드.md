## 문제 요약 (263)

- **상황**: 수요 급증, 대규모 EC2 인스턴스 프로비저닝 필요
- **조건**: Auto Scaling 그룹 사용, **최소 초기화 대기 시간**(최대한 빠른 인스턴스 시작) 필요

---

## 정답 및 해설

### **정답: B**
> **스냅샷에서 Amazon Elastic Block Store(Amazon EBS) 빠른 스냅샷 복원 활성화 스냅샷을 사용하여 AMI 프로비저닝 Auto Scaling 그룹의 AMI를 새 AMI로 교체**

#### **이유**
- **EBS 빠른 스냅샷 복원(Fast Snapshot Restore, FSR)** 기능을 사용하면, 스냅샷에서 생성된 볼륨의 초기화 시간이 크게 단축됩니다.
- FSR을 활성화한 스냅샷을 기반으로 AMI를 만들고, 이를 Auto Scaling 그룹에 적용하면, **최소 초기화 대기 시간**으로 EC2 인스턴스를 빠르게 시작할 수 있습니다.
- AWS 공식 문서에서도 대규모, 신속한 프로비저닝에 FSR 사용을 권장합니다.

---

### **오답 해설**

- **A**: Step Functions로 AMI 교체 및 등록은 자동화에는 유용하지만, 인스턴스 초기화 속도 개선에는 직접적인 도움이 되지 않습니다.
- **C**: DLM과 Lambda를 통한 AMI 관리/자동화는 주기적 관리에는 적합하지만, 초기화 속도 최적화에는 부적합합니다.
- **D**: EventBridge와 백업 수명 주기 정책은 이 시나리오(신속한 초기화)와 맞지 않습니다.

---

## 기억해두면 좋은 영어 표현

- **"Enable Amazon EBS Fast Snapshot Restore to minimize initialization wait time when provisioning EC2 instances at scale."**  
  (Amazon EBS 빠른 스냅샷 복원을 활성화하여 대규모 EC2 인스턴스 프로비저닝 시 초기화 대기 시간을 최소화하세요.)

---

## 영어로 질문하기

**한글 질문:**  
Auto Scaling 그룹에서 대규모로 EC2 인스턴스를 신속하게 시작하려면 어떻게 해야 하나요?

**영어 표현:**  
How can I minimize the initialization wait time when launching a large number of EC2 instances in an Auto Scaling group?

---

추가 궁금한 점이나 이직 관련 정보가 필요하면 언제든 말씀해 주세요!