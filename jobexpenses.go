package main

import (
	"fmt"
)

func readEntries(n int) ([]int, error) {
	in := make([]int, n)
	for i := range in {
		_, err := fmt.Scanf("%d", &in[i])
		if err != nil {
			return in[:i], err
		}
	}

	return in, nil
}

func main() {
	var numberOfEntries int
	fmt.Scanf("%d", &numberOfEntries)
	entries, _ := readEntries(numberOfEntries)
	// fmt.Println("Entries:", entries)

	var sum int
	for _, element := range entries {
		if element < 0 {
			sum += element * (-1)
		}
	}
	fmt.Println(sum)
}
