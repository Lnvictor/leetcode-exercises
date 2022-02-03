import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        if(nums.length == 0) return new ArrayList<>();
        Arrays.sort(nums);
        
        Map<String, List<Integer>> resp = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++){
            for (int k = 0; k < nums.length; k++){
                int difference = -1 * (nums[i] + nums[k]);
                int indexOfThird = Arrays.binarySearch(nums, difference);
                
                if (indexOfThird >=0 && i != k && i!= indexOfThird && k != indexOfThird){
                    int[] temp = {nums[i], nums[k], nums[indexOfThird]};
                    Arrays.sort(temp);
                    String key = ("" + temp[0]) + temp[1] + temp[2];

                    if(!resp.containsKey(key)){
                        List<Integer> l = new ArrayList<>();
                        l.add(temp[0]);
                        l.add(temp[1]);
                        l.add(temp[2]);
                        resp.put(key, l);
                    }
                }
            }
        }
        
        return new ArrayList(resp.values());
    }
}