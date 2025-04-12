### **팩토리 패턴 (Factory Pattern)**

팩토리 패턴은 **객체 생성 로직을 캡슐화**하여, 클라이언트 코드가 객체 생성 방식을 알 필요 없이 객체를 사용할 수 있도록 하는 디자인 패턴입니다.  
즉, 객체 생성의 책임을 팩토리 클래스에 위임하여, 클라이언트 코드가 객체 생성에 대해 독립적이 되도록 설계합니다.

---

## **1. 팩토리 패턴의 구조**

### **구조**

팩토리 패턴은 다음과 같은 구조를 가집니다:

1. **팩토리 클래스 (Factory Class)**
    - 객체 생성 로직을 캡슐화합니다.
    - 클라이언트는 팩토리 클래스를 호출하여 객체를 생성하며, 객체 생성 방식은 팩토리 내부에서 결정됩니다.

2. **클라이언트 (Client)**
    - 객체 생성 방식을 알 필요 없이 팩토리 클래스를 통해 객체를 생성하고 사용합니다.

3. **생성될 객체 (Product)**
    - 팩토리 클래스가 생성하는 객체로, 여러 종류의 객체가 동일한 인터페이스나 상속 구조를 가질 수 있습니다.

---

### **코드 예제: 메시지 발송 시스템**

아래는 팩토리 패턴을 활용하여 다양한 메시지 발송 로직을 캡슐화한 예제입니다.

#### **팩토리 클래스**

```ruby
class MessageFactory
  def self.create_message(type)
    case type
    when :email
      EmailMessage.new
    when :sms
      SmsMessage.new
    when :push
      PushMessage.new
    else
      raise "Unknown message type: #{type}"
    end
  end
end
```

#### **메시지 클래스 (Product)**

```ruby
# 공통 인터페이스
class Message
  def send_message
    raise NotImplementedError, "Subclasses must implement `send_message`"
  end
end

# 이메일 메시지
class EmailMessage < Message
  def send_message
    puts "Sending email message..."
  end
end

# SMS 메시지
class SmsMessage < Message
  def send_message
    puts "Sending SMS message..."
  end
end

# 푸시 알림 메시지
class PushMessage < Message
  def send_message
    puts "Sending push notification..."
  end
end
```

#### **클라이언트 코드**

```ruby
# 클라이언트는 팩토리를 통해 객체를 생성
message = MessageFactory.create_message(:email)
message.send_message
# 출력: Sending email message...

message = MessageFactory.create_message(:sms)
message.send_message
# 출력: Sending SMS message...

message = MessageFactory.create_message(:push)
message.send_message
# 출력: Sending push notification...
```

---

## **2. 팩토리 패턴의 장단점**

### **장점**

1. **객체 생성 로직의 캡슐화**
    - 객체 생성 로직이 팩토리 클래스 내부에 캡슐화되므로, 클라이언트는 객체 생성 방식에 대해 몰라도 됩니다.
    - 클라이언트 코드가 간결해지고 유지보수성이 향상됩니다.

2. **유지보수성 향상**
    - 새로운 객체 유형을 추가할 때, 팩토리 클래스에만 변경을 가하면 됩니다.
    - 클라이언트 코드를 수정하지 않고도 확장이 가능합니다.

3. **의존성 제거**
    - 클라이언트는 특정 클래스에 의존하지 않고, 팩토리 인터페이스를 통해 객체를 생성하므로, 코드의 결합도가 낮아집니다.

4. **코드 재사용성 증가**
    - 동일한 객체 생성 로직을 여러 곳에서 재사용할 수 있습니다.

5. **테스트 용이성**
    - 팩토리를 통해 객체를 생성하면, 테스트 시 다른 구현체로 쉽게 대체할 수 있습니다.

---

### **단점**

1. **복잡성 증가**
    - 단순한 객체 생성에도 팩토리 클래스를 작성해야 하므로, 코드가 불필요하게 복잡해질 수 있습니다.

2. **런타임 오류 가능성**
    - 팩토리에서 잘못된 객체를 반환하거나, 클라이언트가 잘못된 타입을 요청하면 런타임에 오류가 발생할 수 있습니다.

