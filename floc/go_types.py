import ctypes
from typing import List


class GoSlice(ctypes.Structure):
    _fields_ = [  # noqa: WPS120
        ('data', ctypes.POINTER(ctypes.c_void_p)),
        ('len', ctypes.c_longlong),
        ('cap', ctypes.c_longlong),
    ]

    def __len__(self) -> int:
        """Returns the len from the go slice struct."""
        return self.len  # type: ignore[no-any-return]


class GoString(ctypes.Structure):
    _fields_ = [  # noqa: WPS120
        ('p', ctypes.c_char_p),
        ('n', ctypes.c_longlong),
    ]

    def __str__(self) -> str:
        """Returns the string value from go string struct."""
        if self:
            return str(self.p)
        return ''

    def __bool__(self) -> bool:
        """
        Emulate the same python string behavior.

        I it's empty return false, otherwise return True

        """
        return self.n > 0  # type: ignore[no-any-return]


class GoInterface(ctypes.Structure):
    _fields_ = [  # noqa: WPS120
        ('t', ctypes.c_void_p),
        ('v', ctypes.c_void_p),
    ]


class ApplySortingLshResult(ctypes.Structure):
    _fields_ = [  # noqa: WPS120
        ('r0', ctypes.c_uint64),
        ('r1', ctypes.c_char_p),
    ]


class SimulateResult(ctypes.Structure):
    _fields_ = [  # noqa: WPS120
        ('r0', ctypes.c_uint64),
        ('r1', ctypes.c_char_p),
    ]


class SimHashStringResult(ctypes.Structure):
    _fields_ = [  # noqa: WPS120
        ('r0', ctypes.c_uint64),
        ('r1', ctypes.c_char_p),
    ]


def covert_str_list_to_go_slice(str_list: List[str]) -> GoSlice:
    casted_list = [
        ctypes.cast(
            ctypes.c_char_p(string.encode()), ctypes.c_void_p,
        )
        for string in str_list
    ]
    converted_list = (ctypes.c_void_p * len(casted_list))(*casted_list)
    return GoSlice(
        converted_list,
        len(converted_list),
        len(converted_list),
    )
