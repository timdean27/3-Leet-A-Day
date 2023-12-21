def merge(nums1, m, nums2, n):
    for i in range(m, m + n):
        nums1[i] = nums2[i - m]

    # Bubble sort the merged portion of nums1
    for i in range(m + n):
        for j in range(0, m + n - i - 1):
            if nums1[j] > nums1[j + 1]:
                nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]

    return nums1

# Example usage:
result = merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
print(result)
