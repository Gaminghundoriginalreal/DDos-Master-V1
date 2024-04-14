import subprocess
import socket
import pyfiglet

def get_own_ip():
    """Funktion, um die eigene IP-Adresse zu erhalten."""
    try:
        # Öffne eine Verbindung zu einem externen Server, um die eigene IP-Adresse zu ermitteln
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        own_ip = s.getsockname()[0]
        s.close()
        return own_ip
    except Exception as e:
        print("Fehler beim Abrufen der eigenen IP-Adresse:", e)
        return None

def ping_ip(ip_address):
    try:
        own_ip = get_own_ip()

        if ip_address == own_ip:
            print("Du kannst deine eigene IP nicht anpingen.")
            return

        # Führe den Ping-Befehl aus
        ping_process = subprocess.Popen(['ping', '-n', '10000', ip_address], stdout=subprocess.PIPE)

        # Gib die Ausgabe des Ping-Befehls auf der Konsole aus
        while True:
            output = ping_process.stdout.readline().decode('utf-8')
            if output == '' and ping_process.poll() is not None:
                break
            print(output.strip())

    except KeyboardInterrupt:
        # Wenn der Benutzer Strg+C drückt, stoppe den Ping-Prozess
        ping_process.terminate()
        print("\nPing-Prozess gestoppt.")

if __name__ == "__main__":
    # Anzeige des ASCII-Art-Banners
    ascii_banner = pyfiglet.figlet_format("IP Pinger")
    print(ascii_banner)

    print("Willkommen zum IP-Pinger!")
    print("Hinweis: Du kannst deine eigene IP nicht anpingen.")

    ip_address = input("Geben Sie die IP-Adresse ein, die Sie anpingen möchten: ")
    print(f"Pinge {ip_address} an... (Strg+C zum Beenden)")
    ping_ip(ip_address)
