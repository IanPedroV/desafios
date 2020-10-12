FROM adoptopenjdk/openjdk11
FROM maven:alpine

# image layer
WORKDIR /app
ADD pom.xml /app
RUN mvn verify clean --fail-never

# Image layer: with the application
COPY . /app
RUN mvn -v
RUN mvn clean install -DskipTests
ADD ./target/StringFormatter-1.0-SNAPSHOT.jar /developments/
ENTRYPOINT ["java","-jar","/developments/StringFormatter-1.0-SNAPSHOT.jar"]