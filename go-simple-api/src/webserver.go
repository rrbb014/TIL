package main

import (
    "io"
    "log"
    "net/http"
)

func main() {
    // Hello world, the web server 
    helloHandler := func(w http.ResponseWriter, req *http.Request) {
        io.WriteString(w, "Hello, World!\n")
    }

    http.HandleFunc("/hello", helloHandler)
    log.Println("Start webserver")
    log.Println("Try request to localhost:8080/hello")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
