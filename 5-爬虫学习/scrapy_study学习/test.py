# a = [0, 1, 0, 3, 12]
# length1 = len(a)
# for each in a:
#     if each == 0:
#         a.remove(each)
# length2 = len(a)
# b = [0*(length2-length1)]
# a.extend(b)
# print(a)
a = list(map(int, input('请输入你的数组中间用空格隔开每一个数字').split(' ')))
k = int(input('请输入你想找第几个元素')) - 1
sorted_a = sorted(a, reverse=True)
print(sorted_a[k])


def tests(start, graph):
    n = len(graph)
    queue = []
    queue.append(start)
    vis = [False for _ in range(n)]
    vis[start] = True

    while queue:
        tem = queue.pop(0)
        print(tem, end=' ')
        for sub in graph[tem]:
            if not vis[sub]:
                queue.append(sub)
                vis[sub] = True


class Solution:
    def numSquares(self, n):
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        for i in range(n + 1):
            temp = i * i
            if temp <= n:
                if int((n - temp) ** 0.5) ** 2 + temp == n:
                    return 1 + (0 if temp == 0 else 1)
            else:
                break
        return 3


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSquares(13))
