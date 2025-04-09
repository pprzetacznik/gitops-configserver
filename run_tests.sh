#!/bin/bash

set -xe

# pytest -svvv
python -m pytest -svvv \
  tests/test_hieradata_resolver.py
