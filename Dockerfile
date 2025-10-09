FROM ubuntu:latest

# Install network utilities and curl
RUN apt-get update && apt-get install -y \
    curl \
    iputils-ping \
    net-tools \
    netcat-openbsd \
    traceroute \
    dnsutils \
    iproute2 \
    && rm -rf /var/lib/apt/lists/*

# Set entrypoint to sleep infinity
ENTRYPOINT ["sleep", "infinity"]
