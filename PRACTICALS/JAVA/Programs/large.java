import java.util.Scanner;

class large {
    public static void main(String[] args) {
        Scanner myObject = new Scanner(System.in);

        System.out.println("Enter 2 numbers");

        Float number1 = myObject.nextFloat();
        Float number2 = myObject.nextFloat();

        if (number1 > number2) {
            System.out.println(number1 + "is greater than " + number2);

        } else if (number1 == number1) {
            System.out.println(number1 + "and" + number2 + "are same");

        } else {
            System.out.println(number2 + "is larger than " + number1);

        }

    }
}
