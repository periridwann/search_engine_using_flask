from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/automation', methods = ['Get', 'POST'])
def run_automation():
    if request.method == 'POST':
        search_key = request.form.get('search_key')
        title = selenium_code(search_key)
        return ("Automation execution has been completed")

def selenium_code(search_key):
    servis = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=servis)
    driver.maximize_window()
    driver.get("https://google.com")
    driver.find_element(By.XPATH, "//input[@name='q']").send_keys(search_key)
    driver.find_element(By.XPATH, "//input[@name='btnK']").submit()
    title = driver.title
    time.sleep(4)
    driver.quit()
    return title

if __name__ == "__main__":
    app.run(debug=True)