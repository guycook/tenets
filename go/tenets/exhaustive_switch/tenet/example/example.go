package main

import (
	"math/rand"

	"github.com/lingo-reviews/tenets/go/tenets/exhaustive_switch/tenet/example/mypack"
)

type Foo int

const (
	Bar Foo = iota
	Baz
)

func drianPond() mypack.Fish {
	return mypack.Fish(rand.Intn(3))
}

func main() {

	// y := 10

	// // lingo:exhaustive_switch
	//
	// switch y + 10 {
	// case 22:
	// default:
	// }

	x := Bar

	// lingo:exhaustive_switch
	switch x {
	case Baz:
	}

	// lingo:exhaustive_switch
	switch {
	default:
	}

	p := drianPond()

	// lingo:exhaustive_switch
	switch p {
	case mypack.Onefish:
	default:
	}

	// lingo:exhaustive_switch
	switch p {
	case mypack.Onefish, mypack.Twofish:
	default:
	}

	// lingo:exhaustive_switch
	switch p {
	case mypack.Redfish:
	case mypack.Bluefish:
	default:
	}

	// lingo:exhaustive_switch
	switch p {
	case mypack.Onefish, mypack.Twofish:
	case mypack.Redfish:
	default:
	}

	// lingo:exhaustive_switch
	switch p {
	case mypack.Onefish:
	default:
	}

	// should be ignored
	switch p {
	case mypack.Onefish:
	default:
	}

}
