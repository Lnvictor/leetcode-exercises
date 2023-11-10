public class Solution {
    public int ThirdMax(int[] nums) 
    {
        int[] distinctArray = nums.Distinct().ToArray();
        Array.Sort(distinctArray);
        return distinctArray.Length >= 3 ? distinctArray[distinctArray.Length - 3] : distinctArray[distinctArray.Length - 1] ;
    }
}
