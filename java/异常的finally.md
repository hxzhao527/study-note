# finally到底什么时候执行?

参考[Does finally always execute in Java?](https://stackoverflow.com/questions/65035/does-finally-always-execute-in-java)
[Returning from a finally block in Java](https://stackoverflow.com/questions/48088/returning-from-a-finally-block-in-java)
## 情景一, 在```try```或```catch```块中添加return
```java
public class ExceptionStudy {
    public static void main(String[] args){
        System.out.println(test());
    }
    public static void base(Object in) throws Exception{
        throw new Exception("test exception");
    }
    public static int test(){
        try{
            base("a");
            return 1;
        } catch (Exception e){
            return 2;
        } finally {
            System.out.println("in finally");
            //return 3;
        }
    }
}
```
在```try``` 或```catch```返回之前, ```finally```中被执行.
## 情景二, 在```try```或```catch```块中添加```thread.stop()```
```java
public class ExceptionStudy {
    public static void main(String[] args) throws InterruptedException {
        test();
    }
    public static void base(Object in) throws Exception{
        throw new Exception("test exception");
    }
    public static void test() throws InterruptedException {
        Thread thread = new Thread(()->{
            try{
                ExceptionStudy.base("haha");
                System.out.println("in try");
                Thread.currentThread().stop();
            } catch (Exception e){
                System.out.println("in catch");
                Thread.currentThread().stop();
            } finally {
                System.out.println("in finally");
            }
        });
        thread.run();
        thread.join();
    }
}
```
同样, 在```try``` 或```catch```返回之前, ```finally```中被执行.