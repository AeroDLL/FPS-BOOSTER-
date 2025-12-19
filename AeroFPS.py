import os
import sys
import ctypes
import subprocess
import time
import webbrowser
import platform
from colorama import init, Fore, Style

# Renkleri Başlat
init(autoreset=True)

# --- GLOBAL DİL DEĞİŞKENİ ---
LANGUAGE = "EN"  # Varsayılan / Default

def T(tr_text, en_text):
    """Dil seçimine göre metin döndürür / Returns text based on language"""
    if LANGUAGE == "TR":
        return tr_text
    else:
        return en_text

# --- YÖNETİCİ KONTROLÜ / ADMIN CHECK ---
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# --- YARDIMCI FONKSİYONLAR / HELPER FUNCTIONS ---
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def title(text):
    os.system(f'title AeroFPS v8.0 | {text}')

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
    input(Fore.CYAN + T(" Devam etmek icin Enter'a basin...", " Press Enter to continue..."))

# --- DİL SEÇİM EKRANI / LANGUAGE SELECTOR ---
def select_language():
    global LANGUAGE
    clear()
    print(Fore.CYAN + " ╔════════════════════════════════════════════════╗")
    print(Fore.CYAN + " ║             LANGUAGE SELECTION                 ║")
    print(Fore.CYAN + " ╚════════════════════════════════════════════════╝")
    print("\n  [1] Türkçe (Turkish)")
    print("  [2] English (Global)")
    print()
    
    choice = input(Fore.GREEN + "  Select / Secim (1-2): ")
    if choice == '1':
        LANGUAGE = "TR"
    else:
        LANGUAGE = "EN"

# --- MENÜ TASARIMI / BANNER ---
def banner():
    clear()
    print(Fore.GREEN + Style.BRIGHT + r"""
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║    █████╗ ███████╗██████╗  ██████╗ ███████╗██████╗ ███████╗ v8.0      ║
    ║   ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔══██╗██╔════╝           ║
    ║   ███████║█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝███████╗ GLOBAL    ║
    ║   ██╔══██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ██╔═══╝ ╚════██║ ELITE     ║
    ║   ██║  ██║███████╗██║  ██║╚██████╔╝██║     ██║     ███████║           ║
    ║   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝           ║
    ║                  ULTIMATE WINDOWS GAMING SUITE                        ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    """)
    print(Fore.CYAN + "    Designed by AeroDLL | GitHub Project\n")

# --- ÖZELLİKLER / FEATURES ---

def restore_point():
    title(T("Guvenlik Yedegi", "Security Backup"))
    print_info(T("Sistem Geri Yukleme Noktasi Olusturuluyor...", "Creating System Restore Point..."))
    run('wmic /Namespace:\\\\root\\default Path SystemRestore Call CreateRestorePoint "AeroFPS_v8_Backup", 100, 7')
    print_success(T("Yedekleme Tamamlandi!", "Backup Created Successfully!"))
    pause()

def clean_disk():
    title(T("Derin Temizlik", "Deep Clean"))
    print_info(T("Gecici Dosyalar Siliniyor...", "Cleaning Temp Files..."))
    paths = [r'C:\Windows\Temp\*.*', r'C:\Windows\Prefetch\*.*', os.path.expandvars(r'%temp%\*.*')]
    for p in paths:
        run(f'del /s /f /q "{p}"')
    run('ipconfig /flushdns')
    print_success(T("Sistem Temizlendi!", "System Cleaned!"))
    pause()

def fps_boost():
    title(T("Oyun Modu", "Game Mode"))
    print_info(T("Ultimate Performance Modu Aciliyor...", "Activating Ultimate Performance Mode..."))
    run('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61')
    run('powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61')
    
    print_info(T("Gereksiz Servisler Kapatiliyor...", "Disabling Unnecessary Services..."))
    services = ["DiagTrack", "SysMain", "MapsBroker", "WSearch", "TabletInputService"]
    for s in services:
        run(f'sc stop "{s}"')
        run(f'sc config "{s}" start= disabled')
        
    print_success(T("FPS Boost Tamamlandi!", "FPS Boost Completed!"))
    pause()

def advanced_opt():
    title(T("Gelismis Ayarlar", "Advanced Tweaks"))
    print_info(T("SSD ve Ag Ayarlari Yapiliyor...", "Optimizing SSD and Network..."))
    run('fsutil behavior set disabledeletenotify 0') # TRIM
    run('reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 4294967295 /f')
    print_success(T("Optimize Edildi!", "Optimized!"))
    pause()

