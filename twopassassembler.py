Aim: Implementations of two pass Assembler.
Code:
import sys

# Function to check if the instruction is a pseudo-opcode
def chk_pot(arr):
    global p, k, st
    for i in range(len(arr)):
        if arr[i] == pot[0][0]:
            st[p][0] = arr[i - 1]
            st[p][1] = "0"
            st[p][2] = "1"
            st[p][3] = "R"
            p += 1
            return True
        elif arr[i] == pot[1][0]:
            st[p][0] = arr[i - 1]
            st[p][1] = str(k)
            st[p][2] = "4"
            st[p][3] = "R"
            p += 1
            k += 4
            return True
        elif arr[i] == pot[3][0]:
            st[p][0] = arr[i - 1]
            st[p][1] = str(k)
            st[p][2] = "4"
            st[p][3] = "R"
            p += 1
            k = k + 4
            return True
        elif arr[i] == pot[4][0]:
            st[p][0] = ""
            st[p][1] = ""
            st[p][2] = "4"
            st[p][3] = "R"
            return True
    return False

# Function to check and write machine instructions
def chk_mot(arr, bw):
    global mot
    if len(arr) >= 2: # Check if arr has at least 2 elements
        for j in range(len(mot)): # Iterate over machine instructions
            if arr[0] == mot[j][0]: # Check if the instruction matches the opcode
                bw.write(arr[0] + "\t" + arr[1] + ", " + "(0,15)\n")
                bw.write('\n')
                print("Machine instruction written:", arr[0] + "\t" + arr[1] + ", " + "(0,15)")
                return # Exit the function after writing the machine instruction

if __name__ == "__main__":
    # Assign input file path directly
    input_file_path = 'C:/Users/asus/.ipynb_checkpoints/input.txt'
    # Open input and output files
    with open(input_file_path, "r") as file:
        lines = file.readlines()
    with open("output.txt", "w") as file:
        # Initialize variables
        st = [["" for _ in range(4)] for _ in range(4)]
        err = ["" for _ in range(4)]
        bt1 = ["" for _ in range(14)]
        bt = [["" for _ in range(3)] for _ in range(16)]
        mot = [
            ["L", "01011000", "04", "E2"],
            ["A", "01011010", "04", "RX"],
            ["ST", "01010000", "04", "RX"]
        ]
        pot = [
            ["START", "PA", "START"],
            ["USING", "PA", "USING"],
            ["DC", "PA", "DC"],
            ["DS", "PA", "DS"],
            ["END", "PA", "END"]
        ]
        fwr = None
        p = 0
        k = 0
        # Process each line of input
        for line in lines:
            # Remove unwanted characters like square brackets and newlines
            line = line.strip().replace('[', '').replace(']', '').replace('\n', '')
            instructions = line.split() # Split line into individual instructions
            for instruction in instructions:
                arr = instruction.split() # Split instruction into its components
                if not chk_pot(arr):
                    chk_mot(arr, file)

    # Print the contents of input.txt
    print("Contents of input file:")
    with open(input_file_path, "r") as file:
        for line in file:
            print(line.strip())

    # Print the contents of output.txt
    print("\nContents of output file:")
    with open("output.txt", "r") as file:
        for line in file:
            print(line.strip())

Contents of input file:
Input.txt
PRG START 0
USING 0,15
END
L1 FOUR AIFNE A 1-F2
ST 1 TEMP
FOUR DC F4
FIVE DC F5
TEMP DS L4
Contents of output file:
Output:
A1,-(0,15)
1-(0,15)
1,-(0,15)
ST 1-(0,15)
L1,16(0,15)
A 1,20(0,15)
PP
1,28(0,15)
ST 1,24(0,15)
