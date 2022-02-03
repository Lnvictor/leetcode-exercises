class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numsMap = new HashMap<Integer, Integer>();
        int[] ans = new int[2];

        for (int i = 0; i < nums.length; i++){
            numsMap.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++){
            int toSeek = target - nums[i];
            if (numsMap.containsKey(toSeek)){
                int index = numsMap.get(toSeek);

                if (index != i) {
                    ans[0] = i;
                    ans[1] = index;

                    return ans;
                }
            }
        }
        return new int[0];
    }
}