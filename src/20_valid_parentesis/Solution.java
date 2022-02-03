class Solution {
    public boolean isValid(String s) {
        if(s.isEmpty()) return true;
        if(s.length()%2 != 0) return false;

        Stack<Character> nextToClose = new Stack<>();
        Map<Character, Character> brackets = new HashMap<>();

        brackets.put('(', ')');
        brackets.put('{', '}');
        brackets.put('[', ']');


        for (char c : s.toCharArray()){
            if ((!brackets.containsKey(c) && nextToClose.isEmpty()) || !brackets.containsKey(c) &&!brackets.containsValue(c)) return false;

            else if (brackets.containsKey(c)){
                nextToClose.add(brackets.get(c));
            }

            else if (c != nextToClose.pop()) return false;
        }

    
        return nextToClose.empty();
    }
}