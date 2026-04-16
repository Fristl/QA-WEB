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
# Selenoid
```bash
docker-compose -f docker-compose-selenoid.yaml up
```
# Opencart with tests
```bash
docker-compose -f docker-compose.yaml up
```
