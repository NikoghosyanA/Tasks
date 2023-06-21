from sys import maxsize as m

figures = {
    "11111": "I",
    "01111": "O",
    "01101": "C",
    "00101": "L",
    "00110": "H",
    "01100": "P"
}

n = int(input())
matrix = []

# area corners
c_tl, c_tr = (m, m), (-m, m)
c_bl, c_br = (m, -m), (-m, -m)

for y in range(n):
    line = input()
    row = []

    for x, char in enumerate(line):

        # align figure area
        if char == "#":
            if x <= c_tl[0] and y <= c_tl[1]:
                c_tl = (x, y)  # top left corner
            if x >= c_tr[0] and y <= c_tr[1]:
                c_tr = (x, y)  # top right corner
            if x <= c_bl[0] and y >= c_bl[1]:
                c_bl = (x, y)  # bottom left corner
            if x >= c_br[0] and y >= c_br[1]:
                c_br = (x, y)  # bottom right corner

        row.append(char)
    matrix.append(row)

# perimeter by "top left -> bottom right"
p_tl_br = abs(c_tl[0] - c_br[0]) + abs(c_tl[1] - c_br[1])

# perimeter by "top right -> bottom left"
p_tr_bl = abs(c_tr[0] - c_bl[0]) + abs(c_tr[1] - c_bl[1])

# area start & end by tl -> br
if p_tl_br >= p_tr_bl:
    x_s, x_e = c_tl[0], c_br[0]
    y_s, y_e = c_tl[1], c_br[1]

# area start & end by tr -> bl
else:
    x_s, x_e = c_bl[0], c_tr[0]
    y_s, y_e = c_tr[1], c_bl[1]

# solidness
overall, top, left, right, bottom = [1] * 5

for y in range(y_s, y_e + 1):
    for x in range(x_s, x_e + 1):
        if matrix[y][x] == ".":
            overall = 0

            if y == y_s:
                top = 0  # top side
            if x == x_s:
                left = 0  # left side
            if x == x_e:
                right = 0  # right side
            if y == y_e:
                bottom = 0  # bottom side

template = f"{overall}{top}{left}{right}{bottom}"
figure = figures.get(template, "X")

print(figure)
