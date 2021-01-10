# CardRec

## How to install
First of all, run the config.sh file.
```bash
sh config.sh
```
After that, need to compile the darknet on your environment. The following section will demonstrate that how to compile the darknet in 
different environment.

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

## Result
It will return the json format data, such as:
```json
[
  {
    "class_id": 14,
    "class": "back_wheel",
    "relative_coordinates": [
      763.0264319999999,
      653.39648,
      902.061056,
      693.8936319999999
    ],
    "result_text": "",
    "text": "120/70-12 "
  },
  {
    "class_id": 3,
    "class": "brand",
    "relative_coordinates": [
      63.202304,
      373.62611200000003,
      155.04896,
      418.865408
    ],
    "result_text": "",
    "text": "P.G.O. "
  },
  {
    "class_id": 0,
    "class": "id",
    "relative_coordinates": [
      65.98400000000001,
      296.40243200000003,
      278.592,
      368.731648
    ],
    "result_text": "",
    "text": "MR-XX-XX "
  },
  {
    "class_id": 4,
    "class": "model",
    "relative_coordinates": [
      398.30886399999997,
      376.96998399999995,
      716.644864,
      436.28825599999993
    ],
    "result_text": "",
    "text": "JR-125CIAX (ALPHA MAX) AT "
  },
  {
    "class_id": 6,
    "class": "engine_number",
    "relative_coordinates": [
      65.112576,
      479.118592,
      228.30438400000003,
      523.91552
    ],
    "result_text": "",
    "text": "J2E6F00862 "
  },
  {
    "class_id": 7,
    "class": "vin",
    "relative_coordinates": [
      414.4158719999999,
      480.204544,
      692.020224,
      529.42208
    ],
    "result_text": "",
    "text": "RFVJRE6J2J1000861 "
  },
  {
    "class_id": 8,
    "class": "registration_day",
    "relative_coordinates": [
      763.3740799999999,
      496.6845440000001,
      937.250304,
      546.6741760000001
    ],
    "result_text": "",
    "text": "2018/03/23 "
  },
  {
    "class_id": 1,
    "class": "class",
    "relative_coordinates": [
      413.69139199999995,
      296.937472,
      703.894016,
      372.88448
    ],
    "result_text": "",
    "text": "重型摩托車(0 "
  },
  {
    "class_id": 9,
    "class": "from",
    "relative_coordinates": [
      69.417984,
      556.257792,
      271.627264,
      638.7440640000001
    ],
    "result_text": "",
    "text": "中國臺灣 TAIWAN, CHINA "
  },
  {
    "class_id": 2,
    "class": "cc",
    "relative_coordinates": [
      769.2513280000001,
      308.952576,
      929.312768,
      362.55897600000003
    ],
    "result_text": "",
    "text": "124.8 c.c "
  },
  {
    "class_id": 10,
    "class": "seat",
    "relative_coordinates": [
      641.3829119999999,
      571.060736,
      676.433408,
      623.64928
    ],
    "result_text": "",
    "text": ""
  },
  {
    "class_id": 11,
    "class": "kg",
    "relative_coordinates": [
      763.854336,
      571.881472,
      886.8725760000001,
      629.2090880000001
    ],
    "result_text": "",
    "text": "282 kgs "
  },
  {
    "class_id": 12,
    "class": "color",
    "relative_coordinates": [
      73.41568,
      631.79904,
      210.18316799999997,
      714.214656
    ],
    "result_text": "",
    "text": ""
  },
  {
    "class_id": 5,
    "class": "usage",
    "relative_coordinates": [
      773.0959359999999,
      373.76819200000006,
      907.965952,
      472.72140800000005
    ],
    "result_text": "",
    "text": "私人 Particular "
  },
  {
    "class_id": 13,
    "class": "front_wheel",
    "relative_coordinates": [
      411.579904,
      649.9494400000001,
      554.678784,
      694.727936
    ],
    "result_text": "",
    "text": "110/70-12 "
  }
]
```