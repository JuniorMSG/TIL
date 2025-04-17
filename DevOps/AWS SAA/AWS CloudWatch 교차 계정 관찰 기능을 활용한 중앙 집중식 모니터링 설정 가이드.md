## 문제 요약 (597)

- **환경**: AWS Organizations 내 여러 계정, 전용 모니터링 계정 존재
- **목표**: Amazon CloudWatch를 사용하여 모든 계정의 데이터를 중앙에서 쿼리 및 시각화

---

## 정답 및 해설

### **정답: A**
> **모니터링 계정에 대해 CloudWatch 교차 계정 관찰 기능을 활성화합니다. 모니터링 계정에서 제공하는 AWS CloudFormation 템플릿을 각 AWS 계정에 배포하여 모니터링 계정과 데이터를 공유합니다.**

#### **이유**
- AWS의 공식적인 **CloudWatch Cross-Account Observability** 기능은 여러 계정의 CloudWatch 데이터를 중앙의 모니터링 계정에서 쿼리하고 시각화할 수 있도록 지원합니다.
- 각 계정에 CloudFormation 템플릿을 배포해 필요한 권한과 공유 설정을 자동화할 수 있습니다.
- 이 방법은 멀티 계정 환경에서 **중앙집중식 모니터링**을 위한 AWS 권장 방식입니다.

---

### **오답 해설**

- **B (SCP 설정)**:  
  SCP는 계정이나 OU의 권한을 제한/허용하는 정책이지만, 실제 데이터 접근 및 쿼리/시각화 기능을 제공하지 않습니다.

- **C, D (IAM 사용자와 정책)**:  
  IAM 사용자와 정책만으로는 교차 계정 CloudWatch 데이터 집계 및 시각화가 불가능합니다.  
  CloudWatch Cross-Account Observability와 같은 공식 기능이 필요합니다.

---

## 참고 문서명

- **한글:**  
  AWS CloudWatch 교차 계정 관찰 기능을 활용한 중앙 집중식 모니터링 설정 가이드

- **영어:**  
  Centralized Monitoring Across AWS Accounts Using CloudWatch Cross-Account Observability

---

## 기억해두면 좋은 영어 표현

- **"Enable CloudWatch cross-account observability to centrally query and visualize monitoring data from multiple AWS accounts."**  
  (CloudWatch 교차 계정 관찰 기능을 활성화하여 여러 AWS 계정의 모니터링 데이터를 중앙에서 쿼리하고 시각화합니다.)

---

## 영어로 질문하기

**한글 질문:**  
AWS Organizations 환경에서 여러 계정의 CloudWatch 데이터를 한 계정에서 중앙 집중적으로 모니터링하려면 어떻게 해야 하나요?

**영어 표현:**  
How can I centrally monitor and visualize CloudWatch data from multiple AWS accounts within an AWS Organizations environment?

---