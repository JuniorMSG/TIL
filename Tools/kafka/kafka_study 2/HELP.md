# Getting Started

### Reference Documentation
For further reference, please consider the following sections:

* [Official Gradle documentation](https://docs.gradle.org)
* [Spring Boot Gradle Plugin Reference Guide](https://docs.spring.io/spring-boot/docs/2.7.7/gradle-plugin/reference/html/)
* [Create an OCI image](https://docs.spring.io/spring-boot/docs/2.7.7/gradle-plugin/reference/html/#build-image)

### Additional Links
These additional references should also help you:

* [Gradle Build Scans – insights for your project's build](https://scans.gradle.com#gradle)



# 4. 아래 명령어를 실행해서 kafka 스키마와 계정을 생성합니다.
mysql> create database kafka default character set utf8 COLLATE utf8_general_ci;
mysql> create user kafka@localhost identified by 1234;
mysql> create user 'kafka'@'%' identified by '1234';
mysql> grant all privileges on kafka.* to 'kafka'@'localhost';
mysql> grant all privileges on kafka.* to 'kafka'@'%';
mysql> FLUSH PRIVILEGES;
