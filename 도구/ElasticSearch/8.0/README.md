## ES8 세팅 

nano /usr/share/elasticsearch/config/elasticsearch.yml

```bash

docker build --no-cache -t esfastapi-elasticsearch .

sudo wget http://media.sundog-soft.com/es8/shakes-mapping.json

docker stop elasticsearch
docker rm elasticsearch

docker stop kibana
docker rm kibana

# 기존 Elasticsearch 이미지를 삭제
docker rmi esfastapi-elasticsearch:latest


docker ps -a | grep 79ad6c6813d2
docker run -it --user root esfastapi-elasticsearch /bin/bash

```

---

# Elasticsearch 상태 확인

## **요청**
```bash
curl -XGET 127.0.0.1:9208
```

## **응답**
```json
{
  "name": "es-node",
  "cluster_name": "docker-cluster",
  "cluster_uuid": "Y8DK-vMLSh-g41BFUIgDHg",
  "version": {
    "number": "8.9.0",
    "build_flavor": "default",
    "build_type": "docker",
    "build_hash": "8aa461beb06aa0417a231c345a1b8c38fb498a0d",
    "build_date": "2023-07-19T14:43:58.555259655Z",
    "build_snapshot": false,
    "lucene_version": "9.7.0",
    "minimum_wire_compatibility_version": "7.17.0",
    "minimum_index_compatibility_version": "7.0.0"
  },
  "tagline": "You Know, for Search"
}
```

---

## **주요 정보**

### **노드 정보**
- **노드 이름**: `es-node`
- **클러스터 이름**: `docker-cluster`
- **클러스터 UUID**: `Y8DK-vMLSh-g41BFUIgDHg`

### **Elasticsearch 버전**
- **버전 번호**: `8.9.0`
- **빌드 플래버**: `default`
- **빌드 타입**: `docker`
- **빌드 해시**: `8aa461beb06aa0417a231c345a1b8c38fb498a0d`
- **빌드 날짜**: `2023-07-19T14:43:58.555259655Z`
- **Lucene 버전**: `9.7.0`

### **호환성**
- **최소 Wire 호환 버전**: `7.17.0`
- **최소 Index 호환 버전**: `7.0.0`

---

## **Elasticsearch 슬로건**
> **"You Know, for Search"**