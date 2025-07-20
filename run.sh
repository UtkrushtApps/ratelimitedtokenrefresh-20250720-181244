#!/bin/bash
set -e

bash install.sh

# Run the tests
echo "Running tests..."
python3 -m app.tests.test_items

echo "All tests executed."
