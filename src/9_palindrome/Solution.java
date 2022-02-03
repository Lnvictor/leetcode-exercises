class Solution {
    public boolean isPalindrome(int x) {
        String realNumber = String.valueOf(x);
		StringBuilder invertedNumber = new StringBuilder();
		
		for(int i = realNumber.length() - 1; i >= 0; i--) {
			invertedNumber.append(realNumber.charAt(i));
		}
		
		if(realNumber.equals(invertedNumber.toString())) {
			return true;
		}
        
		return false;
    }
}