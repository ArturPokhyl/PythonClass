import allure
from allure_commons.types import AttachmentType

from core.helpers.driver import Driver


def decorator_screenshot(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except AssertionError:
            allure.attach(args[0].driver.get_screenshot_as_png(), name="Failed Screenshot",
                          attachment_type=AttachmentType.PNG)
            raise

    return wrapper
