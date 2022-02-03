class Solution {
    public void setZeroes(int[][] matrix) {
        int[][] copy = new int[matrix.length][matrix[0].length];
        copyOfMatrix(matrix, copy);
            
        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix[i].length; j++){
                if (matrix[i][j] == 0){
                    zerar(copy, i, j);
                }
            }
        }
        copyOfMatrix(copy, matrix);
    }
    
    public void zerar(int[][] matrix, int i, int j){
        for (int k = 0; k < matrix[i].length; k++){
            matrix[i][k] = 0;
        }
        
        for(int l = 0; l < matrix.length; l++){
            matrix[l][j] = 0;
        }
        
    }
    
    public void copyOfMatrix(int[][] originalM, int [][] destiny){
        for (int i = 0; i < originalM.length; i++){
            for (int j = 0; j < originalM[i].length; j++){
                destiny[i][j] = originalM[i][j];
            }
        }
    }
}