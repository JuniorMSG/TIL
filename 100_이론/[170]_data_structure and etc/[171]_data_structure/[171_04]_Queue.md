# [171]_data_structure
## [171_04]_Queue.md

## Queue 큐 구조
    줄을 서는 행위와 유사
    가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
    음식점에서 가장 먼저 줄을 선 사람이 제일 먼저 음식점에 입장하는 것과 동일
    FIFO(First-In, First-Out) 또는 LILO(Last-In, Last-Out) 방식으로 스택과 꺼내는 순서가 반대

![img.png](rsc/171_04_Queue_01.png)


### 알아둘 용어
    Enqueue: 큐에 데이터를 넣는 기능
    Dequeue: 큐에서 데이터를 꺼내는 기능
    Visualgo 사이트에서 시연해보며 이해하기 (enqueue/dequeue 만 클릭해보며): 
    https://visualgo.net/en/list


### 파이썬 queue 라이브러리 활용해서 큐 자료 구조 사용하기¶
    queue 라이브러리에는 다양한 큐 구조로 Queue(), LifoQueue(), PriorityQueue() 제공
    프로그램을 작성할 때 프로그램에 따라 적합한 자료 구조를 사용
    Queue(): 가장 일반적인 큐 자료 구조
    LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조라고 보면 됨)
    PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력

### 참고: 어디에 큐가 많이 쓰일까?
    멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨 (운영체제 참조)
    큐의 경우에는 장단점 보다는 (특별히 언급되는 장단점이 없음), 
    큐의 활용 예로 프로세스 스케쥴링 방식을 함께 이해해두는 것이 좋음