# PSD Spritesheet Utility

Requirements:
- Python 3
- [ImageMagick](https://imagemagick.org/index.php) installed and available in PATH.

## `frames_to_psd.py`

Converts individual frames into a multi-layered `.psd`.

Usage:
```python
python frames_to_psd.py %SOURCE_FOLDER% %FRAME_NUMBERS% %OUTPUT_PSD_PATH%
```

Example:
```python
python frames_to_psd.py ./frames 1 2 10 15 ./frames/layers.psd
```

## `psd_to_spritesheet.py`

Converts a multi-layered `.psd` into a horizontal spritesheet. Output is a `.png` and a `.psd` (placed in the same folder as input).

Usage:
```python
python psd_to_spritesheet.py %PATH_TO_INPUT_PSD%
```

Example:
```python
python psd_to_spritesheet.py ./frames/layers.psd
```