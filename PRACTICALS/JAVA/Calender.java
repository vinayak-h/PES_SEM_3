class Calender
{
  public static void main(String[] args)
  {
  
    int date = 1;
    
    for(int i = 1;i<=7;i++)
    { 
      int dt = date++;
      System.out.println(dt);
      switch(i)
      {
        case 1: System.out.print("Sunday");
        case 2: System.out.print("Monday");
        case 3: System.out.print("Tuesday");
        case 4: System.out.print("Wednesday");
        case 5: System.out.print("Thursday");
        case 6: System.out.print("Friday");
        case 7: System.out.print("Saturday");
      }
      
      while(date <= 31)
      {
        System.out.println(date);
        date += 7;
      }
      
      date = 2;
      
    }
    
  }
  
}
