## 문제 요약 (523)

- **상황**: 700TB NAS 데이터를 90일 이내에 AWS로 이전해야 함
- **환경**: 10Gbps Direct Connect, 하이브리드 환경
- **요구사항**
    - **중단 없이** 데이터 마이그레이션
    - 이전 기간 동안 **데이터 접근 및 업데이트 가능**

---

## 정답 및 해설

### **정답: A**
> **회사 데이터 센터에서 AWS DataSync 에이전트를 생성합니다. 데이터 전송 작업을 만듭니다. Amazon S3 버킷으로 전송을 시작합니다.**

#### **이유**
- **AWS DataSync**는 대용량 NAS 데이터를 AWS로 이전하는 데 최적화된 서비스입니다.
- **Direct Connect**를 활용하여 빠르고 안정적으로 전송할 수 있습니다.
- DataSync는 **증분 복사**(변경된 파일만 복사) 및 **동기화** 기능을 제공하므로, 이전 기간 동안 데이터 접근/업데이트가 가능합니다.
- **마이그레이션 중에도 데이터 중단 없이** 동기화가 계속되어 규제 요구사항 충족 및 비즈니스 연속성 보장.

---

### **오답 해설**

- **B (Snowball Edge)**: 대용량 데이터 이전에는 적합하지만, 디바이스 배송 기간이 필요하고, 이전 중 데이터 접근/업데이트가 어렵습니다.
- **C (rsync + Direct Connect)**: rsync는 대용량 데이터, 변경분 동기화, 오류 복구, 성능 최적화 등에서 DataSync에 비해 효율성이 떨어집니다.
- **D (테이프 백업)**: 테이프는 느리고, 중간에 데이터 접근/업데이트가 불가능합니다.

---

## 기억해두면 좋은 영어 표현

- **"Use AWS DataSync with Direct Connect for seamless, incremental migration of large-scale NAS data to the cloud without downtime."**  
  (다운타임 없이 대규모 NAS 데이터를 클라우드로 점진적으로 마이그레이션하려면 Direct Connect와 함께 AWS DataSync를 사용하세요.)

---

## 영어로 질문하기

**한글 질문:**  
대규모 NAS 데이터를 90일 이내에, 중단 없이 AWS로 이전하면서 이전 기간 동안에도 데이터 접근 및 업데이트가 가능하게 하려면 어떤 AWS 서비스를 사용해야 하나요?

**영어 표현:**  
Which AWS service should I use to migrate large-scale NAS data to AWS within 90 days, without downtime, and with continued access and updates to the data during the migration period?

---

이직이나 실무에 도움이 될 만한 추가 정보가 필요하면 언제든 말씀해 주세요!