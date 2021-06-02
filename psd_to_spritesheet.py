import sys
import subprocess
from subprocess import Popen, PIPE
import os

psd_path = './input.psd'

argc = len(sys.argv)
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue
    if i == 1:
        psd_path = arg
        continue

proc = Popen(
    'magick identify -format "%w+"' +  ' "%s"' % (psd_path, ),
    shell=True,
    stdout=PIPE, stderr=PIPE
)

proc.wait()
res = proc.communicate()  # tuple('stdout', 'stderr')
if proc.returncode:
    print(res[1])

number_of_layers = str(res[0]).count('+')
print('Detected %d effective layers.' % (number_of_layers - 1, ))

def get_temp_file_name(index):
    return '__temp_layer_' + str(index) + '.png'

print('Creating temp layers...')

for i in range(1, number_of_layers):
    file_name = get_temp_file_name(i)
    command = 'magick convert "%s[0]" "%s[%d]" "(" -clone 0 -alpha transparent ")" -swap 0 +delete -coalesce -compose src-over -composite %s' % (psd_path, psd_path, i, file_name)
    subprocess.call(command)

temp_file_names = [get_temp_file_name(i) for i in range(1, number_of_layers)]
temp_images_joint = ' '.join(['"%s"' % (name, ) for name in temp_file_names])

print('Creating PNG...')
subprocess.call('magick convert %s +append "%s_spritesheet.png"' % (temp_images_joint, psd_path))
print('Creating PSD...')
subprocess.call('magick convert %s +append "%s_spritesheet.psd"' % (temp_images_joint, psd_path))

print('Cleaning up...')

for i in range(1, number_of_layers):
    os.remove(get_temp_file_name(i))

print('Done.')
