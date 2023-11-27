# -*- coding: utf-8 -*-
"""Provide common functions for testing."""
import json


def get_event(filespec):
    """Reads a JSON file and returns the event"""
    with open(filespec, "r", encoding="utf-8") as f:  # pylint: disable=invalid-name
        try:
            event = json.load(f)
            return event
        except json.JSONDecodeError:
            print(f"warning: invalid JSON in file: {filespec}")
            return f.read()
