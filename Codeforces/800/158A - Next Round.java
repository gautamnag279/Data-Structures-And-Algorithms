import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int inputs[] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int entries = inputs[0];
        int basePosition = inputs[1] - 1;
        int count = 0;

        int scores[] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        for (int i = 0; i < scores.length; i++) {
            if (basePosition <= entries && scores[i] >= scores[basePosition] && scores[i] != 0)
                count++;
        }
        System.out.println(count);
    }

}
