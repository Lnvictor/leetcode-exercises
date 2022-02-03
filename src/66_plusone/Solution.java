class Solution {
    public int[] plusOne(int[] digits) {
        int index = digits.length - 1;
        
        do{
            if (digits[index] == 9) digits[index] = 0;
            else digits[index]++;
        }while(digits[index--] == 0 && index >= 0);
        
        
        if (digits[0] == 0){
            int [] temp = new int[digits.length + 1];
            temp[0] = 1;
            
            for (int i = 1; i < temp.length; i++){
                temp[i] = digits[i - 1];
            }
            return temp;
        }
        
        return digits;
    }
}