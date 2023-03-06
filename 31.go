package main

import "fmt"

var edges map[int][]int
var used map[int]int

func dfs(cur int) {
	for _, next := range edges[cur]{
		if used[next] == 0{
			used[0]++;
			used[next] = 1
			dfs(next)
		}
	}
}
func main() {
	edges = make(map[int][]int)
	used = make(map[int]int)
	var n, m int
	fmt.Scan(&n, &m)
	for i := 0; i < m; i++ {
		var a, b int
		fmt.Scan(&a, &b)
		used[a] = 0
		used[b] = 0
		edges[a] = append(edges[a], b)
		edges[b] = append(edges[b], a)
	}
	used[0] = 1
	used[1] = 1
	dfs(1)
	fmt.Println(used[0])
	fmt.Print(1)
	for i := 2; i <= n && used[0] > 1; i++ {
		if used[i] == 1 {
			fmt.Printf(" %d", i)
			used[0]--
		}
	}
}
