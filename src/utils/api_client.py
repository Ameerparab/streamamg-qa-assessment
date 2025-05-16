import requests
import json
from src.config.settings import BASE_API_URL, COMMON_HEADERS, API_TIMEOUT, TODOS_ENDPOINT


class APIClient:
    def __init__(self, base_url=BASE_API_URL, headers=COMMON_HEADERS, timeout=API_TIMEOUT):
        self.base_url = base_url
        self.headers = headers
        self.timeout = timeout

    def _send_request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url}{endpoint}"
        try:
            if method == "GET":
                response = requests.get(url, headers=self.headers, params=params, timeout=self.timeout)
            elif method == "POST":
                response = requests.post(url, headers=self.headers, data=json.dumps(data) if data else None, timeout=self.timeout)
            elif method == "PUT":
                response = requests.put(url, headers=self.headers, data=json.dumps(data) if data else None, timeout=self.timeout)
            elif method == "DELETE":
                response = requests.delete(url, headers=self.headers, timeout=self.timeout)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            raise

    def get_todo(self, todo_id):
        return self._send_request("GET", f"{TODOS_ENDPOINT}/{todo_id}")

    def create_todo(self, todo_data):
        return self._send_request("POST", TODOS_ENDPOINT, data=todo_data)

    def update_todo(self, todo_id, todo_data):
        return self._send_request("PUT", f"{TODOS_ENDPOINT}/{todo_id}", data=todo_data)

    def delete_todo(self, todo_id):
        return self._send_request("DELETE", f"{TODOS_ENDPOINT}/{todo_id}")
