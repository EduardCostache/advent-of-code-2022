import 'dart:io';
import 'dart:convert';
import 'dart:async';

const String filename = 'input.txt';

main() async {
  List<String> lines = await readFile(filename);

  part1(lines);
  part2(lines);
}

Future<List<String>> readFile(String filename) async {
  List<String> result = [];
  final file = File(filename);

  Stream<String> lines =
      file.openRead().transform(utf8.decoder).transform(LineSplitter());

  try {
    await for (var line in lines) {
      result.add(line.trim());
    }
  } catch (_) {}

  return result;
}

void part1(List<String> lines) {
  int maxCals = 0;
  int curCals = 0;

  for (String line in lines) {
    int? n = int.tryParse(line);

    curCals = n == null ? 0 : n;

    maxCals = curCals > maxCals ? curCals : maxCals;
  }

  print(maxCals);
}

void part2(List<String> lines) {
  List<int> totalCals = [];
  int curCals = 0;

  for (String line in lines) {
    int? n = int.tryParse(line);

    if (n == null) {
      totalCals.add(curCals);
      curCals = 0;
    } else {
      curCals += n;
    }
  }

  totalCals.sort();
  int lsLength = totalCals.length;

  print(totalCals[lsLength - 1] +
      totalCals[lsLength - 2] +
      totalCals[lsLength - 3]);
}
