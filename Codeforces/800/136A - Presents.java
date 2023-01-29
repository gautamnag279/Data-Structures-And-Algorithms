import java.util.Scanner;

public class Answer {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] gifts = new int[105];

        for (int i = 1; i <= n; i++) {
            int b = sc.nextInt();
            gifts[b] = i;
        }
        for (int i = 1; i <= n; i++) {
            System.out.printf(gifts[i] + " ");
        }
        sc.close();
    }
}

// FUCK THIS QUESTION 
