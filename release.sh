#!/bin/bash


set -e

VERSION=$1
if [ -z "$VERSION" ]
then
    echo "Usage: $0 <version>"
    exit 1
fi

RELEASE=$2
if [ -z "$RELEASE" ]
then
    RELEASE=0
fi

sed -i "s/{{VERSION}}/$VERSION/g" pyproject.toml
rm -rf dist
python -m build
if [ "$RELEASE" -eq 0 ]; then
    twine check dist/*
else
    twine upload dist/*
fi