#!/bin/bash

while true; do
    read -r linha || break

    echo "[SCANNER] Linha recebida: '$linha'"

    read -ra tokens <<< "$linha"

    for token in "${tokens[@]}"; do

        if [[ $token =~ ^[0-9]+$ ]]; then
            echo "NUMBER($token)"

        elif [[ $token =~ ^[a-zA-Z_][a-zA-Z0-9_]*$ ]]; then
            echo "IDENT($token)"

        elif [[ $token == "=" ]]; then
            echo "ASSIGN(=)"

        elif [[ $token == "+" ]]; then
            echo "PLUS(+)"

        elif [[ $token == "*" ]]; then
            echo "MULT(*)"

        else
            echo "UNKNOWN($token)"
        fi

    done

done