import java.util.Stack;

public class Q2S{
  static class Queue {
    Stack<Integer> stack1;
    Stack<Integer> stack2;
  }


  static void push(Stack<Integer> top, int x){
    top.push(x);
  }

  static int pop(Stack<Integer> top){
    if(top.isEmpty()){
      System.out.println("Stack overflow");
      System.exit(0);
    }
    return top.pop();
  }

  static void enQueue(Queue q, int x){
    stack1.push(x);
  }

  static int deQueue(Queue q){
    if(stack2.isEmpty()){
      while(!stack1.isEmpty()){
        stack2.push(stack1.pop());
      }
    }

    int pop = stack2.pop();
    if(stack1.isEmpty()){
      while(!stack2.isEmpty()){
        stack1.push(stack2.pop());
      }
    }

    return pop;
  }

  public static void main(String[] args) {

  }
}
