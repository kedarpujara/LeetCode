class Solution {
    public void invertTreeInt(TreeNode root) {
        TreeNode tmp = null;
        if (root == null) {
            return;
        }

        tmp = root.left;
        root.left = root.right;
        root.right = tmp;

        invertTreeInt(root.left);
        invertTreeInt(root.right);
    }

    public TreeNode invertTree(TreeNode root) {
        invertTreeInt(root);
        return root;
    }
}