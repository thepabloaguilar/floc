from typing import List

from floc.floc_go import FLOC_GO
from floc.go_types import covert_str_list_to_go_slice


class SimHashStringError(RuntimeError):
    """Represents an error occured on Go Side when calling simHashString fun."""


def cityhash(string: str) -> int:
    return FLOC_GO.cityHash64V103(  # type: ignore[no-any-return]
        string.encode(),
    )


def cityhash_with_seeds(string: str, first_seed: int, second_seed: int) -> int:
    return FLOC_GO.cityHash64WithSeedsV103(  # type: ignore[no-any-return]
        string.encode(), first_seed, second_seed,
    )


def cityhash_with_seed(string: str, seed: int) -> int:
    return FLOC_GO.cityHash64WithSeedV103(  # type: ignore[no-any-return]
        string.encode(), seed,
    )


def sim_hash_string(
    domains: List[str],
    k_max_numbers_of_bits_in_floc: int = 50,
) -> int:
    sim_hash_result = FLOC_GO.simHashString(
        covert_str_list_to_go_slice(domains),
        k_max_numbers_of_bits_in_floc,
    )
    if sim_hash_result.r1:
        raise SimHashStringError(sim_hash_result.r1.decode())
    return sim_hash_result.r0  # type: ignore[no-any-return]
