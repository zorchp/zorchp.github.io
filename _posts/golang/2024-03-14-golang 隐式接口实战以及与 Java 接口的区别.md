---
categories: [Golang]
tags: Golang Java
---

## 写在前面

最近在看 go语言学习指南-惯例模式与编程实战, 看到接口那块有点困惑了, 因为之前一直是学 C++的, 对于接口了解的不多, 通过 GPT 补补课. 

首先介绍一下接口, 接口其实是针对一组方法(行为)的抽象, 与抽象类有所不同(虽然在 C++中都是通过虚基类实现的), 抽象类是类层次结构的抽象, 反映了类之间的关系. 

>   下面的代码主要来自 go语言学习指南的 7.6节, 接口是类型安全的鸭子类型. 

## Java 的接口(显式声明)

Java 的接口通过 interface 来声明, 通过 implements 实现接口. 接口本质上也是一个类, 在这个类中给出了需要实现的方法的签名. 

但是 Java 的接口使用的是显式声明, 也就是说每次实现接口都要指定具体实现接口的类名. 来看代码

>   [Learn_Java/Class_Test/Interface_test at main · zorchp/Learn_Java](https://github.com/zorchp/Learn_Java/tree/main/Class_Test/Interface_test);

首先定义接口

```java
public interface Logic {
    String process(String data);
    public static void main(String[] args) {
    }
}
```

然后给出实现

```java
public class LogicImpl implements Logic {
    public String process(String data) {
        // Logic
        System.out.println(data);
        System.out.println("logic impl");
        return new String("nihao");
    }
}
```

客户端调用

```java
public class Client {
    private final Logic logic;

    public Client(Logic logic) {
        this.logic = logic;
    }
    public void program() {
        String data = new String("data is here ");
        this.logic.process(data);
        System.out.println("program()");
    }
}
```

调用接口的实现

```java
public class Interface_1 {
    public static void main(String[] args) {
        Logic logic = new LogicImpl();
        Client c = new Client(logic);
        c.program();

        // equals to :
        //  Client d = new Client(new LogicImpl());
        //  d.program();
    }
}
```



## golang 的接口(隐式接口)

使用隐式接口的话只需要实现, golang 中 实现接口的所有方法就隐式地实现了接口

```go
package main

import "fmt"

type LogicProvider struct{}

func (lp LogicProvider) Process(data string) string {
	fmt.Println(data)
	return ""
}

type Logic interface {
	Process(data string) string
}

type Client struct{ L Logic }

func (c Client) Program() {
	data := "hello"
	c.L.Process(data)
}

func main() {
	c := Client{
		L: LogicProvider{},
	}
	c.Program()
}
```

