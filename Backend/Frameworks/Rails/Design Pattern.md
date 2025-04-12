<!-- TOC -->
* [Ruby on Rails에서의 디자인 패턴 예시와 장단점](#ruby-on-rails에서의-디자인-패턴-예시와-장단점)
  * [1. Singleton 패턴](#1-singleton-패턴)
    * [설명](#설명)
    * [예시: 설정 관리](#예시-설정-관리)
    * [장점](#장점)
    * [단점](#단점)
  * [2. Observer 패턴](#2-observer-패턴)
    * [설명](#설명-1)
    * [예시: ActiveRecord 콜백](#예시-activerecord-콜백)
    * [장점](#장점-1)
    * [단점](#단점-1)
  * [3. Factory 패턴](#3-factory-패턴)
    * [설명](#설명-2)
    * [예시: 객체 생성](#예시-객체-생성)
    * [장점](#장점-2)
    * [단점](#단점-2)
  * [4. Decorator 패턴](#4-decorator-패턴)
    * [설명](#설명-3)
    * [예시: Draper Gem 사용](#예시-draper-gem-사용)
    * [장점](#장점-3)
    * [단점](#단점-3)
  * [5. 템플릿 메서드 패턴](#5-템플릿-메서드-패턴)
    * [설명](#설명-4)
    * [예시: 콜백 메서드](#예시-콜백-메서드)
    * [장점](#장점-4)
    * [단점](#단점-4)
  * [6. 전략 패턴](#6-전략-패턴)
    * [설명](#설명-5)
    * [예시: 결제 처리](#예시-결제-처리)
    * [장점](#장점-5)
    * [단점](#단점-5)
  * [7. 퍼사드 패턴 (Facade Pattern)](#7-퍼사드-패턴-facade-pattern)
    * [설명](#설명-6)
    * [예시: 서비스 객체](#예시-서비스-객체)
    * [장점](#장점-6)
    * [단점](#단점-6)
  * [8. 리포지토리 패턴 (Repository Pattern)](#8-리포지토리-패턴-repository-pattern)
    * [설명](#설명-7)
    * [예시: 데이터 접근](#예시-데이터-접근)
    * [장점](#장점-7)
    * [단점](#단점-7)
  * [9. 빌더 패턴 (Builder Pattern)](#9-빌더-패턴-builder-pattern)
    * [설명](#설명-8)
    * [예시: 폼 객체](#예시-폼-객체)
    * [장점](#장점-8)
    * [단점](#단점-8)
* [디자인 패턴의 장단점](#디자인-패턴의-장단점)
  * [장점](#장점-9)
  * [단점](#단점-9)
<!-- TOC -->

# Ruby on Rails에서의 디자인 패턴 예시와 장단점

## 1. Singleton 패턴

### 설명
싱글톤 패턴은 클래스의 인스턴스를 하나만 생성하여 전역적으로 접근할 수 있도록 하는 패턴입니다.

### 예시: 설정 관리
```ruby
class AppConfig
  include Singleton

  def initialize
    @settings = load_settings
  end

  def get_setting(key)
    @settings[key]
  end

  private

  def load_settings
    { app_name: "MyApp", version: "1.0" }
  end
end

config = AppConfig.instance
puts config.get_setting(:app_name)
```

### 장점
- 전역적으로 접근 가능한 인스턴스를 제공하여 상태 관리가 용이합니다.
- 리소스를 절약할 수 있습니다. (한 번만 생성)

### 단점
- 전역 상태를 가지기 때문에 테스트하기 어려울 수 있습니다.
- 의존성 주입을 방해할 수 있어 유연성이 떨어집니다.

## 2. Observer 패턴

### 설명
옵저버 패턴은 객체의 상태 변화에 따라 다른 객체에 변화를 통지하는 패턴입니다.

### 예시: ActiveRecord 콜백
```ruby
class User < ApplicationRecord
  after_create :send_welcome_email

  private

  def send_welcome_email
    UserMailer.welcome_email(self).deliver_now
  end
end
```

### 장점
- 객체 간의 느슨한 결합을 유지할 수 있습니다.
- 이벤트 기반 시스템을 쉽게 구현할 수 있습니다.

### 단점
- 복잡성이 증가할 수 있으며, 디버깅이 어려울 수 있습니다.
- 옵저버가 많아질 경우 성능에 영향을 줄 수 있습니다.

## 3. Factory 패턴

### 설명
팩토리 패턴은 객체 생성 로직을 캡슐화하여 클라이언트 코드가 구체적인 클래스에 의존하지 않도록 하는 패턴입니다.

### 예시: 객체 생성
```ruby
class NotificationFactory
  def self.create(type)
    case type
    when :email
      EmailNotification.new
    when :sms
      SmsNotification.new
    else
      raise "Unknown notification type"
    end
  end
end

notification = NotificationFactory.create(:email)
```

### 장점
- 객체 생성 로직을 중앙 집중화하여 관리할 수 있습니다.
- 코드의 유연성과 재사용성을 높일 수 있습니다.

### 단점
- 클래스의 수가 증가하여 코드가 복잡해질 수 있습니다.
- 단순한 객체 생성에는 오버헤드가 될 수 있습니다.

## 4. Decorator 패턴

### 설명
데코레이터 패턴은 객체에 기능을 동적으로 추가할 수 있도록 하는 패턴입니다.

### 예시: Draper Gem 사용
```ruby
class ProductDecorator < Draper::Decorator
  delegate_all

  def display_price
    h.number_to_currency(object.price)
  end
end

product = Product.first
decorated_product = ProductDecorator.decorate(product)
puts decorated_product.display_price
```

### 장점
- 객체의 기능을 유연하게 확장할 수 있습니다.
- 기존 코드 수정 없이 기능을 추가할 수 있습니다.

### 단점
- 데코레이터가 많아질 경우 관리가 어려울 수 있습니다.
- 코드의 복잡성이 증가할 수 있습니다.

## 5. 템플릿 메서드 패턴

### 설명
템플릿 메서드 패턴은 상위 클래스에서 알고리즘의 구조를 정의하고, 하위 클래스에서 세부 동작을 구현하는 방식입니다.

### 예시: 콜백 메서드
```ruby
class ApplicationRecord < ActiveRecord::Base
  self.abstract_class = true

  def save_with_logging
    log_before_save
    save
    log_after_save
  end

  private

  def log_before_save
    puts "Before saving #{self.class.name}"
  end

  def log_after_save
    puts "After saving #{self.class.name}"
  end
end
```

### 장점
- 알고리즘의 구조를 재사용할 수 있습니다.
- 코드 중복을 줄일 수 있습니다.

### 단점
- 상속 구조가 복잡해질 수 있습니다.
- 상위 클래스의 변경이 하위 클래스에 영향을 미칠 수 있습니다.

## 6. 전략 패턴

### 설명
전략 패턴은 행위를 캡슐화하여 런타임에 동적으로 교체할 수 있도록 하는 패턴입니다.

### 예시: 결제 처리
```ruby
class StripePayment
  def process(amount)
    puts "Processing payment of $#{amount} with Stripe"
  end
end

class PaypalPayment
  def process(amount)
    puts "Processing payment of $#{amount} with PayPal"
  end
end

class PaymentProcessor
  def initialize(strategy)
    @strategy = strategy
  end

  def process_payment(amount)
    @strategy.process(amount)
  end
end

processor = PaymentProcessor.new(StripePayment.new)
processor.process_payment(100)
```

### 장점
- 알고리즘을 독립적으로 변경할 수 있습니다.
- 코드의 유연성과 확장성을 높일 수 있습니다.

### 단점
- 전략 클래스가 많아질 경우 관리가 복잡해질 수 있습니다.
- 클라이언트가 적절한 전략을 선택해야 합니다.

## 7. 퍼사드 패턴 (Facade Pattern)

### 설명
퍼사드 패턴은 복잡한 시스템의 인터페이스를 단순화하여 사용자가 더 쉽게 접근할 수 있도록 하는 패턴입니다.

### 예시: 서비스 객체
```ruby
class OrderFacade
  def initialize(order)
    @order = order
  end

  def complete_order
    charge_payment
    send_confirmation_email
    update_inventory
  end

  private

  def charge_payment
    # 결제 처리 로직
  end

  def send_confirmation_email
    # 이메일 전송 로직
  end

  def update_inventory
    # 재고 업데이트 로직
  end
end

order = Order.find(1)
facade = OrderFacade.new(order)
facade.complete_order
```

### 장점
- 복잡한 시스템을 단순화하여 사용하기 쉽게 만듭니다.
- 코드의 가독성을 높일 수 있습니다.

### 단점
- 퍼사드에 너무 많은 책임이 집중될 수 있습니다.
- 시스템의 유연성을 제한할 수 있습니다.

## 8. 리포지토리 패턴 (Repository Pattern)

### 설명
리포지토리 패턴은 데이터베이스에 접근하는 로직을 캡슐화하여 비즈니스 로직과 분리하는 패턴입니다.

### 예시: 데이터 접근
```ruby
class UserRepository
  def find_by_email(email)
    User.find_by(email: email)
  end

  def all_active_users
    User.where(active: true)
  end
end

repo = UserRepository.new
active_users = repo.all_active_users
```

### 장점
- 데이터 접근 로직을 중앙 집중화하여 관리할 수 있습니다.
- 비즈니스 로직과 데이터 접근 로직을 분리할 수 있습니다.

### 단점
- 단순한 CRUD 작업에는 오버헤드가 될 수 있습니다.
- 리포지토리 클래스가 많아질 경우 관리가 복잡해질 수 있습니다.

## 9. 빌더 패턴 (Builder Pattern)

### 설명
빌더 패턴은 복잡한 객체의 생성 과정을 단계적으로 구성할 수 있도록 하는 패턴입니다.

### 예시: 폼 객체
```ruby
class UserForm
  attr_accessor :name, :email, :password

  def initialize
    @user = User.new
  end

  def build
    @user.name = name
    @user.email = email
    @user.password = password
    @user
  end
end

form = UserForm.new
form.name = "John Doe"
form.email = "john@example.com"
form.password = "securepassword"
user = form.build
```

### 장점
- 복잡한 객체를 단계적으로 생성할 수 있습니다.
- 객체 생성의 유연성을 높일 수 있습니다.

### 단점
- 빌더 클래스를 추가로 작성해야 하므로 코드가 복잡해질 수 있습니다.
- 간단한 객체 생성에는 오버헤드가 될 수 있습니다.

---

이러한 디자인 패턴들은 각각의 장단점을 가지고 있으며, 적절한 상황에서 사용하면 코드의 가독성, 유지보수성, 확장성을 크게 향상시킬 수 있습니다.



# 디자인 패턴의 장단점

디자인 패턴은 소프트웨어 설계에서 자주 발생하는 문제에 대한 일반적인 해결책을 제공합니다. 각 패턴은 특정 상황에서 유용하지만, 모든 상황에 적합하지 않을 수 있습니다. 따라서 패턴을 선택할 때는 장단점을 고려해야 합니다.

## 장점

- **재사용성**:
    - 패턴은 이미 검증된 솔루션을 제공하여 코드의 재사용성을 높입니다.
    - 다양한 상황에서 쉽게 적용할 수 있습니다.

- **유지보수성**:
    - 코드 구조가 명확해져 유지보수가 용이합니다.
    - 코드의 일관성을 유지하는 데 도움이 됩니다.

- **확장성**:
    - 시스템을 쉽게 확장할 수 있도록 설계됩니다.
    - 새로운 기능 추가 시 기존 코드를 최소한으로 변경할 수 있습니다.

## 단점

- **복잡성 증가**:
    - 일부 패턴은 코드의 복잡성을 증가시킬 수 있습니다.
    - 특히 작은 프로젝트에서는 불필요한 복잡성을 초래할 수 있습니다.

- **오버헤드**:
    - 패턴을 적용함으로써 추가적인 클래스나 인터페이스가 필요할 수 있습니다.
    - 성능에 영향을 줄 수 있는 경우도 있습니다.

- **부적절한 사용**:
    - 잘못된 상황에서 패턴을 적용하면 오히려 코드의 가독성과 효율성을 떨어뜨릴 수 있습니다.
    - 상황에 맞지 않는 패턴 사용은 유지보수를 어렵게 만들 수 있습니다.

따라서 디자인 패턴을 사용할 때는 문제의 본질을 이해하고, 패턴이 실제로 문제 해결에 도움이 되는지 판단하는 것이 중요합니다. 패턴을 무조건적으로 적용하기보다는, 상황에 맞는 적절한 패턴을 선택하는 것이 가장 중요합니다.
