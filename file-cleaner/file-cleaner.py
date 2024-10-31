import os
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--dir", type=str, default=os.getcwd())
args = arg_parser.parse_args()
dir_to_clearn = args.dir

print(dir_to_clearn)

image_extensions = ['png', 'jpg', 'webp', 'bmp', 'jpeg', 'gif', 'tiff', 'svg', 'heic', 'raw']

if os.path.exists(dir_to_clearn) and not os.path.isfile(dir_to_clearn):
    onlyfiles = [f for f in os.listdir(dir_to_clearn) if os.path.isfile(os.path.join(dir_to_clearn, f))]
    for file in onlyfiles:
        filename, file_extension = os.path.splitext(file)
        if not filename.startswith('.') and file_extension != '':
            file_extension = file_extension[1:]
            new_dir_name = file_extension
            if file_extension.lower() in image_extensions:
                new_dir_name = 'images'
            newpath = dir_to_clearn + '/' + new_dir_name
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            os.rename(dir_to_clearn + '/' + file, newpath + '/' + file)
else:
    print(dir_to_clearn, ' - wrong directory')