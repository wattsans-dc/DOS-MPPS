import socket
import time
import threading

def send_packets(destination_ip, destination_port, packet_size, packets_per_second):
    """Envoie des paquets vers l'adresse et le port spécifiés."""
    message = b'A' * packet_size
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    start_time = time.time()
    while time.time() - start_time < 1:
        for _ in range(packets_per_second // 1000):
            sock.sendto(message, (destination_ip, destination_port))
        time.sleep(0.001)
    sock.close()

def main():
    destination_ip = input("Entrez l'adresse IP de destination : ")
    destination_port = int(input("Entrez le port de destination : "))
    mpps = float(input("Entrez le nombre de mpps (millions de paquets par seconde) : "))
    
    packet_size = 64  # Taille du paquet en octets (64 octets est une taille courante pour les tests)
    packets_per_second = int(mpps * 1e6)  # Conversion de mpps en paquets par seconde
    
    print(f"Envoi de {packets_per_second} paquets par seconde vers {destination_ip}:{destination_port}")
    
    threads = []
    for _ in range(10):  # Utilisation de 10 threads pour mieux répartir la charge
        thread = threading.Thread(target=send_packets, args=(destination_ip, destination_port, packet_size, packets_per_second // 10))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
