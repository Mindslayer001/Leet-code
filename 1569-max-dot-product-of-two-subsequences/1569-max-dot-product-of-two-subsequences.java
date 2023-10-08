public class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        int[] current = new int[n + 1], previous = new int[n + 1];
        Arrays.fill(current, Integer.MIN_VALUE);
        Arrays.fill(previous, Integer.MIN_VALUE);

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int curr_product = nums1[i - 1] * nums2[j - 1];
                current[j] = Math.max(Math.max(Math.max(curr_product, previous[j]), current[j - 1]), curr_product + Math.max(0, previous[j - 1]));
            }
            int[] temp = current;
            current = previous;
            previous = temp;
        }
        return previous[n];
    }
}