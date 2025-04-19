# AWS S3 데이터 공유 시 전송 비용 최소화 전략

## 요약

- **상황:**
    - 미국 내 여러 지역에서 수년간 수집한 3TB 이상의 데이터를 S3 버킷에 저장
    - 유럽의 마케팅 회사와 데이터를 공유해야 함
    - 데이터 전송 비용을 최소화하고자 함

---

## 선택지 요약

| 옵션    | 설명                                             | 비용 부담 주체        | 적합성 |
|-------|------------------------------------------------|-----------------|-----|
| **A** | S3 Requester Pays 활성화 (요청자가 데이터 전송 비용 부담)      | 데이터 요청자(마케팅 회사) | ✅   |
| **B** | S3 Cross-Region Replication으로 마케팅 회사 S3 버킷에 복제 | 데이터 소유자(회사)     | ❌   |
| **C** | 크로스 계정 액세스 부여 (마케팅 회사가 직접 접근)                  | 데이터 소유자(회사)     | ❌   |
| **D** | S3 Intelligent-Tiering 사용 및 마케팅 회사 S3 버킷 동기화   | 데이터 소유자(회사)     | ❌   |

---

## 해설

- **Requester Pays** 기능을 사용하면 S3 버킷의 데이터에 접근하는 쪽(즉, 마케팅 회사)이 데이터 전송 비용을 부담함.
- 대용량 데이터를 외부와 공유할 때, 데이터 소유자가 비용 부담 없이 데이터를 제공할 수 있는 최적의 방법.
- **Cross-Region Replication**이나 **크로스 계정 액세스**는 데이터 소유자가 모든 전송 비용을 부담하게 되어 비용 최소화 목적에 부적합.
- **Intelligent-Tiering**은 저장 비용 최적화에는 유용하지만, 데이터 전송 비용 절감과 직접적 연관은 없음.

---

## 결론

- **정답: A (S3 Requester Pays 활성화)**
    - 데이터 접근/다운로드 비용을 요청자(마케팅 회사)가 부담하도록 하여, 데이터 소유자의 전송 비용을 최소화할 수 있음.

---

## 기억해두면 좋은 영어 표현

- **"By enabling the Requester Pays feature on an S3 bucket, the requester is responsible for data
  transfer and request costs rather than the bucket owner."**
    - (S3 버킷에서 Requester Pays 기능을 활성화하면, 데이터 전송 및 요청 비용을 버킷 소유자가 아닌 요청자가 부담하게 됩니다.)

---

## 영어로 질문하기 예시

**한글:**  
S3 버킷의 대용량 데이터를 외부 회사와 공유할 때, 내 데이터 전송 비용을 최소화하려면 어떻게 해야 하나요?

**영어:**  
When sharing large datasets stored in my S3 bucket with an external company, how can I minimize my
data transfer costs?

---

