import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);   
        int numTest = s.nextInt();
        for(int i = 0; i < numTest; i++)
        {
            int[] firstTen = new int[10];
            int lowerBound = s.nextInt();
            int upperBound = s.nextInt();
            for(int j = 0; j < 10; j++)
            {
                firstTen[j] = s.nextInt();        
            }
            Random rnd = new Random();
            for(int k = lowerBound; k < upperBound; k++)
                {
                  rnd.setSeed(k);  
                  if(rnd.nextInt(1000) == firstTen[0])
                  {
                      boolean found = true;  
                      for(int l = 1; l < 10; l++)
                        {
                            if(rnd.nextInt(1000) != firstTen[l])
                            {
                                    found = false;
                                    break;
                            }
                        }
                      if(found)
                      {
                          System.out.print(k + " ");
                          for(int l = 0; l < 10; l++)
                          {
                            System.out.print(rnd.nextInt(1000) + " ");    
                          }
                          System.out.println();
                          break;
                      } 
                      
                  }
            }
        }
    }
}