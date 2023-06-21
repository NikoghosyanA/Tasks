from collections import defaultdict


def addEdge(u, v):
    graph[u].append(v)  # Добавляет дороги


def printAllPathsUtil(u, d, visited, path):
    global cc
    visited[u] = True
    path.append(u)
    if u == d:
        print(path)  # Все принты вместе взятые это все возможные дороги от u до d
        cc += 1  # А это их кол-во
    else:
        for i in graph[u]:
            if not visited[i]:
                printAllPathsUtil(i, d, visited, path)
    path.pop()
    visited[u] = False


def printAllPaths(s, d):
    visited = [False] * (n + 1)
    path = []
    printAllPathsUtil(s, d, visited, path)


graph = defaultdict(list)  # Место для хранения всех путей от i до j
n, m = map(int, input().split())
for _ in range(n - 1):
    a, b = map(int, input().split())
    addEdge(a, b)  # Добавляем уже известные пути
    addEdge(b, a)  # Чтобы дать понять что и обратно тоже можно ехать
dct = {}
lst = []
for _ in range(m):  # Создаем для каждого запроса кол-во путей доступных на данный момент (в виде словаря в dct)
    a = input()
    lst.append(a)  # Добавляем в список все действия для дальнейшего выполнения
    if a[0] == 'Q':
        cc = 0
        b, c = map(int, a[2:].split())
        printAllPaths(b, c)
        dct[a] = cc
cc = 0
for i in range(m):  # Проходим по списку действий
    a = lst[i]
    if a[0] == 'P':
        b, c = map(int, a[2:].split())
        addEdge(b, c)
        addEdge(c, b)  # Добавляем новый возможный путь
    if a[0] == 'Q':
        cc = 0
        b, c = map(int, a[2:].split())
        printAllPaths(b, c)  # Получаем все возможные пути с уже добавленными
        print(cc - dct[a])  # Получаем разницу в количестве путей до и после действий
