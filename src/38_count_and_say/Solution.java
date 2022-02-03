class Solution {
    public String countAndSay(int n) {
        if (n == 1) return "1";

        String val = countAndSay(n - 1);
        String ans = "";
        char current = val.charAt(0);
        int ocurrences = 0;

        for (char c : val.toCharArray()){
            if(Character.compare(c, current) != 0){
                ans += ocurrences; ans += current;
                current = c;
                ocurrences = 1;
            }
            else{
                ocurrences++;
            }
        }


        ans += ocurrences;
        ans += current;


        return ans;
    }
}