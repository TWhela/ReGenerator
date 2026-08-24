#!/usr/bin/env python3
"""Convenience launcher: equivalent to `python -m regenerator`."""

import sys

from regenerator.cli import main

if __name__ == "__main__":
    sys.exit(main())
