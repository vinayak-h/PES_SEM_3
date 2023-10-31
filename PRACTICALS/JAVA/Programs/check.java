class check {
    public static void main(String args[]) {
        int x = 66;
        char alpha = x;
        char alpha = (char) (x); // Explicit typecasting
        System.out.println(alpha);

        // Implicit Typecasting
        char beta = 'a';
        int y = beta;
        System.out.println(y);
    }
}