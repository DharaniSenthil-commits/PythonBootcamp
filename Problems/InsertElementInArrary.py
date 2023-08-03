N = int(input())
List = list(map(int, input().split()))
Index = int(input())
Value = int(input())
List.insert(Index - 1, Value)
for i in List:
    print(i, end=" ")
