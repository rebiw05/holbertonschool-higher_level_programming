import requests
import csv
import json # Used for error handling output, not direct requirement for JSON parsing as requests handles it.

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles."""
    print("--- Fetching and Printing Posts ---")
    try:
        response = requests.get(BASE_URL)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post['title'])
        else:
            print(f"Error: Request failed with status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except json.JSONDecodeError:
        print("Error: API response is not valid JSON.")
    print("-" * 40)

def fetch_and_save_posts():
    """Fetches all posts from JSONPlaceholder and saves them to 'posts.csv'."""
    print("\n--- Fetching and Saving Posts to CSV ---")
    try:
        response = requests.get(BASE_URL)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts_data = response.json()
            if not posts_data:
                print("No posts received. CSV file will not be created.")
                return

            csv_file_name = "posts.csv"
            # Define CSV column headers based on common post keys
            fieldnames = ['id', 'title', 'body', 'userId'] 

            with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for post in posts_data:
                    # Filter keys to match fieldnames, adding empty string for missing ones
                    filtered_post = {key: post.get(key, '') for key in fieldnames}
                    writer.writerow(filtered_post)
            print(f"All posts successfully written to '{csv_file_name}'.")
        else:
            print(f"Error: Request failed with status code {response.status_code}. CSV not created.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except IOError as e:
        print(f"File writing error: {e}")
    except json.JSONDecodeError:
        print("Error: API response is not valid JSON.")
    print("-" * 40)
