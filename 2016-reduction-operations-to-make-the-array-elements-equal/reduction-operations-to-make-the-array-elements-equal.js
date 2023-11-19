/**
 * @param {number[]} nums
 * @return {number}
 */
var reductionOperations = function(nums) {
     let steps = 0;
        nums.sort((a, b) => a - b); // Sort in ascending order
        let ele = nums[0];
        for (let i = 0; i < nums.length; i++) {
            if (ele < nums[i]) {
                steps += nums.length - i;
                ele = nums[i];
            }
        }
        return steps;
};
