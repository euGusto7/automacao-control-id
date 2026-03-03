import os
import allure
from core.driver_factory import create_driver
from allure_commons.types import AttachmentType
from datetime import datetime


def before_scenario(context, scenario):
    context.driver = create_driver()


def after_scenario(context, scenario):
    if scenario.status == "failed" and hasattr(context, "driver"):
        os.makedirs("reports/screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"reports/screenshots/{scenario.name}_{timestamp}.png"
        context.driver.save_screenshot(screenshot_name)

    if hasattr(context, "driver"):
        context.driver.quit()


def after_step(context, step):
    if step.status == "failed":
        os.makedirs("reports/screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"reports/screenshots/{step.name}_{timestamp}.png"
        context.driver.save_screenshot(screenshot_path)

        # allure.attach.file(
        #     screenshot_path, name="Screenshot", attachment_type=AttachmentType.PNG
        # )
