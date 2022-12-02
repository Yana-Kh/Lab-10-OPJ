#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s = input("Enter line: ")
    vowels = {'e', 'y', 'u', 'i', 'o', 'a'}
    n = 0
    for i in s:
        if i in vowels:
            n += 1
    print(f"Number of vowels per line: {n}")
