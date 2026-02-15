FROM jenkinsci/blueocean:latest

USER root

# Instalacja zależności i klienta Docker (apk to menedżer pakietów Alpine)
RUN apk update && \
    apk add --no-cache \
    ca-certificates \
    curl \
    gnupg \
    docker-cli

# Wróć do użytkownika jenkins dla bezpieczeństwa
USER jenkins