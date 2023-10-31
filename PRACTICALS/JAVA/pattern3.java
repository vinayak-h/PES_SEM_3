public class pattern3 {
    public static void main(String[] args) 
    {
        int numPatterns = Integer.parseInt(args[0]);

        int number = 1;
        for (int i = 0; i < numPatterns; i++) 
        {
            number = number * 10 + 1;
            System.out.println((number * number));
        }
    }
}
