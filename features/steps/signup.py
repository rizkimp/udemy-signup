import os
import time
import asyncio
import strgen
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@given(u'go to udemy signup page')
def step_impl(context):
    context.page.goto('https://www.udemy.com/join/signup-popup/')

@then(u'enter valid fullname')
def step_impl(context):
    context.page.fill(f'#{locator.input_fullname}','Rizki Uhuy')

@then(u'enter valid email')
def step_impl(context):
    username = strgen.StringGenerator("[a-z]{3}").render()
    context.page.fill(f'#{locator.input_email}',username+'@udemy.com')

@then(u'enter valid password')
def step_impl(context):
    context.page.fill(f'#{locator.input_password}','Abcde123!')

@when(u'click button signup')
def step_impl(context):
    context.page.click(locator.button_signup)

@then(u'success signup')
def step_impl(context):
    pass