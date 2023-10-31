// public class Test {
// public static void main(String[] args) {
// System.out.println("Hello World");
// }
// }

// public class Exam {
// public static void main(String[] args) {
// System.out.println("Hello Java");
// }
// }

// // Without main method we can create class
// class Empty {
// public void Hello() {
// System.out.println("Hello Mate!");
// }
// }

// _____A class Can have multiple Main Methods with different declaration
// Syntax___
// class Test {
// public static void main(String[] args) {
// System.out.println("In Class Test");
// }

// public static void main(int x) {
// System.out.println("In Main method");

// }
// }

// ____________________Scanner Class
import java.util.Scanner;

class Test {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter your age : ");

        int x = scan.nextInt();
        System.out.println("Your age is : " + x);
    }
}
