import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    static final String FILENAME = "advent-of-code-2022/Day 1/input.txt";

    public static void main(String[] args) {
        Main controller = new Main();

        ArrayList<String> lines = controller.readFile();

        controller.part1(lines);
        controller.part2(lines);
    }

    private void part1(ArrayList<String> lines) {
        int maxCals = 0;
        int curCals = 0;
        for (String line : lines) {
            if (line.equals("")) {
                curCals = 0;
                continue;
            }
            int cal = Integer.parseInt(line);
            curCals += cal;

            maxCals = Math.max(curCals, maxCals);
        }

        System.out.println(maxCals);
    }

    private void part2(ArrayList<String> lines) {
        int curCals = 0;
        ArrayList<Integer> totalCals = new ArrayList<>();

        for (String line : lines) {
            if (line.equals("")) {
                totalCals.add(curCals);
                curCals = 0;
                continue;
            }
            int cal = Integer.parseInt(line);
            curCals += cal;
        }

        Collections.sort(totalCals);
        int listLen = totalCals.size();

        System.out.println(totalCals.get(listLen - 1) + totalCals.get(listLen - 2) + totalCals.get(listLen - 3));
    }

    private ArrayList<String> readFile() {
        ArrayList<String> lines = new ArrayList<>();
        try {
            File file = new File(FILENAME);
            Scanner scanner = new Scanner(file);

            while (scanner.hasNextLine()) {
                lines.add(scanner.nextLine());
            }

            scanner.close();
        } catch (FileNotFoundException ignored) {

        }

        return lines;
    }
}
