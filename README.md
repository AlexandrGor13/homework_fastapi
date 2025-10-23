### API для взаимодействия с ML-моделями

#### Описание проекта
Проект представляет собой API для работы с предварительно обученными моделями машинного перевода: 
[Helsinki-NLP--opus-mt-ru-en](https://huggingface.co/Helsinki-NLP/opus-mt-ru-en), 
[Helsinki-NLP--opus-mt-en-ru](https://huggingface.co/Helsinki-NLP/opus-mt-en-ru)

End-point ```/translation/ru-en/``` предоставляет возможность переводить текс с русского языка на английский, 
```/translation/en-ru/``` переводит с английского на русский.

Используется метод POST с телом:
```json
{
  "text": "Текст, который требуется перевести"
}
```

#### Установка проекта
Клонируем проект
```bash
git clone https://github.com/AlexandrGor13/homework_fastapi.git
```
Устанавливаем проект
```bash
make setup
```

#### Запуск проекта
Запускаем контейнер с проектом в Docker
```bash
make up
```

Останавливаем контейнер
```bash
make down
```

#### Конфигурация Keycloak
Create realm (fastapi-realm)

Create role (admin, user)

Create client (ml-fastapi) 


#### API Endpoints
Получить токен доступа
```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "user", "password": "password"}'
  
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJONEFVaTJsMnByZk9xRXBoZ0FVUkQzWE5COXZ1YWRaZjgxeFJRaXNYdkNrIn0.eyJleHAiOjE3NjEyMDIyMzMsImlhdCI6MTc2MTIwMTkzMywianRpIjoib25ydHJvOmJjNmM0NDQ2LTNlZTktMzliNC02MDE2LTM3YWJjNGVkNjI4MyIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MC9yZWFsbXMvZmFzdGFwaS1yZWFsbSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiIyOGY5ZjlhOC1lNGViLTQxM2EtOGY5ZS1iODVjMTkxMWFhMTEiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJtbC1mYXN0YXBpIiwic2lkIjoiZWQyYTMwNGQtNTMwNi00MDQzLTkzMzYtZjY2YmU0ZGY3MTRiIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwOi8vbG9jYWxob3N0OjgwMDAiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtZmFzdGFwaS1yZWFsbSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iLCJ1c2VyIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6Ikpob24gRG93IiwicHJlZmVycmVkX3VzZXJuYW1lIjoidXNlciIsImdpdmVuX25hbWUiOiJKaG9uIiwiZmFtaWx5X25hbWUiOiJEb3ciLCJlbWFpbCI6InVzZXJAZXhhbXBsZS5jb20ifQ.PbgGh3or7qjqtARr3M_dXzWuBDMEPh7BPCDxt9F9t4bHqhCEtV_y5wU08Mc94c4g4K3Jy_JuhT0T-kD0T-l8yW5N5kNxXkbcJU6K394EsdsMgxu4SFPJ1YPAwf4yqAnxuG6DIhg8m-kVz4vC5IvVDIoniUpxggmaGZdfXEinikQmi1bbwjpftGsir9Wgp0PDhAjZRNt25pzWlGX0poF8kXFImc_CySQlKUYxlLgKfPLIJ-rcampw-F6i25fMmgriDMKvXQVPmaOKOP9wUVLjyJMMoIlEzi3yYEotwnCmKCIOi4IONCHWjBelDAgk1UmdkmY33fY_nsRmWwTPkYaQGw","refresh_token":"eyJhbGciOiJIUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJiMDlhN2E3OC1hMWY4LTQ3MzgtYTNlNC05ZmVjNzY3MTEyMjcifQ.eyJleHAiOjE3NjEyMDM3MzMsImlhdCI6MTc2MTIwMTkzMywianRpIjoiMzkxNTdhNTctNmMzNi01NmM4LWZmNTUtMGJhMmI0NjdmODIwIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9mYXN0YXBpLXJlYWxtIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9mYXN0YXBpLXJlYWxtIiwic3ViIjoiMjhmOWY5YTgtZTRlYi00MTNhLThmOWUtYjg1YzE5MTFhYTExIiwidHlwIjoiUmVmcmVzaCIsImF6cCI6Im1sLWZhc3RhcGkiLCJzaWQiOiJlZDJhMzA0ZC01MzA2LTQwNDMtOTMzNi1mNjZiZTRkZjcxNGIiLCJzY29wZSI6Im9wZW5pZCBzZXJ2aWNlX2FjY291bnQgZW1haWwgYWNyIHByb2ZpbGUgd2ViLW9yaWdpbnMgYmFzaWMgcm9sZXMifQ.uDEsCSbTtJwcjOWCcDAqFI5WPdkPvzFGpMdeH03VqpUaec3m9YlkaW1iUgYelvJso_PH7VxQaumXJX4vSwgL2A","token_type":"Bearer"}
```

Сделать перевод (User)
```bash
curl -X POST http://localhost:8000/translation/ru-en \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"text": "Текст, который требуется перевести"}'
  
{"text":"Text to be translated"}
```

Доступ к информации администратора
```bash
curl -X GET http://localhost:8000/admin \
  -H "Authorization: Bearer $ADMIN_TOKEN"
  
{"message":"Admin access granted","user":{"azp":"ml-fastapi","sub":"7b49b13a-d137-4b00-aa81-1478bc71b838","iat":1761202398,"exp":1761202698,"scope":"openid email profile","email_verified":false,"name":"Jhon Dow","given_name":"Jhon","family_name":"Dow","email":"admin@example.com","preferred_username":"admin","realm_access":{"roles":["default-roles-fastapi-realm","offline_access","admin","uma_authorization","user"]},"resource_access":{"realm-management":{"roles":["view-realm","view-identity-providers","manage-identity-providers","impersonation","realm-admin","create-client","manage-users","query-realms","view-authorization","query-clients","query-users","manage-events","manage-realm","view-events","view-users","view-clients","manage-authorization","manage-clients","query-groups"]},"broker":{"roles":["read-token"]},"account":{"roles":["manage-account","view-applications","view-consent","view-groups","manage-account-links","manage-consent","delete-account","view-profile"]}},"extra_fields":{}}}
```
