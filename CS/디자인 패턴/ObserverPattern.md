## 옵저버 패턴 (Observer Pattern)

**정의**:
옵저버 패턴은 객체의 상태 변화를 관찰하고, 상태가 변경될 때마다 자동으로 통지되는 일대다 관계를 정의하는 디자인 패턴입니다.  
주로 이벤트 핸들링 시스템에 사용됩니다.

**특징**:
- **주제와 옵저버**: 주제(Subject) 객체는 상태 변화를 알리고, 옵저버(Observer) 객체는 상태 변화를 감지합니다.
- **느슨한 결합**: 주제와 옵저버는 느슨하게 결합되어 있어, 주제는 옵저버가 누구인지 알 필요가 없습니다.

**예제 (Ruby)**:
```ruby
class Subject
  def initialize
    @observers = []
  end

  def add_observer(observer)
    @observers << observer
  end

  def remove_observer(observer)
    @observers.delete(observer)
  end

  def notify_observers
    @observers.each { |observer| observer.update(self) }
  end

  def change_state
    # 상태 변경 로직
    notify_observers
  end
end

class Observer
  def update(subject)
    puts "Subject's state has changed!"
  end
end

subject = Subject.new
observer = Observer.new

subject.add_observer(observer)
subject.change_state
```