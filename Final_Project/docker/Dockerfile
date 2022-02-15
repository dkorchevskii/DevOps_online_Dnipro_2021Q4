FROM openjdk:8-jre-alpine
RUN mkdir /app && addgroup -S korchevskii && adduser -S -s /bin/false -G korchevskii korchevskii
WORKDIR /app
COPY ./docker /app
RUN chown -R korchevskii:korchevskii /app && ls -la
USER korchevskii
EXPOSE 8080
CMD ["java", "-jar", "petclinic.jar"]
