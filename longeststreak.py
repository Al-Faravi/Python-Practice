def longest_streak(nums):
    num_set = set(nums)
    visited = set()
    all_streaks = []
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            streak = []

            while current in num_set and current not in visited:
                streak.append(current)
                visited.add(current)
                current += 1

            all_streaks.append(streak)
            longest = max(longest, len(streak))

    return all_streaks, longest

# User Input
user_input = input("Enter numbers separated by spaces: ")
nums = list(map(int, user_input.strip().split()))

# Find all streaks and the longest one
streaks, max_len = longest_streak(nums)

# Output each streak and its length
print("\nConsecutive Sequences:")
for streak in streaks:
    print(" ".join(map(str, streak)), "=", len(streak))

# Final Result
print(f"\nLongest consecutive streak length: {max_len}")

