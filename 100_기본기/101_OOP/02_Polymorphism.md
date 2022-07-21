# 다형성(Polymorphism)

##  다형성(Polymorphism) 이란 ? 
> 여러 (poly) 모습(morph)을 갖는 것  
> 객체 지향에서는 한 객체가 여러 타입을 갖는 것  
> 한 객체가 여러 타입의 기능을 제공   
> 타입 상속으로 다형성 구현 


```Java
  public class Timer {
    public void start(){ .. }
    public void stop() { .. }
  }
  public interface Rechargeable{
    void charge();
  }
  
```   

```Java
  public class TimerSeoul extends Timer implements Rechargeable {
   ... 
  }
  public void charge(){
   ...
  }
  TimerSeoul it = new TimerSeoul();
  it.start();
  it.stop();
  
  Timer t = it;
  t.start()
  t.stop()
  
  Rechargeable r = it;
  r.charge()
```