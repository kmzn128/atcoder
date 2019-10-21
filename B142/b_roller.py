N, K = map(int, input().split())
people = list(map(int, input().split()))
def eligible_roller(N, K, p):
    return len(list(filter(lambda x: x >= K, people)))

print(eligible_roller(N, K, people))