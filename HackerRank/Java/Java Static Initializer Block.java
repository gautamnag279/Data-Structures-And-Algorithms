import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int b, h;
        b = sc.nextInt();
        h = sc.nextInt();

        if (b>0 && h>0) {
            int area = (int) b*h;
            System.out.println(area);
        }
        else{
            System.out.println("java.lang.Exception: Breadth and height must be positive"); 
        }
    }
}
