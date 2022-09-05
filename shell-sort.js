const shell_sort = (list) => {
  let gap = parseInt(list.length / 2);
  while (gap > 0) {
    for (let i = 0; i < list.length; i++) {
      gap_insertion_sort(list, i, gap);
    }
    console.log(
      "Después de los incrementos de tamaño ",
      gap,
      " La lista es ",
      list
    );
    gap = parseInt(gap / 2);
  }
};

function gap_insertion_sort(list, start, gap) {
  let current;
  let position;
  for (let i = start + gap; i < list.length; i += gap) {
    current = list[i];
    position = i;
    while (position >= gap && list[position - gap] > current) {
      list[position] = list[position - gap];
      position = position - gap;
    }

    list[position] = current;
  }
}

items = [54, 26, 93, 17, 77, 31, 44, 55, 20];

shell_sort(items);
console.log(items);
