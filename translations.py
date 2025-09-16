import locale
import json
import os

CONFIG_FILE = "config.json"

i18n = i18n = {
  "ar": {
    "name": "العربية",
    "flag": "🇸🇦",
    "stats": "الإحصائيات",
    "quit": "خروج",
    "edit": "تحرير",
    "links": "روابط",
    "reload": "إعادة تحميل",
    "language": "اللغة",
    "about": "حول",
    "close_window": "إغلاق النافذة"
  },
  "bn": {
    "name": "বাংলা",
    "flag": "🇧🇩",
    "stats": "পরিসংখ্যান",
    "quit": "প্রস্থান",
    "edit": "সম্পাদনা",
    "links": "লিঙ্ক",
    "reload": "রিফ্রেশ",
    "language": "ভাষা",
    "about": "সম্বন্ধে",
    "close_window": "উইন্ডো বন্ধ করুন"
  },
  "da": {
    "name": "dansk",
    "flag": "🇩🇰",
    "stats": "Statistik",
    "quit": "Afslut",
    "edit": "Rediger",
    "links": "Links",
    "reload": "Opdater",
    "language": "Sprog",
    "about": "Om",
    "close_window": "Luk vindue"
  },
  "de": {
    "name": "Deutsch",
    "flag": "🇩🇪",
    "stats": "Statistiken",
    "quit": "Beenden",
    "edit": "Bearbeiten",
    "links": "Links",
    "reload": "Aktualisieren",
    "language": "Sprache",
    "about": "Über",
    "close_window": "Fenster schließen"
  },
  "en": {
    "name": "English",
    "flag": "🇬🇧",
    "stats": "Stats",
    "quit": "Quit",
    "edit": "Edit",
    "links": "Links",
    "reload": "Reload",
    "language": "Language",
    "about": "About",
    "close_window": "Close window"
  },
  "es": {
    "name": "español",
    "flag": "🇪🇸",
    "stats": "Estadísticas",
    "quit": "Salir",
    "edit": "Editar",
    "links": "Hiperenlaces",
    "reload": "Recargar",
    "language": "Idioma",
    "about": "Acerca de",
    "close_window": "Cerrar ventana"
  },
  "et": {
    "name": "eesti",
    "flag": "🇪🇪",
    "stats": "Statistika",
    "quit": "Välju",
    "edit": "Muuda",
    "links": "Lingid",
    "reload": "Värskenda",
    "language": "Keel",
    "about": "Teave",
    "close_window": "Sulge aken"
  },
  "fa": {
    "name": "فارسی",
    "flag": "🇮🇷",
    "stats": "آمار",
    "quit": "خروج",
    "edit": "ویرایش",
    "links": "پیوندها",
    "reload": "بارگذاری مجدد",
    "language": "زبان",
    "about": "درباره",
    "close_window": "بستن پنجره"
  },
  "fi": {
    "name": "suomi",
    "flag": "🇫🇮",
    "stats": "Tilastot",
    "quit": "Poistu",
    "edit": "Muokkaa",
    "links": "Linkit",
    "reload": "Päivitä",
    "language": "Kieli",
    "about": "Tietoja",
    "close_window": "Sulje ikkuna"
  },
  "fr": {
    "name": "français",
    "flag": "🇫🇷",
    "stats": "Statistiques",
    "quit": "Quitter",
    "edit": "Modifier",
    "links": "Liens",
    "reload": "Rafraîchir",
    "language": "Langue",
    "about": "À propos",
    "close_window": "Fermer la fenêtre"
  },
  "gu": {
    "name": "ગુજરાતી",
    "flag": "🇮🇳",
    "stats": "આંકડા",
    "quit": "બહાર નીકળો",
    "edit": "સંપાદિત કરો",
    "links": "લિંક્સ",
    "reload": "રીફ્રેશ કરો",
    "language": "ભાષા",
    "about": "વિશે",
    "close_window": "વિન્ડો બંધ કરો"
  },
  "hi": {
    "name": "हिन्दी",
    "flag": "🇮🇳",
    "stats": "आँकड़े",
    "quit": "बाहर जाएँ",
    "edit": "संपादित करें",
    "links": "लिंक",
    "reload": "रिफ्रेश",
    "language": "भाषा",
    "about": "के बारे में",
    "close_window": "विंडो बंद करें"
  },
  "id": {
    "name": "Bahasa Indonesia",
    "flag": "🇮🇩",
    "stats": "Statistik",
    "quit": "Keluar",
    "edit": "Edit",
    "links": "Tautan",
    "reload": "Muat ulang",
    "language": "Bahasa",
    "about": "Tentang",
    "close_window": "Tutup jendela"
  },
  "it": {
    "name": "italiano",
    "flag": "🇮🇹",
    "stats": "Statistiche",
    "quit": "Chiudi",
    "edit": "Modifica",
    "links": "Collegamenti",
    "reload": "Ricarica",
    "language": "Lingua",
    "about": "Informazioni",
    "close_window": "Chiudi finestra"
  },
  "ja": {
    "name": "日本語",
    "flag": "🇯🇵",
    "stats": "統計",
    "quit": "終了",
    "edit": "編集",
    "links": "リンク",
    "reload": "更新",
    "language": "言語",
    "about": "情報",
    "close_window": "ウィンドウを閉じる"
  },
  "ko": {
    "name": "한국어",
    "flag": "🇰🇷",
    "stats": "통계",
    "quit": "종료",
    "edit": "편집",
    "links": "링크",
    "reload": "새로고침",
    "language": "언어",
    "about": "정보",
    "close_window": "창 닫기"
  },
  "la": {
    "name": "latine",
    "flag": "🏛️",
    "stats": "Statistica",
    "quit": "Exire",
    "edit": "Emendare",
    "links": "Nexus",
    "reload": "Renovare",
    "language": "Lingua",
    "about": "De",
    "close_window": "Fenestram claude"
  },
  "mr": {
    "name": "मराठी",
    "flag": "🇮🇳",
    "stats": "आकडेवारी",
    "quit": "बाहेर पडा",
    "edit": "संपादित करा",
    "links": "दुवे",
    "reload": "रीफ्रेश करा",
    "language": "भाषा",
    "about": "विषयी",
    "close_window": "विंडो बंद करा"
  },
  "nl": {
    "name": "Nederlands",
    "flag": "🇳🇱",
    "stats": "Statistieken",
    "quit": "Afsluiten",
    "edit": "Bewerken",
    "links": "Links",
    "reload": "Vernieuwen",
    "language": "Taal",
    "about": "Over",
    "close_window": "Venster sluiten"
  },
  "no": {
    "name": "norsk",
    "flag": "🇳🇴",
    "stats": "Statistikk",
    "quit": "Avslutt",
    "edit": "Rediger",
    "links": "Lenker",
    "reload": "Oppdater",
    "language": "Språk",
    "about": "Om",
    "close_window": "Lukk vindu"
  },
  "pa": {
    "name": "ਪੰਜਾਬੀ",
    "flag": "🇮🇳",
    "stats": "ਅੰਕੜੇ",
    "quit": "ਬਾਹਰ ਜਾਓ",
    "edit": "ਸੰਪਾਦਿਤ ਕਰੋ",
    "links": "ਲਿੰਕ",
    "reload": "ਰੀਫ੍ਰੈਸ਼",
    "language": "ਭਾਸ਼ਾ",
    "about": "ਬਾਰੇ",
    "close_window": "ਵਿੰਡੋ ਬੰਦ ਕਰੋ"
  },
  "pl": {
    "name": "polski",
    "flag": "🇵🇱",
    "stats": "Statystyki",
    "quit": "Zakończ",
    "edit": "Edytuj",
    "links": "Linki",
    "reload": "Odśwież",
    "language": "Język",
    "about": "Informacje",
    "close_window": "Zamknij okno"
  },
  "pt": {
    "name": "português",
    "flag": "🇵🇹",
    "stats": "Estatísticas",
    "quit": "Sair",
    "edit": "Editar",
    "links": "Links",
    "reload": "Recarregar",
    "language": "Idioma",
    "about": "Sobre",
    "close_window": "Fechar janela"
  },
  "ro": {
    "name": "română",
    "flag": "🇷🇴",
    "stats": "Statistici",
    "quit": "Ieșire",
    "edit": "Editează",
    "links": "Linkuri",
    "reload": "Reîncarcă",
    "language": "Limbă",
    "about": "Despre",
    "close_window": "Închide fereastra"
  },
  "sw": {
    "name": "Kiswahili",
    "flag": "🇰🇪",
    "stats": "Takwimu",
    "quit": "Toka",
    "edit": "Hariri",
    "links": "Viungo",
    "reload": "Pakia upya",
    "language": "Lugha",
    "about": "Kuhusu",
    "close_window": "Funga dirisha"
  },
  "sv": {
    "name": "svenska",
    "flag": "🇸🇪",
    "stats": "Statistik",
    "quit": "Avsluta",
    "edit": "Redigera",
    "links": "Länkar",
    "reload": "Uppdatera",
    "language": "Språk",
    "about": "Om",
    "close_window": "Stäng fönster"
  },
  "tlh": {
    "name": "tlhIngan",
    "flag": "🖖",
    "stats": "lo’",
    "quit": "SoQmoH",
    "edit": "lIS",
    "links": "rar",
    "reload": "ghItlhqa’",
    "language": "Hol",
    "about": "Del",
    "close_window": "Qorwagh SoQmoH"
  },
  "tr": {
    "name": "Türkçe",
    "flag": "🇹🇷",
    "stats": "İstatistikler",
    "quit": "Çıkış",
    "edit": "Düzenle",
    "links": "Bağlantılar",
    "reload": "Yenile",
    "language": "Dil",
    "about": "Hakkında",
    "close_window": "Pencereyi kapat"
  },
  "uk": {
    "name": "українська",
    "flag": "🇺🇦",
    "stats": "Статистика",
    "quit": "Вийти",
    "edit": "Редагувати",
    "links": "Посилання",
    "reload": "Оновити",
    "language": "Мова",
    "about": "Про програму",
    "close_window": "Закрити вікно"
  },
  "vi": {
    "name": "Tiếng Việt",
    "flag": "🇻🇳",
    "stats": "Thống kê",
    "quit": "Thoát",
    "edit": "Chỉnh sửa",
    "links": "Liên kết",
    "reload": "Tải lại",
    "language": "Ngôn ngữ",
    "about": "Giới thiệu",
    "close_window": "Đóng cửa sổ"
  }
}





def get_system_language():
    # Rileva lingua di sistema (default 'en')
    lang, _ = locale.getdefaultlocale()
    if lang:
        code = lang.split("_")[0]
        if code in i18n:
            return code
    return "en"

def load_config_language():
    # Carica la lingua dal file di configurazione, o sistema se non esiste
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "language" in data and data["language"] in i18n:
                    return data["language"]
        except Exception:
            pass
    return get_system_language()

def save_config_language(lang):
    # Salva la lingua scelta nel file di configurazione
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"language": lang}, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving config: {e}")

def t(key, lang):
    # Restituisce la traduzione della chiave nella lingua scelta
    return i18n.get(lang, i18n["en"]).get(key, key)
