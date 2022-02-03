class Solution {
    public String convert(String s, int numRows) {
        String converted_string = "";
        int interval = ((numRows - 1) * 2);
        
        if(numRows == 1) return s;

        for (int i = 0; i < numRows; i++) {
            int current_pos = i;

            while (current_pos < s.length()) {
                converted_string = converted_string.concat(s.substring(current_pos, current_pos + 1));

                if (i > 0 && i < (numRows - 1)) {
                    int next_pos = ((numRows - i - 2) * 2 + 2);
                    current_pos += next_pos;

                    if (current_pos < s.length()) {
                        converted_string += s.substring(current_pos, current_pos + 1);
                        current_pos += (interval - next_pos);
                        next_pos = interval - next_pos;
                    }

                } else {
                    current_pos += interval;
                }

            }
        }
        
        return converted_string;

    }
}