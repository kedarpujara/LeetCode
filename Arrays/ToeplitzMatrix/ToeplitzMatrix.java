class ToeplitzMatrix {
  public boolean isToeplitzMatrix(int[][] matrix){
    boolean isMtrx = false;
    int num = matrix[0][0];
    for(int i = 0; i < matrix.length; i++){
      for(int j = 0; j < matrix[i].length; j++){
        if(i == j){
          if(num != matrix[i][j])
            return false;
        }

      }
    }
    return true;
  }

  public static void main(String[] args) {
    ToeplitzMatrix tm = new ToeplitzMatrix();
    System.out.println(tm.isToeplitzMatrix({{1,2,3,4},{5,1,2,3},{9,5,1,2}}));
  }
}
