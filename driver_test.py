from src.ui.driver.manager import UIDriverManager
import logging

from src.ui.driver.element.strategy.playwright_strategy_element import PlaywrightElementStrategy

logging.basicConfig(level=logging.DEBUG)

def main():
    driver = UIDriverManager().with_playwright().with_chrome().for_environment("https://practice-automation.com/").create()
    driver.set_elements(PlaywrightElementStrategy())
    try:
        driver.init()
        driver.start()
        print(driver.utilities().url())
        driver.Element().from_css("h1").with_value("Welcome to your software automation practice website!").build().should_().be_on_page()
        btn = driver.Button().from_text('Form Fields').build().should_().be_on_page()
        btn.action().click()
        driver.Element().from_css("h1").with_value("Form Fields").build().should_().be_on_page()
        print("End")

    except Exception as ex:
        print(ex)
    finally:
        driver.stop()

if __name__ == "__main__":
    main()
