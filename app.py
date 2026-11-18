from flask import Flask, render_template, abort

app = Flask(__name__)

# Lista de felinos. Cada elemento es un diccionario con los datos de un animal.
felinos = [
    {
        "id": "leon",
        "nombre": "León",
        "cientifico": "Panthera leo",
        "categoria": "Gran felino social",
        "descripcion": "El único felino que vive en grupos familiares, llamados manadas.",
        "imagen": "img/leon.jpg",
        "habitat": "Sabanas y pastizales de África; una pequeña población en el bosque de Gir, India.",
        "peso": "Machos: 150 a 250 kg. Hembras: 120 a 180 kg.",
        "esperanza": "10 a 14 años en libertad; hasta 20 en cautiverio.",
        "conservacion": "Vulnerable",
        "aspecto": "Pelaje color arena a dorado y cola con un mechón oscuro en la punta. "
                   "El macho se reconoce por su melena, que se oscurece y crece con la edad. "
                   "La hembra no tiene melena y es más pequeña y ágil.",
        "habitos": "Duerme entre 16 y 20 horas al día y caza sobre todo al atardecer, de noche "
                   "y al amanecer. Se comunica con rugidos que se oyen a 8 km de distancia.",
        "alimentacion": "Carnívoro. Caza cebras, ñus, búfalos, antílopes y jirafas jóvenes. "
                        "También aprovecha carroña.",
        "estilo_vida": "Vive en manadas de 3 a 30 individuos, formadas por varias hembras "
                       "emparentadas, sus crías y uno o pocos machos.",
        "macho": "Defiende el territorio de la manada, marca los límites con orina y rugidos "
                 "y patrulla. Es el primero en comer cuando hay una presa. Los machos jóvenes "
                 "son expulsados de la manada hacia los 2 o 3 años.",
        "hembra": "Es la principal cazadora: caza en equipo y rodea a la presa. Cría a los "
                  "cachorros en grupo con otras leonas. Tras unos 110 días de gestación "
                  "nacen de 1 a 4 crías.",
        "dato": "Un rugido de león puede oírse a unos 8 km de distancia.",
    },
    {
        "id": "tigre",
        "nombre": "Tigre",
        "cientifico": "Panthera tigris",
        "categoria": "Gran felino solitario",
        "descripcion": "El felino más grande del mundo, reconocible por sus rayas únicas.",
        "imagen": "img/tigre.jpg",
        "habitat": "Bosques, selvas y manglares de Asia: India, Rusia, Indonesia y otros países.",
        "peso": "Machos: 180 a 260 kg (el tigre siberiano puede superar los 300 kg). "
                "Hembras: 100 a 160 kg.",
        "esperanza": "10 a 15 años en libertad; hasta 20 en cautiverio.",
        "conservacion": "En peligro",
        "aspecto": "Pelaje anaranjado con rayas negras y vientre blanco. El patrón de rayas "
                   "es único en cada individuo, como una huella digital. Las rayas también "
                   "están en su piel.",
        "habitos": "Caza de noche y al atardecer, acechando entre la vegetación. A diferencia "
                   "de otros felinos, le gusta el agua: nada con facilidad y se refresca en ríos.",
        "alimentacion": "Carnívoro. Come ciervos, jabalíes y búfalos. Un tigre adulto puede "
                        "comer más de 20 kg de carne en una sola comida.",
        "estilo_vida": "Es solitario y territorial. Cada individuo recorre su propio territorio "
                       "y se comunica con marcas de olor, arañazos en los árboles y rugidos.",
        "macho": "Tiene un territorio muy amplio, que puede abarcar el de varias hembras. "
                 "Lo defiende de otros machos y no participa en la crianza de los cachorros.",
        "hembra": "Tiene un territorio más pequeño. Tras unos 100 días de gestación nacen "
                  "de 2 a 4 cachorros, que vivirán con ella hasta los 2 años aproximadamente.",
        "dato": "Quedan unos 4.500 tigres en libertad, según estimaciones recientes.",
    },
    {
        "id": "guepardo",
        "nombre": "Guepardo (chita)",
        "cientifico": "Acinonyx jubatus",
        "categoria": "Felino velocista",
        "descripcion": "El animal terrestre más rápido: alcanza más de 100 km/h en carreras cortas.",
        "imagen": "img/guepardo.webp",
        "habitat": "Sabanas y llanuras abiertas de África y una pequeña población en Irán.",
        "peso": "Machos: 40 a 65 kg. Hembras: 35 a 55 kg.",
        "esperanza": "8 a 12 años en libertad; hasta 17 en cautiverio.",
        "conservacion": "Vulnerable",
        "aspecto": "Cuerpo delgado, patas largas y cabeza pequeña. Su pelaje amarillo "
                   "dorado tiene manchas negras sólidas y dos líneas negras, llamadas "
                   "'líneas lagrimales', que van de los ojos a la boca.",
        "habitos": "A diferencia de la mayoría de los felinos, caza de día, cuando hay menos "
                   "leones y hienas que le roben la presa. Persigue en carreras de 20 a 30 "
                   "segundos y después necesita descansar.",
        "alimentacion": "Carnívoro. Caza gacelas, impalas y liebres. Sus garras son "
                        "semirretráctiles, como los tacos de un corredor, y le dan tracción.",
        "estilo_vida": "Vive en espacios abiertos. No ruge: ronronea, chirría y emite sonidos "
                       "agudos parecidos a un pájaro.",
        "macho": "Suele vivir en coaliciones de 2 o 3 machos, normalmente hermanos, que "
                 "defienden un territorio y cazan juntos. Es una excepción entre los felinos.",
        "hembra": "Vive sola y cría sola a sus cachorros. Tras unos 93 días de gestación "
                  "nacen de 3 a 5 crías. Las cambia de escondite con frecuencia para "
                  "protegerlas de los depredadores.",
        "dato": "Pasa de 0 a 100 km/h en unos 3 segundos.",
    },
    {
        "id": "gato",
        "nombre": "Gato doméstico",
        "cientifico": "Felis catus",
        "categoria": "Felino doméstico",
        "descripcion": "El felino más cercano a nosotros: acompaña a las personas desde hace miles de años.",
        "imagen": "img/gato.jpg",
        "habitat": "Hogares, ciudades y campos de todo el mundo, excepto la Antártida.",
        "peso": "Machos: 4 a 6 kg. Hembras: 3 a 5 kg.",
        "esperanza": "12 a 18 años viviendo en casa; menos si vive en la calle.",
        "conservacion": "No evaluado (especie doméstica)",
        "aspecto": "Pequeño, flexible y de pelaje muy variado. El de la foto es un gato atigrado, "
                   "con rayas oscuras sobre fondo marrón. Tiene bigotes sensibles, pupilas "
                   "verticales y garras retráctiles.",
        "habitos": "Duerme entre 12 y 16 horas al día. Es más activo al amanecer y al atardecer. "
                   "Se acicala varias veces al día y comunica sus emociones con ronroneos, "
                   "maullidos y la posición de la cola.",
        "alimentacion": "Carnívoro estricto: necesita proteína animal. Un gato casero come "
                        "alimento balanceado, y uno callejero caza ratones, pájaros e insectos.",
        "estilo_vida": "Combina independencia y afecto. Marca su territorio con arañazos y con "
                       "el roce de su cara, y necesita lugares altos y rascadores.",
        "macho": "Es algo más grande y, si no está esterilizado, marca con orina, recorre "
                 "grandes distancias y pelea con otros machos por el territorio.",
        "hembra": "Si no está esterilizada, entra en celo varias veces al año. La gestación "
                  "dura unos 64 días y tiene camadas de 3 a 5 gatitos. Es una madre muy "
                  "protectora.",
        "dato": "Su ronroneo vibra entre 25 y 150 Hz, una frecuencia asociada a la calma.",
    },
    {
        "id": "puma",
        "nombre": "Puma",
        "cientifico": "Puma concolor",
        "categoria": "Felino de montaña",
        "descripcion": "El felino salvaje con más rango del continente americano, de Canadá a la Patagonia.",
        "imagen": "img/puma.jpg",
        "habitat": "Montañas, bosques, desiertos y pastizales. En Chile vive desde el norte hasta la Patagonia.",
        "peso": "Machos: 53 a 100 kg. Hembras: 29 a 64 kg.",
        "esperanza": "8 a 13 años en libertad; hasta 20 en cautiverio.",
        "conservacion": "Preocupación menor",
        "aspecto": "Pelaje liso de un solo color, entre café claro y gris, con el vientre más "
                   "claro. Tiene cuerpo largo, patas traseras potentes y una cola larga con "
                   "la punta oscura. Los cachorros nacen manchados.",
        "habitos": "Es crepuscular y nocturno, discreto y difícil de ver. Salta hasta 5 m de "
                   "altura y 12 m de largo. No ruge: ronronea, bufa y emite chillidos.",
        "alimentacion": "Carnívoro. Caza ciervos, guanacos, liebres y roedores. Entierra "
                        "parte de la presa bajo hojas y ramas para comerla después.",
        "estilo_vida": "Solitario, cubre territorios muy amplios y evita a las personas. "
                       "Descansa en cuevas, grietas rocosas y vegetación densa.",
        "macho": "Su territorio es más grande y se superpone con el de varias hembras. "
                 "Lo marca con arañazos y orina, y puede recorrer decenas de kilómetros.",
        "hembra": "Cría sola a sus cachorros en una guarida. La gestación dura unos 93 días "
                  "y nacen de 1 a 6 crías, normalmente 2 o 3. Las crías viven con ella "
                  "cerca de dos años.",
        "dato": "Tiene más nombres que ningún otro mamífero: puma, león de montaña, "
                "cougar y pantera, entre otros.",
    },
]


# Ruta 1: página de inicio. Muestra una tarjeta resumida de cada felino.
@app.route("/")
def inicio():
    return render_template("index.html", felinos=felinos)


# Ruta 2: catálogo completo con la información de cada felino.
@app.route("/felinos")
def catalogo():
    return render_template("felinos.html", felinos=felinos)


# Ruta 3: página "Nosotros" con el objetivo del sitio.
@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html", total=len(felinos))


if __name__ == "__main__":
    app.run(debug=True)
