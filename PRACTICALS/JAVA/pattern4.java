/*
public class pattern4
{
    public static void main(String[] args) {
        int numRows = Integer.parseInt(args[0]);

        int currentNumber = 1;

        for (int i = 1; i <= numRows; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(currentNumber + " ");
                currentNumber++;
            }
            System.out.println();
        }
    }
}
*/

class pattern4
{
  public static void main(String[] args)
  {
    int n = Integer.parseInt(args[0]);
  
    for(int i=1;i<=n;i++)
    {
      System.out.println(i*i);
      i = i * 10; 
    }
  }
}
