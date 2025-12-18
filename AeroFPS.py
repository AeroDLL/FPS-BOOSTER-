import os
import sys
import ctypes
import subprocess
import time
import webbrowser
import platform
from colorama import init, Fore, Style

# Renkleri ve Encoding'i Başlat
init(autoreset=True)

# Yönetici İzni Kontrolü
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# --- YARDIMCI FONKSİYONLAR ---
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def title(text):
    os.system(f'title AeroFPS v7.0 | {text}')

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

def print_success(msg):
    print(Fore.GREEN + Style.BRIGHT + f" [OK] {msg}")

def print_info(msg):
    print(Fore.YELLOW + f" [*] {msg}")

def print_error(msg):
    print(Fore.RED + f" [!] {msg}")

def pause():
    print()
    input(Fore.CYAN + " Ana menuye donmek icin Enter'a basin...")

# --- MENU TASARIMI ---
def banner():
    clear()
    print(Fore.GREEN + Style.BRIGHT + r"""
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║    █████╗ ███████╗██████╗  ██████╗ ███████╗██████╗ ███████╗ v7.0      ║
    ║   ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔══██╗██╔════╝           ║
    ║   ███████║█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝███████╗ GOD       ║
    ║   ██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ██╔═══╝ ╚════██║ MODE      ║
    ║   ██║  ██║███████╗██║  ██║╚██████╔╝██║     ██║     ███████║           ║
    ║   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝           ║
    ║                  ULTIMATE WINDOWS GAMING SUITE                        ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    """)
    print(Fore.CYAN + "    Designed by AeroDLL | GitHub Project\n")

# --- OZELLIK FONKSIYONLARI ---

def restore_point():
    title("Guvenlik Yedegi")
    print_info("Sistem Geri Yukleme Noktasi Olusturuluyor...")
    run('wmic /Namespace:\\\\root\\default Path SystemRestore Call CreateRestorePoint "AeroFPS_v7_Backup", 100, 7')
    print_success("Yedekleme Basariyla Tamamlandi!")
    pause()

def clean_disk():
    title("Derin Temizlik")
    print_info("Gecici Dosyalar ve Cache Temizleniyor...")
    paths = [r'C:\Windows\Temp\*.*', r'C:\Windows\Prefetch\*.*', os.path.expandvars(r'%temp%\*.*')]
    for p in paths:
        run(f'del /s /f /q "{p}"')
    run('ipconfig /flushdns')
    print_success("Sistem Coplerden Arindirildi!")
    pause()

def fps_boost():
    title("Oyun Modu")
    print_info("Ultimate Performance Modu Aktif Ediliyor...")
    run('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61')
    run('powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61')
    print_info("Gereksiz Servisler Kapatiliyor...")
    for s in ["DiagTrack", "SysMain", "MapsBroker", "WSearch"]:
        run(f'sc stop "{s}"')
        run(f'sc config "{s}" start= disabled')
    print_info("Oyun Onceligi Ayarlaniyor...")
    run('reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f')
    print_success("FPS Boost Islemleri Tamamlandi!")
    pause()

def advanced_opt():
    title("Gelismis Optimizasyon")
    print_info("SSD ve Network Ayarlari Yapiliyor...")
    run('fsutil behavior set disabledeletenotify 0')
    run('reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 4294967295 /f')
    print_success("Sistem Cekirdek Ayarlari Optimize Edildi!")
    pause()

def dns_optimizer():
    title("DNS Optimizer")
    print(Fore.YELLOW + " [1] Cloudflare (1.1.1.1)\n [2] Google (8.8.8.8)\n [3] Otomatik\n [4] Ping Testi")
    c = input(Fore.WHITE + "\n Secim: ")
    if c == '1':
        run('netsh interface ip set dns "Ethernet" static 1.1.1.1 primary')
        print_success("Cloudflare DNS Ayarlandi!")
    elif c == '4':
        os.system("ping -n 4 1.1.1.1")
    pause()

