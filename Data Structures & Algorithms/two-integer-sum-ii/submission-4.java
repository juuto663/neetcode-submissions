class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;

        while (l < r) {
            int localSum = numbers[l] + numbers[r];
            if (localSum == target) {
                return new int[] {l + 1, r + 1};
            } else if (localSum < target) {
                l++;
            } else if (localSum > target) {
                r--;
            }
        }
        return null;
    }
}
