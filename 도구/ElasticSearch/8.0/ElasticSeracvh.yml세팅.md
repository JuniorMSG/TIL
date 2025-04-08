Elasticsearch 8 (ES8)의 `elasticsearch.yml` 설정 파일에서 중요한 부분들을 정리해 드리겠습니다. ES8에서는 보안 기능(X-Pack)이 기본적으로 활성화되어 있으며, Docker와 같은 컨테이너 환경에서 자주 사용되는 설정도 포함되어 있습니다.

---

## **1. 클러스터 설정**

### **클러스터 이름**
```yaml
cluster.name: "my-cluster"
```
- 클러스터의 고유 이름을 지정합니다.
- 동일한 클러스터 이름을 가진 노드만 같은 클러스터에 속할 수 있습니다.

---

### **노드 이름**
```yaml
node.name: "node-1"
```
- 노드의 고유 이름을 설정합니다.
- 기본적으로 호스트 이름이 사용되지만, 명시적으로 지정하는 것이 좋습니다.

---

### **노드 역할**
```yaml
node.roles: ["master", "data", "ingest"]
```
- 노드가 수행할 역할을 정의합니다.
- 주요 역할:
    - `master`: 클러스터 관리를 담당.
    - `data`: 데이터를 저장하고 검색 요청을 처리.
    - `ingest`: 데이터 처리 파이프라인을 실행.
    - `ml`: 머신 러닝 작업 담당.
    - `remote_cluster_client`: 리모트 클러스터와 통신.

---

### **초기 마스터 노드**
```yaml
cluster.initial_master_nodes: ["node-1", "node-2"]
```
- 클러스터를 처음 시작할 때 마스터 노드를 선출하기 위한 초기 후보 노드 리스트입니다.
- 클러스터 부트스트랩 시에만 필요하며, 이후에는 자동으로 관리됩니다.

---

### **시드 호스트**
```yaml
discovery.seed_hosts: ["node-1", "node-2"]
```
- 클러스터 내 다른 노드를 검색하기 위한 초기 노드 리스트입니다.
- IP 주소나 호스트 이름을 지정합니다.

---

### **디스커버리 타입 (단일 노드 설정)**
```yaml
discovery.type: single-node
```
- 단일 노드 환경에서 클러스터 디스커버리를 비활성화합니다.
- 개발 또는 테스트 환경에서 유용합니다.

---

## **2. 네트워크 설정**

### **호스트 및 포트**
```yaml
network.host: 0.0.0.0
http.port: 9200
```
- `network.host`: Elasticsearch가 요청을 수신할 네트워크 인터페이스를 지정합니다.
    - `localhost`: 로컬 접근만 허용.
    - `0.0.0.0`: 모든 네트워크 인터페이스에서 요청 수신.
- `http.port`: HTTP API가 사용하는 포트를 설정합니다. 기본값은 `9200`입니다.

---

### **HTTPS 설정**
ES8에서는 HTTPS가 기본적으로 권장됩니다.
```yaml
xpack.security.http.ssl.enabled: true
xpack.security.http.ssl.key: certs/http.key
xpack.security.http.ssl.certificate: certs/http.crt
xpack.security.http.ssl.certificate_authorities: certs/ca.crt
```
- HTTPS를 활성화하고 SSL 인증서를 설정합니다.
- 기본적으로 Elasticsearch는 자체 서명된 인증서를 생성합니다.

---

## **3. 데이터 경로**

### **데이터 및 로그 디렉토리**
```yaml
path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch
```
- `path.data`: Elasticsearch 데이터가 저장되는 경로.
- `path.logs`: Elasticsearch 로그가 저장되는 경로.
- Docker 환경에서는 볼륨 마운트를 통해 외부 경로로 설정하는 것이 일반적입니다.

---

## **4. JVM 메모리 설정**

### **Heap 크기 설정**
JVM 힙 메모리는 Elasticsearch 성능에 중요한 영향을 미칩니다.
```yaml
jvm.options:
  -Xms2g
  -Xmx2g
```
- `-Xms`: 힙 메모리의 최소 크기.
- `-Xmx`: 힙 메모리의 최대 크기.
- 두 값을 동일하게 설정하는 것이 권장됩니다.
- 메모리 크기는 시스템 메모리의 50%를 넘지 않도록 설정하세요.

