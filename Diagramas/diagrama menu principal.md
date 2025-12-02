graph TD
    %% Definiciones de estilo para claridad, opcional
    classDef action fill:#FAEBD7,stroke:#BB2525,stroke-width:2px;
    classDef decision fill:#e0f7fa,stroke:#00acc1,stroke-width:2px;
    classDef start_end fill:#BB2525,stroke:#333,color:#fff;

    %% Nodos del diagrama
    A([Inicio])
    B[Imprimir menú y opciones]
    C{Solicitar opción \\ al usuario}
    D{Opción es válida?}
    E{Opción es "0"?}
    F[Imprimir "Saliendo..."]
    G([Fin])
    H[Opción no válida]

    OP1[Llamar a ingresarPaises()]
    OP2[Llamar a actualizarPais()]
    OP3[Llamar a mostrarPais()]
    OP4[Llamar a filtrarPaises()]
    OP5[Llamar a mostrarEstadisticas()]
    OP6[Llamar a mostrarPaises()]


    %% Conexiones (Flujo)

    A --> B
    B --> C
    C --> D

    D -- No --> H
    H --> C %% Vuelve a pedir la opción

    D -- Sí --> E

    E -- Sí --> F
    F --> G

    E -- No --> OpcionesSwitch

    %% El Switch Case
    subgraph OpcionesSwitch [Match Opcion]
      direction TB
      OP1 --> Continua
      OP2 --> Continua
      OP3 --> Continua
      OP4 --> Continua
      OP5 --> Continua
      OP6 --> Continua
    end

    OpcionesSwitch --> C %% Después de cualquier opción, vuelve al menú principal

    %% Aplicar estilos (Opcional, pero ayuda a la visualización)
    class A,G start_end;
    class B,H,OP1,OP2,OP3,OP4,OP5,OP6 action;
    class C,D,E decision;
