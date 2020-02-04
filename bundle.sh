#!/usr/bin/env bash

m=$(date +%s)
touch /tmp/.lambda.mark.$m

echo "========================= Installing dependencies ==============================="
pip3 install -r reqs.txt -t .

echo "========================= Creating Zip ======================================"

zip -r /tmp/ecr-scan-lambda.zip .

echo "========================= Artificat saved to /tmp/ecr-scan-lambda.zip =============================="

echo "========================= Cleaning up =============================="

find . -type d -newer /tmp/.lambda.mark.$m -exec rm -rf {} \; 2>/dev/null

rm -f /tmp/.lambda.mark.$m