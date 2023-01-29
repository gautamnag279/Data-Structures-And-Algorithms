import java.io.*;
import java.util.*;

public class Solution 
{

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        if ((num%2 != 0) || ((num%2 == 0) && (num >= 6) && (num <=20)))
        {
            System.out.println("Weird");
        }
        else
        {
            System.out.println("Not Weird");
        }
        
    }
}
