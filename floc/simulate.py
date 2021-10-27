from importlib.resources import read_text
from typing import List

from floc.floc_go import FLOC_GO
from floc.go_types import covert_str_list_to_go_slice

SORTING_CLUSTER_DATA = read_text('floc', 'SortingLshClusters')


class SimulateError(RuntimeError):
    """Represents an error occured on Go Side when calling the simulate func."""


def simulate(
    host_list: List[str],
    sorting_cluster_data: str = SORTING_CLUSTER_DATA,
    k_max_numbers_of_bits_in_floc: int = 50,
    check_sensiveness: bool = True,
) -> int:
    simulation_result = FLOC_GO.simulate(
        covert_str_list_to_go_slice(host_list),
        sorting_cluster_data.encode(),
        k_max_numbers_of_bits_in_floc,
        check_sensiveness,
    )
    if simulation_result.r1:
        raise SimulateError(simulation_result.r1.decode())
    return simulation_result.r0  # type: ignore[no-any-return]
