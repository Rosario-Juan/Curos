public class Jav {
    public static void main(String[] args){
        Cliente cliente = new Cliente();
        Trabajador trabajador = new Trabajador();
        cliente.nombre = "Juan";
        cliente.edad = 19;
        cliente.telefono = 829280105;
        cliente.credito = 170.55;
        System.out.println("Soy " + cliente.nombre + ", tengo " + cliente.edad + " años y mi telefono es " + cliente.telefono
                + " y mi credito disponible es " + cliente.credito + "$ Peso Dominicano");

        trabajador.nombre = "Manuela";
        trabajador.edad = 50;
        trabajador.telefono = 80912345;
        trabajador.salario = 70000.32;
        System.out.println("Soy " + trabajador.nombre + ", tengo " + trabajador.edad + " años y mi telefono es " + trabajador.telefono
                + " y mi salario es de " + trabajador.salario + "$ Pesos Domincano");
    }
}


class persona{
    int edad;
    int telefono;
    String nombre;
}

class Cliente extends persona{
    double credito;
}

class Trabajador extends persona {
    double salario;
}