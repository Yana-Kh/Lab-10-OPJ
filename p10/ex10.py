#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s1 = set(input("Enter line №1: "))
    s2 = set(input("Enter line №2: "))
    print(f"common characters in two lines: {s1.intersection(s2)}")
