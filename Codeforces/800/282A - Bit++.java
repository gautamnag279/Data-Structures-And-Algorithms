import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        List<String> s = new ArrayList<String>();
        for (int i = 0; i <= input; i++) {
            String x = sc.nextLine();
            s.add(x);
        }

        int countPositive = 0;
        int countNegetive = 0;

        for (int i = 0; i < s.size(); i++) {
            if ((s.get(i)).contains("++"))
                countPositive++;
            else if ((s.get(i)).contains("--"))
                countNegetive++;
        }

        System.out.println(countPositive - countNegetive);
        sc.close();
    }
}
