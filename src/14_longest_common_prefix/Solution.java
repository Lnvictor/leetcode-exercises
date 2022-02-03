class Solution {
    public String longestCommonPrefix(String[] strs) {
       if (strs.length == 0) return "";
        String ans = "";
        int i = 0;

        while(true){
            boolean isTrue = true;
            char temp;

            try {
                temp = strs[0].charAt(i);

                if(strs.length > 0){
                    for (int j = 1; j < strs.length; j++){
                        if (strs[j].charAt(i) != temp){
                            if (ans.isEmpty()) return "";
                            isTrue = false;
                        }
                    }
                }
            }catch (Exception e){
                break;
            }
        
            if(isTrue) ans += temp;
            i++;
        }

        return ans;
    }
}