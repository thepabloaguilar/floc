from typing import List

from floc.floc_go import FLOC_GO
from floc.go_types import covert_str_list_to_go_slice


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


def sim_hash_string(domains: List[str]) -> int:
    return FLOC_GO.simHashString(  # type: ignore[no-any-return]
        covert_str_list_to_go_slice(domains),
    )
