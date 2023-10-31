class prime
{
  public static void main(String[] args)
  {
    int l = Integer.parseInt(args[0]);
    int u = Integer.parseInt(args[1]);
    
    for(int i = l;i<=u;i++)
    {
      if(checkPrime(i))
      {
        System.out.println(i);
      }
    }
  }
  
  public static boolean checkPrime(int x)
  {
    if(x<2)
    {
      return false;
    }
    for(int i = 2;i<x;i++)
    {
      if(x % i == 0)
      {
        return false;
      }
    }
    
    return true;
  }
}

