// https://adventofcode.com/2021/day/1

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func readFile() []string {
	f, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)

	var data []string

	for scanner.Scan() {
		data = append(data, scanner.Text())
	}

	return data
}

func main() {
	data := readFile()
	// part 1
	prev := -1
	count := 0
	for _, element := range data {
		i, _ := strconv.Atoi(element)
		if i > prev {
			count += 1
		}
		prev = i
	}
	// minus 1 as first count does not
	// go towards the score
	print(count - 1)

	
	//fmt.Print(data)
}
