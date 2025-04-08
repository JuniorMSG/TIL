### **템플릿 메서드 패턴 (Template Method Pattern)**

템플릿 메서드 패턴은 **상위 클래스에서 알고리즘의 골격을 정의**하고, **세부 구현은 하위 클래스에서 제공**하는 디자인 패턴입니다.  
즉, 알고리즘의 공통적인 부분은 상위 클래스에서 처리하고, 변해야 하는 부분만 하위 클래스에서 구현하도록 강제합니다.

---

## **1. 템플릿 메서드 패턴의 구조**

### **구조**

템플릿 메서드 패턴은 다음과 같은 구조를 가집니다:

1. **상위 클래스 (Abstract Class)**
    - 알고리즘의 전체 흐름을 정의합니다.
    - 일부 메서드는 구현되어 있고, 일부는 추상 메서드로 정의되어 하위 클래스에서 구현하도록 강제합니다.

2. **하위 클래스 (Concrete Class)**
    - 상위 클래스에서 정의된 추상 메서드를 구현하여, 알고리즘의 특정 부분을 정의합니다.

---

### **코드 예제: 데이터 처리 파이프라인**

아래는 템플릿 메서드 패턴을 활용하여 데이터를 처리하는 파이프라인을 설계한 예제입니다.

#### **상위 클래스 (Abstract Class)**

```ruby
# 템플릿 메서드 패턴의 상위 클래스
class DataProcessor
  # 템플릿 메서드: 알고리즘의 골격을 정의
  def process
    load_data
    transform_data
    save_data
  end

  # 공통적으로 사용되는 메서드 구현
  def load_data
    puts "Loading data..."
  end

  # 하위 클래스에서 구현해야 하는 추상 메서드
  def transform_data
    raise NotImplementedError, "Subclasses must implement `transform_data`"
  end

  # 공통적으로 사용되는 메서드 구현
  def save_data
    puts "Saving data..."
  end
end
```

#### **하위 클래스 (Concrete Class)**

```ruby
# JSON 데이터를 처리하는 클래스
class JsonProcessor < DataProcessor
  def transform_data
    puts "Transforming JSON data..."
  end
end

# CSV 데이터를 처리하는 클래스
class CsvProcessor < DataProcessor
  def transform_data
    puts "Transforming CSV data..."
  end
end
```

#### **클라이언트 코드**

```ruby
# JSON 데이터 처리
json_processor = JsonProcessor.new
json_processor.process
# 출력:
# Loading data...
# Transforming JSON data...
# Saving data...

# CSV 데이터 처리
csv_processor = CsvProcessor.new
csv_processor.process
# 출력:
# Loading data...
# Transforming CSV data...
# Saving data...
```

---

## **2. 템플릿 메서드 패턴의 장단점**

### **장점**

1. **코드 재사용성 증가**
    - 알고리즘의 공통 부분은 상위 클래스에서 정의하고, 변해야 하는 부분만 하위 클래스에서 구현하기 때문에 중복 코드를 줄일 수 있습니다.

2. **일관성 유지**
    - 알고리즘의 구조가 상위 클래스에서 정의되므로, 하위 클래스에서 구현된 메서드가 동일한 흐름으로 실행됩니다.

3. **유연성 제공**
    - 하위 클래스에서 특정 메서드만 재정의하면 되므로, 전체 알고리즘을 수정하지 않고도 동작을 변경할 수 있습니다.

4. **확장성**
    - 새로운 하위 클래스를 추가하여 다른 동작을 구현할 수 있습니다. 기존 상위 클래스의 코드를 수정할 필요가 없습니다.

5. **의존성 역전 원칙(DIP) 준수**
    - 상위 클래스는 세부 사항(하위 클래스)에 의존하지 않고, 하위 클래스가 상위 클래스의 정의에 따라 행동합니다.

---

### **단점**

1. **추상 클래스 의존**
    - 상위 클래스에서 정의된 추상 메서드를 반드시 구현해야 하므로, 하위 클래스의 구현 부담이 증가할 수 있습니다.

2. **복잡성 증가**
    - 알고리즘의 골격과 세부 구현이 분리되면서 코드 구조가 복잡해질 수 있습니다.
    - 특히, 상위 클래스와 하위 클래스 간의 관계가 많아질 경우 관리가 어려워질 수 있습니다.

