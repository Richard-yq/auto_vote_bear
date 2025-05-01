import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import random
import time

# 常見英文名字列表
common_names = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Liam", "Olivia", "Noah", "Emma", "Oliver", "Sophia", "Elijah", "Isabella", "William", "Mia",
    "James", "Charlotte", "Benjamin", "Amelia", "Lucas", "Harper", "Henry", "Evelyn", "Alexander", "Abigail",
    "Samuel", "Emily", "Joseph", "Elizabeth", "Daniel", "Chloe", "Matthew", "Ella", "Michael", "Scarlett",
    "Ethan", "Madison", "Jacob", "Lily", "Ryan", "Aubrey", "Andrew", "Grace", "Joshua", "Natalie",
    "Gabriel", "Addison", "Christian", "Leah", "Owen", "Hannah", "Savannah", "Caleb", "Brooklyn"
]

def vote(url):
    """
    開啟網頁，點擊投票按鈕，輸入隨機名稱並完成投票。

    Args:
        url (str): 目標投票網頁的 URL。
    """
    driver = None
    try:
        # 初始化 Chrome WebDriver
        options = webdriver.ChromeOptions()
        # 你可以取消註解下一行以在背景執行 (無頭模式)
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        # 等待投票按鈕出現並點擊 (等待時間增加到 20 秒)
        vote_button_xpath = "//*[@id=\"surface-panels\"]/div[1]/div/div[2]/div/div[3]/button"
        vote_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, vote_button_xpath))
        )
        vote_button.click()

        # 等待輸入名稱的欄位出現並輸入隨機名稱 (等待時間增加到 20 秒)
        name_input_xpath = "//*[@id=\"app\"]/div[4]/div/div/div/div/form/div[1]/div/input"
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, name_input_xpath))
        )
        random_name = random.choice(common_names)
        name_input.send_keys(random_name)

        # 等待送出投票的按鈕出現並點擊 (等待時間增加到 20 秒)
        submit_button_xpath = "//*[@id=\"app\"]/div[4]/div/div/div/div/form/div[2]/button"
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, submit_button_xpath))
        )
        submit_button.click()
        time.sleep(2.5)

        print(f"已成功投票，使用的名稱是: {random_name}")

    except TimeoutException:
        print("錯誤：等待元素超時，可能是網頁結構改變或載入緩慢 (等待時間已增加到 20 秒)。")
    except NoSuchElementException:
        print("錯誤：找不到指定的網頁元素，可能是 XPath 不正確。")
    except Exception as e:
        print(f"發生其他錯誤: {e}")

    finally:
        if driver:
            driver.quit()

def parallel_vote(url, num_votes):
    for _ in range(num_votes):
        vote(url)
        time.sleep(0.15) # 可以調整每次投票後的等待時間

if __name__ == "__main__":
    target_url = "https://padlet.com/linda903_1/113-wov7zbn9gdtsokji/wish/Xb8YaL4g9RlVayn1"
    num_threads = 15  # 設定要同時執行的執行緒數量
    votes_per_thread = 25000  # 每個執行緒執行的投票次數
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=parallel_vote, args=(target_url, votes_per_thread))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("所有投票已完成！")