### Go Programming Variables
how to declare the variable in go programming language

Below are the different variable data types.
var      age    int     = 20 
Variable Name DataType  = Value

string 
boolean
float 
byte
rune - single character
float64
complex64

We will go one by one.


============= 
day2.go file

package main
import "fmt"

function main() {
    var name string = "Jegan"
    var age int = 32
    fmt.Println("Name: ", name)
    fmt.Println("Age: ", age)

    // next variable declaring option
    var city ="Chennai"
    fmt.Println("City: ", city)
    // Next option of variable declaring
    name1 :=  "Jegan"
    age1 := "32"
    const pi = 3.14
    fmt.Println("PI value is ", pi)
    // pi =1234 // this will throw error as already declared in constant.
    // in python we will not have separate declaration like a constant language
}

===============
To run the above file, use 
>> go run day2.go
To build the file.
>> go build day2.go
once build is done. then we can run with the filename itself.
>> day2.exe

============
For formatting in go programming language is
fmt.Println("Name: %s and age : %d", name, age)
If the variable to be printed in middleware of the text then formatting will be used. 

Ex: 
// "This is a day2 test file"
// "This is a %s test file", filename
// "This is a ", filename, " test file"
============

go lang will be look like a combination of javascript and python programming for learning purpose.

## input example.

================
============ input.go===========

package main 
import ( 
        "fmt"
        "bufio"
        "os"
)
func main() {
    var name string; // this will allocate in memory 
    fmt.Println("Enter your name: ")
    fmt.Scanln(&name) // this will store in that name variable in memory. this is like a container which will store in that variable. this is like a input function in python.
    fmt.Scanf("Hello %s", &name)
    fmt.Println("Hello ", name)
}

================
To run the above program.
>> go run input.go
output 
''' Enter your name : Jegan raj Kumar '''
''' Jegan'''
Accepts until the single space input only.


To accept the string with space. bufio package.

================
=== file name: "input1.go" >> in this prgoram we are planning to give input with spaces========

package main 
import ("fmt" 
        "os"
        "bufio"
        )
func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Println("Enter your name")
    name, _ := reader.ReadString('\n')
    fmt.Println("Hello", name)

    var a, b string;
    fmt.Println("Enter the value of a and b")
    fmt.Scanf("%s and second word %s ", &a , &b)
    fmt.Println("a value is %s and  b value is %s", a, b)
}

buffer is like temporary storing data and displaying next.
===============

### Loops concept

filename : "loop.go"

'''
package main 

import "fmt"

func main() {
    var age int = 18 
    if age >= 18 {
        fmt.Println("Eligible to vote")
    } else {
        fmt.Println("not Eligible)
    }

    for i :=1; i <= 10; i ++ {
        fmt.Println(i)
    }

    // Below piece of code is like a WHILE loop condition.
    var itr int = 0
    for itr <= 10 {
        fmt.Println(itr)
        itr ++;
    }
    // Ifinite looop
    for {
        fmt.Println("Running...")
    }
}
========
always keep in mind {} is mandatory with proper spaces in Go programmin language.
No while loop concept in Go programming language.
