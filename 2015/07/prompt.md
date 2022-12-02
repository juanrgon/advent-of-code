## --- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and <a href="https://en.wikipedia.org/wiki/Bitwise_operation">bitwise logic gates</a>!  Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a <a href="https://en.wikipedia.org/wiki/16-bit">16-bit</a> signal (a number from `0` to `65535`).  A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations.  A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: `x AND y -> z` means to connect wires `x` and `y` to an AND gate, and then connect its output to wire `z`.

For example:

- `123 -> x` means that the signal `123` is provided to wire `x`.
- `x AND y -> z` means that the <a href="https://en.wikipedia.org/wiki/Bitwise_operation#AND">bitwise AND</a> of wire `x` and wire `y` is provided to wire `z`.
- `p LSHIFT 2 -> q` means that the value from wire `p` is <a href="https://en.wikipedia.org/wiki/Logical_shift">left-shifted</a> by `2` and then provided to wire `q`.
- `NOT e -> f` means that the <a href="https://en.wikipedia.org/wiki/Bitwise_operation#NOT">bitwise complement</a> of the value from wire `e` is provided to wire `f`.

Other possible gates include `OR` (<a href="https://en.wikipedia.org/wiki/Bitwise_operation#OR">bitwise OR</a>) and `RSHIFT` (<a href="https://en.wikipedia.org/wiki/Logical_shift">right-shift</a>).  If, for some reason, you'd like to **emulate** the circuit instead, almost all programming languages (for example, <a href="https://en.wikipedia.org/wiki/Bitwise_operations_in_C">C</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_Operators">JavaScript</a>, or <a href="https://wiki.python.org/moin/BitwiseOperators">Python</a>) provide operators for these gates.

For example, here is a simple circuit:

```
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
```

After it is run, these are the signals on the wires:

```
d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
```

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to **wire `a`**?