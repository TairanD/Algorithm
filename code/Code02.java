package code;

public class Code02 {
    public void mergeSort(int[] arr, int l, int r){
        if (arr == null || r - l < 2){
            return;
        }

        int mid = l + ((r - l) >> 1);
        mergeSort(arr, l, mid);
        mergeSort(arr, mid, r);

        merge(arr, l, mid, r);
    }

    public void merge(int[] arr, int l, int mid, int r){
        int lPointer = l;
        int rPointer = mid + 1;
        int currentIndex = l;
        int[] temp = new int[arr.length];
        while (lPointer<=mid && rPointer<=r){
            if (arr[lPointer]<arr[rPointer]){
                temp[currentIndex] = arr[lPointer];
                lPointer += 1;
            } else{
                temp[currentIndex] = arr[rPointer];
                rPointer += 1;
            }
            currentIndex += 1;
            // the above code equals to the following code
            // temp[currentIndex++] = arr[lPointer]<arr[rPointer] ? arr[lPointer++] : arr[rPointer++];
        }


        while (lPointer<=mid){
            temp[currentIndex] = arr[lPointer];
            lPointer += 1;
            currentIndex += 1;
            // the above code equals to the following code
            // temp[currentIndex++] = arr[lPointer++];
        }
        while (rPointer<=mid){
            temp[currentIndex] = arr[rPointer];
            rPointer += 1;
            currentIndex += 1;
        }


        arr = temp;
    }
}
