# Resource
## [Spring](https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#resources)
# 잡설


# Spring Resource
* java.net.URL의 한계(classpath 내부 접근이나 상대경로 등)를 넘어서기 위해 스프링에서 추가로 구현
*  스프링의 내부 동작을 이해하기 위해서 필요한 부분

## Resource Interface와 그 구현체들

```java
public interface Resource extends InputStreamSource {

    boolean exists();
    boolean isReadable();
    boolean isOpen();
    boolean isFile();
    URL getURL() throws IOException;
    URI getURI() throws IOException;
    File getFile() throws IOException;
    ReadableByteChannel readableChannel() throws IOException;
    long contentLength() throws IOException;
    long lastModified() throws IOException;
    Resource createRelative(String relativePath) throws IOException;
    String getFilename();
    String getDescription();
}
```
## Resource 구현체 목록
    Spring 내부 Resource 구현체 중 대표적인 몇가지

### UrlResource
    java.net.URL을 래핑한 버전, 다양한 종류(ftp:, file:, http:,  등의 prefix로 접근유형 판단)의 Resource에 접근 가능하지만 기본적으로는 http(s)로 원격접근

### ClassPathResource
    classpath(소스코드를 빌드한 결과(기본적으로 target/classes 폴더)) 하위의 리소스 접근 시 사용

### FileSystemResource
    이름과 같이 File을 다루기 위한 리소스 구현체
### SevletContextResource, InputStreamResource, ByteArrayResource
    Servlet 어플리케이션 루트 하위 파일, InputStream, ByteArrayInput 스트림을 가져오기 위한 구현체
---

## Spring ResourceLoader
스프링 프로젝트 내 Resource(파일 등)에 접근할 때 사용하는 기능

- 기본적으로 applicationContext에서 구현이 되어 있음
- 프로젝트 내 파일(주로 classpath 하위 파일)에 접근할 일이 있을 경우 활용
- 대부분의 사전정의된 파일들은 자동으로 로딩되도록 되어 있으나, 추가로 필요한 파일이 있을 때 이 부분 활용 가능

```java
@Service
public class ResourceService {
	@Autowired
	ApplicationContext ctx;

	public void setResource() {
		Resource myTemplate = 
			ctx.getResource("classpath:some/resource/path/myTemplate.txt");
			// ctx.getResource("file:/some/resource/path/myTemplate.txt");
			// ctx.getResource("http://myhost.com/resource/path/myTemplate.txt");
		// use myTemplate...
	}
}
```

---

## ResourcePatternResolver
    스프링 ApplicationContext에서 ResourceLoader를 불러올 때 사용하는 Interface
    위치 지정자 패턴("classpath:***", "file:***", "http:")에 따라 자동으로 Resouce 로더 구현체를 선택
```java
public interface ApplicationContext extends EnvironmentCapable, 
		ListableBeanFactory, HierarchicalBeanFactory,
		MessageSource, ApplicationEventPublisher, **ResourcePatternResolver** {
		// Spring ApplicationContext interface
}
```

---

## Application Contexts & Resource Paths
applicationContext(스프링의 핵심설정)을 이루는 설정값을 가져오는 방법들

```java
// let's create an applicationContext
ApplicationContext ctx = new ClassPathXmlApplicationContext("conf/appContext.xml");

ApplicationContext ctx =
    new FileSystemXmlApplicationContext("conf/appContext.xml");

ApplicationContext ctx =
    new FileSystemXmlApplicationContext("classpath:conf/appContext.xml");

// then you can use ctx as a Spring
Bear bear = (Bear) ctx.getBean("bear");
```

---
