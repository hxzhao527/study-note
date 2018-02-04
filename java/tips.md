# java Tips

1. 如何检查一个类是不是已经被加载了?
```java
package com.hxzhao.stu;


public class TestClassLoaded {
    public static void main(String[] args) throws Exception {
        java.lang.reflect.Method m = ClassLoader.class.getDeclaredMethod("findLoadedClass", new Class[] { String.class });
        m.setAccessible(true);
        ClassLoader cl = ClassLoader.getSystemClassLoader();
        Object test1 = m.invoke(cl, "com.hxzhao.stu.TestClassLoaded$ClassToTest");
        System.out.println(test1 != null);
        com.hxzhao.stu.TestClassLoaded.ClassToTest.reportLoaded();
        Object test2 = m.invoke(cl, "com.hxzhao.stu.TestClassLoaded$ClassToTest");
        System.out.println(test2 != null);
    }
    static class ClassToTest {
        static {
            System.out.println("Loading " + ClassToTest.class.getName());
        }
        static void reportLoaded() {
            System.out.println("Loaded");
        }
    }
}
```
**注:** 类的描述要全, 即包名类名