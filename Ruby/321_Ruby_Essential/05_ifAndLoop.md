# Ruby 제어문, 반복문
    실행의 흐름을 제어하기 위한 문법
    조건문 if, else, unless 
    반복문 for, while

## 조건문
|종류|의미|
|---|---|
|if|만약 ~~ 라면|
|unless|만약 ~~가 아니라면|


```ruby
if true
    puts "조건 1이 참일때"
elsif 1 == 1
    puts "조건1은 거짓이고 조건2 (1 == 1) 이 참일때"
else
    puts " 둘다 거짓"
end

unless false
  puts "조건 1이 거짓일때"
else
  puts "조건 1이 참일때"
end
```
![img_3](https://user-images.githubusercontent.com/22822369/186434195-1c740611-7747-4e09-a4cd-a17e9253fe94.png)
## 반복문

| 종류    | 의미            |
|-------|---------------|
| while | ~~ 하는 동안      |
| for   | ...동안 ...를 하라 |

### while 
```ruby
num = 0
while num <= 100
  if num%3 == 0
    puts num
  end
  num += 1
end
```
![img_1](https://user-images.githubusercontent.com/22822369/186434211-2c67e8be-781c-470d-84ad-f09e566d034e.png)


### for
```ruby
# for - 범위
puts "==== for - 범위 .. ===="
for num in 0..3
  puts num
end

puts "==== for - 범위 ... ===="
for num in 0...3
  puts num
end

# for - 배열

puts "==== for - 배열 ===="
arr = [1, 2 ,3 ,4]
for num in arr
  puts num
end
```
![img_4](https://user-images.githubusercontent.com/22822369/186434228-ae149643-c851-4cdb-92f6-828cb5319f47.png)