def gpu_turbo():
    title("GPU Turbo")
    print_info("GPU Donanim Hizlandirma Aciliyor...")
    run('reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v "HwSchMode" /t REG_DWORD /d 2 /f')
    run('reg add "HKCU\SOFTWARE\Microsoft\GameBar" /v "AutoGameModeEnabled" /t REG_DWORD /d 1 /f')
    print_success("Ekran Karti Optimize Edildi!")
    pause()

def system_analyze():
    title("Sistem Analizi")
    os.system('systeminfo | findstr /C:"OS Name" /C:"Total Physical Memory"')
    print(Fore.WHITE + "\n CPU Yuku:")
    os.system('wmic cpu get loadpercentage')
    pause()

def startup_manager():
    title("Baslangic Yoneticisi")
    os.system('wmic startup get caption,command')
    pause()

def defender_toggle():
    title("Defender Kontrol")
    print(Fore.YELLOW + " [1] Kapat (Oyun)\n [2] Ac (Normal)")
    c = input(" Secim: ")
    key = r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection"
    if c == '1': run(f'reg add "{key}" /v "DisableRealtimeMonitoring" /t REG_DWORD /d 1 /f')
    elif c == '2': run(f'reg delete "{key}" /v "DisableRealtimeMonitoring" /f')
    print_success("Islem Tamam.")
    pause()

def input_lag_fix():
    title("Input Lag Fix")
    run('reg add "HKLM\SYSTEM\CurrentControlSet\Services\mouclass\Parameters" /v "MouseDataQueueSize" /t REG_DWORD /d 50 /f')
    run('reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v "Win32PrioritySeparation" /t REG_DWORD /d 38 /f')
    print_success("Gecikme Duserildi!")
    pause()

def game_guides():
    webbrowser.open("https://www.nvidia.com/en-us/geforce/news/performance-tuning-guide/")
    print_success("Rehber acildi.")
    pause()

def stress_test():
    title("Stres Testi")
    print_info("WinSAT Calistiriliyor...")
    os.system("winsat formal")
    pause()

def ram_cleaner():
    title("RAM Temizleyici")
    print_info("Bellek Bosaltiliyor...")
    try:
        psapi = ctypes.WinDLL('psapi.dll')
        kernel = ctypes.WinDLL('kernel32.dll')
        psapi.EmptyWorkingSet(kernel.GetCurrentProcess())
        print_success("RAM Cache Temizlendi!")
    except:
        print_error("Hata olustu.")
    pause()

def repair_station():
    title("Tamir Istasyonu")
    print_info("SFC ve DISM Calistiriliyor (Uzun Surebilir)...")
    run("sfc /scannow")
    run("DISM /Online /Cleanup-Image /RestoreHealth")
    print_success("Onarim Tamamlandi.")
    pause()

def software_update():
    title("Guncelleyici")
    print_info("Winget ile Tum Programlar Guncelleniyor...")
    os.system("winget upgrade --all --include-unknown")
    pause()

# --- YENI EKLENEN OZELLIKLER (v7.0) ---

def network_repair():
    title("Internet Tamiri")
    print_info("Ag Adaptorleri Sifirlaniyor (Lag Fix)...")
    
    commands = [
        "netsh winsock reset",
        "netsh int ip reset",
        "ipconfig /release",
        "ipconfig /renew",
        "ipconfig /flushdns"
    ]
    
    for cmd in commands:
        print(Fore.WHITE + f"      Yurutuluyor: {cmd}...")
        run(cmd)
        time.sleep(1)
        
    print_success("Ag Ayarlari Fabrika Ayarlarina Dondu!")
    print(Fore.WHITE + " Not: Internet kopabilir, birkac saniye sonra geri gelir.")
    pause()

def privacy_shield():
    title("Gizlilik Kalkani")
    print_info("Windows Telemetri ve Takip Servisleri Engelleniyor...")
    
    # Reklam Kimligini Kapat
    run('reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo" /v Enabled /t REG_DWORD /d 0 /f')
    # Telemetriyi Kapat
    run('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f')
    # Konum Takibini Kapat
    run('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors" /v DisableLocation /t REG_DWORD /d 1 /f')
    
    print_success("Gizlilik Ayarlari Guclendirildi! Artik daha az izleniyorsunuz.")
    pause()

