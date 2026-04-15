# QA-WEB 

Help info


OPENCART_USERNAME: user
OPENCART_PASSWORD: bitnami

docker-compose up -d
pytest tests
pytest --browser=chrome --base_url=http://localhost:8080  (default)

--alluredir=allure-reports

```bash
uv run allure serve allure-reports
```
```bash
docker build -t tests_app ./
```
```bash
docker run --rm -it tests_app --browser=firefox --base_url=http://host.docker.internal:8080 --alluredir=allure-reports
```