3. **추적 어려움**
    - 객체 생성 로직이 팩토리 내부에 숨겨져 있어, 디버깅 시 객체 생성 과정을 추적하기 어려울 수 있습니다.

4. **오버엔지니어링 위험**
    - 간단한 객체 생성에도 팩토리 패턴을 남용하면, 불필요한 추상화와 복잡성이 추가될 수 있습니다.

---

## **3. 팩토리 패턴을 적용하면 좋은 경우**

팩토리 패턴은 **객체 생성 로직이 복잡하거나, 클라이언트 코드가 객체 생성 방식에 독립적이어야 할 때** 적합합니다.

### **적용 사례**

1. **객체 생성 로직이 복잡할 때**
    - 객체 생성 시 여러 설정이나 초기화 작업이 필요할 경우, 팩토리에서 이를 처리하도록 위임할 수 있습니다.

2. **클라이언트 코드가 특정 클래스에 의존하지 않아야 할 때**
    - 클라이언트가 객체 생성 방식을 몰라도 동작해야 하는 경우, 팩토리를 통해 객체를 생성하도록 설계할 수 있습니다.

3. **유사한 객체를 여러 타입으로 생성해야 할 때**
    - 동일한 인터페이스를 구현하는 여러 객체를 생성해야 하는 경우, 팩토리 패턴을 사용하면 객체 생성 로직을 일원화할 수 있습니다.

4. **테스트 가능성을 높이고 싶을 때**
    - 팩토리를 사용하면 테스트 환경에서 실제 객체 대신 Mock 객체를 생성하여 테스트할 수 있습니다.

5. **의존성 주입(Dependency Injection)이 필요한 경우**
    - 팩토리를 통해 객체 생성 시 필요한 의존성을 주입할 수 있습니다.

---

## **4. 팩토리 패턴의 확장 예제**

#### **추상 팩토리 패턴 (Abstract Factory Pattern)**

팩토리 패턴의 확장으로, 여러 관련 객체를 그룹화하여 생성할 수 있는 추상 팩토리를 설계할 수 있습니다.

```ruby
# 추상 팩토리
class NotificationFactory
  def create_message
    raise NotImplementedError, "Subclasses must implement `create_message`"
  end

  def create_sender
    raise NotImplementedError, "Subclasses must implement `create_sender`"
  end
end

# 이메일 팩토리
class EmailNotificationFactory < NotificationFactory
  def create_message
    EmailMessage.new
  end

  def create_sender
    EmailSender.new
  end
end

# SMS 팩토리
class SmsNotificationFactory < NotificationFactory
  def create_message
    SmsMessage.new
  end

  def create_sender
    SmsSender.new
  end
end
```

#### **클라이언트 코드**

```ruby
factory = EmailNotificationFactory.new
message = factory.create_message
sender = factory.create_sender

message.send_message
sender.send
```

---

## **5. 정리**

### **팩토리 패턴의 핵심**

- 객체 생성 로직을 캡슐화하여, 클라이언트 코드가 객체 생성 방식에 독립적이 되도록 설계합니다.
- 객체 생성과 관련된 변경 사항이 클라이언트 코드에 영향을 미치지 않도록 합니다.

### **장단점 요약**

| **장점**          | **단점**          |
|-----------------|-----------------|
| 객체 생성 로직 캡슐화    | 복잡성 증가          |
| 유지보수성과 확장성 향상   | 런타임 오류 가능성      |
| 의존성 제거 및 결합도 감소 | 객체 생성 과정 추적 어려움 |
| 테스트 용이성 증가      | 오버엔지니어링 위험      |

### **적용하면 좋은 경우**

- 객체 생성 로직이 복잡하거나, 클라이언트 코드가 객체 생성 방식에 의존하지 않도록 설계해야 할 때.
- 객체 생성과 관련된 변경 사항이 자주 발생하거나, 다양한 객체 유형을 생성해야 할 때.

팩토리 패턴은 특히 **유지보수성과 확장성**이 중요한 프로젝트에서 매우 유용하게 사용됩니다. 다만, 남용하지 않도록 주의해야 합니다.