public class persona{
    public static void main(String[] args) {
        Personaa persona = new Personaa();
        persona.setNombre("Juan");


        System.out.println("mi nombre es :" + persona.getNombre());
        persona.setEdad( 19 );

        System.out.println("Mi edad es " + persona.getEdad() + "");
        persona.setTelefono(829901053);

        System.out.println("mi telefono es " + persona.getTelefono());


    }
}
class Personaa{
    private int Edad;
    private String nombre;
    private int Telefono;

    public int getEdad() {
        return Edad;
    }

    public void setEdad(int Edad) {
        this.Edad = Edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getTelefono() {
        return Telefono;
    }

    public void setTelefono(int telefono) {
        this.Telefono = telefono;
    }
}
