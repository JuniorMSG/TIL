## 문제 요약

- **요구사항**
    - 고가용성 3계층(웹, 앱, DB) 아키텍처
    - HTTPS 콘텐츠를 **최대한 에지에 가깝게** 전달(지연 최소화)
    - **가장 안전한** 솔루션

---

## 정답 및 해설

### **정답: C**
> **프라이빗 서브넷의 여러 중복 Amazon EC2 인스턴스로 퍼블릭 Application Load Balancer(ALB)를 구성합니다. 퍼블릭 ALB를 원본으로 사용하여 HTTPS 콘텐츠를 제공하도록 Amazon CloudFront를 구성합니다.**

#### **이유**
- **EC2 인스턴스는 프라이빗 서브넷**에 두어 외부 공격 노출을 최소화합니다.
- **퍼블릭 ALB**만 인터넷에 노출하고, CloudFront가 ALB를 오리진으로 사용해 HTTPS 트래픽을 처리합니다.
- **CloudFront**는 글로벌 에지 로케이션에서 HTTPS 콘텐츠를 캐싱/전달하여 지연을 최소화합니다.
- **가장 안전함:**
    - EC2 인스턴스는 외부에서 직접 접근할 수 없고,
    - ALB만 퍼블릭이며, CloudFront와 연동하여 WAF 등 추가 보안도 적용 가능

---

### **오답 해설**

- **A, D**: EC2 인스턴스가 퍼블릭 서브넷에 있어 외부 공격에 노출되어 안전하지 않음.
- **B**: EC2 인스턴스를 원본(오리진)으로 CloudFront에 연결하면, ALB의 보안 이점(SSL 종료, WAF, 보안 그룹 등)을 활용하지 못함.

---

## 기억해두면 좋은 영어 표현

- **"Place EC2 instances in private subnets behind a public Application Load Balancer, and use CloudFront to deliver HTTPS content as close to the edge as possible."**  
  (EC2 인스턴스를 프라이빗 서브넷에 배치하고, 퍼블릭 ALB 뒤에 두며, CloudFront로 HTTPS 콘텐츠를 최대한 에지에서 제공하세요.)

---

## 영어로 질문하기

**한글 질문:**  
고가용성 3계층 애플리케이션에서, 가장 안전하고 에지에 가까운 HTTPS 콘텐츠 전달을 위해 어떤 AWS 아키텍처를 사용해야 하나요?

**영어 표현:**  
What is the most secure AWS architecture for delivering HTTPS content as close to the edge as possible in a highly available three-tier application?

