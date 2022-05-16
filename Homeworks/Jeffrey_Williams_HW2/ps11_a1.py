# Problem Set 1
# Name: Jeffrey Williams
# Time Spent: 1:00
# Last Modified: Oct 8, 2021

"""
Module for currency exchange

This module provides several string parsing functions to implement a simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Jeffrey Williams, 5030143
Date:   October 8, 2021
"""


def usd_to_eur(amount):
    exchange_rate = 0.87
    amount = amount * exchange_rate
    return amount


def eur_to_usd(amount):
    exchange_rate = 1.16
    amount = amount * exchange_rate
    return amount


def usd_to_aud(amount):
    exchange_rate = 1.37
    amount = amount * exchange_rate
    return amount


def aud_to_usd(amount):
    exchange_rate = 0.73
    amount = amount * exchange_rate
    return amount


def usd_to_jpy(amount):
    exchange_rate = 112.14
    amount = amount * exchange_rate
    return amount


def jpy_to_usd(amount):
    exchange_rate = 0.0089
    amount = amount * exchange_rate
    return amount


def usd_to_php(amount):
    exchange_rate = 50.58
    amount = amount * exchange_rate
    return amount


def php_to_usd(amount):
    exchange_rate = 0.020
    amount = amount * exchange_rate
    return amount