---

## **5. 보안 설정 (X-Pack)**

### **보안 활성화**
ES8에서는 보안(X-Pack)이 기본적으로 활성화되어 있습니다.
```yaml
xpack.security.enabled: true
```
- Elasticsearch 보안을 활성화합니다.
- 기본적으로 사용자 인증과 역할 기반 접근 제어(RBAC)가 활성화됩니다.

---

### **사용자 인증 및 암호**
Elasticsearch는 기본적으로 `elastic` 사용자 계정을 제공합니다. 초기 비밀번호를 설정하려면 다음 명령을 실행합니다:
```bash
bin/elasticsearch-reset-password -u elastic
```

---

### **TLS 설정 (클러스터 간 통신)**
```yaml
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.key: certs/transport.key
xpack.security.transport.ssl.certificate: certs/transport.crt
xpack.security.transport.ssl.certificate_authorities: certs/ca.crt
```
- 클러스터 노드 간 통신에 TLS를 활성화합니다.

---

## **6. 인덱스 설정**

### **인덱스 생성 기본값**
```yaml
index.number_of_shards: 1
index.number_of_replicas: 1
```
- `index.number_of_shards`: 기본 샤드 수.
- `index.number_of_replicas`: 기본 복제본 수.

---

## **7. 모니터링 및 로그**

### **모니터링 활성화**
```yaml
xpack.monitoring.enabled: true
xpack.monitoring.collection.enabled: true
```
- Elasticsearch 클러스터 상태를 모니터링하기 위해 활성화합니다.
- Kibana와 함께 사용하면 클러스터 상태를 시각적으로 확인할 수 있습니다.

---

### **슬로우 로그**
슬로우 로그는 느린 쿼리나 색인 작업을 기록합니다.
```yaml
index.search.slowlog.threshold.query.warn: 10s
index.search.slowlog.threshold.fetch.warn: 1s
index.indexing.slowlog.threshold.index.warn: 1s
```
- 느린 작업을 기록할 임계값을 설정합니다.

---

## **8. 기타 설정**

### **가비지 컬렉터 설정**
```yaml
jvm.options:
  -XX:+UseG1GC
```
- G1GC(Garbage First Garbage Collector)는 Elasticsearch에서 권장되는 가비지 컬렉터입니다.

---

### **Thread Pool 설정**
```yaml
thread_pool.write.size: 16
thread_pool.search.size: 16
```
- 쓰레드 풀 크기를 조정하여 성능을 최적화할 수 있습니다.

---

## **요약**
Elasticsearch 8에서 중요한 설정들은 다음과 같습니다:

1. **클러스터 및 노드 설정**: `cluster.name`, `node.name`, `discovery.seed_hosts`, `discovery.type`.
2. **네트워크 설정**: `network.host`, `http.port`, HTTPS 및 TLS 설정.
3. **데이터 경로**: `path.data`, `path.logs`.
4. **JVM 메모리**: 힙 메모리 크기(`-Xms`, `-Xmx`).
5. **보안**: X-Pack 보안 활성화 및 TLS 설정.
6. **인덱스 설정**: 샤드 및 복제본 수.
7. **모니터링 및 로그**: 슬로우 로그 및 클러스터 모니터링.

## 풀세팅 EX
Elasticsearch 8.x 버전에 적합한 `elasticsearch.yml` 파일의 예제입니다. 
**단일 노드 모드**와 **보안 활성화**를 포함, Docker 환경에서 사용하기에 적합합니다. 필요에 따라 수정하여 사용하세요.

