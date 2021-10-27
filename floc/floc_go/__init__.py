import ctypes
import sys
from importlib import resources

from floc.go_types import (
    ApplySortingLshResult,
    GoSlice,
    SimHashStringResult,
    SimulateResult,
)

floc_go_so = f'floc_go-{sys.platform}.so'
with resources.path('floc.floc_go', floc_go_so) as floc_go_file:
    FLOC_GO = ctypes.cdll.LoadLibrary(str(floc_go_file))

FLOC_GO.cityHash64V103.argtypes = [ctypes.c_char_p]
FLOC_GO.cityHash64V103.restype = ctypes.c_uint64

FLOC_GO.cityHash64WithSeedsV103.argtypes = [
    ctypes.c_char_p, ctypes.c_uint64, ctypes.c_uint64,
]
FLOC_GO.cityHash64WithSeedsV103.restype = ctypes.c_uint64

FLOC_GO.cityHash64WithSeedV103.argtypes = [ctypes.c_char_p, ctypes.c_uint64]
FLOC_GO.cityHash64WithSeedV103.restype = ctypes.c_uint64

FLOC_GO.simHashString.argtypes = [GoSlice, ctypes.c_uint8]
FLOC_GO.simHashString.restype = SimHashStringResult

FLOC_GO.applySortingLsh.argtypes = [
    ctypes.c_uint64, ctypes.c_char_p, ctypes.c_uint8, ctypes.c_bool,
]
FLOC_GO.applySortingLsh.restype = ApplySortingLshResult

FLOC_GO.simulate.argtypes = [
    GoSlice, ctypes.c_char_p, ctypes.c_uint8, ctypes.c_bool,
]
FLOC_GO.simulate.restype = SimulateResult
