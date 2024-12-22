#!/usr/bin/env python3

import os
import subprocess

def install_dependencies():
    """
    Memastikan semua dependensi yang diperlukan terinstal.
    """
    print("[*] Memeriksa dan menginstal dependensi...")
    try:
        # Update Termux dan install OpenVPN
        os.system("pkg update && pkg upgrade -y")
        os.system("pkg install openvpn -y")
        os.system("pkg install python -y")
        print("[*] Semua dependensi telah diinstal.")
    except Exception as e:
        print(f"[!] Gagal menginstal dependensi: {e}")
        exit(1)

def start_openvpn(config_path):
    """
    Menjalankan OpenVPN dengan file konfigurasi.
    """
    try:
        print("[*] Memulai OpenVPN...")
        # Pastikan file konfigurasi ada
        if not os.path.exists(config_path):
            print(f"[!] File konfigurasi tidak ditemukan: {config_path}")
            return
        # Jalankan OpenVPN dengan file konfigurasi
        subprocess.run(["openvpn", "--config", config_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Terjadi kesalahan saat menjalankan OpenVPN: {e}")
    except KeyboardInterrupt:
        print("\n[!] VPN dihentikan oleh pengguna.")
    finally:
        print("[*] OpenVPN selesai.")

def main():
    """
    Fungsi utama untuk menjalankan script.
    """
    print("""
====================================
    OpenVPN Client for Termux
====================================
    """)
    # Cek dan install dependensi jika diperlukan
    install_dependencies()
    
    # Minta path file konfigurasi .ovpn
    config_path = input("Masukkan path file konfigurasi (.ovpn): ").strip()
    if not os.path.isfile(config_path):
        print(f"[!] File konfigurasi tidak ditemukan: {config_path}")
        return
    
    # Jalankan OpenVPN
    start_openvpn(config_path)

if __name__ == "__main__":
    main()
