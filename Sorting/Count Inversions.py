# To count the no.of inversions we shave to check for the elements where it satisfies the condition: a[i] > a[j] where i < j then the inverstion should take place.
# So in merge sort while checking the condition in merge function we can increment count and return it.
# Then while passing elements in the mergeSort function count is incremented because previously stored count is added to the present count.
# When mergeSort is called in inversion function, the count is returned to main function.
class Solution:
    def merge(self, arr, left, mid, right):
        count = 0
        i = left
        j = mid + 1
        temp = []

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                count += (mid - i + 1)
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):
            arr[left + k] = temp[k]

        return count

    def mergeSort(self, arr, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2
        count = 0
        count += self.mergeSort(arr, left, mid)
        count += self.mergeSort(arr, mid + 1, right)
        count += self.merge(arr, left, mid, right)

        return count

    def inversionCount(self, arr):
        l = len(arr)
        return self.mergeSort(arr, 0, l - 1)


if __name__ == '__main__':
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        arr = list(map(int, input("Enter array elements: ").strip().split()))
        obj = Solution()
        print(f"Inversion count: {obj.inversionCount(arr)}")
