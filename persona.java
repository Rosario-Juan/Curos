public class persona{
    private int edad;
    private String nombre;
    private String telefono;

    public int getedad() {
        return edad;
    }


    public void setedad(int edad) {
        this.edad = edad;
    }

    public String getnombre() {
        return nombre;
    }

    public void setnombre(String nombre) {
        this.nombre = nombre;
    }

    public String gettelefono() {
        return telefono;
    }

    public void settelefono(String telefono) {
        this.telefono = telefono;
    }
}
class Main{
    public static void main(String[] args) {
        persona persona = new persona();

        persona.setedad(25);
        persona.setnombre("Juan");
        persona.settelefono("8298795067");

        System.out.println("La persona se llama " + persona.getnombre() +
                ", tiene " + persona.getedad() + " años y su teléfono es " +
                persona.gettelefono());

    }
}
