# AWS 데이터 레이크 시각화 및 접근 제어 솔루션 비교 (3)

## 요약

- **AWS 데이터 레이크**: S3와 RDS(PostgreSQL) 데이터 포함
- **주요 요구사항**
    - 모든 데이터 소스 시각화 및 리포팅
    - 경영진은 전체 접근, 나머지는 제한적 접근

---

## 선택지 요약

| 옵션    | 설명                                                 |
|-------|----------------------------------------------------|
| **A** | QuickSight, IAM 역할로 대시보드 공유 (세밀한 사용자/그룹 권한 부족)     |
| **B** | QuickSight, 사용자 및 그룹별로 대시보드 공유 (세분화된 접근 제어 가능, 정답) |
| **C** | Glue ETL + S3 리포트, S3 정책으로 접근 제한 (실시간 시각화/대시보드 불가) |
| **D** | Glue + Athena + S3 리포트, S3 정책 (실시간 시각화/대시보드 불가)    |

---

## 요구사항 vs 선택지 비교표

| 요구사항         | A (QuickSight+IAM) | B (QuickSight+User/Group) | C (Glue+S3) | D (Glue+Athena+S3) |
|--------------|:------------------:|:-------------------------:|:-----------:|:------------------:|
| 모든 데이터 소스 포함 |         ✅          |             ✅             |      ✅      |         ✅          |
| 시각화/대시보드 제공  |         ✅          |             ✅             |      ❌      |         ❌          |
| 경영진 전체 접근    |         ✅          |             ✅             |      ✅      |         ✅          |
| 세분화된 접근 제어   |         ❌          |             ✅             |      ❌      |         ❌          |
| 운영 오버헤드 최소화  |         ✅          |             ✅             |      ❌      |         ❌          |

---

## 해설

- **QuickSight**는 S3, RDS 등 다양한 데이터 소스를 연결하여 대시보드/리포트 작성이 가능
- **사용자 및 그룹별 공유**(옵션 B)는 경영진과 일반 직원의 접근 권한을 세분화해서 관리할 수 있음
- S3 리포트 방식(C, D)은 실시간 대시보드 제공 및 세밀한 접근 제어가 어려움
- IAM 역할 기반 공유(A)는 사용자/그룹별 세밀한 권한 제어에 한계가 있음

---

## 결론

- **추천 솔루션: B (Amazon QuickSight에서 사용자 및 그룹별 대시보드 공유)**
    - 모든 요구사항을 가장 효과적으로 충족

---

## 기억해두면 좋은 영어 표현

- **"Amazon QuickSight allows you to share dashboards with specific users and groups, enabling
  fine-grained access control for your data visualizations."**
    - (Amazon QuickSight는 특정 사용자 및 그룹과 대시보드를 공유할 수 있어, 데이터 시각화에 대한 세밀한 접근 제어가 가능합니다.)

---

## 영어로 질문하기 예시

**한글:**  
QuickSight에서 대시보드를 사용자와 그룹별로 공유하여 접근 권한을 세분화할 수 있나요?

**영어:**  
Can I share dashboards in QuickSight with specific users and groups to enable fine-grained access
control?

---
