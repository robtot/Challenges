/** CodeEval Longest Word Challenge Solution **/
import java.io.File;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.FileReader;

public class Main {
  public static void main(String[] args) throws IOException {
    File file = new File(args[0]);
    BufferedReader input = new BufferedReader(new FileReader(file));
    String line;
    while ((line = input.readLine()) != null) {
      String[] words = line.split(" ");
      int wordLength = 0;
      String result = "";
      for (String word : words) {
        if (word.length() > wordLength) {
          wordLength = word.length();
          result = word;
        }

      }

      System.out.println(result);
    }

  }

}
