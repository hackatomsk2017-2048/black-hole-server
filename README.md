# black-hole-server
Сервер для игры Black Hole

# Endpoints

В настоящее время доступны следующие API

| Endpoing        | Протокол           | Описание  |
| ------------- |:-------------:| -----:|
| /             | HTTP GET | Главная страница. Возвращяет Hello world |
| /cards      | HTTP GET      |   Возвращяет число от 0 до 5. |
| /websocket | WS      |    Эхо api для теста websockets |

# Тестирование
Проверить работу вебсокетов можно легко из консоли браузера
```javascript
var ws = new WebSocket("ws://localhost:8888/websocket");
ws.onopen = function() {
   ws.send("Hello, world");
};
ws.onmessage = function (evt) {
   alert(evt.data);
};
ws.onopen()
```
Если все ок, должен появиться алерт с сообщением от сервера
