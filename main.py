from config.config import settings
from src.selenium.pipeline_automation import PipelineAutomation
from src.selenium.action_type import ActionType as AT
from src.notifier import failed, success
from config.logging import setup_logging
import logging

BASE_URL = settings.URLS.base_url

ACTIONS = [
    {
        'type': AT.INPUT,
        'xpath': settings.XPATH.LOGIN.email_input,
        'value': settings.LOGIN.user
    },
    {
        'type': AT.INPUT,
        'xpath': settings.XPATH.LOGIN.password_input,
        'value': settings.LOGIN.password
    },
    {
        'type': AT.CLICK,
        'xpath': settings.XPATH.LOGIN.login_button
    },
    {
        'type': AT.CLICK,
        'xpath': settings.XPATH.MAIN.register_button
    },
    {
        'type': AT.WAIT_FOR,
        'xpath': settings.XPATH.MAIN.popup_div
    },
    {
        'type': AT.SLEEP,
        'time': 5,
        'callbacks': [
            success().show
        ]
    }
]

def main():
    setup_logging()
    
    automation = PipelineAutomation(BASE_URL)
    
    try:
        automation.execute_pipeline(ACTIONS)
    except Exception as e:
        logging.error(e)
        failed().show()
        
    automation.quit()


if __name__ == '__main__':
    main()
