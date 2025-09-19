#!/bin/bash
cd /home/kavia/workspace/code-generation/order-lifecycle-management-dashboard-137336-137345/order_processing_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

