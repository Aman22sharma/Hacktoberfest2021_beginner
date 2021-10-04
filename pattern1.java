 /*AUTHOR: prm1999
 Python3 Concept: Print pattern
 *
 ***
*****
 ***
  *
 GITHUB: https://github.com/prm1999*/





import java.util.Scanner;
public class s1 {
    public static void main(String[] args) { 
        for(int i=1;i<=2;i++){
            for(int j=0;j<=2-i;j++)
                System.out.print(" ");
            for(int j=0;j<((2*i)-1);j++)
                System.out.print("*");
            System.out.println(); }
        for(int i=0;i<3;i++){
            for(int j=0;j<i;j++)
                System.out.print(" ");
            for(int j=0;j<(5-(2*i));j++)
                System.out.print("*");
            System.out.println();}}}
