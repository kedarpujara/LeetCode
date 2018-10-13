//'main' method must be in a class 'Rextester'.
//Compiler version 1.8.0_111

import java.util.*;
import java.lang.*;

class Rextester
{
    private static int[] A;
    private static int[] B;   
    
    public static void main(String[] args)
    {
        A = new int[] { 2, 3, 6, 7 };
        B = new int[] { 1, 4, 5, 8 };
        int[] answer = merge(A, B);
        
        System.out.println(Arrays.toString(answer));
    }
    
    static int[] merge(int[] a, int[] b) 
    {
        //Your code here
        int i = 0;
        int j = 0;
        int lenA = a.length;
        int lenB = b.length;
        int aVal = 0;
        int bVal = 0;
        boolean aFinished = false;
        boolean bFinished = false;
        int[] mergeAr = new int[lenA + lenB];
        for (int k = 0; k < mergeAr.length; k++) {
            
            aVal = a[i]; 
            bVal = b[j];
            if(aFinished == true) {
                mergeAr[k] = bVal;
                j++;
                continue;
            }
            if(bFinished == true) {
                mergeAr[k] = aVal;
                i++;
                continue;
            }
  
            if (aVal < bVal && aFinished == false) {
                i++;
                if (i == lenA) {
                    aFinished = true;
                    i = lenA-1;
                    }
                mergeAr[k] = aVal;
            } else if (aVal > bVal && bFinished == false) {
                j++;
                    if (j == lenB) {
                        bFinished = true;
                        j = lenB-1;
                    }
                mergeAr[k] = bVal;
            } else if(aVal == bVal) {
                i++;
                mergeAr[k] = aVal;
            }
        }
        return mergeAr;
    }
    
}