# Trace Execution Tool
## Prerequisites
* GCC Compiler: Ensure you have the GCC compiler installed on your system.

* C++ Program: You should have a C++ program (program.cpp) that you want to trace.

## Compile and Run
### Step 1: Save the Updated C++ Program
Make sure your C++ program (program.cpp) is saved and ready to be compiled.

### Step 2: Compile the Trace Execution Tool
First, compile the `trace_execution` tool using the following command:

```
g++ -o trace_execution trace_execution.cpp
```
This will generate an executable named `trace_execution`.

### Step 3: Compile Your C++ Program with Debugging Symbols
Next, compile your C++ program (`program.cpp`) with debugging symbols enabled. This allows the tracer to capture detailed information about the program's execution.

```
g++ -g -o program program.cpp
```
This will generate an executable named `program` with debugging symbols included.

### Step 4: Run the Tracer
Now, run the `trace_execution` tool with your compiled program as an argument:

```
./trace_execution ./program
```
This will execute your program and generate an execution trace.

### Step 5: Check the Output
The execution trace will be saved in a file named `execution_trace.txt`. You can open this file to review the cleaned output and analyze the flow of your program.
