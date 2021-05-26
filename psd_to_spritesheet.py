import sys
import subprocess

psd_path = './input.psd'

argc = len(sys.argv)
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue
    if i == 1:
        psd_path = arg
        continue

subprocess.call('magick convert "%s" -delete 0 +append "%s_spritesheet.png"' % (psd_path, psd_path))
subprocess.call('magick convert "%s" -delete 0 +append "%s_spritesheet.psd"' % (psd_path, psd_path))