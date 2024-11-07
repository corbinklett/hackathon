import argparse
import os
import sys
import glob
import requests

# Python program to translate MicroPython/CircuitPython program to Arduino C
# API for ESP32 boards from Heltec Automation. Requires a translation server
# host and port information.

def translate_py_to_c(args: list, py_file: str) -> str:
    '''
      Translates a single Python program to Arduino C code for the given board.
      If translation is successful, generated C code will be returned,
      otherwise returns None.
    '''
    with open(py_file) as f:
        py_code = f.read()
    try:
        response = requests.post(args.host + ":" + str(args.port),
                                 json={
                                  "source_code": py_code,
                                  "source_lang": args.source_lang,
                                  "target_lang": "arduino-c",
                                  "target_hardware": args.board})
        if args.verbose:
            print(response.json())
        return response.json()['output_code']
    except Exception as e:
        if args.verbose:
            print('Request received exception:' + str(e))
        return None


parser = argparse.ArgumentParser(
            prog='micropy2c',
            description='Translate MicroPython or CircuitPython program(s) '
                        'to Arduino C SDK for ESP32 boards from Heltec '
                        'Automation.')
parser.add_argument('board',
                    help='Heltec board for which to generate Arduino C code',
                    choices=['heltec-wireless-tracker', 'heltec-wifi-lora-v3'])
parser.add_argument('source_file_or_dir', help='Python program file or a dir '
                    'containing Python programs')
parser.add_argument('-d', '--source-dir',
                    help='Input is a directory containing Python source files',
                    action='store_true')
parser.add_argument('-o', '--output-dir',
                    help='Directory to store generated Arduino C files',
                    default='/tmp')
parser.add_argument('-l', '--source-lang',
                    help='Language of Python program',
                    choices=['micropython', 'circuitpython'],
                    default='micropython')
parser.add_argument('-u', '--host', help='Translation API host',
                    default='localhost')
parser.add_argument('-p', '--port', help='Translation API port',
                    type=int, default=8080)
parser.add_argument('-v', '--verbose', help='Prints response details.',
                    action='store_true')
args = parser.parse_args()

# Sanity checks
if args.source_dir and not os.path.isdir(args.source_file_or_dir):
    print(f'ERROR: {args.source_file_or_dir} is not a directory')
    sys.exit(1)
if args.source_dir is False and not os.path.isfile(args.source_file_or_dir):
    print(f'ERROR: {args.source_file_or_dir} is not a file')
    sys.exit(1)

# If output directory does not exist, create it.
if os.path.isdir(args.output_dir):
    print(f'{args.output_dir} exists. Please provide an empty directory.')
    sys.exit(1)
else:
    os.mkdir(args.output_dir)

# Generate a list of Python programs to translate to Arduino C.
# Not a recursive search - if recursive is needed, set it to True.
py_progs = glob.glob("*.py", root_dir=args.source_file_or_dir) \
            if args.source_dir else [args.source_file_or_dir]
for py_prog in py_progs:
    print(f'Translating {py_prog}..')
    c_code = translate_py_to_c(args, py_prog)
    if c_code is not None:
        # from hello.py, we generate hello and hello/hello.ino
        c_file_dir = os.path.splitext(py_prog)[0]
        c_file_dir_path = os.path.join(args.output_dir, c_file_dir)
        os.mkdir(c_file_dir_path)
        c_file_path = os.path.join(c_file_dir_path, c_file_dir + ".ino")
        with open(c_file_path, 'w') as f:
            f.write(c_code)
        print(f'Generated Arduino sketch in {c_file_path}')
