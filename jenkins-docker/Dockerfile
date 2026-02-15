FROM jenkinsci/blueocean:latest

USER root

# Instalacja zależności dla Docker client
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Dodaj klucz GPG Docker
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Dodaj repo Docker
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Zainstaluj Docker client (tylko cli, bez daemon)
RUN apt-get update && apt-get install -y docker-ce-cli

# Wróć do użytkownika jenkins
USER jenkins