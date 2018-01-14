package com.hxzhao.stu;

public class Selection {
    private Selection(){}
    public static void sort(Comparable[] A){
        for(int currentIndex=1; currentIndex<A.length;currentIndex++){
            int minEleIndex = currentIndex;
            for (int innerIndex=currentIndex; innerIndex<A.length; innerIndex++){
                if (A[innerIndex].compareTo(A[minEleIndex])<0){
                    minEleIndex = innerIndex;
                }
            }
            exchange(A, currentIndex, minEleIndex);
        }
    }
    public static void exchange(Object[] A, int a, int b){
        Object temp = A[a];
        A[a] = A[b];
        A[b] = temp;
    }
    public static void printArray(Object[] A) {
        for(Object i :A){
            System.out.println(i.toString());
        }
    }
    public static void main(String[] args){
        Integer[] target = new Integer[]{1,2,3, 6, 7,4, 3, 1, 9};
        sort(target);
        printArray(target);
    }
}
