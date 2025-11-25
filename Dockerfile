FROM python:3.10-slim

# Install Python and libgpiod for gpio control
COPY ./requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

RUN rm requirements.txt

WORKDIR /app

CMD ["/bin/bash"]
