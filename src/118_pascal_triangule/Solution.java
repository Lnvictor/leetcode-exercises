class Solution {
    public List<List<Integer>> generate(int numRows) {
        if (numRows == 0) return new ArrayList<>();
		if (numRows == 1) {
            List<Integer> t = new ArrayList<>();
			t.add(1);
            List<List<Integer>> tmp = new ArrayList<>();
			tmp.add(t);
            return tmp;
        }
        
        
        if (numRows == 2){
			List<Integer> t = new ArrayList<>();
			t.add(1);
            List<List<Integer>> tmp = new ArrayList<>();
			tmp.add(t);
            t = new ArrayList<>();
            t.add(1);t.add(1);
			tmp.add(t);
			return tmp;
		}
		
		List<Integer> tmp = new ArrayList<>();
		List<List<Integer>> t = generate(numRows - 1);
		
		tmp.add(1);
		
		for (int i = 0; i < t.get(t.size() - 1).size() - 1; i++){
			tmp.add(t.get(t.size()-1).get(i) + t.get(t.size()-1).get(i + 1));
		}
        
		tmp.add(1);
        t.add(tmp);
		return t;
    }
}