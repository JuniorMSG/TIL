## 싱글톤 패턴 (Singleton Pattern)

**정의**:
싱글톤 패턴은 클래스의 인스턴스가 하나만 존재하도록 제한하고, 이 인스턴스에 전역적인 접근을 제공하는 디자인 패턴입니다.
주로 애플리케이션에서 하나만 존재해야 하는 객체에 사용됩니다.


**특징**:
- **단일 인스턴스**: 특정 클래스의 인스턴스가 하나만 생성되고, 동일한 인스턴스에 접근할 수 있습니다.
- **전역 접근**: 클래스의 인스턴스를 전역적으로 접근할 수 있는 메서드를 제공합니다.

**예제 (Ruby)**:
```ruby
class SingletonExample
  @instance = new

  private_class_method :new

  def self.instance
    @instance
  end

  def some_method
    # 메서드 구현
  end
end

# 인스턴스 접근
singleton = SingletonExample.instance
singleton.some_method
```