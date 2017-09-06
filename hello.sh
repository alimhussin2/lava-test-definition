
#!/bin/bash

# This file is used to test LAVA bash script

set -e

echo "hello world. This is a bash script!"

for i in {1..10}
do
    echo "test-case-$i    ERROR "
done

for i in {11..20}
do
    echo "test-case-$i    FAIL "
done

for i in {21..30}
do
    echo "test-case-$i    PASS "
done

exit 0
