function merge_sort(items_list) {
  if (items_list.length > 1) {
    let mid = parseInt(items_list.length / 2);
    let left = items_list.slice(0, mid);
    let right = items_list.slice(mid);

    merge_sort(left);
    merge_sort(right);

    i = 0;
    j = 0;
    k = 0;

    while (i < left.length && j < right.length) {
      if (left[i] < right[j]) {
        items_list[k] = left[i];
        i += 1;
      } else {
        items_list[k] = right[j];
        j += 1;
      }
      k += 1;
    }

    while (i < left.length) {
      items_list[k] = left[i];
      i += 1;
      k += 1;
    }
    while (j < right.length) {
      items_list[k] = right[j];
      j += 1;
      k += 1;
    }
  }
}

items = [54, 26, 93, 17, 77, 31, 44, 55, 20];
merge_sort(items);
console.log(items);
