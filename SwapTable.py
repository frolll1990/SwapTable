from prettytable import PrettyTable
import csv

def append(rr):
    f = open("file_with_tables.txt", "a+")
    f.write("\n" + rr + "\n")
    f.close

def t_swap(w, x, y, z):
    summ = w * x * y * z
    return summ


vol = float(input("Enter Volume of position\n:"))

c_size = float(input('Enter Contract size\n:')) /100
#print(c_size)

quizzz = str(input("Is Base currency equal to deposit currency\nY/N\n:"))

convers = 0.0

if quizzz == "n" or quizzz == "N":
    convers = float(input("Enter Bid for Sell or Ask for Buy\n:"))

else:
    convers = float(1)

swaps = []

quizz = int(input("Enter swaps manually orrrr read it from a file?\n"
                  "for Manualy enter 1\n"
                  "for reading the file enter 2\n:"))

if quizz == 1:
    for i in range(19):
        zz = float(input("SP" + str(i+1)+":    "))
        swaps.append(zz)
    print(swaps)

elif quizz == 2:
    pathh = str(input("Enter full path to your file\n:"))

    with open(pathh, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        swaps = list(reader)

    swaps = swaps[0]


total_s = []
for x in swaps:
    total_s.append(t_swap(float(x), vol, convers, c_size))

st = PrettyTable()

st.field_names = ["Swap Counter", "Swap", "Swap in money", "Total Swap"]
st.add_row(["SP0", 0.0, 0.0, 0.0])
st.add_row(["SP1", swaps[0], round(total_s[0], 8), total_s[0]])
st.add_row(["SP2", swaps[1], round(total_s[1], 8), round(sum(total_s[0:2]), 8)])
st.add_row(["SP3", swaps[2], round(total_s[2], 8), round(sum(total_s[0:3]), 8)])
st.add_row(["SP4", swaps[3], round(total_s[3], 8), round(sum(total_s[0:4]), 8)])
st.add_row(["SP5", swaps[4], round(total_s[4], 8), round(sum(total_s[0:5]), 8)])
st.add_row(["SP6", swaps[5], round(total_s[5], 8), round(sum(total_s[0:6]), 8)])
st.add_row(["SP7", swaps[6], round(total_s[6], 8), round(sum(total_s[0:7]), 8)])
st.add_row(["SP8", swaps[7], round(total_s[7], 8), round(sum(total_s[0:8]), 8)])
st.add_row(["SP9", swaps[8], round(total_s[8], 8), round(sum(total_s[0:9]), 8)])
st.add_row(["SP10", swaps[9], round(total_s[9], 8), round(sum(total_s[0:10]), 8)])
st.add_row(["SP11", swaps[10], round(total_s[10], 8), round(sum(total_s[0:11]), 8)])
st.add_row(["SP12", swaps[11], round(total_s[11], 8), round(sum(total_s[0:12]), 8)])
st.add_row(["SP13", swaps[12], round(total_s[12], 8), round(sum(total_s[0:13]), 8)])
st.add_row(["SP14", swaps[13], round(total_s[13], 8), round(sum(total_s[0:14]), 8)])
st.add_row(["SP15", swaps[14], round(total_s[14], 8), round(sum(total_s[0:15]), 8)])
st.add_row(["SP16", swaps[15], round(total_s[15], 8), round(sum(total_s[0:16]), 8)])
st.add_row(["SP17", swaps[16], round(total_s[16], 8), round(sum(total_s[0:17]), 8)])
st.add_row(["SP18", swaps[17], round(total_s[17], 8), round(sum(total_s[0:18]), 8)])
st.add_row(["SP19", swaps[18], round(total_s[18], 8), round(sum(total_s[0:]), 8)])

print(st)
append(str(st))
ex=input("\nTABLE SAVED TO file_with_table.txt\n\n TO FINISH PRESS ENTER")