import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url, timeout=10)
response.raise_for_status()
users = response.json()
for user in users[:5]:
    print(user["name"], user["email"])


# 2.
import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=10
    )
    response.raise_for_status()

except requests.exceptions.Timeout:
    print("The API took too long to respond")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)


# 3.
import requests
import time

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    for attempt in range(1, 4):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as error:
            print(f"Attempt {attempt} failed: {error}")

            if attempt < 3:
                time.sleep(2 ** (attempt - 1))
            else:
                raise

users = fetch_users()
print("Users fetched:", len(users))

# 4.
import requests

url = "https://jsonplaceholder.typicode.com/posts"

all_posts = []
page = 1
limit = 20

while True:
    response = requests.get(
        url,
        params={"_page": page, "_limit": limit},
        timeout=10
    )
    response.raise_for_status()

    posts = response.json()

    if not posts:
        break

    all_posts.extend(posts)
    print(f"Fetched page {page}: {len(posts)} posts")

    page += 1

print("Total posts:", len(all_posts))

# 5.
import csv
import logging
import time
import requests

logging.basicConfig(level=logging.INFO)

BASE_URL = "https://jsonplaceholder.typicode.com/posts"
OUTPUT_FILE = "posts_output.csv"


def fetch_page(page, limit=20, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(
                BASE_URL,
                params={"_page": page, "_limit": limit},
                timeout=10
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException:
            if attempt == max_attempts:
                raise

            wait_seconds = 2 ** (attempt - 1)
            logging.warning(
                "Page %s failed; retrying in %s seconds",
                page, wait_seconds
            )
            time.sleep(wait_seconds)


def ingest_posts():
    total = 0
    page = 1

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "userId", "title", "body"]
        )
        writer.writeheader()

        while True:
            posts = fetch_page(page)

            if not posts:
                break

            writer.writerows(posts)
            total += len(posts)

            logging.info("Fetched page %s: %s records", page, len(posts))
            page += 1

    logging.info("Ingestion complete: %s records", total)


if __name__ == "__main__":
    ingest_posts()