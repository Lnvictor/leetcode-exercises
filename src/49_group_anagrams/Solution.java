import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> ans = new HashMap<>();
        
        for (int i = 0; i < strs.length; i++){
            String s = strs[i];
            char[] helper = s.toCharArray();
            Arrays.sort(helper);
            String key = String.valueOf(helper);
            
            if(!ans.containsKey(key)) ans.put(key, new ArrayList<>());
            
            ans.get(key).add(s);
        }
        
        return new ArrayList(ans.values());
    }
}