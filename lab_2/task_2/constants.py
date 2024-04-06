from functions_assistant import load_json

PATHS = 'paths.json'
CPP_P = 'cpp_png'
JAVA_P = 'java_png'

N = 128
M = 8
P0, P1, P2, P3 = 0.2148, 0.3672, 0.2305, 0.1875

paths_dictionary = load_json(PATHS)
PATH_CPP_PNG = paths_dictionary[CPP_P]
PATH_JAVA_PNG = paths_dictionary[JAVA_P]
