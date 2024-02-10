import { Cell } from "./Cell.js";
const Paths = [];
let seqVal = [15, 20, 30];
let sequences = [
  ["BD", "E9", "1C"],
  ["BD", "7A", "BD"],
  ["BD", "1C", "BD", "55"],
];

let seqAns = [];
let maxVal = 0;
let rowAns = [];
let colAns = [];

let inputForm = document.getElementById("inputForm");

inputForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let filename = document.getElementById("filename");
  console.log(filename.value);

});

function resetArr(arr) {
  for (var i = 0; i < arr.length; i++) {
    for (var j = 0; j < arr[0].length; j++) {
      arr[i][j].visited = false;
    }
  }
}

function solve(arr, sequences) {
  for (var i = 0; i < arr.length; i++) {
    compareArr(arr[i], sequences);
  }
}

function compareArr(arr, sequences) {
  let ans = 0;
  for (var i = 0; i < sequences.length; i++) {
    for (var j = 0; j < arr.length; j++) {
      if (arr[j].value == sequences[i][0]) {
        // console.log(arr[j]);
        let cek = true;
        let a = 0;
        let b = j;
        while (cek && b < arr.length && a < sequences[i].length) {
          // console.log(arr[b]);
          if (arr[b].value != sequences[i][a]) {
            cek = false;
          }
          a++;
          b++;
        }
        if (a == sequences[i].length && cek) {
          ans += seqVal[i];
        }
        if (ans > maxVal) {
          seqAns = [];
          rowAns = [];
          colAns = [];
          maxVal = ans;
          for (var x = 0; x < arr.length; x++) {
            seqAns.push(arr[x].value);
            rowAns.push(arr[x].row);
            colAns.push(arr[x].column);
          }
        }
      }
    }
  }
}

function Visit(row, col, cnt, path, visitRow, buffMax, arr) {
  let cellNow = arr[row][col];
  cellNow.visited = true;
  path.push(cellNow);

  if (cnt == buffMax - 1) {
    Paths.push([...path]);
    cellNow.visited = false;
    path.pop();
    return;
  } else {
    let limit;
    if (visitRow) {
      limit = arr.length;
    } else {
      limit = arr[0].length;
    }

    for (var i = 0; i < limit; i++) {
      if (visitRow) {
        if (arr[i][col].visited) continue;

        Visit(i, col, cnt + 1, path, false, buffMax, arr);
      } else {
        if (arr[row][i].visited) continue;

        Visit(row, i, cnt + 1, path, true, buffMax, arr);
      }
    }
  }

  cellNow.visited = false;
  path.pop();
}
const start = Date.now();
let arr = [
  [
    new Cell(1, 1, false, "7A"),
    new Cell(1, 2, false, "55"),
    new Cell(1, 3, false, "E9"),
    new Cell(1, 4, false, "E9"),
    new Cell(1, 5, false, "1C"),
    new Cell(1, 6, false, "55"),
  ],
  [
    new Cell(2, 1, false, "55"),
    new Cell(2, 2, false, "7A"),
    new Cell(2, 3, false, "1C"),
    new Cell(2, 4, false, "7A"),
    new Cell(2, 5, false, "E9"),
    new Cell(2, 6, false, "55"),
  ],
  [
    new Cell(3, 1, false, "55"),
    new Cell(3, 2, false, "1C"),
    new Cell(3, 3, false, "1C"),
    new Cell(3, 4, false, "55"),
    new Cell(3, 5, false, "E9"),
    new Cell(3, 6, false, "BD"),
  ],
  [
    new Cell(4, 1, false, "BD"),
    new Cell(4, 2, false, "1C"),
    new Cell(4, 3, false, "7A"),
    new Cell(4, 4, false, "1C"),
    new Cell(4, 5, false, "55"),
    new Cell(4, 6, false, "BD"),
  ],
  [
    new Cell(5, 1, false, "BD"),
    new Cell(5, 2, false, "55"),
    new Cell(5, 3, false, "BD"),
    new Cell(5, 4, false, "7A"),
    new Cell(5, 5, false, "1C"),
    new Cell(5, 6, false, "1C"),
  ],
  [
    new Cell(6, 1, false, "1C"),
    new Cell(6, 2, false, "55"),
    new Cell(6, 3, false, "55"),
    new Cell(6, 4, false, "7A"),
    new Cell(6, 5, false, "55"),
    new Cell(6, 6, false, "7A"),
  ],
];

for (var i = 0; i < 3; i++) {
  console.log(i);
  resetArr(arr);
  Visit(0, i, 0, [], true, 7, arr);
}
solve(Paths, sequences);

console.log(maxVal);
console.log(seqAns);
for (var j = 0; j < rowAns.length; j++) {
  console.log(`${colAns[j]},${rowAns[j]}`);
}
const end = Date.now();
console.log(`${end - start} ms`);
