public class BST {

  public class Node {
    private int key;
    private Node left;
    private Node right;

    Node root;

    public Node(int x){
      val = x;
      left = right = null;
    }

    public BST(){
      root = null;
    }


    /*
    if root == null, add at root
    else if()


    */
    public Node insert(Node root, int key){
      if(root == null){
        root = new Node(root.key);
        return root;
      } else {
        if(key < root.key){
          root.left = insert(root.left, key);
        } else if (key > root.key){
          root.right = insert(root.right, key);
        }
      }
      return root;
    }

    public search(Node n){

    }

    public delete(Node n){

    }

  }
}
