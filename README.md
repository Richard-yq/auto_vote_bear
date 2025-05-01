# Padlet Auto-Voter Bot

This Python script automates the voting process on a specified Padlet page. It uses the Selenium library to simulate browser actions, including clicking a button, filling in a name field with a random common English name, and submitting the vote. The script also implements multi-threading to potentially increase the voting speed.

## Prerequisites

Before running this script, ensure you have the following installed:

1.  **Python 3:** Make sure you have Python 3 installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2.  **Selenium:** Install the Selenium library using pip:
    ```bash
    pip install selenium
    ```

3.  **ChromeDriver:** Selenium requires a browser driver to interact with Chrome. Download the ChromeDriver that matches your Chrome browser version from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads). Place the `chromedriver` executable in a directory that is included in your system's PATH environment variable, or in the same directory as your Python script.

## Setup

1.  **Save the Script:** Save the provided Python code as a `.py` file (e.g., `auto_vote.py`).

2.  **Configure the Target URL:** In the `if __name__ == "__main__":` block, ensure the `target_url` variable is set to the correct URL of the Padlet voting page.

3.  **Adjust Voting Parameters (Optional):**
    * `num_threads`: This variable controls the number of threads that will run concurrently to perform voting. Increasing this number can potentially speed up the overall voting process but may also increase resource consumption and the risk of being flagged by the website's anti-bot mechanisms. The default is set to `5`.
    * `votes_per_thread`: This variable determines how many times each thread will execute the voting process. The default is set to `2000`.
    * `time.sleep(0.5)` in the `parallel_vote` function: This sets a delay (in seconds) between consecutive votes within each thread. You can adjust this value. A smaller value might lead to faster voting but could also increase the risk of detection.

## How to Run

1.  **Open Terminal or Command Prompt:** Navigate to the directory where you saved the `auto_vote.py` file.

2.  **Execute the Script:** Run the script using the Python interpreter:
    ```bash
    python auto_vote.py
    ```

    The script will start multiple threads, each performing the voting process. The console will output messages indicating successful votes or any errors encountered.

## Script Details

### `common_names` List

This list contains a collection of common English names that will be randomly selected and entered into the name field during the voting process. You can extend or modify this list as needed.

### `vote(url)` Function

This function performs a single voting action:

1.  **Initializes Chrome WebDriver:** Sets up the Selenium WebDriver to control a Chrome browser instance.
2.  **Navigates to the URL:** Opens the specified Padlet URL in the browser.
3.  **Locates and Clicks the Vote Button:** Uses XPath to find the vote button and clicks it. It waits up to 15 seconds for the button to be present.
4.  **Locates and Fills the Name Input Field:** Uses XPath to find the name input field, selects a random name from the `common_names` list, and enters it into the field. It waits up to 24 seconds for the input field to be present.
5.  **Locates and Clicks the Submit Button:** Uses XPath to find the submit button and clicks it. It waits up to 15 seconds for the button to be present.
6.  **Introduces a Delay:** Pauses for 3 seconds after submitting the vote to allow the website to process the action.
7.  **Prints Success Message:** If all steps are successful, it prints a message indicating that a vote has been cast with a random name.
8.  **Error Handling:** Includes `try...except` blocks to catch potential errors such as `TimeoutException` (if an element is not found within the specified time) and `NoSuchElementException` (if an element cannot be located). It also catches other general exceptions.
9.  **Quits WebDriver:** Ensures that the browser instance is closed in the `finally` block, regardless of whether an error occurred.

### `parallel_vote(url, num_votes)` Function

This function takes the target URL and the number of votes as arguments and executes the `vote()` function multiple times with a small delay between each vote. This function is designed to be run by multiple threads.

### `if __name__ == "__main__":` Block

This is the main execution block of the script:

1.  **Sets the Target URL:** Defines the URL of the Padlet voting page.
2.  **Sets the Number of Threads:** Specifies the number of concurrent threads to use for voting.
3.  **Sets Votes Per Thread:** Determines how many times each thread will call the `vote()` function.
4.  **Creates and Starts Threads:** Creates a list of thread objects, each targeting the `parallel_vote()` function with the specified URL and number of votes. It then starts each thread.
5.  **Waits for Threads to Finish:** Uses `thread.join()` to wait for all the created threads to complete their execution before printing a final message.

## Important Considerations

* **Website Terms of Service:** Ensure that automating voting on the target website does not violate its terms of service.
* **Anti-Bot Measures:** Websites often have mechanisms to detect and block automated bots. Excessive or rapid voting might trigger these measures, leading to your IP address being blocked or votes being discarded. Use this script responsibly and consider implementing delays or other techniques to mimic human behavior more closely.
* **Resource Usage:** Running multiple browser instances concurrently can consume significant system resources (CPU and memory). Adjust the number of threads (`num_threads`) based on your computer's capabilities.
* **Error Handling:** The script includes basic error handling, but you might need to enhance it further to handle specific issues or implement logging for better debugging.
* **Website Changes:** If the structure of the Padlet page changes (e.g., button IDs, class names, XPath paths), the script may fail to locate the elements. You might need to inspect the page again and update the XPath expressions accordingly.

This README provides a detailed overview of the Python script and instructions on how to use it. Remember to use it ethically and responsibly.
