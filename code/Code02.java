package code;

public class Code02 {
    public static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void mergeSort(int[] arr, int l, int r){
        if (arr == null || r - l < 2){
            return;
        }

        int mid = l + ((r - l) >> 1);
        mergeSort(arr, l, mid);
        mergeSort(arr, mid, r);

        merge(arr, l, mid, r);
    }

    public static void merge(int[] arr, int l, int mid, int r){
        int lPointer = l;
        int rPointer = mid + 1;
        int currentIndex = l;
        int[] temp = new int[arr.length];
        while (lPointer<=mid && rPointer<=r){
//            if (arr[lPointer]<arr[rPointer]){
//                temp[currentIndex] = arr[lPointer];
//                lPointer += 1;
//            } else{
//                temp[currentIndex] = arr[rPointer];
//                rPointer += 1;
//            }
//            currentIndex += 1;
            // the above code equals to the following code
            temp[currentIndex++] = arr[lPointer]<arr[rPointer] ? arr[lPointer++] : arr[rPointer++];
        }


        while (lPointer<=mid){
//            temp[currentIndex] = arr[lPointer];
//            lPointer += 1;
//            currentIndex += 1;
            // the above code equals to the following code
            temp[currentIndex++] = arr[lPointer++];
        }
        while (rPointer<=mid){
            temp[currentIndex] = arr[rPointer];
            rPointer += 1;
            currentIndex += 1;
        }
        arr = temp;
    }

    public static void q1(int[] arr, int num){
        // pointer p represents the first location that is unchecked/examined
        int p = 0;
        for (int i = 0; i<arr.length; i++){
            if (arr[i] <= num){
                swap(arr, p, i);
            }
            p++;
        }
    }

    public static void q2(int[] arr, int num){
        int less = 0;
        int greater = arr.length-1;
        int i = 0;
        while (i<=greater){
            if (arr[i] < num){
                swap(arr, i++, less++);
            } else if (arr[i] > num) {
                swap(arr, i, greater--);
            }else {
                i++;
            }
        }
    }

    public static void main(String[] args) {
        int[] testArr = {4, 43,23,12,14, 64,67,2,7,3};
        q2(testArr, 4);
        for (int i: testArr){
            System.out.println(i);
        }

    }
}
