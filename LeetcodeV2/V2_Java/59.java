import java.util.Arrays;
class Solution59 {
    public int[][] generateMatrix(int n) {
        int [][] res=new int[n][n];

        int cur=1;

        int top=0;
        int bottom=n-1;
        int left=0;
        int right=n-1;

        while(cur<= n*n){
            for(int i =left; i<=right;i++){
                res[top][i]=cur++;
                
            }
            top++;
            for(int i=top;i<=bottom;i++){
                res[i][right]=cur++;
                
            }
            right--;
            for(int i=right;i>=left;i--){
                res[bottom][i]=cur++;
                
            }
            bottom--;
            for(int i=bottom;i>=top;i--){
                res[i][left] = cur++;
            }
            left++;
        }

    return res;
    }

        public static void main(String[] args) {
        Solution59 sol = new Solution59();


        System.out.println("n = 3 的结果：");
        printMatrix(sol.generateMatrix(3));


        System.out.println("\nn = 1 的结果：");
        printMatrix(sol.generateMatrix(1));
    }


    private static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}
