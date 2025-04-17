## 문제 요약 (280)

- **상황**: Oracle DB를 AWS로 마이그레이션
- **데이터**: 수백만 개 GIS 이미지를 포함하는 단일 테이블, 각 이미지는 지리 코드(geo code)로 식별
- **특징**: 자연재해 시 수만 장의 이미지가 몇 분마다 업데이트됨 (쓰기 부하 높음)
- **요구사항**: 가용성, 확장성, 비용 효율성

---

## 정답 및 해설

### **정답: B**
> **Amazon S3 버킷에 이미지를 저장합니다. 지리적 코드를 키로, 이미지 S3 URL을 값으로 사용하여 Amazon DynamoDB를 사용합니다.**

#### **이유**
- **S3**: 대용량 이미지 저장에 최적화, 확장성·내구성·비용 효율성 뛰어남
- **DynamoDB**: 초고속 읽기/쓰기, 무제한 확장성, 지리 코드로 빠른 조회 가능
- **조합**: 이미지 저장은 S3, 메타데이터(geo code와 S3 URL)는 DynamoDB에 저장 → 대규모 업데이트와 조회에 적합, 비용도 저렴

---

### **오답 해설**

#### A. RDS(Oracle)에 이미지와 지리 코드 저장
- 이미지까지 RDS에 저장하면 저장 비용이 매우 높고, 대량 쓰기/읽기 시 확장성 및 성능 한계

#### C. DynamoDB에 이미지와 지리 코드 저장
- DynamoDB는 대용량 바이너리(이미지) 저장에 적합하지 않음, 저장 비용이 비쌈

#### D. S3에 이미지 저장, RDS(Oracle)에 geo code 및 S3 URL 저장
- RDS는 대량의 업데이트 트래픽과 대규모 확장성에 한계, 비용도 DynamoDB보다 높음

---

## 기억해두면 좋은 영어 표현

- **"For highly scalable and cost-effective storage of large images, use Amazon S3 for image files and DynamoDB for metadata."**  
  (대용량 이미지를 확장성 있고 비용 효율적으로 저장하려면 이미지 파일은 S3, 메타데이터는 DynamoDB를 사용하세요.)

---

## 영어로 질문하기

**한글 질문:**  
이런 상황에서 가장 확장성 있고 비용 효율적인 AWS 아키텍처는 무엇인가요?

**영어 표현:**  
What is the most scalable and cost-effective AWS architecture for this scenario?

---
