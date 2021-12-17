n = int(input("Size of The Game:\n"))
x = []
y = []
for i in range(n ** 2):
    y.append(i)
    if len(y) == n:
        a = y[:]
        x.append(a)
        y.clear()
z = []
for i in x:
    for j in i:
        b = len(str(n ** 2 - 1))
        if len(str(j)) < b:
            z.append(str(j) + " " * (b - len(str(j))))
            i = z[:]
        else:
            z.append(str(j))
            i = z[:]
    z.clear()
    print(' '.join([str(elem) for elem in i]))
l = x[:]
def move_X():
    g = []
    move = int(input("Player 1 turn-->\n"))
    for i in x:
        g.extend(i)
    if g[move] == "X":
        print("You have made this choice before\n")
    elif g[move] == "O":
        print("The other player select this cell before\n")
    for i in x:
        for j in i:
            if j == move:
                i[i.index(j)] = "X"
    for i in x:
        for j in i:
            b = len(str(n ** 2 - 1))
            if len(str(j)) < b:
                z.append(str(j) + " " * (b - len(str(j))))
                i = z[:]
            else:
                z.append(str(j))
                i = z[:]
        z.clear()
        print(' '.join([str(elem) for elem in i]))
def move_O():
    g = []
    move = int(input("Player 2 turn-->\n"))
    for i in x:
        g.extend(i)
    if g[move] == "O":
        print("You have made this choice before\n")
    elif g[move] == "X":
        print("The other player select this cell before\n")
    for i in x:
        for j in i:
            if j == move:
                i[i.index(j)] = "O"
    for i in x:
        for j in i:
            b = len(str(n ** 2 - 1))
            if len(str(j)) < b:
                z.append(str(j) + " " * (b - len(str(j))))
                i = z[:]
            else:
                z.append(str(j))
                i = z[:]
        z.clear()
        print(' '.join([str(elem) for elem in i]))
def winner_vertical_X():
    l = 0
    k = 0
    g = []
    for i in x:
        g.extend(i)
    for i in g:
        b = []
        b = g[l::n]
        l += 1
        if l == n - 1:
            break
        for j in b:
            if j == "X":
                k += 1
        if k == len(b):
            print("Winner: X")
            return "Winner: X"
def winner_vertical_O():
    l = 0
    k = 0
    g = []
    for i in x:
        g.extend(i)
    for i in g:
        b = []
        b = g[l::n]
        l += 1
        if l == n - 1:
            break
        for j in b:
            if j == "O":
                k += 1
        if k == len(b):
            print("Winner: O")
            return "Winner: O"
def winner_horizontal_X():
    for i in x:
        if i.count("X") == n:
            print("Winner: X")
            return "Winner: X"
def winner_horizontal_O():
    for i in x:
        if i.count("O") == n:
            print("Winner: O")
            return "Winner: O"
def winner_diagonal_X():
    k = 0
    g = []
    for i in x:
        g.extend(i)
    b = []
    b = g[::n + 1]
    for j in b:
        if j == "X":
            k += 1
    if k == len(b):
        print("Winner: X")
        return "Winner: X"
def winner_diagonal_O():
    k = 0
    g = []
    for i in x:
        g.extend(i)
    b = []
    b = g[::n + 1]
    for j in b:
        if j == "O":
            k += 1
    if k == len(b):
        print("Winner: O")
        return "Winner: O"
def winner_diagonal_reverse_X():
    k = 0
    g = []
    for i in x:
        g.extend(i)
    b = []
    b = g[n - 1:-1:n - 1]
    for j in b:
        if j == "X":
            k += 1
    if k == len(b):
        print("Winner: X")
        return "Winner: X"
def winner_diagonal_reverse_O():
    k = 0
    g = []
    for i in x:
        g.extend(i)
    b = []
    b = g[n - 1:-1:n - 1]
    for j in b:
        if j == "O":
            k += 1
    if k == len(b):
        print("Winner: O")
        return "Winner: O"
def no_winner():
    g = []
    k = 0
    for i in x:
        g.extend(i)
    for i in g:
        if type(i) == str:
            k += 1
    if k == len(g):
        print("No winner")
        return "No winner"
while True:
    try:
        move_X()
    except:
        pass
    if winner_vertical_X() == "Winner: X" or winner_horizontal_X() == "Winner: X" or winner_diagonal_X() == "Winner: X" or winner_diagonal_reverse_X() == "Winner: X" or no_winner() == "No winner":
        break
    try:
        move_O()
    except:
        pass
    if winner_vertical_O() == "Winner: O" or winner_horizontal_O() == "Winner: O" or winner_diagonal_O() == "Winner: O" or winner_diagonal_reverse_O() == "Winner: O" or no_winner() == "No winner":
        break