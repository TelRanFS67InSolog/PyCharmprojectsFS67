#!/usr/bin/env python3
"""
🚀 Космическая Экспедиция: Развивающая интерактивная игра для детей (7 лет)
Скрипт запускает локальный веб-сервер и открывает игру в браузере Safari на macOS.
"""

import http.server
import os
import socket
import socketserver
import subprocess
import sys
import threading
import time
import webbrowser

PORT = 8765
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "space_game")


def find_free_port(preferred_port=8765):
    """Находит свободный порт, начиная с предпочитаемого."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("", preferred_port))
            return preferred_port
        except OSError:
            s.bind(("", 0))
            return s.getsockname()[1]


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Подавляем лишний вывод логов в терминал, оставляем только чистый интерфейс
        pass


def open_in_safari(url):
    """Открывает указанный URL в браузере Safari на macOS."""
    try:
        # Прямой вызов Safari через системную утилиту macOS open
        subprocess.run(["open", "-a", "Safari", url], check=True)
        print("🎮 Safari успешно запущен с игрой!")
    except Exception as e:
        print(f"⚠️ Не удалось открыть напрямую через Safari ({e}), пробуем стандартный браузер...")
        webbrowser.open(url)


def main():
    port = find_free_port(PORT)
    url = f"http://localhost:{port}/index.html"

    print("=" * 60)
    print("🚀 ЗАПУСК КОСМИЧЕСКОЙ ЭКСПЕДИЦИИ ДЛЯ ДЕТЕЙ (7 ЛЕТ)")
    print("=" * 60)
    print(f"📁 Директория игры: {DIRECTORY}")
    print(f"🌐 Адрес сервера:   {url}")
    print("-" * 60)

    # Запускаем открытие Safari в отдельном потоке с небольшой задержкой, чтобы сервер успел подняться
    timer = threading.Timer(0.8, open_in_safari, args=[url])
    timer.daemon = True
    timer.start()

    # Запуск HTTP сервера
    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        print(f"🟢 Сервер активен на порту {port}. Нажмите Ctrl+C для остановки.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Игра завершена. Сервер остановлен. До новых приключений!")
            sys.exit(0)


if __name__ == "__main__":
    main()
