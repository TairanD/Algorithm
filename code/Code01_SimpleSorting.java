package code;

public class Code01_SimpleSorting {
    private static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }


    public static void selectionSort(int[] arr){
        for (int i=0; i<arr.length-1; i++){
            int minIndex = i;
            for (int j=i+1; j!= arr.length; j++){
                minIndex = arr[j]<arr[i] ? j : minIndex;
            }
            swap(arr, i, minIndex);
        }
    }


    public static void bubbleSort(int[] arr){
        for (int i=arr.length-1; i>0; i--){
            for (int j=0; j<i; j++){
                if (arr[j]>arr[j+1]){
                    swap(arr, j, j+1);
                }
            }
        }
    }


    public static void insertionSort(int[] arr){
        for (int i=1; i< arr.length; i++){
            for (int j=i; j>0 && arr[j]<arr[j-1]; j--){
                swap(arr, j, j-1);
            }
        }
    }
}
