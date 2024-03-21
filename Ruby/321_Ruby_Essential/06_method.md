# 메소드란
    문장은 명사와 동사로 이루어져 있다.
    루비에서 객체(Object)가 명사이고 (누가)
    메소드(Method)가 동사이다. (...을 한다)
    함수랑 크게 다를건 없는 부분!

```ruby
def calc_plus(x, y)
  sum = x + y
  return sum
end

def is_even? (number)
  if number % 2 == 0
    puts "even"
  else
    puts "odd"
  end
end

puts calc_plus(5, 7)
puts is_even?(5)
puts is_even?(4)
```
![img](https://user-images.githubusercontent.com/22822369/186435726-b893d4ea-a9c2-4812-a6f1-5a4b3d9769ea.png)
