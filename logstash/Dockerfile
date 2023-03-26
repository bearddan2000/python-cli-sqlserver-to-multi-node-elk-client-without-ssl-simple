##############################
########## Build 0 ###########
##############################

FROM maven:3-openjdk-17

ENV ARTIFACT com.microsoft.sqlserver

ENV GROUP msssql-jdbc

ENV VERSION 8.4.1.jre11

RUN mvn -Dmaven.repo.local=. dependency:get -Dartifact=${ARTIFACT}:${GROUP}:${VERSION}

##############################
########## Main Build ########
##############################

FROM logstash:7.12.0

ENV ARTIFACT com.microsoft.sqlserver

ENV GROUP msssql-jdbc

ENV VERSION 8.4.1.jre11

ENV JAR ${GROUP}-${VERSION}.jar

ENV WAIT_VERSION 2.7.2

USER logstash

COPY --from=0 /${ARTIFACT}/${GROUP}/${VERSION}/${JAR} /usr/share/logstash/data

COPY ./mystash.conf /usr/share/logstash/pipeline

COPY ./logstash.yml /usr/share/logstash/config

EXPOSE 9600

ADD --chown=logstash https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait

RUN chmod +x /wait

CMD ["logstash", "-f", "/usr/share/logstash/pipeline/mystash.conf"]