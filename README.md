# 💪 Tabla "Navaja Suiza" de Comandos Linux para Scripting

## Comandos más útiles

| Comando | Parámetro(s) útil(es) | Descripción breve | Ejemplo de comando | Ejemplo de ejecución |
|:--------|:----------------------|:------------------|:-------------------|:---------------------|
| `ps` | `-e`, `-o pid,comm` | Listar procesos | `ps -e -o pid,comm` | Muestra todos los procesos y sus nombres |
| `kill` | `-9 pid` | Matar un proceso | `kill -9 1234` | Mata el proceso con PID 1234 |
| `pkill` | `nombre` | Matar proceso por nombre | `pkill firefox` | Mata todos los procesos `firefox` |
| `grep` | `-i`, `-r` | Buscar en texto | `grep -i error /var/log/syslog` | Busca "error" en syslog sin distinguir mayúsculas/minúsculas |
| `find` | `-name`, `-size` | Buscar archivos | `find /home -name "*.sh"` | Busca scripts `.sh` en `/home` |
| `awk` | `'{print $1}'` | Procesar columnas de texto | `ps -e -o comm= | awk '{print $1}'` | Lista solo los nombres de procesos |
| `cut` | `-d ' ' -f n` | Cortar delimitado | `echo "uno,dos,tres" | cut -d ',' -f 2` | Devuelve `dos` |
| `sed` | `s/buscar/reemplazar/` | Reemplazar texto | `echo "linux rules" | sed 's/linux/unix/'` | Muestra `unix rules` |
| `tar` | `-czvf`, `-xzvf` | Comprimir/descomprimir archivos | `tar -czvf backup.tar.gz carpeta/` | Comprime carpeta a backup.tar.gz |
| `cp` | `-r`, `-u`, `-v` | Copiar archivos | `cp -ru origen/ destino/` | Copia solo archivos nuevos o actualizados |
| `mv` | `-v`, `-i` | Mover archivos | `mv -vi archivo.txt /destino/` | Mueve `archivo.txt` preguntando si sobrescribir |
| `rm` | `-r`, `-f`, `-v` | Borrar archivos | `rm -rf carpeta/` | Borra carpeta sin pedir confirmación |
| `chmod` | `+x`, `755` | Cambiar permisos | `chmod +x script.sh` | Hace ejecutable `script.sh` |
| `chown` | `usuario:grupo` | Cambiar propietario | `chown pepe:users archivo.txt` | Asigna archivo a usuario `pepe` |
| `date` | `+%Y-%m-%d` | Formato de fecha | `date "+%Y-%m-%d %H:%M:%S"` | Imprime la fecha actual formateada |
| `uptime` | *(sin parámetros)* | Tiempo encendido | `uptime` | Dice cuánto lleva encendido el sistema |
| `df` | `-h`, `-T` | Espacio disco | `df -hT` | Muestra espacio libre y tipo de filesystem |
| `free` | `-h` | Uso de memoria | `free -h` | Muestra RAM usada y libre |
| `who` | *(sin parámetros)* | Usuarios conectados | `who` | Muestra quién está conectado |
| `uname` | `-a`, `-r`, `-m` | Info sistema | `uname -a` | Muestra todo sobre el sistema operativo |
| `hostname` | *(sin parámetros)* | Nombre del host | `hostname` | Muestra nombre de la máquina |
| `crontab` | `-l`, `-e` | Tareas programadas | `crontab -l` | Lista las tareas cron del usuario |
| `scp` | `-r`, `-P` | Copiar por SSH | `scp archivo.txt usuario@192.168.1.10:/home/usuario/` | Copia archivo a servidor remoto |
| `ssh` | *(usuario@servidor)* | Conectar remoto | `ssh usuario@192.168.1.10` | Conecta vía terminal al servidor remoto |

---

# 💡 Recomendación
- Combina estos comandos en scripts para automatizar tareas.
- Puedes agruparlos según:
  - **Procesos:** `ps`, `kill`, `pkill`
  - **Archivos:** `cp`, `mv`, `rm`, `find`, `tar`
  - **Sistema:** `uname`, `uptime`, `df`, `free`
  - **Red:** `scp`, `ssh`
  - **Automatización:** `crontab`

---

# 🚀 Siguiente paso
¿Quieres ejemplos de **mini-scripts** combinando estos comandos para tareas reales? (como "backup automático", "limpieza de logs", "monitorización de CPU"...)