3. **디버깅 어려움**
    - 상위 클래스에서 정의된 로직과 하위 클래스의 구현이 결합되어 있어, 디버깅 시 흐름을 추적하기 어려울 수 있습니다.

4. **과도한 사용 위험**
    - 모든 경우에 템플릿 메서드 패턴을 적용하면 불필요한 추상화와 상속 구조가 생길 수 있습니다.

---

## **3. 템플릿 메서드 패턴을 적용하면 좋은 경우**

템플릿 메서드 패턴은 **알고리즘의 구조는 동일하지만, 일부 단계의 구현이 달라져야 할 때** 적합합니다.

### **적용 사례**

1. **데이터 처리 파이프라인**
    - 데이터를 로드, 변환, 저장하는 과정이 동일하지만, 데이터의 형식(JSON, CSV 등)에 따라 변환 로직이 달라질 때.

2. **보고서 생성**
    - 보고서를 생성하는 과정(데이터 수집, 분석, 출력)이 동일하지만, 출력 형식(PDF, HTML 등)이 달라질 때.

3. **UI 컴포넌트 렌더링**
    - UI 컴포넌트의 렌더링 과정이 동일하지만, 특정 컴포넌트의 스타일이나 동작이 다를 때.

4. **게임 개발**
    - 게임에서 캐릭터의 행동 알고리즘(이동, 공격, 방어)이 동일한 흐름을 따르지만, 캐릭터 유형(마법사, 전사 등)에 따라 동작이 달라질 때.

5. **프레임워크 설계**
    - 프레임워크에서 공통적인 작업 흐름(예: 요청 처리, 인증, 응답 생성)을 정의하고, 특정 동작은 사용자(개발자)가 구현하도록 할 때.

---

## **4. 템플릿 메서드 패턴의 확장 예제**

#### **상위 클래스에 Hook 메서드 추가**

템플릿 메서드 패턴은 **Hook 메서드**를 활용하여, 하위 클래스가 선택적으로 동작을 변경할 수 있도록 할 수 있습니다.

```ruby
class DataProcessor
  def process
    load_data
    transform_data
    save_data
    after_process_hook # Hook 메서드 호출
  end

  def load_data
    puts "Loading data..."
  end

  def transform_data
    raise NotImplementedError, "Subclasses must implement `transform_data`"
  end

  def save_data
    puts "Saving data..."
  end

  # Hook 메서드: 기본 구현은 비어 있지만, 하위 클래스에서 재정의 가능
  def after_process_hook
  end
end

# 하위 클래스에서 Hook 메서드 재정의
class JsonProcessor < DataProcessor
  def transform_data
    puts "Transforming JSON data..."
  end

  def after_process_hook
    puts "JSON processing complete!"
  end
end

json_processor = JsonProcessor.new
json_processor.process
# 출력:
# Loading data...
# Transforming JSON data...
# Saving data...
# JSON processing complete!
```

---

## **5. 정리**

### **템플릿 메서드 패턴의 핵심**

- 상위 클래스에서 알고리즘의 공통 흐름을 정의하고, 변해야 하는 부분만 하위 클래스에서 구현하도록 강제합니다.
- 공통 로직과 세부 구현을 분리하여 코드의 일관성과 재사용성을 높입니다.

### **장단점 요약**

| **장점**           | **단점**               |
|------------------|----------------------|
| 공통 로직 재사용 가능     | 추상 클래스 의존으로 구현 부담 증가 |
| 알고리즘 구조의 일관성 유지  | 상속 구조로 인해 복잡성 증가     |
| 유연하게 세부 동작 변경 가능 | 디버깅 시 흐름 추적 어려움      |
| 새로운 하위 클래스 추가 용이 | 과도한 사용 시 불필요한 추상화 위험 |

### **적용하면 좋은 경우**

- 알고리즘의 구조는 동일하지만, 일부 단계의 구현이 달라져야 할 때.
- 데이터 처리, 보고서 생성, UI 렌더링, 게임 캐릭터 동작 등에서 활용 가능.

템플릿 메서드 패턴은 **유지보수성과 확장성**을 높이는 데 매우 유용하지만, 모든 경우에 적용하기보다는 **공통 흐름과 변동성이 명확히 구분될 때** 사용하는 것이 좋습니다.