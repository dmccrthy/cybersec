#!/bin/bash

# Flood linux system with hundreds of compromised users
# Author: Dan McCarthy
# Date: 3/24/2025

echo "$1"

chars=abcdefghijklmnopqrstuvwxyz
for i in {1..6} ; do
    echo -n "${chars:RANDOM%${#chars}:1}"
done

# useradd tester

# echo "tester:password" | chpasswd

# echo "tester ALL=(ALL) ALL" | sudo tee -a /etc/sudoers.d/tester
