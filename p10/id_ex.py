#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = {"a", "h", "m", "o", "r"}
    b = {"j", "k", "o", "u", "y"}
    c = {"g", "h", "j"}
    d = {"g", "j", "q"}

    x = (a.intersection(c)).union(d.intersection(b))
    y = (a.intersection(b).union(d.difference(c)))
    print(f"x = {x}, y = {y}")
