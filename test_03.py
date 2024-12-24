def longestIncreasingSubsequence(nums: list[int]) -> int:
    LIS = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    return max(LIS)


def main() -> None:
    print(longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print(longestIncreasingSubsequence([0, 1, 0, 3, 2, 3]))
    print(longestIncreasingSubsequence([7, 7, 7, 7, 7]))


if __name__ == '__main__':
    main()
