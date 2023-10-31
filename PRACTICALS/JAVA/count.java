//Use sizeof() operator and count the string and integer elements
class count {
    public static void main(String[] args) 
    {
        int stringCount = 0;
        int intCount = 0;

        for (String arg : args)
        {
            try 
            {
                Integer.parseInt(arg);
                intCount++;
            } 
            catch (NumberFormatException e) 
            {
                stringCount++;
            }
        }

        System.out.println("String Count: " + stringCount);
        System.out.println("Integer Count: " + intCount);
    }
}

