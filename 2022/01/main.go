package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var inventory [][]int
	var calories []int

	// Load lines into inventory object
	for scanner.Scan() {
		snack := scanner.Text()
		if snack == "" {
			inventory = append(inventory, calories)
			calories = nil
			continue
		}
		calorie, err := strconv.Atoi(snack)
		if err != nil {
			fmt.Fprintln(os.Stderr, "string conversion to int:", err)
		}
		calories = append(calories, calorie)
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}
	inventory = append(inventory, calories)

	var reduced_inventory []int

	for _, v := range inventory {
		inner_sum := 0
		for _, w := range v {
			inner_sum += w
		}
		reduced_inventory = append(reduced_inventory, inner_sum)
	}

	sort.Ints(reduced_inventory)

	fmt.Println("Part 1:",
		reduced_inventory[len(reduced_inventory)-1],
	)
	fmt.Println("Part 2:",
		reduced_inventory[len(reduced_inventory)-1]+
			reduced_inventory[len(reduced_inventory)-2]+
			reduced_inventory[len(reduced_inventory)-3],
	)
}
