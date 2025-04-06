package main

import (
    "syscall/js" // Biblioteca para interagir com JavaScript/DOM
)

func hello(this js.Value, args []js.Value) interface{} {
    name := args[0].String() // Pega o primeiro argumento passado pelo JS
    return "Parabens, " + name + "! (Go compilado webassembly + html )"
}

func main() {
    // Registra a função "hello" para ser chamada pelo JavaScript
    js.Global().Set("helloFromGo", js.FuncOf(hello))

    // Mantém o programa rodando
    <-make(chan struct{})
}