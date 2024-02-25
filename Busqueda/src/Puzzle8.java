import java.util.Collection;

public class Puzzle8 {

    public static String initialState = "12578 346";
    public static String finalState = "12345678 ";

    public static void main(String[] args) {


        // Instanciar el árbol de búsqueda
        ArbolBusqueda arbolBusqueda = new ArbolBusqueda(new Nodo(initialState), finalState);

        // Ejecutar la búsqueda

        // Anchura
        long startTime = System.nanoTime();
        System.out.println("Búsqueda por Anchura");
        arbolBusqueda.busquedaPorAnchura();
        long endTime = System.nanoTime();
        long duration = endTime - startTime;
        System.out.println("Tiempo: " + (float)duration / 1000000000);


        // Profundidad
        long startTime2 = System.nanoTime();
        System.out.println("Búsqueda por Profundidad");
        arbolBusqueda.busquedaPorProfundidad();
        long endTime2 = System.nanoTime();
        long duration2 = endTime2 - startTime2;
        System.out.println("Tiempo: " + (float)duration2 / 1000000000);


        // Heurística 1
        long startTime3 = System.nanoTime();
        System.out.println("Búsqueda por Heurística 1");
        arbolBusqueda.busquedaHeuristica();
        long endTime3 = System.nanoTime();
        long duration3 = endTime3 - startTime3;
        System.out.println("Tiempo: " + (float)duration3 / 1000000000);


        // Heurística 2
        long startTime4 = System.nanoTime();
        System.out.println("Búsqueda por Heurística 2");
        arbolBusqueda.busquedaHeuristica2();
        long endTime4 = System.nanoTime();
        long duration4 = endTime4 - startTime4;
        System.out.println("Tiempo: " + (float)duration4 / 1000000000);

        // Imprimir movimientos
        System.out.println("Búsqueda por Anchura");
        System.out.println("Tiempo: " + (float)duration / 1000000000);
        System.out.println("Búsqueda por Profundidad");
        System.out.println("Tiempo: " + (float)duration2 / 1000000000);
        System.out.println("Búsqueda por Heurística 1");
        System.out.println("Tiempo: " + (float)duration3 / 1000000000);
        System.out.println("Búsqueda por Heurística 2");
        System.out.println("Tiempo: " + (float)duration4 / 1000000000);
    }
}
