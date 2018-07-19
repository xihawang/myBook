#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

def test(requst):
    test = 1

    return render(requst,'base.html',{"test":test})