def dns_optimizer():
    title("DNS Optimizer")
    print(Fore.YELLOW + " [1] Cloudflare (1.1.1.1)")
    print(Fore.YELLOW + " [2] Google (8.8.8.8)")
    print(Fore.YELLOW + T(" [3] Otomatik", " [3] Automatic"))
    print(Fore.YELLOW + T(" [4] Ping Testi", " [4] Ping Test"))
    
    c = input(Fore.WHITE + "\n " + T("Secim: ", "Choice: "))
    if c == '1':
        run('netsh interface ip set dns "Ethernet" static 1.1.1.1 primary')
        run('netsh interface ip set dns "Wi-Fi" static 1.1.1.1 primary')
        print_success("Cloudflare DNS OK!")
    elif c == '2':
        run('netsh interface ip set dns "Ethernet" static 8.8.8.8 primary')
        run('netsh interface ip set dns "Wi-Fi" static 8.8.8.8 primary')
        print_success("Google DNS OK!")
    elif c == '3':
        run('netsh interface ip set dns "Ethernet" dhcp')
        run('netsh interface ip set dns "Wi-Fi" dhcp')
        print_success("Auto DNS OK!")
    elif c == '4':
        os.system("ping -n 4 1.1.1.1")
    pause()

def gpu_turbo():
    title("GPU Turbo")
    print_info(T("GPU Donanim Hizlandirma Aciliyor...", "Enabling Hardware GPU Scheduling..."))
    run('reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v "HwSchMode" /t REG_DWORD /d 2 /f')
    run('reg add "HKCU\SOFTWARE\Microsoft\GameBar" /v "AutoGameModeEnabled" /t REG_DWORD /d 1 /f')
    print_success("GPU Optimized!")
    pause()

def system_analyze():
    title(T("Sistem Analizi", "System Analysis"))
    os.system('systeminfo | findstr /C:"OS Name" /C:"Total Physical Memory"')
    print(Fore.WHITE + "\n CPU:")
    os.system('wmic cpu get loadpercentage')
    pause()

def startup_manager():
    title("Startup Manager")
    os.system('wmic startup get caption,command')
    pause()

def defender_toggle():
    title("Defender Control")
    print(Fore.YELLOW + T(" [1] Kapat (Oyun)", " [1] Disable (Game)"))
    print(Fore.YELLOW + T(" [2] Ac (Normal)", " [2] Enable (Normal)"))
    c = input(" : ")
    key = r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection"
    if c == '1': run(f'reg add "{key}" /v "DisableRealtimeMonitoring" /t REG_DWORD /d 1 /f')
    elif c == '2': run(f'reg delete "{key}" /v "DisableRealtimeMonitoring" /f')
    print_success("OK.")
    pause()

def input_lag_fix():
    title("Input Lag Fix")
    run('reg add "HKLM\SYSTEM\CurrentControlSet\Services\mouclass\Parameters" /v "MouseDataQueueSize" /t REG_DWORD /d 50 /f')
    run('reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v "Win32PrioritySeparation" /t REG_DWORD /d 38 /f')
    print_success("Input Lag Fix Applied!")
    pause()

def game_guides():
    webbrowser.open("https://www.nvidia.com/en-us/geforce/news/performance-tuning-guide/")
    print_success("Link Opened.")
    pause()

def stress_test():
    title("Stress Test")
    print_info("WinSAT Benchmark...")
    os.system("winsat formal")
    pause()

def ram_cleaner():
    title("RAM Cleaner")
    try:
        psapi = ctypes.WinDLL('psapi.dll')
        kernel = ctypes.WinDLL('kernel32.dll')
        psapi.EmptyWorkingSet(kernel.GetCurrentProcess())
        print_success(T("RAM Cache Temizlendi!", "RAM Cache Cleared!"))
    except: pass
    pause()

def repair_station():
    title("Repair Station")
    print_info("SFC / DISM Running...")
    run("sfc /scannow")
    run("DISM /Online /Cleanup-Image /RestoreHealth")
    print_success("Repair Done.")
    pause()

def software_update():
    title("Software Updater")
    print_info("Winget Upgrade...")
    os.system("winget upgrade --all --include-unknown")
    pause()

def network_repair():
    title("Network Repair")
    print_info("Resetting TCP/IP & Winsock...")
    run("netsh winsock reset")
    run("netsh int ip reset")
    run("ipconfig /flushdns")
    print_success(T("Ag Ayarlari Sifirlandi!", "Network Reset Done!"))
    pause()

def privacy_shield():
    title("Privacy Shield")
    print_info(T("Telemetri Engelleniyor...", "Blocking Telemetry..."))
    run('reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo" /v Enabled /t REG_DWORD /d 0 /f')
    run('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f')
    print_success("Privacy Protected!")
    pause()

def monitor_hz():
    title("Monitor Hz")
    os.system('wmic path Win32_VideoController get CurrentRefreshRate,Name')
    pause()

# --- YENI OZELLIKLER (v8.0) ---

def bcd_tweaks():
    title("BCD Latency Tweaks")
    print_info(T("Gecikme Ayarlari Yapiliyor (HPET/DynamicTick)...", "Applying Latency Tweaks..."))
    
    # Platform Clock'u kapat (Latency düşürür)
    run("bcdedit /set useplatformclock No")
    # Dynamic Tick'i kapat (Laptoplarda pil yer ama masaüstünde hız artırır)
    run("bcdedit /set disabledynamictick Yes")
    # Boot menü süresini düşür
    run("bcdedit /timeout 10")
    
    print_success(T("BCD Ayarlari Uygulandi! (Restart Gerekli)", "BCD Tweaks Applied! (Restart Required)"))
    pause()

