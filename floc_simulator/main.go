package main

/*
#include <stdlib.h>
*/
import "C"
import (
	"fmt"
	"unsafe"

	"github.com/shigeki/floc_simulator/packages/floc"

	"golang.org/x/net/publicsuffix"
)

// floc_simulator is caluculate CohortId with using host lists and SortingLshClusters.
// This needs a json file of host list for history data.
var kMaxNumberOfBitsInFloc uint8 = 50

//export cityHash64V103
func cityHash64V103(cStr *C.char) uint64 {
	str := C.GoString(cStr)
	return floc.CityHash64V103([]byte(str))
}

//export cityHash64WithSeedsV103
func cityHash64WithSeedsV103(cStr *C.char, firstSeed, secondSeed uint64) uint64 {
	str := C.GoString(cStr)
	return floc.CityHash64WithSeedsV103([]byte(str), firstSeed, secondSeed)
}

//export cityHash64WithSeedV103
func cityHash64WithSeedV103(cStr *C.char, seed uint64) uint64 {
	str := C.GoString(cStr)
	return floc.CityHash64WithSeedV103([]byte(str), seed)
}

//export simHashString
func simHashString(domainList []*C.char, kMaxNumberOfBitsInFloc uint8) (uint64, *C.char) {
	domainsSlice := convertSliceCharPointerToSliceString(domainList)

	var newDomainList []string
	for _, host := range domainsSlice {
		eTLDPlusOne, err := publicsuffix.EffectiveTLDPlusOne(host)
		if err != nil {
			return 0, C.CString(err.Error())
		}
		newDomainList = append(newDomainList, eTLDPlusOne)
	}

	return floc.SimHashString(newDomainList, kMaxNumberOfBitsInFloc), C.CString("")
}

//export applySortingLsh
func applySortingLsh(
	simHash uint64,
	clusterData *C.char,
	kMaxNumberOfBitsInFloc uint8,
	checkSensiveness bool,
) (uint64, *C.char) {
	clusterDataStr := C.GoString(clusterData)
	result, err := floc.ApplySortingLsh(
		simHash,
		[]byte(clusterDataStr),
		kMaxNumberOfBitsInFloc,
		checkSensiveness,
	)

	if err != nil {
		return 0, C.CString(err.Error())
	}

	return result, C.CString("")
}

//export simulate
func simulate(
	hostList []*C.char,
	sortingLshClusterData *C.char,
	kMaxNumberOfBitsInFloc uint8,
	checkSensiveness bool,
) (uint64, *C.char) {
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

	simHash := floc.SimHashString(domainList, kMaxNumberOfBitsInFloc)

	cohortId, err := floc.ApplySortingLsh(
		simHash,
		[]byte(sortingLshClusterDataStr),
		kMaxNumberOfBitsInFloc,
		checkSensiveness,
	)
	if err != nil {
		return 0, C.CString(err.Error())
	}

	return cohortId, C.CString("")
}

//export freeString
func freeString(str *C.char) {
	C.free(unsafe.Pointer(str))
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
