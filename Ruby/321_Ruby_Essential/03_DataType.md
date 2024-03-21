## ruby 데이터 타입
    원시 자료형이 사실상 존재하지 않고 모든 것이 객체인 언어
    여러 종류의 데이터를 식별하는 분류

### 숫자
    2
```ruby
num = 2
puts('숫자형', num)
```

### 문자열
    'Hello World'
```ruby
str = 'String'
puts('문자형', str)
```

### nil
    null 이랑 같은 값?
    'Null'과 'nil'은 동의어이며 둘 다 값에서 '0' 또는 '무'를 의미합니다. 두 단어는 주로 사용하는 분야에 따라 다릅니다. 
    우리는 주로 수학, 프로그래밍, 비즈니스 및 법률 문제에서 'null'을 사용합니다. 
    반면에 우리는 스포츠와 게임에서 'nil'을 사용합니다.

```ruby
xNil = nil
puts('null => nil', xNil)
```
### Boolean
    Boolean이라고 부르긴 하나? 애매하군!
    true / false
```ruby
boolean = true
puts('boolean true/false', boolean)
```
### 배열 (Array)
    인덱스와 번호에 대응하는 데이터들로 이루어진 자료 구조
    다른언어와 비교했을때 같은 타입은 대략 이런 느낌임 
    ruby = []
    python = [] 
    js = []
    Java = List<Type> or ArrayList<Type>
```ruby
people = ['Alice', 123, 3.14, nil, false, true]
puts("puts(people[0]) : ", people[0])
```


### 해시 (Hash)
    다른언어와 비교했을때 같은 타입은 대략 이런 느낌임 
    js => json, python => dict
    java => HashMap
    ruby => Hash?
    
```ruby
colors = {'red' => 'ff0000', 'green' => '00ff00'}
puts("colors('red') : ", colors['red'])
```

### Reference
[Null vs Nil](https://grammarhow.com/null-vs-nil/)


## 변수와 상수
    루비는 타입을 선언하지 않는다. 
    변수는 변하는 값
    상수는 변하지 않는 값임
    
    변수는 스코프가 중요한데
    스코프에 따라서 지역변수, 전역변수, 인스턴스 변수, 클래스 변수 등으로 불린다.


### 지역변수
    지역변수는 해당 지역에서만 참조 가능함 
    함수 내부면 함수 내부에서만
    클래스 메소드 내부면 클래스 메소드 내부에서만
    근데 루비에선 어떠려나??
    var = 'range of variables is local Area'

```ruby
    x = 2
    x += 2
    puts('지역 변수  ', x)
```

### 전역변수
    전역변수는 어디서 선언하던, 어느곳에서나 불러 올 수 있는 변수
    루비에선 $를 붙여서 선언한다.
    $var = 'range of variables is All Area'

```ruby
x = 2
$allArea = '전체 영역 변수'
def HelloWord
    puts '전체 변수', $allArea
    puts '지역 변수', x
end
HelloWord()
```
#### 오류
    x는 지역변수 이기 때문에 함수 내부에서 호출이 불가능 한 것을 볼 수 있다.
    전역변수는 잘 된다.
![img](https://user-images.githubusercontent.com/22822369/185753382-d5c982e2-d876-429e-a1a9-213ace4be914.png)


#### 주의점
    전역변수는 메모리를 항상 차지하고 삭제되지 않기 때문에 남발하면 안된다.
    

### 인스턴스 변수
    클래스 내에 있는 인스턴스에서 불러올 수 있다.
    @var = 'range of variables by Instance Area'

### 클래스 변수
    @@var = 'range of variables is Class Area'

```ruby
class Clock
  @@hello = 1
  def get_time
    puts @times
    puts @@hello
  end
  def set_time
    @times = '20220820'
    puts @@hello
  end
end
```

