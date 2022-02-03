class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> repr = new HashMap<>();
        
        repr.put('I', 1);
        repr.put('V', 5);
        repr.put('X', 10);
        repr.put('L', 50);
        repr.put('C', 100);
        repr.put('D', 500);
        repr.put('M', 1000);
        
        
        int partial = 0;
        char[] charArr = s.toCharArray();
            
            
        for (int i = 0; i < charArr.length; i++){ 
            int curr = repr.get(charArr[i]);
            
            if (i > 0 && repr.get(charArr[i - 1]) < curr){
                int pr = repr.get(charArr[i - 1]);
                partial-= pr;
                partial += curr -pr;
            }
            else{
                partial += curr;
            }
        }
        
        return partial;
        
    }
}