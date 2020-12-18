package main

import (
	"fmt"
	"sort"
	"strconv"
)

func readCup() (string, int) {
	var firstParam string
	var secondParam string
	fmt.Scanf("%s %s", &firstParam, &secondParam)

	if convertedFirstParam, err := strconv.Atoi(firstParam); err == nil {
		outRadius := convertedFirstParam / 2
		return secondParam, outRadius
	}

	convertedSecondParan, _ := strconv.Atoi(secondParam)
	return firstParam, convertedSecondParan
}

func main() {
	var numberofCups int
	fmt.Scanf("%d", &numberofCups)

	cupMap := make(map[int]string)
	for i := 0; i < numberofCups; i++ {
		cupColor, cupRadius := readCup()
		cupMap[cupRadius] = cupColor
	}
	// fmt.Println("Cup map unsorted", cupMap)

	var keys []int
	for k := range cupMap {
		keys = append(keys, k)
	}

	sort.Ints(keys)

	for _, k := range keys {
		fmt.Println(cupMap[k])
	}
}
