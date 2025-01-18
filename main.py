# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        self.send_response(200)
        if "static" in self.path.lower():
            path = "HTML" + self.path
            with open(path, "rb") as file:
                contact_page = file.read()
        else:
            contact_page = self.get_contact_page()

        self.end_headers()
        self.wfile.write(contact_page)

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        response = f"Received POST data: {post_data.decode('utf-8')}"
        print(response)
        self.send_response(200)
        self.end_headers()
        contact_page = self.get_contact_page()
        self.wfile.write(contact_page)

    def get_contact_page(self):
        path = "HTML/contact.html"
        with open(path, "rb") as file:
            return file.read()


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:

        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
