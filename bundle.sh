#!/usr/bin/env bash

m=$(date +%s)
touch /tmp/.lambda.mark.$m

echo "========================= Installing dependencies ==============================="
pip3 install -r reqs.txt -t .

echo "========================= Creating Zip ======================================"

zip -r /tmp/ecr-scan-lambda.zip .

echo "========================= Artificat saved to /tmp/ecr-scan-lambda.zip =============================="

find . -type d -newer /tmp/.lambda.mark.$m