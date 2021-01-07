import javax.swingJOptionPane;
import java.util.Scanner;

public class Characters {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("What is your name? ");
        String name = scanner.toString().trim();
        System.out.println("You have chosen the name: " + name);

        String one = JOptionPane.showInputDialog("Enter first number");
        String two = JOptionPane.showInputDialog("Enter second number");

        int num1 = Integer.parseInt(one);
        int num2 = Integer.parseInt(two);
        int sum = num1 + num2;

        JOptionPane.showMessageDialog(null, "The answer is " + sum, "Title", JOptionPane.PLAIN_MESSAGE);

    }
}