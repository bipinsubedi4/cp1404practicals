import wikipedia
import warnings

# Suppress BeautifulSoup warnings for cleaner output
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")


def main():
    """
        Main function to interact with the user and fetch Wikipedia pages based on user input.
        Handles cases like disambiguation, non-existent pages, and unexpected errors.
        """
    print("Welcome to the Wikipedia Search Tool!")

    # Prompt user for input
    user_input = input("\nEnter page title: ").strip()

    while user_input:
        try:
            # Perform a search to validate input and fetch the page
            search_results = wikipedia.search(user_input)
            if not search_results:
                # No results found
                print(f'\nPage id "{user_input}" does not match any pages. Try another id!')
            else:
                # Fetch the first search result
                page = wikipedia.page(search_results[0])
                print(f"\n{page.title}")
                print(f"{page.summary[:500]}")  # Print the first 500 characters of the summary
                print(f"{page.url}")