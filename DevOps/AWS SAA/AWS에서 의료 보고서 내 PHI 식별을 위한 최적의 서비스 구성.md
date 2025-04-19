# AWS에서 의료 보고서 내 PHI 식별을 위한 최적의 서비스 구성

## 핵심 요약

**상황**: 병원이 Amazon API Gateway와 AWS Lambda를 사용하여 RESTful API를 배포했으며, PDF 및 JPEG 형식의 보고서를 업로드하고
있습니다.  
**목표**: Lambda 코드를 수정하여 보고서에서 보호 대상 건강 정보(PHI)를 식별해야 합니다.  
**요구사항**: 운영 오버헤드가 최소화되는 솔루션이 필요합니다.

## 선택지/해설

| 옵션 | 접근 방식                                                           | 장점                         | 단점                               |
|----|-----------------------------------------------------------------|----------------------------|----------------------------------|
| A  | Python 라이브러리로 텍스트 추출 및 PHI 식별                                   | 맞춤형 솔루션 가능                 | 운영 오버헤드 높음, 유지보수 책임              |
| B  | Amazon Textract로 텍스트 추출 + Amazon SageMaker로 PHI 식별              | 정확한 텍스트 추출, 맞춤형 모델 가능      | SageMaker 모델 개발/유지에 오버헤드 필요      |
| C  | Amazon Textract로 텍스트 추출 + Amazon Comprehend Medical로 PHI 식별     | 완전 관리형 서비스, 의료 특화, 최소 오버헤드 | 매우 특수한 PHI 유형에는 한계 가능성           |
| D  | Amazon Rekognition으로 텍스트 추출 + Amazon Comprehend Medical로 PHI 식별 | 간단한 통합                     | Rekognition은 문서 텍스트 추출에 최적화되지 않음 |

**해설**:

- **옵션 A**: 직접 Python 라이브러리를 사용하면 모든 구현과 유지보수를 자체적으로 해야 하므로 운영 오버헤드가 가장 큽니다.
- **옵션 B**: Textract는 문서에서 텍스트를 추출하는 데 효과적이지만, SageMaker를 사용하려면 PHI 식별을 위한 모델을 직접 개발, 훈련, 배포해야 합니다.
- **옵션 C**: Textract는 PDF와 이미지에서 텍스트를 효과적으로 추출하고, Comprehend Medical은 의료 텍스트에서 PHI를 자동으로 식별하도록 특별히
  설계된 관리형 서비스입니다.
- **옵션 D**: Rekognition은 이미지 인식에 특화되어 있으며, 복잡한 문서에서 텍스트 추출 기능은 Textract보다 제한적입니다.

## 결론

**옵션 C**(Amazon Textract + Amazon Comprehend Medical)가 운영 오버헤드를 최소화하면서 요구사항을 충족하는 최적의 솔루션입니다. 두 서비스
모두 완전 관리형으로, 별도의 모델 개발이나 유지보수 없이 바로 사용할 수 있으며, 특히 Comprehend Medical은 의료 데이터에서 PHI 식별에 특화되어 있습니다.

## 영어 표현

- **Protected Health Information (PHI)**: 보호 대상 건강 정보
- **Operational overhead**: 운영 오버헤드
- **Fully managed service**: 완전 관리형 서비스
- **Text extraction**: 텍스트 추출
- **Document processing**: 문서 처리

**영어 질문 예시**:
"Which AWS services should I use to identify PHI in medical reports in PDF and JPEG formats with
minimal operational overhead?"

## 추가 팁

- **면접 준비**: AWS 의료 분야 규정 준수(HIPAA)에 대한 이해를 보여주는 것이 중요합니다.
- **실무 적용**: Textract와 Comprehend Medical을 통합할 때 Step Functions를 사용하여 워크플로우를 구성하면 더욱 견고한 파이프라인을 구축할
  수 있습니다.
- **비용 관리**: Comprehend Medical은 처리된 문자 수에 따라 비용이 부과되므로, 대량의 문서를 처리할 경우 비용 모니터링이 필요합니다.
- **보안 강화**: PHI를 다룰 때는 데이터 전송과 저장 시 암호화를 적용하고, IAM 역할을 통한 최소 권한 원칙을 적용하는 것이 좋습니다.