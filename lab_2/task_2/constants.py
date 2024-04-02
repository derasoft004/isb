from functions_assistant import load_json

PATHS = 'paths.json'
N = 128
M = 8
P0, P1, P2, P3 = 0.2148, 0.3672, 0.2305, 0.1875

paths_dictionary = load_json(PATHS)
PATH_CPP_PNG = paths_dictionary['cpp_png']
PATH_JAVA_PNG = paths_dictionary['java_png']
