#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "MARCUS CHIRIBOGA"

import cProfile
import pstats
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.

    https://zapier.com/engineering/profiling-python-boss/
    """
    def wrapper(*args, **kwargs):
        print("about to run")
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            sortby = "CUMULATIVE".lower()
            ps = pstats.Stats(profile).sort_stats(sortby)
            ps.print_stats()
            return result
        finally:
            profile.print_stats()
        print("done running")
        return result
    return wrapper


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    found = set([])
    keep = []
    for item in movies:
        if item not in found:
            found.add(item)
            keep.append(item)
        else:
            duplicates.append(item)
    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(
        stmt="find_duplicate_movies('movies.txt')",
        setup="from __main__ import find_duplicate_movies")
    result = t.repeat(number=3, repeat=7)
    print(result)
    return


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
