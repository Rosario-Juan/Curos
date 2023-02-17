import java.net.CacheRequest;

public class J0{
    public static int  sumarTresValores(int a, int b, int c) {
        int sumar = a + b + c;
        return sumar;
    }
    public static void main(String [] args) {
        int resultado = sumarTresValores (2, 10,15);
        System.out.println("la suma de los Tres Valores es: " + resultado);
    }
}

