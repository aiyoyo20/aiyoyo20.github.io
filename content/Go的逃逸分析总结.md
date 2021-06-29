Title: Go的逃逸分析
Date: 2017-11-15 15：29
Category: Note
Tags: go


# Go的逃逸分析

编译型语言，在编译代码的时候，会根据情况选择将变量放在栈或堆上。在栈上分配的变量可以随着栈的退出而释放，在堆上的变量就需要通过垃圾回收或者程序员手动释放。

根据官方文档[Frequently Asked Questions (FAQ) - The Go Programming Language](https://golang.org/doc/faq#stack_or_heap) 中说的，就是程序员不用去主动关心到底变量是分配在栈上还是堆上。`Go` 在编译时会进行逃逸分析帮你确定变量到底是放在哪里。

大致规则就是：函数中的本地变量和参数会被分配在栈上，如果变量非常大，则很有可能会被分配在堆上。对于那些通过地址引用的变量，如果函数返回后，这个变量还会被继续引用，或者编译器不能确定这个变量后续还会不会被引用，那么这个变量就会分配在堆上。

# 查看逃逸

查看代码中哪些变量逃逸到了堆，我们可以通过 `go tool compile -m -l` 命令查看，`-m` 会打印出包括逃逸分析在内的优化信息。 `-l`不是必需的参数，它表示禁止编译器进行对代码进行内联优化，这样可以让优化信息输出更简洁。

比如代码：

	package main
	
	func foor(a int) *int {
		b := 3 + a
		return &b
	}
	
	func main() {
		println(foor(2))
	}

输出为：

	x.go:5:9: &b escapes to heap
	x.go:4:11: moved to heap: b

我们可以知道，变量 `b` 逃逸到了堆上，而 `a` 没有，符合前文讲的规则。


# 逃逸缺陷

`Go`虽然会自动判断变量的分配位置，但是毕竟不那么直观，有些情况下让人比较迷惑，很多认为不会逃逸的变量结果逃逸到了堆。这一段根据网上的资料，摘录了几种逃逸分析的缺陷。

## 闭包调用

	var y int  // BAD: y escapes
	func(p *int, x int) {
	    *p = x
	}(&y, 42)
	
	
	x := 0  // BAD: x escapes
	defer func(p *int) {
	    *p = 1
	}(&x)

原因是闭包并不进行逃逸分析，因此直接分配了

## ...参数逃逸（Go1.5已修复）


	func noescape(y ...interface{}) {
	}
	
	func main() {
	    x := 0 // BAD: x escapes
	    noescape(&x)
	}

根据 [cmd/gc: pessimistic escape analysis · Issue #7710 · golang/go](https://github.com/golang/go/issues/7710)，可以看到该问题已经在 `Go 1.5` 版本修复。

自己测试输出的逃逸信息（Go 1.9）：

	x.go:3:20: noescape y does not escape
	x.go:8:11: main &x does not escape
	x.go:8:11: main &x does not escape
	x.go:8:10: main ... argument does not escape


## 间接赋值








