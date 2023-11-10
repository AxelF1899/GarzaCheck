from markupsafe import Markup

def determinar_estrategia(puntuacion):
    if 14 <= puntuacion <= 20:
        return Markup('''
                      <p class="line-height">
Recuerda que cada paso que das, por pequeño que sea, te acerca a tus metas. Tu esfuerzo y dedicación son la clave para alcanzar el éxito. No importa cuántas veces te caigas, lo que realmente cuenta es cuántas veces te levantas y sigues adelante.
\n<br>
Tu trabajo está haciendo una diferencia en la vida de los demás. Al ayudar a los demás, no solo estás mejorando sus vidas, sino que también estás mejorando la tuya. La bondad y la empatía que muestras hacia los demás son un reflejo de la increíble persona que eres.
\n<br>
Así que sigue adelante, sigue trabajando duro y nunca dejes de creer en tí mism@. ¡Tú puedes hacerlo! 💪
\n<br>
                      <img class="strategy" src="..//static/icons/estudio3.png" alt="imagen jeje">                      
\n<br></p>
<h2>Salud emocional:</h2><p class="line-height">
\n<br>
-Practicar la autocompasión: Sé amable contigo mismo y reconoce que todos cometemos errores.
\n<br>
-Expresar tus emociones de manera saludable: Busca formas seguras y constructivas de expresar tus sentimientos.
\n<br>

<img class="strategy" src="..//static/icons/emocion.png" alt="imagen jeje">                      

</p>
''')
    elif 20 <= puntuacion <= 30:
        return Markup('''
<h2>Sueño:</h2><p class="line-height">
\n<br>
-Evitar las siestas largas durante el día: Si necesitas una siesta, intenta que sea corta y temprano en la tarde6.
\n<br>
-Limitar la ingesta de cafeína y alcohol: Ambos pueden interferir con la calidad del sueño.
\n<br>

                      
<img class="strategy" src="..//static/icons/sueno.png" alt="imagen jeje">
 </p>                     
<h2>Salud emocional:</h2><p class="line-height">
\n<br>
-Practicar la autocompasión: Sé amable contigo mismo y reconoce que todos cometemos errores.
\n<br>
-Expresar tus emociones de manera saludable: Busca formas seguras y constructivas de expresar tus sentimientos.
\n<br>
                      
<img class="strategy" src="..//static/icons/emocion1.png" alt="imagen jeje">                  
                        
</p>
''')
    elif 30 <= puntuacion <= 40:
        return Markup('''
<h2>Sueño:</h2><p class="line-height">
\n<br>
-Evitar las siestas largas durante el día: Si necesitas una siesta, intenta que sea corta y temprano en la tarde.
\n<br>
-Limitar la ingesta de cafeína y alcohol: Ambos pueden interferir con la calidad del sueño.
\n<br>

                      
<img class="strategy" src="..//static/icons/sueno1.png" alt="imagen jeje">
   </p>                   
<h2>Salud emocional:</h2><p class="line-height">
\n<br>
-Practicar la autocompasión: Sé amable contigo mismo y reconoce que todos cometemos errores.
\n<br>
-Expresar tus emociones de manera saludable: Busca formas seguras y constructivas de expresar tus sentimientos.
\n<br>

                      
<img class="strategy" src="..//static/icons/emocion2.png" alt="imagen jeje">
</p>
<h2>Desempeño escolar:</h2><p class="line-height">
\n<br>
-Tomar descansos regulares durante el estudio: Los descansos cortos pueden ayudar a mantener la concentración a largo plazo.
\n<br>
-Pedir ayuda cuando sea necesario: No dudes en buscar ayuda de profesores o compañeros de clase si tienes dificultades con el material de estudio.
\n<br>
                      
<img class="strategy" src="..//static/icons/estudio.png" alt="imagen jeje">
                      
</p>
''')
    elif 40 <= puntuacion <= 50:
        return Markup('''
<h2>Salud emocional:</h2> <p class="line-height">
\n<br>
-Practicar la autogestión: Aprende a identificar y manejar tus emociones de manera efectiva.
\n<br>
-Fomentar las relaciones interpersonales saludables: Mantén una red de apoyo social sólida y busca ayuda cuando la necesites.
\n<br>
-Practicar la atención plena: La meditación y otras prácticas de atención plena pueden ayudarte a mantener un estado mental equilibrado.
\n<br>

<img class="strategy" src="..//static/icons/emocion3.png" alt="imagen jeje">

</p>
''')
    elif 50 <= puntuacion <= 57:
        return Markup('''
<h2>Sueño:</h2><p class="line-height">
\n<br>
-Establecer una rutina de sueño: Intenta acostarte y levantarte a la misma hora todos los días, incluso los fines de semana.
\n<br>
-Evitar el uso de dispositivos electrónicos antes de dormir: La luz de las pantallas puede estimular la actividad cerebral y dificultar el sueño. Es aconsejable no usar el teléfono incluso dos horas antes de ir a dormir.
\n<br>
-Crear un ambiente propicio para el sueño: Mantén tu habitación oscura, tranquila y a una temperatura cómoda.
\n<br>

                      
<img class="strategy" src="..//static/icons/sueno2.png" alt="imagen jeje">
     </p>                 
<h2>Salud emocional:</h2><p class="line-height">
\n<br>
-Practicar la autogestión: Aprende a identificar y manejar tus emociones de manera efectiva.
\n<br>
-Fomentar las relaciones interpersonales saludables: Mantén una red de apoyo social sólida y busca ayuda cuando la necesites.
\n<br>
-Practicar la atención plena: La meditación y otras prácticas de atención plena pueden ayudarte a mantener un estado mental equilibrado.
\n<br>

<img class="strategy" src="..//static/icons/emocion.png" alt="imagen jeje">

</p>
''')
    else:
        return Markup('''
<h2>Sueño:</h2><p class="line-height">
\n<br>
-Establecer una rutina de sueño: Intenta acostarte y levantarte a la misma hora todos los días, incluso los fines de semana.
\n<br>
-Evitar el uso de dispositivos electrónicos antes de dormir: La luz de las pantallas puede estimular la actividad cerebral y dificultar el sueño. Es aconsejable no usar el teléfono incluso dos horas antes de ir a dormir.
\n<br>
-Crear un ambiente propicio para el sueño: Mantén tu habitación oscura, tranquila y a una temperatura cómoda.
\n<br>

                      
<img class="strategy" src="..//static/icons/sueno3.png" alt="imagen jeje">
</p>
<h2>Salud emocional:</h2><p class="line-height">
\n<br>
-Practicar la autogestión: Aprende a identificar y manejar tus emociones de manera efectiva.
\n<br>
-Fomentar las relaciones interpersonales saludables: Mantén una red de apoyo social sólida y busca ayuda cuando la necesites.
\n<br>
-Practicar la atención plena: La meditación y otras prácticas de atención plena pueden ayudarte a mantener un estado mental equilibrado.
\n<br>

                      
<img class="strategy" src="..//static/icons/emocion1.png" alt="imagen jeje">
</p>
<h2>Desempeño escolar:</h2><p class="line-height">
\n<br>
-Organizar el material de estudio: Tener un espacio de estudio ordenado y libre de distracciones puede ayudar a mejorar la concentración.
\n<br>
-Utilizar técnicas de estudio efectivas: Experimenta con diferentes técnicas de estudio para encontrar las que mejor funcionen para tí.
\n<br>
-Gestionar el tiempo de manera efectiva: Planifica tu tiempo de estudio y descanso para evitar el agotamiento.
\n<br>
                      
<img class="strategy" src="..//static/icons/estudio2.png" alt="imagen jeje">                 
                      </p>
''')