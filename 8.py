import requests

# ==========================
# 1. Звичайний GET-запит
# ==========================

def simple_get_request():
    url = "https://example.com"
    print("\n=== Звичайний GET-запит ===")
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Статус-код:", response.status_code)
        print("Вміст перших 300 символів:\n", response.text[:300])
        return response
    except requests.exceptions.RequestException as e:
        print("Помилка GET-запиту:", e)


# ==========================
# 2. GET-запит з параметрами
# ==========================

def get_with_params():
    url = "https://httpbin.org/get"
    params = {"name": "Ivan", "age": 25}

    print("\n=== GET-запит з параметрами ===")
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        print("URL запиту:", response.url)  # показує, як виглядає URL після підставлення параметрів
        print("Отримані дані:\n", response.text)
        return response
    except requests.exceptions.RequestException as e:
        print("Помилка GET з параметрами:", e)


# ==========================
# 3. POST-запит
# ==========================

def post_request():
    url = "https://httpbin.org/post"
    data = {"username": "admin", "password": "12345"}

    print("\n=== POST-запит ===")
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print("Відповідь сервера:\n", response.text)
        return response
    except requests.exceptions.RequestException as e:
        print("Помилка POST-запиту:", e)


# ==========================
# 4. Вивід заголовків відповіді
# ==========================

def print_headers(response):
    if response:
        print("\n=== Заголовки відповіді ===")
        for key, value in response.headers.items():
            print(f"{key}: {value}")


# ==========================
# 5. Збереження сторінки в файл
# ==========================

def save_to_file(response, filename="saved_page.html"):
    if response:
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"\n=== Вміст збережено у файл: {filename} ===")
        except Exception as e:
            print("Помилка під час збереження:", e)


# ==========================
# ГОЛОВНА ПРОГРАМА
# ==========================

if __name__ == "__main__":
    # 1. GET-запит
    response_get = simple_get_request()

    # 2. GET із параметрами
    response_params = get_with_params()

    # 3. POST-запит
    response_post = post_request()

    # 4. Заголовки відповіді (на прикладі GET)
    print_headers(response_get)

    # 5. Збереження сторінки у файл
    save_to_file(response_get)
