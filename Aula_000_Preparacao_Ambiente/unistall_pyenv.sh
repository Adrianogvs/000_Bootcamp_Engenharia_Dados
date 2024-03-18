#!/bin/bash

versions=$(pyenv versions --bare)

for version in $versions
do
    if [[ $version != "*" ]]; then
        echo "Removendo a versão $version..."
        pyenv uninstall $version
    fi
done