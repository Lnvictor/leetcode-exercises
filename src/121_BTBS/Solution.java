class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
		
		for(int i = 0; i < prices.length; i++){
			int curr = prices[i];
			for (int j = i + 1; j < prices.length; j++){
				if (prices[j] - curr> maxP){
					maxP = prices[j] - curr;
				}
			}
		}
		
		return maxP;
    }
}