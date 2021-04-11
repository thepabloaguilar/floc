import ctypes
from importlib import resources

from floc.go_types import ApplySortingLshResult, GoSlice, SimulateResult

with resources.path('floc.floc_go', 'floc_go.so') as floc_go_file:
    FLOC_GO = ctypes.cdll.LoadLibrary(str(floc_go_file))

FLOC_GO.cityHash64V103.argtypes = [ctypes.c_char_p]
FLOC_GO.cityHash64V103.restype = ctypes.c_uint64

FLOC_GO.cityHash64WithSeedsV103.argtypes = [
    ctypes.c_char_p, ctypes.c_uint64, ctypes.c_uint64,
]
FLOC_GO.cityHash64WithSeedsV103.restype = ctypes.c_uint64

FLOC_GO.cityHash64WithSeedV103.argtypes = [ctypes.c_char_p, ctypes.c_uint64]
FLOC_GO.cityHash64WithSeedV103.restype = ctypes.c_uint64

FLOC_GO.simHashString.argtypes = [GoSlice]
FLOC_GO.simHashString.restype = ctypes.c_uint64

FLOC_GO.applySortingLsh.argtypes = [ctypes.c_uint64, ctypes.c_char_p]
FLOC_GO.applySortingLsh.restype = ApplySortingLshResult

FLOC_GO.simulate.argtypes = [GoSlice, ctypes.c_char_p]
FLOC_GO.simulate.restype = SimulateResult
