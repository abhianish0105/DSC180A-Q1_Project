import os
import pulsar
import time
import random
import string
import logging
import sys
import tweepy
from tweepy import StreamingClient, StreamRule
from producer_test import Producer, IDPrinter

producer = Producer()

printer = IDPrinter(producer, "AAAAAAAAAAAAAAAAAAAAAGBNhwEAAAAAhZQnur29U9tf5cQwIqzQL5EeFEQ%3DOGdHnKXZHJ0uyPIdO2iZUdEnTBqrS6mgY6rwkaN8TfsvoTJ25y")

rule_ids = []
result = printer.get_rules()
for rule in result.data:
    rule_ids.append(rule.id)
print(rule_ids)
if (len(rule_ids) > 0):
    printer.delete_rules(rule_ids)

printer.add_rules(StreamRule('"pandemic" '))
printer.add_rules(StreamRule('"remote work" '))
printer.add_rules(StreamRule('lang:en'))
printer.add_rules(StreamRule('-is:quote'))
printer.add_rules(StreamRule('-has:cashtags'))
printer.add_rules(StreamRule('-has:media'))
printer.add_rules(StreamRule('has:hashtags'))
printer.add_rules(StreamRule('-is:retweet'))

printer.filter()
printer.sample()