````artifact
id: elasticsearch-yml-config
name: Elasticsearch YML Config
type: code.yaml
content: |-
  # ---------------------------------- Cluster -----------------------------------
  cluster.name: "my-cluster" # 클러스터 이름
  node.name: "node-1"        # 노드 이름
  
  # ---------------------------------- Node --------------------------------------
  node.roles: ["master", "data", "ingest"] # 노드 역할
  
  # --------------------------------- Network ------------------------------------
  network.host: 0.0.0.0   # 모든 네트워크 인터페이스에서 요청을 수신
  http.port: 9200         # HTTP 포트 (기본값: 9200)
  
  # ------------------------------- Discovery ------------------------------------
  discovery.type: single-node # 단일 노드 모드 (개발/테스트 환경에 적합)
  
  # --------------------------------- Paths --------------------------------------
  path.data: /var/lib/elasticsearch  # 데이터 저장 경로
  path.logs: /var/log/elasticsearch  # 로그 저장 경로
  
  # ---------------------------------- Memory ------------------------------------
  # JVM 힙 메모리 설정 (Docker 환경에서는 jvm.options 파일에서 설정 가능)
  # Xms와 Xmx를 동일하게 설정하는 것이 권장됨
  # jvm.options:
  #   -Xms2g
  #   -Xmx2g
  
  # --------------------------------- Security -----------------------------------
  xpack.security.enabled: true # X-Pack 보안 활성화
  xpack.security.http.ssl.enabled: true # HTTPS 활성화
  xpack.security.http.ssl.key: certs/http.key
  xpack.security.http.ssl.certificate: certs/http.crt
  xpack.security.http.ssl.certificate_authorities: certs/ca.crt
  
  # 클러스터 간 통신에서 TLS 활성화
  xpack.security.transport.ssl.enabled: true
  xpack.security.transport.ssl.key: certs/transport.key
  xpack.security.transport.ssl.certificate: certs/transport.crt
  xpack.security.transport.ssl.certificate_authorities: certs/ca.crt
  
  # -------------------------------- Index Settings ------------------------------
  index.number_of_shards: 1     # 기본 샤드 수
  index.number_of_replicas: 1   # 기본 복제본 수
  
  # ------------------------------- Monitoring -----------------------------------
  xpack.monitoring.enabled: true # 클러스터 모니터링 활성화
  xpack.monitoring.collection.enabled: true
  
  # ------------------------------- Slow Logs ------------------------------------
  index.search.slowlog.threshold.query.warn: 10s
  index.search.slowlog.threshold.fetch.warn: 1s
  index.indexing.slowlog.threshold.index.warn: 1s
````

---

### **설명**
1. **클러스터 및 노드 설정**
    - `cluster.name`: 클러스터 이름을 지정합니다.
    - `node.name`: 노드의 고유 이름을 설정합니다.
    - `node.roles`: 노드가 수행할 역할을 지정합니다.

2. **네트워크 설정**
    - `network.host`: 모든 네트워크 인터페이스에서 요청을 수신합니다(`0.0.0.0`).
    - `http.port`: HTTP API 요청을 수신할 포트를 설정합니다(기본값은 `9200`).

3. **보안 설정**
    - X-Pack 보안이 활성화되어 있으며, HTTPS와 TLS 설정이 포함되어 있습니다.
    - 인증서 경로(`certs/http.key`, `certs/http.crt`, `certs/ca.crt`)는 환경에 맞게 수정해야 합니다.

4. **데이터 및 로그 경로**
    - `path.data`: 데이터 저장 경로.
    - `path.logs`: 로그 저장 경로.
    - Docker에서는 볼륨 마운트를 통해 외부 경로를 연결하는 것이 일반적입니다.

5. **인덱스 설정**
    - 기본 샤드 수와 복제본 수를 설정합니다.

6. **모니터링**
    - X-Pack 모니터링을 활성화하여 클러스터 상태를 추적할 수 있습니다.

7. **슬로우 로그**
    - 느린 쿼리나 색인 작업을 기록하는 슬로우 로그 설정이 포함되어 있습니다.

---

### **사용 방법**
1. 위 파일을 `elasticsearch.yml`로 저장합니다.
2. Docker로 실행할 경우, `docker-compose.yml`에서 `elasticsearch.yml`을 마운트합니다:

```yaml
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.9.0
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
    volumes:
      - ./elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml
      - ./certs:/usr/share/elasticsearch/config/certs
    ports:
      - "9200:9200"
      - "9300:9300"
```

3. Elasticsearch를 실행하고, 인증 및 HTTPS 설정이 제대로 작동하는지 확인합니다.

---

### 추가 참고
- 인증서 경로(`certs/`)는 직접 생성하거나 Elasticsearch에서 제공하는 도구(`elasticsearch-certutil`)를 사용해 생성해야 합니다.
- 위 설정은 단일 노드 환경에 적합하며, 클러스터 구성을 원할 경우 `discovery.seed_hosts` 및 `cluster.initial_master_nodes` 설정을 추가해야 합니다.