import ctypes

from floc.floc_go import FLOC_GO


class ApplySortingLshError(RuntimeError):
    """Represents an error occured on Go Side when calling the func."""


def apply_sorting_lsh(
    sim_hash: int,
    sorting_cluster_data: str,
    k_max_numbers_of_bits_in_floc: int = 50,
    check_sensiveness: bool = True,
) -> int:
    apply_sorting_result = FLOC_GO.applySortingLsh(
        sim_hash,
        sorting_cluster_data,
        k_max_numbers_of_bits_in_floc,
        check_sensiveness,
    )

    error = ctypes.cast(apply_sorting_result.r1, ctypes.c_char_p).value
    FLOC_GO.freeString(apply_sorting_result.r1)

    if error:
        raise ApplySortingLshError(error.decode())
    return apply_sorting_result.r0  # type: ignore[no-any-return]
