class TreeNode{
  private int val;
  private int TreeNode t1;
  private int TreeNode t2;

  public TreeNode mergeTrees(TreeNode t1, TreeNode t2){
    if(t1 == null) return t2;
    if(t2 == null) return t1;

    TreeNode newNode = new TreeNode(t1.val + t2.val);
    newNode.right = mergeTrees(t1.right, t2.right);
    newNode.left = mergeTrees(t1.left, t2.left);

    return newNode;
  }

  public static void main(String[] args) {
    
  }


}
