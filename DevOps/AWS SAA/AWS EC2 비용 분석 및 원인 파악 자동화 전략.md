# AWS EC2 비용 분석 및 원인 파악 자동화 전략

## 요약

- **상황:** 최근 EC2 비용이 증가, 일부 인스턴스에서 원치 않는 vertical scaling(더 큰 인스턴스 타입으로 변경)이 발생
- **목표:** 최근 2개월간 EC2 비용을 인스턴스 타입별로 비교하고, vertical scaling의 원인을 분석
- **제약:** 운영 오버헤드(Operational Overhead)를 최소화해야 함

---

## 선택지 요약

| 옵션    | 설명                                                                                                  |
|-------|-----------------------------------------------------------------------------------------------------|
| **A** | AWS Budgets로 예산 리포트 생성, 인스턴스 타입별 비용 비교 (비교 기능은 있으나, 상세 분석 및 필터링 한계)                  |
| **B** | Cost Explorer의 세분화 필터링 기능으로 인스턴스 타입별 EC2 비용 심층 분석 (운영 오버헤드 최소, 실시간/상세 분석, **정답**) |
| **C** | Billing & Cost Management 대시보드의 그래프 활용 (기본적인 비교만 가능, 상세 분석 어려움)                        |
| **D** | Cost and Usage Report → S3 → QuickSight로 시각화 (강력한 분석 가능하나, 설정/운영 오버헤드 큼)                        |

---

## 요구사항 vs 선택지 비교표

| 요구사항                      | A (Budgets) | B (Cost Explorer) | C (Billing Dash) | D (CUR + QuickSight) |
|---------------------------|:-----------:|:-----------------:|:----------------:|:--------------------:|
| 인스턴스 타입별 상세 분석        |      ❌      |        ✅         |        ❌        |         ✅           |
| 최근 2개월 비교               |      ✅      |        ✅         |        ✅        |         ✅           |
| 운영 오버헤드 최소화           |      ✅      |        ✅         |        ✅        |         ❌           |
| 대시보드/그래프 기반 분석       |      ❌      |        ✅         |        ✅        |         ✅           |

---

## 해설

- **Cost Explorer**는 인스턴스 타입, 태그, 기간 등 다양한 기준으로 세분화된 필터링 및 시각화가 가능하여,  
  EC2 비용 증가의 원인(예: 특정 인스턴스 타입의 과도한 사용)을 빠르게 파악할 수 있음.
- **운영 오버헤드**도 거의 없고, AWS 콘솔에서 바로 분석 가능.
- **CUR + QuickSight** 방식은 데이터 분석에 유연하지만, S3 연동 및 QuickSight 설정 등 추가 작업이 많아 요구사항에 비해 과함.

---

## 결론

- **추천 솔루션: B (Cost Explorer의 세분화 필터링 기능 활용)**
  - 인스턴스 타입별로 최근 2개월간의 EC2 비용을 쉽게 비교 및 분석 가능
  - 운영 오버헤드 최소화

---

## 기억해두면 좋은 영어 표현

- **"With AWS Cost Explorer, you can use granular filtering to analyze EC2 costs by instance type and easily identify trends or anomalies."**
  - (AWS Cost Explorer를 사용하면 인스턴스 타입별로 EC2 비용을 세분화하여 분석하고, 트렌드나 이상 징후를 쉽게 파악할 수 있습니다.)

---

## 영어로 질문하기 예시

**한글:**  
Cost Explorer에서 인스턴스 타입별로 EC2 비용을 비교하고, 최근 2개월간의 변화 추이를 분석할 수 있나요?

**영어:**  
Can I use Cost Explorer to compare EC2 costs by instance type and analyze changes over the past two months?

---

이 문서명과 구조로 정리해두면, 실무에서 EC2 비용 이슈 분석이나 AWS 비용 최적화 전략을 세울 때 바로 참고하기 좋습니다!  
추가로 궁금한 점이나 다른 상황도 요청해 주세요.