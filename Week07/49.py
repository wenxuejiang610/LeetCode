#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if not strs:
            return [[]]

        anagram_dict = {}
        for str in strs:
            str_sorted = "".join(sorted(str))
            if str_sorted not in anagram_dict:
                anagram_dict[str_sorted] = [str]
            else:
                anagram_dict[str_sorted].append(str)

        anagram_groups = []
        for key in anagram_dict:
            anagram_dict[key].sort()
            anagram_groups.append(anagram_dict[key])

        return anagram_groups