# bugsworld-asm

Custom assembly-ish language compiler for the bytecode used by the OSU CSE BugsWorld project.

The project description can be found [here](http://web.cse.ohio-state.edu/software/2231/web-sw2/readings/bugs-world.html).

## Background

BugsWorld is a project in the OSU CSE curriculum. Part of it includes building a compiler in java for a simple programming language. The compiler outputs bytecode to be interpreted by an interpreter that we also build. By compiling several test programs, I reverse-engineered the bytecode structure without looking at any future assignment descriptions.

`bugsworld-asm` is a compiler for my own custom assembly-like language that targets the same bytecode format used in BugsWorld. Compiler-time optimization is out of scope for this project.

## Bytecode reference

| bytecode sequence | meaning        |
| ----------------- | -------------- |
| `0`               | move           |
| `1`               | turnleft       |
| `2`               | turnright      |
| `3`               | infect         |
| `4`               | skip           |
| `5`               | end program    |
| `6`               | jump           |
| `7`               | next-is-empty  |
| `8`               |                |
| `9`               | next-is-wall   |
| `10`              |                |
| `11`              | next-is-friend |
| `12`              |                |
| `13`              | next-is-enemy  |
| `14`              |                |
| `15`              | random         |
| `16`              | true           |

Jump operations use the numeric value of the next bytecode as the target address.
Conditions like `next-is-empty` and `random` funciton like a jump, but will only perform the jump if the condition is false.
