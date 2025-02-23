// Copyright 2025 Fidesinnova.

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

//     http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>

// Function to clean up the GDB output file
void cleanupTraceFile(const std::string& filename) {
    std::ifstream inFile(filename);
    if (!inFile) {
        std::cerr << "Failed to open trace file for cleaning." << std::endl;
        return;
    }

    std::vector<std::string> lines;
    std::string line;
    bool isBlockActive = false;
    std::string currentBlock;
    bool initialRegistersProcessed = false;

    // Read the file line by line
    while (std::getline(inFile, line)) {
        // Handle the initial register dump (before the first instruction)
        if (!initialRegistersProcessed && (line.find("x") == 0 || line.find("sp") == 0 || line.find("pc") == 0 ||
                                          line.find("cpsr") == 0 || line.find("fpsr") == 0 || line.find("fpcr") == 0)) {
            lines.push_back(line + "\n");
            continue;
        }

        // Start a new block when an instruction line is found
        if (line.find("=>") != std::string::npos) {
            if (isBlockActive) {
                // Save the current block
                lines.push_back(currentBlock);
                lines.push_back("-----------------------------------------------------\n"); // Separator between blocks
            }
            // Start a new block
            currentBlock = line + "\n";
            isBlockActive = true;
            initialRegistersProcessed = true; // Mark that initial registers have been processed
        }
        // Add register lines to the current block
        else if (line.find("x") == 0 || line.find("sp") == 0 || line.find("pc") == 0 ||
                 line.find("cpsr") == 0 || line.find("fpsr") == 0 || line.find("fpcr") == 0) {
            if (isBlockActive) {
                currentBlock += line + "\n";
            }
        }
    }

    // Save the last block if it exists
    if (isBlockActive) {
        lines.push_back(currentBlock);
    }
    inFile.close();

    // Write the cleaned lines back to the file
    std::ofstream outFile(filename);
    if (!outFile) {
        std::cerr << "Failed to open trace file for writing cleaned data." << std::endl;
        return;
    }

    for (const auto& cleanedLine : lines) {
        outFile << cleanedLine;
    }
    outFile.close();
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <program_to_execute>" << std::endl;
        return 1;
    }

    std::string program = argv[1];
    std::string gdbCommand = "gdb --batch --command=gdb_commands.txt " + program + " > /dev/null 2>&1";
    std::string outputFile = "execution_trace.txt";

    // Create a GDB command file
    std::ofstream gdbCommands("gdb_commands.txt");
    if (!gdbCommands) {
        std::cerr << "Failed to create GDB command file." << std::endl;
        return 1;
    }

    gdbCommands << "set logging file " << outputFile << std::endl;
    gdbCommands << "set logging overwrite on" << std::endl; // Overwrite the file
    gdbCommands << "set logging on" << std::endl;
    gdbCommands << "break main" << std::endl; // Set a breakpoint at main
    gdbCommands << "run" << std::endl; // Run the program until main
    gdbCommands << "info registers" << std::endl; // Capture registers before the first instruction
    gdbCommands << "while $pc < main + 40" << std::endl; // Stop after main's assembly block
    gdbCommands << "info registers" << std::endl; // Log registers
    gdbCommands << "x/i $pc" << std::endl; // Log the current instruction
    gdbCommands << "stepi" << std::endl; // Step to the next instruction
    gdbCommands << "end" << std::endl;
    gdbCommands << "set logging off" << std::endl;
    gdbCommands << "quit" << std::endl;
    gdbCommands.close();

    // Execute the GDB command and suppress terminal output
    int result = std::system(gdbCommand.c_str());
    if (result != 0) {
        std::cerr << "GDB execution failed." << std::endl;
        return 1;
    }

    // Clean up the trace file
    cleanupTraceFile(outputFile);

    std::cout << "Execution trace saved and cleaned in " << outputFile << std::endl;
    return 0;
}