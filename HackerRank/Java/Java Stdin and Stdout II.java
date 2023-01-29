import java.io.*;
import java.util.*;

public class Solution 
{

    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);
        
        int num = scan.nextInt();
        Double deci = scan.nextDouble();
        //This extra 'scan.nextLine() is needed to clear the buffer'
        scan.nextLine();
        String str = scan.nextLine();
        
        System.out.println("String: " + str);
        System.out.println("Double: " + deci);
        System.out.println("Int: " + num);
    }
}
