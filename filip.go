package main

import (
	"fmt"
	"strconv"
)

func read() ([]int, error) {
	in := make([]int, 2)
	for i := range in {
		_, err := fmt.Scanf("%d", &in[i])
		if err != nil {
			return in[:i], err
		}
	}

	return in, nil
}

func reverse(number int) int {
	strNumber := strconv.Itoa(number)
	reverseStrNumber := ""
	for lenght := len(strNumber); lenght > 0; lenght-- {
		reverseStrNumber += string(strNumber[lenght-1])
	}

	reverseNum, error := strconv.Atoi(reverseStrNumber)
	if error != nil {
		fmt.Println("Failed to convert!")
	}
	return reverseNum
}

func main() {

	entr, _ := read()
	var greatest int

	for _, element := range entr {
		if reverse(element) > greatest {
			greatest = reverse(element)
		}
	}
	fmt.Println(greatest)
}
