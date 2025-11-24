FROM debian:latest

# Install Python and libgpiod for gpio control
RUN apt-get update \
    && apt-get install -y python3 python3-pip python3-libgpiod python3-flask \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

CMD ["/bin/bash"]
