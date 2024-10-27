from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright

def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    #context.page = context.browser.new_page(viewport={'width': 1280, 'height': 800})
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    context.page.close()
    context.browser.close()
    context.playwright.stop()

def before_all(context):
    pass

def after_all(context):
    pass