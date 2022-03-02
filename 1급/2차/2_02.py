# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
"""
합이 k배가 되는 수
https://www.notion.so/pdg0526/04-k-732e8101ffcf4f64a0d2618a539f6f02
"""

from itertools import combinations

solution = lambda arr, K : len([sum(i) for i in combinations(arr, 3) if sum(i) % K == 0])