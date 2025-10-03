class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b)  {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
}


public class overload {
    public static void main(Strint[] args) {
        Calculator calc = new Calculator();
        System.out.println(calc.add(1, 2));
        System.out.println(calc.add(1.0, 2.5));
        System.out.println(calc.add(1, 2, 3));
    }
}

Calculator calc = new Calculator();
calc.add(1, 2);
calc.add(1.0, 2.5);
calc.add(1, 2, 3);