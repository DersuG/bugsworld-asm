# bugsworld-asm

Custom assembly-ish language compiler for the bytecode used by the OSU CSE BugsWorld project.

The project description can be found [here](http://web.cse.ohio-state.edu/software/2231/web-sw2/readings/bugs-world.html).

## Background

BugsWorld is a project in the OSU CSE curriculum. Part of it includes building a compiler in java for a simple programming language. The compiler outputs bytecode to be interpreted by an interpreter that we also build. By compiling several test programs, I reverse-engineered the bytecode structure without looking at any future assignment descriptions.

`bugsworld-asm` is a compiler for my own custom assembly-like language that targets the same bytecode format used in BugsWorld. Compiler-time optimization is out of scope for this project.
