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
    wget https://codeload.github.com/AlexeyAB/darknet/zip/master
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        unzip darknet-master.zip
        cd darknet
        ./build.sh
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        unzip darknet-master.zip
        cd darknet
        ./build.sh
    elif [[ "$OSTYPE" == "msys" ]]; then
        git clone https://github.com/microsoft/vcpkg/master
        cd vcpkg
        $env:VCPKG_ROOT=$PWD
        .\bootstrap-vcpkg.bat
        .\vcpkg install darknet[full]:x64-windows
        cd ..
        git clone https://github.com/AlexeyAB/darknet
        cd darknet
        powershell -ExecutionPolicy Bypass -File .\build.ps1
    fi
fi