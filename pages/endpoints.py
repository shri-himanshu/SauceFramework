from __future__ import absolute_import, unicode_literals

from enum import Enum


class SauceDemoAPIs(Enum):  # pylint: disable=too-few-public-methods
    """Enumeration of supported SauceDemo Rest API base paths"""
    base_url = 'https://www.saucedemo.com'
    login = '/'
    inventory = '/inventory.html'
    cart = '/cart.html'
    checkout_step1 = '/checkout-step-one.html'
    checkout_step2 = '/checkout-step-two.html'
    checkout_complete = '/checkout-complete.html'

