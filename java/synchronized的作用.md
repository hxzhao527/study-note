# Java 线程之 synchronized

可参见[编程思想之多线程与多进程](http://blog.csdn.net/luoweifu/article/details/46595285) 了解一下线程及周边概念.
本文由阅读[Java中Synchronized的用法](http://blog.csdn.net/luoweifu/article/details/46613015)而来, 对其中示例没有给清和自己想到的做一些补充.

1. 修饰代码块 vs 修饰方法
* ##修饰代码块
```java
class SyncThread implements Runnable {
    private static int count;

    public SyncThread() {
        count = 0;
    }

    public void run() {
        synchronized(this) {
            for (int i = 0; i < 5; i++) {
                try {
                    System.out.println(Thread.currentThread().getName() + ":" + (count++));
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
        // 特意在语句块外面加了一句, 测一下和修饰方法的区别
        System.out.println(Thread.currentThread().getName() + " : " + "outside "+ count);
    }
}
public class MyStudy {
    public static void main(String args[]){
        SyncThread syncThread = new SyncThread();
        Thread thread1 = new Thread(syncThread, "A");
        Thread thread2 = new Thread(syncThread, "B");
        thread1.start();
        thread2.start();
    }
}
```
* ##修饰方法
``` java
class SyncThread implements Runnable {
    private static int count;

    public SyncThread() {
        count = 0;
    }

    public synchronized void run() {
        //synchronized(this) {
            for (int i = 0; i < 5; i++) {
                try {
                    System.out.println(Thread.currentThread().getName() + ":" + (count++));
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        //}
        System.out.println(Thread.currentThread().getName() + " : " + "outside "+ count);
    }

    public int getCount() {
        return count;
    }
}
public class SsistStudy {
    public static void main(String args[]){
        SyncThread syncThread = new SyncThread();
        Thread thread1 = new Thread(syncThread, "A");
        Thread thread2 = new Thread(syncThread, "B");
        thread1.start();
        thread2.start();
    }
}
```
**修饰方法的输出结果**
```
A:0
A:1
A:2
A:3
A:4
A : outside 5
B:5
B:6
B:7
B:8
B:9
B : outside 10
```
**修饰代码块的输出结果**
```
A:0
A:1
A:2
A:3
A:4
A : outside 5
B:5
B:6
B:7
B:8
B:9
B : outside 10
```
貌似没什么区别(滑稽脸,,), 这不是废话么, **锁语句**块是执行到语句块锁住, 在一个函数体里, 按照编码顺序执行, 所以这样写(上锁部分在方法开头)和锁方法没区别.
* ##修饰代码块
```java
class SyncThread implements Runnable {
    private static int count;

    public SyncThread() {
        count = 0;
    }

    public void run() {
        // 放在上锁的语句块前面才能对比区别
        System.out.println(Thread.currentThread().getName() + " : " + "outside "+ count);
        synchronized(this) {
            for (int i = 0; i < 5; i++) {
                try {
                    System.out.println(Thread.currentThread().getName() + ":" + (count++));
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }

    }
}
public class MyStudy {
    public static void main(String args[]){
        SyncThread syncThread = new SyncThread();
        Thread thread1 = new Thread(syncThread, "A");
        Thread thread2 = new Thread(syncThread, "B");
        thread1.start();
        thread2.start();
    }
}
```
* ##修饰方法
``` java
class SyncThread implements Runnable {
    private static int count;

    public SyncThread() {
        count = 0;
    }

    public synchronized void run() {
        System.out.println(Thread.currentThread().getName() + " : " + "outside "+ count);
        //synchronized(this) {
            for (int i = 0; i < 5; i++) {
                try {
                    System.out.println(Thread.currentThread().getName() + ":" + (count++));
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        //}
    }

    public int getCount() {
        return count;
    }
}
public class SsistStudy {
    public static void main(String args[]){
        SyncThread syncThread = new SyncThread();
        Thread thread1 = new Thread(syncThread, "A");
        Thread thread2 = new Thread(syncThread, "B");
        thread1.start();
        thread2.start();
    }
}
```

2. 修饰代码块 vs 修饰实例

```java
class AccountOperator implements Runnable{
    private Account account;
    public AccountOperator(Account account) {
        this.account = account;
    }

    public void run() {
        if (Thread.currentThread().getName() == "A"){
            synchronized (this) {
                try {
                    Thread.sleep(10000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                account.deposit(500);
                account.withdraw(500);
                System.out.println(Thread.currentThread().getName() + ":" + account.getBalance());
            }

        } else if (Thread.currentThread().getName() == "B"){
            synchronized (this) {
            account.deposit(500);
            System.out.println(Thread.currentThread().getName() + ":" + account.getBalance());
            }
        }

    }
}
public class SsistStudy {
    public static void main(String args[]){
        Account account = new Account("zhang san", 10000.0f);
        AccountOperator accountOperator = new AccountOperator(account);
        Thread a = new Thread(accountOperator, "A");
        Thread b = new Thread(accountOperator, "B");
        a.start();
        b.start();

    }
}
```
怎么就实现了锁实例? 这个和前面的锁代码块(括号里写this的)有什么区别?
其实锁代码块和锁实例, 实际 **锁** 的都是
```java
synchronized (this) {}
``` 
这个synchronized不能同时作用于一个对象. 所以如果其他地方没有用```synchronized (object) {}```, 那还是可以改动的和调用的.
可以参见[use-of-synchronized-on-a-block-with-instance-variable](https://stackoverflow.com/questions/42259061/use-of-synchronized-on-a-block-with-instance-variable)

3. 修饰方法
> * 是不能修饰接口中的方法的
> * 是不能修饰抽象方法的

4. 修饰类
和修饰代码块无异