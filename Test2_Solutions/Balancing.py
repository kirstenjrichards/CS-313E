def generate_pd(n):
    if n % 2 == 1 or n == 0:
        return []

    ans = []
    backtrack(ans, n)
    return ans

def backtrack(ans, n, curr_balanced = None, num_left = 0, num_right = 0):
    if curr_balanced == None:
        curr_balanced = []
    
    if len(curr_balanced) == n:
        ans.append("".join(curr_balanced))
        return

    if num_left < n // 2:
        curr_balanced.append("p")
        backtrack(ans, n, curr_balanced, num_left+1, num_right)
        curr_balanced.pop()

    if num_right < num_left:
        curr_balanced.append("d")
        backtrack(ans, n, curr_balanced, num_left, num_right+1)
        curr_balanced.pop()

def main():
    n = int(input())

    print(generate_pd(n))

if __name__ == "__main__":
    main()