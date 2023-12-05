def find_serving_order(n, priorities, k):
  count = 0

  while True:
    served_order = priorities.pop(0)
    count += 1

    if served_order == max(priorities):
      break

    priorities = [priority + 1 for priority in priorities]

  return count + k


# Input
n = int(input())
priorities = list(map(int, input().split()))
k = int(input())

# Output
result = find_serving_order(n, priorities, k)
print(result)