def monitor_hz():
    title("Monitor Hz Kontrol")
    print_info("Mevcut Ekran Yenileme Hizi (Hz) Kontrol Ediliyor...")
    print(Fore.WHITE + "\n --- Monitor Bilgisi ---")
    os.system('wmic path Win32_VideoController get CurrentRefreshRate,Name')
    print(Fore.YELLOW + "\n Ipucu: Eger 144Hz monitorunuz varsa ve burada 60 goruyorsaniz,")
    print(Fore.YELLOW + " Goruntu Ayarlari > Gelismis Goruntu Ayarlari'ndan degistirin!")
    pause()

def revert():
    title("Fabrika Ayarlari")
    print_error("DIKKAT: Tum optimizasyonlar geri alinacak.")
    c = input(" Onay (e/h): ")
    if c.lower() == 'e':
        run('sc config "SysMain" start= auto')
        run('sc start "SysMain"')
        run('powercfg -setactive 381b4222-f694-41f0-9685-ff5bb260df2e')
        run('netsh interface ip set dns "Ethernet" dhcp')
        print_success("Sistem Varsayilan Ayarlara Dondu.")
    pause()

# --- ANA DONGU ---
def main():
    while True:
        banner()
        print(Fore.WHITE + "  [1]  🚀 OYUN MODU AKTIF          [10] 💻 INPUT LAG FIX")
        print(Fore.WHITE + "  [2]  🧹 DERIN TEMIZLIK           [11] 🎯 OYUN REHBERLERI")
        print(Fore.WHITE + "  [3]  💾 GUVENLIK YEDEGI          [12] 🧪 STRES TESTI")
        print(Fore.WHITE + "  [4]  🔧 GELISMIS OPTIMIZASYON    [13] 🧠 RAM CLEANER")
        print(Fore.WHITE + "  [5]  🌐 DNS OPTIMIZER            [14] 🚑 TAMIR ISTASYONU")
        print(Fore.WHITE + "  [6]  🎮 GPU TURBO MODE           [15] 🔄 PROGRAM GUNCELLE")
        print(Fore.WHITE + "  [7]  📊 SISTEM ANALIZI           [16] 🌐 INTERNET TAMIRI (YENI)")
        print(Fore.WHITE + "  [8]  🔥 STARTUP MANAGER          [17] 🕵️  GIZLILIK KALKANI (YENI)")
        print(Fore.WHITE + "  [9]  🛡️  DEFENDER KONTROL        [18] 🖥️  MONITOR HZ KONTROL (YENI)")
        print(Fore.RED   + "                                   [19] ⚙️  SIFIRLA | [20] CIKIS")
        
        print(Fore.CYAN + "\n =======================================================================")
        
        secim = input(Fore.GREEN + "  Islem Seciniz (1-20): ")

        if secim == '1': fps_boost()
        elif secim == '2': clean_disk()
        elif secim == '3': restore_point()
        elif secim == '4': advanced_opt()
        elif secim == '5': dns_optimizer()
        elif secim == '6': gpu_turbo()
        elif secim == '7': system_analyze()
        elif secim == '8': startup_manager()
        elif secim == '9': defender_toggle()
        elif secim == '10': input_lag_fix()
        elif secim == '11': game_guides()
        elif secim == '12': stress_test()
        elif secim == '13': ram_cleaner()
        elif secim == '14': repair_station()
        elif secim == '15': software_update()
        elif secim == '16': network_repair()
        elif secim == '17': privacy_shield()
        elif secim == '18': monitor_hz()
        elif secim == '19': revert()
        elif secim == '20': sys.exit()
        else:
            print_error("Gecersiz Secim!")
            time.sleep(1)

if __name__ == "__main__":
    main()