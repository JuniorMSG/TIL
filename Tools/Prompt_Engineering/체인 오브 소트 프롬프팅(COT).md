# 체인 오브 소트(Chain of Thought) 프롬프팅 개념 정리

## 체인 오브 소트란?
체인 오브 소트(Chain of Thought, CoT) 프롬프팅은 AI가 복잡한 문제를 해결할 때 단계적인 사고 과정을 거치도록 유도하는 프롬프트 기법입니다. 이 방식은 AI에게 "생각의 흐름"을 명시적으로 보여주도록 요청함으로써, 특히 논리적 추론이나 다단계 문제 해결에서 정확도를 크게 향상시킵니다.

## 주요 특징 및 장점

### 1. 단계적 사고 유도
- AI가 최종 답변만 제시하는 것이 아니라, 그 결론에 도달하기까지의 중간 과정을 모두 보여줍니다
- 복잡한 문제를 작은 단계로 분해하여 해결하는 방식을 학습합니다

### 2. 정확도 향상
- 구글 리서치 팀의 연구에 따르면, 복잡한 추론 문제에서 CoT를 적용했을 때 정확도가 최대 40% 향상되었습니다
- 특히 수학 문제, 논리 퍼즐, 다단계 의사결정 문제에서 효과적입니다

### 3. 오류 감지 용이성
- 사고 과정이 명시적으로 드러나기 때문에 오류가 발생한 지점을 쉽게 식별할 수 있습니다
- 사용자가 AI의 추론 과정을 검토하고 필요시 수정 지시를 내릴 수 있습니다

## 체인 오브 소트 적용 방법

### 기본 형태
```
"다음 문제를 단계별로 풀어보세요. 각 단계에서의 생각 과정을 모두 설명해주세요."
```

### 제로샷 CoT
AI에게 별도의 예시 없이 단계적 사고를 요청합니다:
```
"다음 문제를 해결하기 위한 단계별 접근 방식을 보여주세요. 천천히 생각해보세요."
```

### 퓨샷 CoT
몇 가지 예시와 함께 단계적 사고 과정을 보여줍니다:
```
"문제: 사과 3개의 가격이 10달러입니다. 사과 9개의 가격은 얼마인가요?
사고 과정: 사과 3개가 10달러이므로, 사과 1개는 10÷3 = 약 3.33달러입니다. 따라서 사과 9개는 3.33×9 = 30달러입니다.

이제 다음 문제를 같은 방식으로 풀어보세요: [새로운 문제]"
```

## 실제 적용 사례

### 수학 문제
```
문제: 철수는 120페이지 책을 읽고 있습니다. 첫날에 전체의 1/4을 읽었고, 둘째 날에는 남은 페이지의 1/3을 읽었습니다. 철수가 지금까지 읽은 총 페이지 수는?

체인 오브 소트 접근법:
1) 책은 총 120페이지입니다.
2) 첫날에 전체의 1/4을 읽었으므로, 120 × 1/4 = 30페이지를 읽었습니다.
3) 첫날 후 남은 페이지는 120 - 30 = 90페이지입니다.
4) 둘째 날에는 남은 페이지의 1/3을 읽었으므로, 90 × 1/3 = 30페이지를 더 읽었습니다.
5) 따라서 철수가 지금까지 읽은 총 페이지 수는 30 + 30 = 60페이지입니다.
```

### 논리 추론 문제
```
문제: 다섯 명의 친구 A, B, C, D, E가 있습니다. A는 B보다 키가 큽니다. C는 D보다 키가 작습니다. E는 A보다 키가 큽니다. C는 B보다 키가 큽니다. 키가 가장 큰 사람은 누구인가요?

체인 오브 소트 접근법:
1) 주어진 정보를 정리해보겠습니다:
   - A > B (A는 B보다 키가 큼)
   - C < D (C는 D보다 키가 작음)
   - E > A (E는 A보다 키가 큼)
   - C > B (C는 B보다 키가 큼)
2) A > B와 C > B를 통해 B가 가장 작지는 않을 수 있습니다.
3) C < D이므로 D는 C보다 큽니다.
4) E > A이고 A > B이므로, E > A > B입니다.
5) 또한 C > B이지만 C < D이므로, D > C > B입니다.
6) 따라서 E와 D 중 하나가 가장 클 것입니다.
7) 하지만 E와 D의 직접적인 비교 정보가 없습니다.
8) 추가 정보가 필요하지만, 주어진 정보만으로는 E가 가장 클 가능성이 높습니다(E > A > B, 그리고 D > C > B).
```

## 체인 오브 소트의 한계
- 매우 복잡한 문제에서는 중간 단계에서 오류가 발생할 수 있습니다
- 단계가 많아질수록 이전 단계의 오류가 누적될 위험이 있습니다
- 토큰 사용량이 증가하여 비용이 더 많이 발생할 수 있습니다

## 효과적인 CoT 프롬프트 작성 팁
1. "천천히 생각해보세요"와 같은 문구를 추가하면 정확도가 향상됩니다
2. 문제를 작은 하위 문제로 분해하도록 명시적으로 요청합니다
3. 중간 계산 결과를 확인하도록 요청합니다
4. 최종 답변 전에 자체 검증을 수행하도록 유도합니다

=
## 기억해두면 좋은 영어 표현
- "Break down the problem into steps" (문제를 단계별로 분해하다)
- "Walk through your reasoning process" (추론 과정을 단계별로 설명하다)
- "Think step by step" (단계적으로 생각하다)
- "Show your work" (풀이 과정을 보여주다)

## 한글 질문의 영어 표현
한글: "체인 오브 소트 프롬프팅은 어떤 상황에서 가장 효과적인가요?"
영어: "In what situations is Chain of Thought prompting most effective?"

한글: "복잡한 수학 문제를 단계별로 풀어주세요."
영어: "Please solve this complex math problem step by step, showing your reasoning."