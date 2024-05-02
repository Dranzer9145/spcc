class TAC:
    def main(self):
        input_string = "a=b*c+d*e"
        s = list(input_string)
        ctr = 1
        print("Input:")
        print(''.join(s))
        print("\nTAC:")
        i = 0
        while i < len(s):
            if s[i] == "*":
                s[i] = "t" + str(ctr)
                print(s[i] + "=" + s[i - 1] + "*" + s[i + 1])
                s.pop(i + 1)
                s.pop(i - 1)
                ctr += 1
                i -= 1
            i += 1

        i = 0
        while i < len(s):
            if s[i] == "+":
                s[i] = "t" + str(ctr)
                print(s[i] + "=" + s[i - 1] + "+" + s[i + 1])
                s.pop(i + 1)
                s.pop(i - 1)
                ctr += 1
                i -= 1
            i += 1

        print(''.join(s))

if __name__ == "__main__":
    TAC().main()


Output:
Input:
a=b*c+d*e
TAC:
t1=b*c
t2=d*e
t3=t1+t2
a=t3
