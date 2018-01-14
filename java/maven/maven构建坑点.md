# maven构建坑点

POM文件的描述见[maven-model](https://maven.apache.org/ref/3.5.2/maven-model/maven.html)

* **build-plugin**

    如[官方文档](https://maven.apache.org/plugins/maven-compiler-plugin/)所写, 默认的构建下, ```source```和```target```都是1.5, 这不是坑爹是什么, **1.5**这么原始的版本. 需要自己通过[Setting the -source and -target of the Java Compiler](https://maven.apache.org/plugins/maven-compiler-plugin/examples/set-compiler-source-and-target.html)设置, 
    例如:
    ```xml
    <project>
    [...]
    <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
    </properties>
    [...]
    </project>
    ```
    或者
    ```xml
    <project>
    [...]
    <build>
      [...]
      <plugins>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-compiler-plugin</artifactId>
          <version>3.7.0</version>
          <configuration>
            <source>1.8</source>
            <target>1.8</target>
          </configuration>
        </plugin>
      </plugins>
      [...]
    </build>
    [...]
    </project>
    ```
    这里指定了```target```版本也不保证在这个版本的jre上可跑, 万一用到了新版本才有的api, 只会在运行期才报错, 编译不受影响. 所以完全靠自己.