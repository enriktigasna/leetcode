// Beats 100% in memory

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(i in nums){
        tar = target - nums[i];
        tartar = nums.indexOf(tar)
        if(nums.includes(tar) && i != tartar){
            return [i, tartar];
        }
    }
};

