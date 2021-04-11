package main

import "C"
import (
	"fmt"

	"golang.org/x/net/publicsuffix"
)

// floc_simulator is caluculate CohortId with using host lists and SortingLshClusters.
// This needs a json file of host list for history data.
var kMaxNumberOfBitsInFloc uint8 = 50

//export cityHash64V103
func cityHash64V103(cStr *C.char) uint64 {
	str := C.GoString(cStr)
	return CityHash64V103([]byte(str))
}

//export cityHash64WithSeedsV103
func cityHash64WithSeedsV103(cStr *C.char, firstSeed, secondSeed uint64) uint64 {
	str := C.GoString(cStr)
	return CityHash64WithSeedsV103([]byte(str), firstSeed, secondSeed)
}

//export cityHash64WithSeedV103
func cityHash64WithSeedV103(cStr *C.char, seed uint64) uint64 {
	str := C.GoString(cStr)
	return CityHash64WithSeedV103([]byte(str), seed)
}

//export simHashString
func simHashString(domainList []*C.char) uint64 {
	domainsSlice := convertSliceCharPointerToSliceString(domainList)
	return SimHashString(domainsSlice)
}

//export applySortingLsh
func applySortingLsh(simHash uint64, clusterData *C.char) (uint64, *C.char) {
	clusterDataStr := C.GoString(clusterData)
	result, err := ApplySortingLsh(simHash, []byte(clusterDataStr))

	if err != nil {
		return 0, C.CString(err.Error())
	}

	return result, C.CString("")
}

//export simulate
func simulate(hostList []*C.char, sortingLshClusterData *C.char) (uint64, *C.char) {
	kFlocIdMinimumHistoryDomainSizeRequired := 7
	sortingLshClusterDataStr := C.GoString(sortingLshClusterData)
	convertedHostList := convertSliceCharPointerToSliceString(hostList)

	if len(convertedHostList) < kFlocIdMinimumHistoryDomainSizeRequired {
		errStr := fmt.Sprintf(
			"FLoC needs more than %d domains. Current %d",
			kFlocIdMinimumHistoryDomainSizeRequired,
			len(convertedHostList),
		)
		return 0, C.CString(errStr)
	}

	var domainList []string
	for _, host := range convertedHostList {
		eTLDPlusOne, err := publicsuffix.EffectiveTLDPlusOne(host)
		if err != nil {
			return 0, C.CString(err.Error())
		}
		domainList = append(domainList, eTLDPlusOne)
	}

	simHash := SimHashString(domainList)

	cohortId, err := ApplySortingLsh(simHash, []byte(sortingLshClusterDataStr))
	if err != nil {
		return 0, C.CString(err.Error())
	}

	return cohortId, C.CString("")
}

func convertSliceCharPointerToSliceString(slice []*C.char) []string {
	convertedSlice := make([]string, 0)
	for _, d := range slice {
		// We need to make a copy of the `[]*C.char`,
		// so that the memory can be managed by Go GC
		convertedString := C.GoString(d)
		convertedSlice = append(convertedSlice, convertedString)
	}
	return convertedSlice
}

func main() {}
