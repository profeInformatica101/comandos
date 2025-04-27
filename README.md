# 💪 Comandos Linux organizados por Temas de Sistemas Operativos (Educación en Informática)

---

# 📈 1. Gestión de Procesos

| Comando | Parámetro(s) útil(es) | Descripción breve | Ejemplo de comando | Ejemplo de ejecución |
|:--------|:----------------------|:------------------|:-------------------|:---------------------|
| `ps` | `-e`, `-o pid,comm, %cpu` | Listar procesos | `ps -e -o pid,comm` | Muestra todos los procesos y sus nombres |
| `kill` | `-9 pid` | Matar un proceso | `kill -9 1234` | Mata el proceso con PID 1234 |
| `pkill` | `nombre` | Matar proceso por nombre | `pkill firefox` | Mata todos los procesos `firefox` |

# 📚 2. Gestión de Archivos y Permisos

| Comando | Parámetro(s) útil(es) | Descripción breve | Ejemplo de comando | Ejemplo de ejecución |
|:--------|:----------------------|:------------------|:-------------------|:---------------------|
| `cp` | `-r`, `-u`, `-v` | Copiar archivos | `cp -ru origen/ destino/` | Copia solo archivos nuevos o actualizados |
| `mv` | `-v`, `-i` | Mover archivos | `mv -vi archivo.txt /destino/` | Mueve `archivo.txt` preguntando si sobrescribir |
| `rm` | `-r`, `-f`, `-v` | Borrar archivos | `rm -rf carpeta/` | Borra carpeta sin pedir confirmación |
| `chmod` | `+x`, `755` | Cambiar permisos | `chmod +x script.sh` | Hace ejecutable `script.sh` |
| `chown` | `usuario:grupo` | Cambiar propietario | `chown pepe:users archivo.txt` | Asigna archivo a usuario `pepe` |
| `find` | `-name`, `-size` | Buscar archivos | `find /home -name "*.sh"` | Busca scripts `.sh` en `/home` |

# 📅 3. Planificación y Automatización de Tareas

| Comando | Parámetro(s) útil(es) | Descripción breve | Ejemplo de comando | Ejemplo de ejecución |
|:--------|:----------------------|:------------------|:-------------------|:---------------------|
| `crontab` | `-l`, `-e` | Tareas programadas | `crontab -l` | Lista las tareas cron del usuario |

# 📶 4. Redes y Comunicaciones

| Comando | Parámetro(s) útil(es) | Descripción breve | Ejemplo de comando | Ejemplo de ejecución |
|:--------|:----------------------|:------------------|:-------------------|:---------------------|
| `ping` | `-c n` | Comprobar conectividad | `ping -c 4 google.com` | Envía 4 paquetes a Google |
| `traceroute` | *(destino)* | Rastrear ruta de paquetes | `traceroute google.com` | Muestra el camino hasta Google |
| `scp` | `-r`, `-P` | Copiar archivos por SSH | `scp archivo.txt usuario@192.168.1.10:/home/usuario/` | Copia archivo vía SSH |
| `ssh` | *(usuario@servidor)* | Conexión remota segura | `ssh usuario@192.168.1.10` | Conectarse a otro sistema |
| `curl` | `-I`, `-L` | Realizar peticiones HTTP | `curl -I https://google.com` | Ver cabeceras HTTP de una web |
| `wget` | `URL` | Descargar archivos vía HTTP/FTP | `wget http://example.com/file.txt` | Descarga un archivo |

# 💻 5. Información del Sistema

| Comando | Parámetro(s) útil(es) | Descripción breve | Ejemplo de comando | Ejemplo de ejecución |
|:--------|:----------------------|:------------------|:-------------------|:---------------------|
| `uname` | `-a`, `-r`, `-m` | Info sistema | `uname -a` | Muestra todo sobre el sistema operativo |
| `hostname` | *(sin parámetros)* | Nombre del host | `hostname` | Muestra nombre de la máquina |
| `uptime` | *(sin parámetros)* | Tiempo encendido | `uptime` | Dice cuánto lleva encendido el sistema |
| `df` | `-h`, `-T` | Espacio disco | `df -hT` | Muestra espacio libre y tipo de filesystem |
| `free` | `-h` | Uso de memoria | `free -h` | Muestra RAM usada y libre |
| `who` | *(sin parámetros)* | Usuarios conectados | `who` | Muestra quién está conectado |

# 📖 6. Manipulación de Texto

| Comando | Parámetro(s) útil(es) | Descripción breve | Ejemplo de comando | Ejemplo de ejecución |
|:--------|:----------------------|:------------------|:-------------------|:---------------------|
| `grep` | `-i`, `-r` | Buscar en texto | `grep -i error /var/log/syslog` | Busca "error" en syslog |
| `awk` | `'{print $1}'` | Procesar columnas de texto | `ps -e -o comm= | awk '{print $1}'` | Lista nombres de procesos |
| `cut` | `-d ' ' -f n` | Cortar delimitado | `echo "uno,dos,tres" | cut -d ',' -f 2` | Devuelve `dos` |
| `sed` | `s/buscar/reemplazar/` | Reemplazar texto | `echo "linux rules" | sed 's/linux/unix/'` | Muestra `unix rules` |

# 💡 Recomendaciones
- **Practicar scripts** combinando comandos de cada tema.
- **Hacer proyectos pequeños** como backup automático, monitor de red, etc.
- **Explicar la importancia de los permisos** (`chmod`, `chown`) en seguridad.
- **Integrar automatización** con `crontab` para gestionar tareas periódicas.

---

¿Quieres ejemplos de mini-scripts organizados también por tema? (por ejemplo: script de backup, monitor de conexión de red, gestor de procesos...)
🚀
