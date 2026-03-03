from behave import given, when, then
from time import sleep
from pages.login_page import LoginPage
from pages.sinc_hour import SincHourPage
from core.config import Config

import logging
import allure

log = logging.getLogger(__name__)


@given("que esteja logado no sistema do Control ID")
def step_init(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open(Config.BASE_URL)

    screenshot = context.driver.get_screenshot_as_png()
    allure.attach(
        screenshot, name="Tela de Login", attachment_type=allure.attachment_type.PNG
    )

    context.login_page.login(Config.USERNAME, Config.PASSWORD)
    sleep(2)


@when("eu acessar as configurações de horário")
def step_access_time_settings(context):
    context.sinc_hour_page = SincHourPage(context.driver)
    context.sinc_hour_page.click_settings_button()


@when("eu selecionar o horário de Brasília (GMT-3)")
def step_select_brasilia_time(context):
    context.sinc_hour_page = SincHourPage(context.driver)
    context.sinc_hour_page.select_brasilia_timezone()


@when("eu salvar as alterações")
def step_save_changes(context):
    screenshot = context.driver.get_screenshot_as_png()
    allure.attach(
        screenshot,
        name="Tela de Salvar Alterações",
        attachment_type=allure.attachment_type.PNG,
    )

    context.sinc_hour_page = SincHourPage(context.driver)
    context.sinc_hour_page.click_save_button()


@then("o horário do sistema deve ser atualizado para o horário de Brasília")
def step_verify_timezone_update(context):
    context.sinc_hour_page = SincHourPage(context.driver)
    assert (
        context.sinc_hour_page.is_loaded()
    ), "O horário do sistema não foi atualizado corretamente."
