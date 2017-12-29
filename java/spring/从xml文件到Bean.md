先贴一张继承关系图, 后面讲解方法会用到.

![继承关系](img/容器继承关系.png)

*注:*图中最后的```BusApplicationContext```非spring内容, 这里不会涉及.

拿dubbo的demo为例, main函数里就下面这一点, 到底发生了啥就把服务暴露出去了?
```java
ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext(new String[]{"META-INF/spring/dubbo-demo-provider.xml"});
context.start();
```
后面的字符串路径里其实就是若干**Bean**的配置文件,关于什么是Bean,可以参考[7.3 Bean overview](https://docs.spring.io/spring/docs/4.3.x/spring-framework-reference/html/beans.html#beans-definition),如果一点概念都没,,, 这个,,你可以不看下面的东西了.
经跳转可看到,其实是调用的下面构造函数以实例化, 产生一个spring容器, 这里保留注释可以看下官方说明:
```java
/**
 * Create a new ClassPathXmlApplicationContext with the given parent,
 * loading the definitions from the given XML files.
 * @param configLocations array of resource locations
 * @param refresh whether to automatically refresh the context,
 * loading all bean definitions and creating all singletons.
 * Alternatively, call refresh manually after further configuring the context.
 * @param parent the parent context
 * @throws BeansException if context creation failed
 * @see #refresh()
 */
public ClassPathXmlApplicationContext(String[] configLocations, boolean refresh, ApplicationContext parent)
		throws BeansException {

	super(parent);
	setConfigLocations(configLocations);
	if (refresh) {
		refresh();
	}
}
```
```setConfigLocations``` 就是将配置的 xml文件路径 记录在容器属性中.
```java
/**
 * Set the config locations for this application context.
 * <p>If not set, the implementation may use a default as appropriate.
 */
public void setConfigLocations(String... locations) {
	if (locations != null) {
		Assert.noNullElements(locations, "Config locations must not be null");
		this.configLocations = new String[locations.length];
		for (int i = 0; i < locations.length; i++) {
			this.configLocations[i] = resolvePath(locations[i]).trim();
		}
	}
	else {
		this.configLocations = null;
	}
}
```
核心部分在```refresh```函数的调用上, 这是定义在```AbstractApplicationContext```上的方法, 在最顶层.

```java
@Override
public void refresh() throws BeansException, IllegalStateException {
	synchronized (this.startupShutdownMonitor) {
		// Prepare this context for refreshing.
		prepareRefresh();

		// Tell the subclass to refresh the internal bean factory.
		ConfigurableListableBeanFactory beanFactory = obtainFreshBeanFactory();

		// Prepare the bean factory for use in this context.
		prepareBeanFactory(beanFactory);

		try {
			// Allows post-processing of the bean factory in context subclasses.
			postProcessBeanFactory(beanFactory);

			// Invoke factory processors registered as beans in the context.
			invokeBeanFactoryPostProcessors(beanFactory);

			// Register bean processors that intercept bean creation.
			registerBeanPostProcessors(beanFactory);

			// Initialize message source for this context.
			initMessageSource();

			// Initialize event multicaster for this context.
			initApplicationEventMulticaster();

			// Initialize other special beans in specific context subclasses.
			onRefresh();

			// Check for listener beans and register them.
			registerListeners();

			// Instantiate all remaining (non-lazy-init) singletons.
			finishBeanFactoryInitialization(beanFactory);

			// Last step: publish corresponding event.
			finishRefresh();
		}

		catch (BeansException ex) {
			if (logger.isWarnEnabled()) {
				logger.warn("Exception encountered during context initialization - " +
						"cancelling refresh attempt: " + ex);
			}

			// Destroy already created singletons to avoid dangling resources.
			destroyBeans();

			// Reset 'active' flag.
			cancelRefresh(ex);

			// Propagate exception to caller.
			throw ex;
		}

		finally {
			// Reset common introspection caches in Spring's core, since we
			// might not ever need metadata for singleton beans anymore...
			resetCommonCaches();
		}
	}
}
```
首先```prepareRefresh```部分就是一些数据的准备,检查和重置, 函数里面执行的操作比较简单, 这里不再赘余.

**核心一**, spring的核心思路就是BeanFactory, 而```ConfigurableListableBeanFactory beanFactory = obtainFreshBeanFactory();```正是对*BeanFactory*的操作, 关于*BeanFactory*, 可参考[1.2版本spring关于Bean介绍时附带的BeanFactory描述](https://docs.spring.io/spring/docs/1.2.x/reference/beans.html)和[4.3.x中的描述](https://docs.spring.io/spring/docs/4.3.x/spring-framework-reference/html/beans.html#beans-beanfactory)

直说这个表达式里函数的核心部分, ```obtainFreshBeanFactory```核心是```refreshBeanFactory```函数的调用, 我们只关心我们继承链上的方法, 所以在```AbstractRefreshableApplicationContext```中找到了下面的定义, 
```java
/**
 * This implementation performs an actual refresh of this context's underlying
 * bean factory, shutting down the previous bean factory (if any) and
 * initializing a fresh bean factory for the next phase of the context's lifecycle.
 */
@Override
protected final void refreshBeanFactory() throws BeansException {
	if (hasBeanFactory()) {
		destroyBeans();
		closeBeanFactory();
	}
	try {
		DefaultListableBeanFactory beanFactory = createBeanFactory();
		beanFactory.setSerializationId(getId());
		customizeBeanFactory(beanFactory);
		loadBeanDefinitions(beanFactory);
		synchronized (this.beanFactoryMonitor) {
			this.beanFactory = beanFactory;
		}
	}
	catch (IOException ex) {
		throw new ApplicationContextException("I/O error parsing bean definition source for " + getDisplayName(), ex);
	}
}
```
先是检查是否已经有BeanFactory, 有就销毁掉. 然后创建新的.
```java
/**
 * Create an internal bean factory for this context.
 * Called for each {@link #refresh()} attempt.
 * <p>The default implementation creates a
 * {@link org.springframework.beans.factory.support.DefaultListableBeanFactory}
 * with the {@linkplain #getInternalParentBeanFactory() internal bean factory} of this
 * context's parent as parent bean factory. Can be overridden in subclasses,
 * for example to customize DefaultListableBeanFactory's settings.
 * @return the bean factory for this context
 * @see org.springframework.beans.factory.support.DefaultListableBeanFactory#setAllowBeanDefinitionOverriding
 * @see org.springframework.beans.factory.support.DefaultListableBeanFactory#setAllowEagerClassLoading
 * @see org.springframework.beans.factory.support.DefaultListableBeanFactory#setAllowCircularReferences
 * @see org.springframework.beans.factory.support.DefaultListableBeanFactory#setAllowRawInjectionDespiteWrapping
 */
protected DefaultListableBeanFactory createBeanFactory() {
    return new DefaultListableBeanFactory(getInternalParentBeanFactory());
}
```
创建的是```DefaultListableBeanFactory```实例, 暂时先不管这个类的具体定义细节, 这个方法在```AbstractRefreshableApplicationContext```中.
之后定制化一下BeanFactory, 就到了核心的加载**BeanDefinition**的环节, 关于**BeanDefinition**可以参见[3.2.2. The BeanDefinition](https://docs.spring.io/spring/docs/1.2.x/reference/beans.html), 粗糙的说就是bean的配置信息.

同样,我们只关心我们继承链上的实现, 在```AbstractXmlApplicationContext```中找到了如下定义,
```java
/**
 * Loads the bean definitions via an XmlBeanDefinitionReader.
 * @see org.springframework.beans.factory.xml.XmlBeanDefinitionReader
 * @see #initBeanDefinitionReader
 * @see #loadBeanDefinitions
 */
@Override
protected void loadBeanDefinitions(DefaultListableBeanFactory beanFactory) throws BeansException, IOException {
	// Create a new XmlBeanDefinitionReader for the given BeanFactory.
	XmlBeanDefinitionReader beanDefinitionReader = new XmlBeanDefinitionReader(beanFactory);

	// Configure the bean definition reader with this context's
	// resource loading environment.
	beanDefinitionReader.setEnvironment(this.getEnvironment());
	beanDefinitionReader.setResourceLoader(this);
	beanDefinitionReader.setEntityResolver(new ResourceEntityResolver(this));

	// Allow a subclass to provide custom initialization of the reader,
	// then proceed with actually loading the bean definitions.
	initBeanDefinitionReader(beanDefinitionReader);
	loadBeanDefinitions(beanDefinitionReader);
}
```
显然,前面都是实例和配置```beanDefinitionReader```, 真正的加载发生在```loadBeanDefinitions(beanDefinitionReader);```.
这还是在```AbstractXmlApplicationContext```这一层的方法, 
```java
/**
 * Load the bean definitions with the given XmlBeanDefinitionReader.
 * <p>The lifecycle of the bean factory is handled by the {@link #refreshBeanFactory}
 * method; hence this method is just supposed to load and/or register bean definitions.
 * @param reader the XmlBeanDefinitionReader to use
 * @throws BeansException in case of bean registration errors
 * @throws IOException if the required XML document isn't found
 * @see #refreshBeanFactory
 * @see #getConfigLocations
 * @see #getResources
 * @see #getResourcePatternResolver
 */
protected void loadBeanDefinitions(XmlBeanDefinitionReader reader) throws BeansException, IOException {
	Resource[] configResources = getConfigResources();
	if (configResources != null) {
		reader.loadBeanDefinitions(configResources);
	}
	String[] configLocations = getConfigLocations();
	if (configLocations != null) {
		reader.loadBeanDefinitions(configLocations);
	}
}
```
我们前面调用了```setConfigLocations(configLocations);```, 这里必然是```String[] configLocations = getConfigLocations();```.
*```getConfigResources();```暂不讨论, 它存的是类的搜索路径(可这样理解).*

我们直接看最终调用的方法, 在```AbstractBeanDefinitionReader```中, 
```java
@Override
public int loadBeanDefinitions(Resource... resources) throws BeanDefinitionStoreException {
	Assert.notNull(resources, "Resource array must not be null");
	int counter = 0;
	for (Resource resource : resources) {
		counter += loadBeanDefinitions(resource);
	}
	return counter;
}
```
转化为```org.springframework.core.io.Resource```后进行加载, 这个load的方法定义在XmlBeanDefinitionReader中, 
```java
/**
 * Load bean definitions from the specified XML file.
 * @param encodedResource the resource descriptor for the XML file,
 * allowing to specify an encoding to use for parsing the file
 * @return the number of bean definitions found
 * @throws BeanDefinitionStoreException in case of loading or parsing errors
 */
public int loadBeanDefinitions(EncodedResource encodedResource) throws BeanDefinitionStoreException {
	Assert.notNull(encodedResource, "EncodedResource must not be null");
	if (logger.isInfoEnabled()) {
		logger.info("Loading XML bean definitions from " + encodedResource.getResource());
	}

	Set<EncodedResource> currentResources = this.resourcesCurrentlyBeingLoaded.get();
	if (currentResources == null) {
		currentResources = new HashSet<EncodedResource>(4);
		this.resourcesCurrentlyBeingLoaded.set(currentResources);
	}
	if (!currentResources.add(encodedResource)) {
		throw new BeanDefinitionStoreException(
				"Detected cyclic loading of " + encodedResource + " - check your import definitions!");
	}
	try {
		InputStream inputStream = encodedResource.getResource().getInputStream();
		try {
			InputSource inputSource = new InputSource(inputStream);
			if (encodedResource.getEncoding() != null) {
				inputSource.setEncoding(encodedResource.getEncoding());
			}
			return doLoadBeanDefinitions(inputSource, encodedResource.getResource());
		}
		finally {
			inputStream.close();
		}
	}
	catch (IOException ex) {
		throw new BeanDefinitionStoreException(
				"IOException parsing XML document from " + encodedResource.getResource(), ex);
	}
	finally {
		currentResources.remove(encodedResource);
		if (currentResources.isEmpty()) {
			this.resourcesCurrentlyBeingLoaded.remove();
		}
	}
}
```
这才真正的读入xml文件, 然后调用```doLoadBeanDefinitions```加载得到```org.w3c.dom.Document```, 再抛给```registerBeanDefinitions```实际处理, 这些都在 前面实例的```Reader```中, 由于[这段](#192)的存在, 所以在```Reader```中能将解析出的Bean配置注册到容器中.

```java
/**
 * Register the bean definitions contained in the given DOM document.
 * Called by {@code loadBeanDefinitions}.
 * <p>Creates a new instance of the parser class and invokes
 * {@code registerBeanDefinitions} on it.
 * @param doc the DOM document
 * @param resource the resource descriptor (for context information)
 * @return the number of bean definitions found
 * @throws BeanDefinitionStoreException in case of parsing errors
 * @see #loadBeanDefinitions
 * @see #setDocumentReaderClass
 * @see BeanDefinitionDocumentReader#registerBeanDefinitions
 */
public int registerBeanDefinitions(Document doc, Resource resource) throws BeanDefinitionStoreException {
	BeanDefinitionDocumentReader documentReader = createBeanDefinitionDocumentReader();
	int countBefore = getRegistry().getBeanDefinitionCount();
	documentReader.registerBeanDefinitions(doc, createReaderContext(resource));
	return getRegistry().getBeanDefinitionCount() - countBefore;
}
```
其中```createBeanDefinitionDocumentReader();```返回一个```DefaultBeanDefinitionDocumentReader```实例. 
终于, 在```BeanDefinitionDocumentReader```的实现类```DefaultBeanDefinitionDocumentReader```中见到了熟悉的
![bean配置xml默认解析类](img/bean配置xml默认解析类.png)

再次跳转, 发现实际调用的是```DefaultBeanDefinitionDocumentReader```的```parseBeanDefinitions```,
```java
/**
 * Parse the elements at the root level in the document:
 * "import", "alias", "bean".
 * @param root the DOM root element of the document
 */
protected void parseBeanDefinitions(Element root, BeanDefinitionParserDelegate delegate) {
	if (delegate.isDefaultNamespace(root)) {
		NodeList nl = root.getChildNodes();
		for (int i = 0; i < nl.getLength(); i++) {
			Node node = nl.item(i);
			if (node instanceof Element) {
				Element ele = (Element) node;
				if (delegate.isDefaultNamespace(ele)) {
					parseDefaultElement(ele, delegate);
				}
				else {
					delegate.parseCustomElement(ele);
				}
			}
		}
	}
	else {
		delegate.parseCustomElement(root);
	}
}
```
这个地方对默认的[XML命名空间](https://msdn.microsoft.com/en-us/library/aa468565.aspx)和非默认做了区分, 
![spring默认xml命名空间](img/spring默认xml命名空间.png)<br />
spring默认的(这里列的URI)是```http://www.springframework.org/schema/beans```或者为空

先挑简单的, custom, 下面的方法在```BeanDefinitionParserDelegate```中
```java
public BeanDefinition parseCustomElement(Element ele) {
	return parseCustomElement(ele, null);
}

public BeanDefinition parseCustomElement(Element ele, BeanDefinition containingBd) {
	String namespaceUri = getNamespaceURI(ele);
	NamespaceHandler handler = this.readerContext.getNamespaceHandlerResolver().resolve(namespaceUri);
	if (handler == null) {
		error("Unable to locate Spring NamespaceHandler for XML schema namespace [" + namespaceUri + "]", ele);
		return null;
	}
	return handler.parse(ele, new ParserContext(this.readerContext, this, containingBd));
}
```
对于定制的命名空间, 使用
```java
NamespaceHandler handler = this.readerContext.getNamespaceHandlerResolver().resolve(namespaceUri);
```
获取解析器, 然后调用解析器的``parse``方法, 这也就是[基于Spring可扩展Schema提供自定义配置支持](http://blog.csdn.net/cutesource/article/details/5864562)这种操作的入口, dubbo中在dubbo/dubbo-config/dubbo-config-spring/src/main/java/com/alibaba/dubbo/config/spring/schema中的 DubboBeanDefinitionParser.java 和 DubboNamespaceHandler.java的作用.
关于NamespaceHandlerResolver这部分参考上面的自定义配置支持,这里不再赘余.

再来说默认的解析器, 在```DefaultBeanDefinitionDocumentReader```中,
```java
private void parseDefaultElement(Element ele, BeanDefinitionParserDelegate delegate) {
	if (delegate.nodeNameEquals(ele, IMPORT_ELEMENT)) {
		importBeanDefinitionResource(ele);
	}
	else if (delegate.nodeNameEquals(ele, ALIAS_ELEMENT)) {
		processAliasRegistration(ele);
	}
	else if (delegate.nodeNameEquals(ele, BEAN_ELEMENT)) {
		processBeanDefinition(ele, delegate);
	}
	else if (delegate.nodeNameEquals(ele, NESTED_BEANS_ELEMENT)) {
		// recurse
		doRegisterBeanDefinitions(ele);
	}
}
```
很是好奇,我们的**BeanDefinition**去哪了, 没有这个东西怎么配置定义Bean, 怎么注册到容器中的呢?
```java
/**
 * Process the given bean element, parsing the bean definition
 * and registering it with the registry.
 */
protected void processBeanDefinition(Element ele, BeanDefinitionParserDelegate delegate) {
	BeanDefinitionHolder bdHolder = delegate.parseBeanDefinitionElement(ele);
	if (bdHolder != null) {
		bdHolder = delegate.decorateBeanDefinitionIfRequired(ele, bdHolder);
		try {
			// Register the final decorated instance.
			BeanDefinitionReaderUtils.registerBeanDefinition(bdHolder, getReaderContext().getRegistry());
		}
		catch (BeanDefinitionStoreException ex) {
			getReaderContext().error("Failed to register bean definition with name '" +
					bdHolder.getBeanName() + "'", ele, ex);
		}
		// Send registration event.
		getReaderContext().fireComponentRegistered(new BeanComponentDefinition(bdHolder));
	}
}
```
在这个里面
```java
getReaderContext().fireComponentRegistered(new BeanComponentDefinition(bdHolder));
```
就做了这个操作, 将解析完的*BeanDefinition*注册到容器中.


至此, 我们的*Bean*可算注册到容器中了. 这还只是```refresh```函数中的第二步, 其他操作另写.

--------------------------------------------------------------------
附:
1. [How to add bean instance at runtime in spring WebApplicationContext?](https://stackoverflow.com/questions/43051394/how-to-add-bean-instance-at-runtime-in-spring-webapplicationcontext)