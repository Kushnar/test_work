from main.models import Weather
from weather.celery import app
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# # Func to create objects in db
# def update_or_create_weather_obj(data):
#     try:
#
#     except Exception as ex:
#         # Log report here. Ex.: write_something_in_log_func(ex)
#         pass


# Creating tasks for celery, by adding decorator @app.task to mark function as task
@app.task
def run_parser():
    parse_result = parse_weather()
    for i in parse_result:
        default_params = {k: v for k, v in i.items() if k != 'date'}
        Weather.objects.update_or_create(date=i.get('date'), defaults={**default_params})
    return parse_result


@app.task
def run_beat_parser():

    parse_result = parse_weather()
    for i in parse_result:
        default_params = {k: v for k, v in i.items() if k != 'date'}
        Weather.objects.update_or_create(date=i.get('date'), defaults={**default_params})
    return parse_result


# Parser, based on selenium and Undetected Chrome Driver.
# Target web-application includes Cloudflare defence, so we need to pass it using Undetected Chrome Driver
def parse_weather():
    # Set-up headers and options
    user_agent = "user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "HeadlessChrome/91.0.4472.114 Safari/537.36' "
    url = 'https://pogoda.meta.ua/ua/Kyivska/Kyivskiy/Kyiv/'

    options = Options()

    # Required arguments! Root user runs docker container, and we can't run driver without --headless and --no-sandbox
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    # ------
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(user_agent)
    driver = uc.Chrome(version_main=91, options=options)

    # Try-except block to catch exceptions
    try:
        driver.get(url)
        # Sleep for 6 seconds to pass captcha
        # time.sleep(6)
        days = driver.find_elements(By.CLASS_NAME, 'city__day')
        li = []
        # forming list of dictionaries to return
        for i in days:
            date = i.get_attribute('id')
            tempr = i.find_element(By.CLASS_NAME, 'city__day-temperature').find_element(By.TAG_NAME,
                                                                                        'span').text.replace('°', '')
            desc = driver.find_element(By.CLASS_NAME, 'city__main-image-descr').text
            # Pause, before next action
            li.append({'date': date, 'temperature': int(tempr), 'weather_description': desc})
            time.sleep(2)
            i.click()
        return li if li else None

    except Exception as ex:
        # Log report here. Ex.: write_something_in_log_func(ex)
        raise ex
    finally:
        # Make sure that process is stopped
        # driver.close()
        pass
