import requests


def fetch_data(api_url):
    page = 1
    citations = []

    while True:
        response = requests.get(api_url, params={'page': page})
        data = response.json()

        print("Page", page, "data:", data)  # Add this line for debugging

        if not data['data']:
            break

        for item in data['data']:
            if isinstance(item, dict):
                citations.extend(get_citations(item))

        if 'next_page_url' not in data:
            break

        page += 1

    return citations


def get_citations(item):
    citations = []
    for source in item['source']:
        citations.append({'id': source['id'], 'link': source.get('link', '')})
    return citations


def main():
    api_url = 'https://devapi.beyondchats.com/api/get_message_with_sources'
    citations = fetch_data(api_url)
    print(citations)


if __name__ == "__main__":
    main()
