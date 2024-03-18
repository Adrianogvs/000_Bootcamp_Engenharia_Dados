#!/bin/bash

versions=("2.7" "3.11.5" "3.12.1")

for version in "${versions[@]}"
do
    pyenv install $version
done