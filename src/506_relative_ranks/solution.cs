public class Solution {
    public string[] FindRelativeRanks(int[] score) {
        var sortedArray = score.OrderByDescending(x => x).ToArray();
        string[] resp = new string[score.Length];

        for (int i = 0; i < score.Length; i++){
            int position = Array.IndexOf(sortedArray, score[i]);
            string placement;

            if (position == 0)
            {
                placement = "Gold Medal";
            }
            else if (position == 1)
            {
                placement = "Silver Medal";
            }
            else if (position == 2)
            {
                placement = "Bronze Medal";
            }
            else 
            {
                placement = $"{position + 1}";
            }

            resp[i] = placement;
        }

        return resp;
    }
}