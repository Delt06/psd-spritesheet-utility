import sys
import subprocess

sprite_file_names = []
source_folder = '.'
destination_path = './result.psd'

argc = len(sys.argv)
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue
    if i == 1:
        source_folder = arg
        continue
    if i == argc - 1:
        destination_path = arg
        continue
    sprite_file_names.append('%04d.png' % (int(arg), ))

flattened_layer_name = 'flattenedlayer'
subprocess.call('magick ' + ' '.join(['%s/%s' % (source_folder, name) for name in sprite_file_names]) + ' -background none -flatten ' + flattened_layer_name, shell=True) 

layers_with_labels = ' '.join(['-label "%s" %s/%s' % (name.replace('.png', ''), source_folder, name) for name in sprite_file_names])
subprocess.call('magick ' + flattened_layer_name + ' ' + layers_with_labels + ' ' + destination_path, shell=True)