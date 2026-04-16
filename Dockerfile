FROM python:3.12

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    firefox-esr \
    xvfb fonts-liberation tzdata ca-certificates curl \
 && rm -rf /var/lib/apt/lists/*

RUN curl -L -o geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz \
    && tar -zxvf geckodriver.tar.gz \
    && mv geckodriver /usr/bin \
    && chmod +x /usr/bin/geckodriver \
    && rm geckodriver.tar.gz

ENV CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER=/usr/bin/chromedriver \
    FIREFOX_BIN=/usr/bin/firefox-esr \
    GECKODRIVER=/usr/bin/geckodriver


RUN mkdir /tests_app
WORKDIR /tests_app

COPY pyproject.toml .

RUN pip install --upgrade pip && pip install uv
RUN uv pip install --group dev --system

COPY ./src/ ./src
COPY ./tests/ ./tests

ENTRYPOINT ["pytest"]
