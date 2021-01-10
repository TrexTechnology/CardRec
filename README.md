# CardRec

## How to install
### How to compile on Linux/macOS (using CMake)
```bash
cd darknet
./build.sh
```

### How to compile on Windows (using `vcpkg`)
```bash
git clone https://github.com/microsoft/vcpkg
cd vcpkg
$env:VCPKG_ROOT=$PWD
.\bootstrap-vcpkg.bat
.\vcpkg install darknet[full]:x64-windows #replace with darknet[opencv-base,cuda,cudnn]:x64-windows for a quicker install of dependencies
cd ../
cd darknet
powershell -ExecutionPolicy Bypass -File .\build.ps1
```

## How to use
```bash
python3 rec.py --image='[path of the image]'
```