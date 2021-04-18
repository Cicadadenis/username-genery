#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author github.com/Cicadadenis/

__all__ = ["replace_placeholders", "user_agent"]

from faker import Faker

faker = Faker()

user_agent = faker.user_agent()