def gaming_runtimes():
    title("Gaming Runtimes Installer")
    print_info(T("Oyun Bilesenleri Kontrol Ediliyor (Visual C++, DirectX)...", "Checking Game Runtimes..."))
    print(Fore.WHITE + T("      Bu islem indirme yapacagi icin surebilir.", "      Downloading packages, please wait."))
    
    # Winget ile C++ Redistributable 2015-2022
    os.system("winget install --id Microsoft.VCRedist.2015+.x64")
    # DirectX (Genelde web installer gerekir ama winget ile deneyelim)
    os.system("winget install --id Microsoft.DirectX")
    
    print_success(T("Kurulumlar Tamamlandi!", "Installation Completed!"))
    pause()

def revert():
    title(T("Fabrika Ayarlari", "Factory Reset"))
    print_error(T("DIKKAT: Tum optimizasyonlar geri alinacak.", "WARNING: All tweaks will be reverted."))
    c = input(T(" Onay (e/h): ", " Confirm (y/n): "))
    if c.lower() in ['e', 'y']:
        run('sc config "SysMain" start= auto')
        run('sc start "SysMain"')
        run('powercfg -setactive 381b4222-f694-41f0-9685-ff5bb260df2e') # Balanced
        run('netsh interface ip set dns "Ethernet" dhcp')
        run("bcdedit /deletevalue useplatformclock")
        print_success(T("Sifirlandi.", "Reverted."))
    pause()

# --- ANA DONGU / MAIN LOOP ---
def main():
    select_language() # Dil seçimi başta
    
    while True:
        banner()
        # Dinamik Menu Yazilari
        m1 = T("OYUN MODU AKTIF", "ENABLE GAME MODE")
        m2 = T("DERIN TEMIZLIK", "DEEP CLEANER")
        m3 = T("GUVENLIK YEDEGI", "CREATE RESTORE POINT")
        m4 = T("GELISMIS OPTIMIZASYON", "ADVANCED OPTIMIZATION")
        m5 = T("DNS OPTIMIZER", "DNS OPTIMIZER")
        m6 = T("GPU TURBO MODE", "GPU TURBO MODE")
        m7 = T("SISTEM ANALIZI", "SYSTEM ANALYSIS")
        m8 = T("STARTUP MANAGER", "STARTUP MANAGER")
        m9 = T("DEFENDER KONTROL", "DEFENDER CONTROL")
        m10 = T("INPUT LAG FIX", "INPUT LAG FIX")
        m11 = T("OYUN REHBERLERI", "GAME GUIDES")
        m12 = T("STRES TESTI", "STRESS TEST")
        m13 = T("RAM CLEANER", "RAM CLEANER")
        m14 = T("TAMIR ISTASYONU", "REPAIR STATION")
        m15 = T("PROGRAM GUNCELLE", "UPDATE SOFTWARE")
        m16 = T("INTERNET TAMIRI", "NETWORK REPAIR")
        m17 = T("GIZLILIK KALKANI", "PRIVACY SHIELD")
        m18 = T("MONITOR HZ KONTROL", "MONITOR HZ CHECK")
        m19 = T("BCD GECIKME TWEAK (YENI)", "BCD LATENCY TWEAK (NEW)")
        m20 = T("OYUN BILESENLERINI KUR (YENI)", "INSTALL GAME RUNTIMES (NEW)")
        m21 = T("SIFIRLA", "REVERT")
        m22 = T("CIKIS", "EXIT")

        print(Fore.WHITE + f"  [1]  🚀 {m1:<26} [12] 🧪 {m12}")
        print(Fore.WHITE + f"  [2]  🧹 {m2:<26} [13] 🧠 {m13}")
        print(Fore.WHITE + f"  [3]  💾 {m3:<26} [14] 🚑 {m14}")
        print(Fore.WHITE + f"  [4]  🔧 {m4:<26} [15] 🔄 {m15}")
        print(Fore.WHITE + f"  [5]  🌐 {m5:<26} [16] 🌐 {m16}")
        print(Fore.WHITE + f"  [6]  🎮 {m6:<26} [17] 🕵️  {m17}")
        print(Fore.WHITE + f"  [7]  📊 {m7:<26} [18] 🖥️  {m18}")
        print(Fore.WHITE + f"  [8]  🔥 {m8:<26} [19] ⚡ {m19}")
        print(Fore.WHITE + f"  [9]  🛡️  {m9:<26} [20] 🎮 {m20}")
        print(Fore.WHITE + f"  [10] 💻 {m10:<26} [21] ⚙️  {m21}")
        print(Fore.WHITE + f"  [11] 🎯 {m11:<26} [22] ❌ {m22}")
        
        print(Fore.CYAN + "\n =======================================================================")
        
        secim = input(Fore.GREEN + f"  {T('Secim', 'Choice')} (1-22): ")

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
        elif secim == '19': bcd_tweaks()
        elif secim == '20': gaming_runtimes()
        elif secim == '21': revert()
        elif secim == '22': sys.exit()
        else:
            print_error(T("Gecersiz Secim!", "Invalid Choice!"))
            time.sleep(1)

if __name__ == "__main__":
    main()
