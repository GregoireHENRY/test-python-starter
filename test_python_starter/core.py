#!/usr/bin/env python3

"""
test-python-starter
"""

from pudb import set_trace as bp  # noqa: F401


def start() -> None:
    """test-python-starter"""


def demo(name: str, demo: str) -> str:
    """Description."""
    return f"{name}: {demo}"


def power(value: float) -> float:
    """Compute power."""
    return value ** 2
