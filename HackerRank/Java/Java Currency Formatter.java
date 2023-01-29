import java.util.*;
import java.text.NumberFormat;

public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double amount = sc.nextDouble();
        sc.close();

        Locale indiaLocale = new Locale("en", "IN");

        NumberFormat us = NumberFormat.getCurrencyInstance(Locale.US);
        NumberFormat india = NumberFormat.getCurrencyInstance(indiaLocale);
        NumberFormat china = NumberFormat.getCurrencyInstance(Locale.CHINA);
        NumberFormat france = NumberFormat.getCurrencyInstance(Locale.FRANCE);

        System.out.println("US:" + " " + us.format(amount));
        System.out.println("India:" +" " + india.format(amount));
        System.out.println("China:" +" " + china.format(amount));
        System.out.println("France:" + " " + france.format(amount));

    }
}
