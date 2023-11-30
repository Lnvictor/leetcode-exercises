public class Solution {
    public int[][] LargestLocal(int[][] grid) {
        int newSize = grid.Length - 2;
        int[][] resp = new int[newSize][];
        int[] reducedArr = new int[9];

        int col = 0;
        int row = 0;

        for (int i = 0; i < newSize; i++)
        {
            resp[i] = new int[newSize];
        }

        while (row < newSize)
        {
            reducedArr[0] = grid[row][col];
            reducedArr[1] = grid[row][col + 1];
            reducedArr[2] = grid[row][col + 2];
            reducedArr[3] = grid[row + 1][col];
            reducedArr[4] = grid[row + 1][col + 1];
            reducedArr[5] = grid[row + 1][col + 2];
            reducedArr[6] = grid[row + 2][col];
            reducedArr[7] = grid[row + 2][col + 1];
            reducedArr[8] = grid[row + 2][col + 2];

            Array.Sort(reducedArr);

            resp[row][col] = reducedArr[8];

            if (col == newSize - 1){
                col = 0;
                row++;
            }
            else{
                col++;
            }
        }

        return resp;
    }
}