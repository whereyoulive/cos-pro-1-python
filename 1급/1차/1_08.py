# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
누가 당선되나요
https://www.notion.so/pdg0526/08-2d32af36fb424c00807a903a9b10a7a3
"""
def solution(N, votes):
	vote_counter = [0 for i in range(N+1)]
	for i in votes:
		vote_counter[i] += 1

	max_val = max(vote_counter)

	answer = []
	for idx in range(1, N + 1):
		if vote_counter[idx] == max_val:
			answer.append(idx)

	return answer