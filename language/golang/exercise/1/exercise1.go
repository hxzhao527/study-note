package main

import "fmt"
import "os"

func main() {
	var s, sep string
	for _, part := range os.Args {
		s += sep + part
		sep = "  "
	}
	fmt.Println(s)
}
