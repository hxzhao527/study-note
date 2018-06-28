# HttpServletRequest.getParameter

这个接口的定义就是屎一样, 
```java
public interface ServletRequest {
    /**
     * Returns the value of a request parameter as a <code>String</code>, or
     * <code>null</code> if the parameter does not exist. Request parameters are
     * extra information sent with the request. For HTTP servlets, parameters
     * are contained in the query string or posted form data.
     * <p>
     * You should only use this method when you are sure the parameter has only
     * one value. If the parameter might have more than one value, use
     * {@link #getParameterValues}.
     * <p>
     * If you use this method with a multivalued parameter, the value returned
     * is equal to the first value in the array returned by
     * <code>getParameterValues</code>.
     * <p>
     * If the parameter data was sent in the request body, such as occurs with
     * an HTTP POST request, then reading the body directly via
     * {@link #getInputStream} or {@link #getReader} can interfere with the
     * execution of this method.
     *
     * @param name
     *            a <code>String</code> specifying the name of the parameter
     * @return a <code>String</code> representing the single value of the
     *         parameter
     * @see #getParameterValues
     */
    public String getParameter(String name);
}
```
```getParameter```方法, 既可能拿到post表单信息, 还可能是query信息, 这不是搞事? 
使用spring的注解, 写成
```java
    @RequestMapping(method = RequestMethod.POST)
    public ResponseMsg test(HttpServletRequest request, @RequestParam("test") String test) {
        log.info("======= get RequestParam test {}", test);
        return new ResponseMsg();
    }
```
如果query和form里都提供了, 就输出
```
2018-06-28 20:20:52.816  INFO 26956 --- [io-12346-exec-1] c.i.v.c.controller.TestController        : ======= get RequestParam test 2,1
```
再把参数```test```类型改为```Integer```, 输出就变成了
```
2018-06-28 20:22:01.111  INFO 8036 --- [io-12346-exec-1] c.i.v.c.controller.TestController        : ======= get RequestParam test 2
```

**?????**
那怎么只取form的或者query的呢? 通过注解或者```HttpServletRequest```, 对不起, 不存在的.

因此, 如果http请求比较"特殊", 后端就可能取到错误数据, 真是,,, 日了狗!!!