#!/bin/bash

set -e

cp README.md docs/index.md
pip-compile docs/requirements.in
