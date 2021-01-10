FILE=test
if [ -d "$FILE" ]; then
    echo "$FILE directory exists. Skip this step."
else
    mkdir test
fi

FILE=darknet
if [ -d "$FILE" ]; then
    echo "$FILE directory exists. Skip this step."
else
    git clone https://github.com/AlexeyAB/darknet
fi