
import java.util.scanner;

public class hellodarn {
    public static void main(String[] args) {
        Car myPorsche = new Car(1, 320);

        Scanner a = new Scanner();

        Person Kim = new Person();
        Person Alex = new Person();

        int myAge = 19;
        int herAge = myAge;

        System.out.println(herAge);

        if (9 > 10) {
            System.out.println("Kim proceeds to kill herself.");
        } else {
            System.out.println("Alex proceeds to kill himself.");
        }
    }
}