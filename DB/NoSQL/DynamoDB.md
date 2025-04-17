아래와 같이 정리해드릴게요.

---

## DynamoDB의 데이터베이스 기반

- **DynamoDB는 NoSQL 데이터베이스입니다.**
    - **키-값(Key-Value) 및 문서(Document) 저장 모델**을 지원합니다.
    - 관계형 데이터베이스(RDBMS)가 아니며, 테이블 구조는 있지만 스키마가 유연합니다.
    - SQL이 아닌 자체적인 쿼리 언어와 API를 사용합니다.

### 주요 특징

- **완전관리형(Managed)**
    - AWS에서 자동으로 확장성, 내결함성, 백업, 보안을 관리합니다.
- **수평적 확장(Scalable)**
    - 트래픽이 늘어나도 자동으로 처리 용량이 늘어나며, 초당 수백만 건의 요청을 처리할 수 있습니다.
- **고성능/저지연**
    - 밀리초 단위의 응답 속도를 제공합니다.
- **스키마리스(Schemaless)**
    - 각 아이템(행)은 서로 다른 속성을 가질 수 있습니다.
- **NoSQL**
    - 전통적인 관계형 데이터베이스(RDB)와 달리 조인, 트랜잭션, 복잡한 쿼리 기능이 제한적입니다.

### DynamoDB의 내부 구조

- **Amazon의 Dynamo 논문**에서 영감을 받은 분산형 아키텍처
- **파티셔닝**을 통해 데이터를 여러 서버에 분산 저장
- **키-값** 및 **문서 형식(JSON)** 저장 지원

---

## 추천 문서명

- **한글:**  
  DynamoDB의 데이터베이스 구조와 특징 정리

- **영어:**  
  Overview of DynamoDB Database Model and Features

---

## 기억해두면 좋은 영어 표현

- **"DynamoDB is a fully managed NoSQL database service that supports both key-value and document data models."**  
  (DynamoDB는 키-값 및 문서 데이터 모델을 지원하는 완전관리형 NoSQL 데이터베이스 서비스입니다.)


---





# Amazon의 Dynamo 논문이란?

**Amazon의 Dynamo 논문**은 2007년 Amazon에서 발표한 **분산 키-값 저장소**(Distributed Key-Value Store) 시스템인 **Dynamo**의 설계와 구현에 대해 다룬 논문입니다. 이 논문은 대규모 웹 서비스(특히 Amazon.com)의 가용성과 확장성을 보장하기 위해 어떻게 데이터베이스 시스템을 설계했는지 설명합니다.

---

## 핵심 내용 요약

- **목적**  
  대규모 서비스에서 **항상 사용 가능한(Highly Available)** 데이터 저장소를 만들기 위해 설계됨.  
  (예시: 장바구니, 결제 등 서비스 중단이 치명적인 기능)

- **특징**
    1. **분산 시스템**: 여러 서버에 데이터를 분산 저장하여 장애에 강함
    2. **Eventually Consistent**: 항상 완벽하게 일치하는 데이터보다, 가용성과 응답 속도를 더 중시함
    3. **노드 추가/제거 용이**: 서버를 쉽게 추가하거나 제거할 수 있음 (확장성)
    4. **충돌 해결**: 데이터 충돌이 발생할 수 있으며, 이를 애플리케이션 레벨에서 해결할 수 있도록 설계

- **주요 기술**
    - **Consistent Hashing**: 데이터 분배를 효율적으로 처리
    - **Vector Clocks**: 데이터 버전 관리 및 충돌 감지
    - **Quorum Protocol**: 읽기/쓰기 성공 기준을 유연하게 조정 가능
    - **Gossip Protocol**: 노드 상태 동기화

---

## 왜 중요한가?

- **NoSQL** 계열 분산 데이터베이스의 개념적 토대가 됨  
  (Cassandra, Riak 등 여러 시스템에 영향을 줌)
- **CAP 이론**에서 **가용성(Availability)**과 **파티션 허용성(Partition tolerance)**을 우선시하는 설계

---

## 기억해두면 좋은 영어 표현

- **Dynamo is a highly available key-value storage system developed by Amazon.**
    - Dynamo는 Amazon에서 개발한 고가용성 키-값 저장 시스템이다.
- **It prioritizes availability and partition tolerance over strong consistency.**
    - 강한 일관성보다 가용성과 파티션 허용성을 우선시한다.
- **Dynamo uses techniques like consistent hashing and vector clocks to manage data distribution and versioning.**
    - Dynamo는 데이터 분산과 버전 관리를 위해 Consistent Hashing과 Vector Clock과 같은 기법을 사용한다.

---

## 영어로 질문하기

- **What is the Dynamo paper by Amazon?**
- **Can you explain the main concepts of Amazon's Dynamo paper?**
- **How did Dynamo influence modern NoSQL databases?**

---

## 이직에 도움되는 정보

- **Dynamo 논문**은 **분산 시스템 설계, NoSQL 데이터베이스, 대규모 시스템 아키텍처**에 대한 깊은 이해를 보여줄 수 있는 좋은 주제입니다.
- 면접에서 "Dynamo 논문에서 배운 점"이나 "Dynamo와 CAP 이론의 관계" 등을 설명할 수 있으면 높은 평가를 받을 수 있습니다.

---

추가적으로 논문 원문이 필요하거나, 세부 기술(Consistent Hashing, Vector Clock 등)에 대한 설명이 필요하면 언제든 요청해 주세요!