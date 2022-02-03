#include <vector>

class Solution {
public:
    int majorityElement(vector<int>& nums) { 
        
        if (nums.size() == 1) return nums[0];
        int toReturn = nums[0];
        map<int, int> myMap;
        
        for (int i = 0; i < nums.size(); i++){
            if (myMap.count(nums[i])){
                myMap[nums[i]] += 1;
            }
            else{
                myMap.insert(pair<int, int>(nums[i], 1));
            }
            
            if (myMap[toReturn] < myMap[nums[i]]){
                toReturn = nums[i];
            }
        }
        
        return toReturn;
    }
};