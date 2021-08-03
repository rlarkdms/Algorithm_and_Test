#정렬된 두 묶음의 숫자 카드가 있음
# 각 숫자 카드의 수를 A,B라 하면 보통 두 묶음을 합치려면 A+B
# 그래서 구하는 건 여러장의 묶음이 있을 때 비교 하는 방법.
# (10+20)+(30+40)=100 ???
# -> (10+20)=30 -> (30+40) =70 ->100?
# 아니 문제가 이상한데 뭐지ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
#최소 비교 횟수
# 10 20 30 40->
# 10+20=30 30+30 =60 60+40=100 ->190 아니 이거 무조건 이렇게 가는 건가?
#10+20=30 30+40=70 30+70=100  ->200
#40+10 =50 20+30=50 50+50=100 ->200
# 예제 케이스가 너무 없어...ㅜㅠ 이게 맞는지 알려면 최소한 2개의 케이스는 필요한데...
# 1개일 때 고려하고
import heapq
N=int(input())
arr=[]
#우선순위 큐를 할 줄 알아야한다는데... 말이 진짜...

for i in range(N):
    arr.append(int(input()))

#새로운 값이 생겼는데도 정렬이 제일 빠른 알고리즘이 이문제에서는 제일인데
#결국에는 힙sort가 시간이 얼마 안걸린다는 얘기인데...
#아니 힙정렬인데 이정도면 어쩌란 말이지...? 음...? 도대체 어떻게 해야 빨라질까?

#이번 기회에 힙정렬을 배우자 최대힙과 최소힙
#힙정렬을 사용하는 이유가 어느정도 정렬이 되어있는 경우에는 힙정렬을 사용하는게 가장 빠르게 때문이다.
#arr.sort(reverse=True)
#힙정렬 잘 모르겠다. 내일 다시 공부하자 2시간동안 잡고 있었더니 대가리 빵꾸 나겠다.
# def heapify(unsorted, index, heap_size):
#     largest = index
#     left_index = 2 * index + 1
#     right_index = 2 * index + 2
#     if left_index < heap_size and unsorted[left_index] < unsorted[largest]:
#         largest = left_index
#     if right_index < heap_size and unsorted[right_index] < unsorted[largest]:
#         largest = right_index
#     if largest != index:
#         unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
#         return heapify(unsorted, largest, heap_size)
#

# def heap_sort(unsorted):
#     n = len(unsorted)
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(unsorted, i, n)
#     for i in range(n - 1, 0, -1):
#         unsorted[0], unsorted[i] = unsorted[i], unsorted[0]#여기가 있으면 무조건 이중문을 돌아서 시간 초과가 남.
#         heapify(unsorted, 0, i)
#     return unsorted
# standard=0
# sum_value=0

heapq.heapify(arr)
standard=0
sum_value=0
while True:
    if len(arr)<2:
        break
    a=heapq.heappop(arr)
    b=heapq.heappop(arr)
    standard=a+b
    sum_value+=standard
    heapq.heappush(arr,standard)
# #아 이거 '0'때문이잖아
# while True:
#     if len(arr)<2:
#         break
#     arr=heap_sort(arr)#? 이게 오래걸릴 일이 없는데? 왜지? 이유를 아예 모르겠네;;뭐지?
#     standard=arr.pop()+arr.pop()
#
#     sum_value+=standard
#     arr.append(standard)
#

print(sum_value)
