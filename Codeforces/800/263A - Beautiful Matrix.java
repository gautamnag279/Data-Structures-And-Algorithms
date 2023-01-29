import java.util.Scanner;

public class Answer {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = 0;
        for (int i = 1; i <= 5; ++i) {
            for (int j = 1; j <= 5; ++j) {
                n = sc.nextInt();
                if (n == 1) {
                    System.out.println(Math.abs(i - 3) + Math.abs(j - 3));
                }
            }
        }
        sc.close();
    }
}
