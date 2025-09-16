#!/usr/bin/env python3
# vega_launcher.py
import sys
import os
import json
import subprocess
import webbrowser
import logging
import base64
from typing import Any
from functools import partial

from PyQt5.QtWidgets import (
    QApplication,
    QSystemTrayIcon,
    QMenu,
    QDialog,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QAction,
)
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor, QFont
from PyQt5.QtCore import Qt

# import traduzioni e gestione lingua
from translations import i18n, t, load_config_language, save_config_language

# ---------------- Configurabili ----------------
ICON_BASE64 = "iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAAbEAAAGxAGo1xHEAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAABTZJREFUeNrlW8Fx3TgMRTy+Ww1koq0gbCCz7CA65hZuBVEHUQkqQalglQ7kmS1AqSDKIaccIp9y2sFeqAwNgyAhUc73hjMc2/r8Ih8IPIAA/QwR4Xdu1/8jLNb32ncDADfC+FsAsE9dAE3Qb34XDagBoAUAJ4C+BYAVAGbmMwcAL56iAJzvfzKffQKAAQBGAFgyTOVJCaABgD5c9A7QYVv9z+rSBVB5gK/J8w8A0ClB0/f+FMT1Be/6QGz81pvAUnKiSxRADwDvgr+/eNIbyTjjBQUAMPmub4h4Kb1CxBnvt94/D8cZRJzwYZsR0WbMs/rxAyJejABMsDD0vzcZ47jWJoS8te5SBEBBzYhYRxa/MOMqDyZ8h4vMZYMxzSUIgIIfGJXfeheMG5lxjmgCJ8RwjP3VAuDAS+O33V+EMQ0REv18DEwMEBGenXAaDA8jVWTMTNzcB+/iRL4ODzHCuAEA3vrf/wjcZgUA3x/MV2Ana088M+5rQ+Y8S2D70jhL1ZxR/58EewS4i7ijM8BTDmgS6+IEEKp/tVcAG+MuDJjF++3WT1wLO6MFv829BiBMgleWiPu7N69mAW3EB0+JHdnMZE0QVE5vSKzQCnO0ZO1bM1oBmIh9DxFXw/WJaEp10PRSbYxozgMPsmcyDXDuHTbTzLbeRIhuiYDvBe5wGgH0jKqbA3abClNj5wHpe87v9uQ3xgimt3KaF1vEqIivpT4qSU9ypfbg/D03JrUDy45d54gnx+4bEudXxHxm5fw2Z36J7MYDZEUZuVH6eZvD4ArTi2qPdBw1B5h6ItyhdXGDdIJTzi+aXkh4ayTJ4JSa0GacynI4YGSCLqucf06tnaqNixDRGmHZlOp3BbJCGhKl0WZSi6XgZ9ihFSUCnoo5Y7gdvJPzHchZTK5WtDsWnQJkM4VINafPnUebwJC0YiW7/6uSqZPm+3sndImgxeHjZZUWDemVEEBKK/49eNg5kkxVz1tSDbf27RHAN4pkqtivCl5O2NqPkytHHQD8TcpmbVD0VLWrgrW8rT0/uVj6nvnM7H3pVcFMMK3ll2zG1/7eBs/uSrz46qTd6oWU+B7tmgDgZfDsI9G66mwBmOACktS++p83Xl2PatVI7P0OAP4i4GGv/efUBWoSlq6RA8k25h8SHww7Wb5jAi7K9PZgsiTpBmOVWC61NJL4f90pBC7XFxP6qQLggoxBiLUdiQK575sE8CmS3a0ykq2mpACkCEsqTy0kmcJpEM0tvokAXzPC6XBDoJQAJPBD4rRFixYdIr4S0tdSTj8nqltKHLyk83QM/Jqpltq2KlJe1d7TnySAORO8ySCyKRNwCEITy7sDWad7/TqI3F4GFxCt961hrf0ueG6FW1mT/9ww/nq7GzD54OWzf7YofXlD7gPA0TigZYiK2/leSVSa7G21Q/3noyfL0P5phoeCHwpWbDhVblF/T6AtJQCuFhgDv5JFHN2FVcHmVarWd9QNhqmuzR3FSHBg1LcJ3NOYWRPoFdrUFgizVRmhGHiuZhczkZQQ6kxQNMSuzxZADniM8MOkvA2SQ4Z9gRsm2QLIBe8Y8I4pTVcHybDODMSKCKAEeKMktxQZziWZXxJAafCaGkGMDPuSfl8SgAa8ywSvSVdzZNgUvFwlCmBWgK8iO6y9+5siQ5txL7CIAGzkSkxsly0DsgR46TTZ4ElFFgqoTYCnhIXM5YqjAcr6mHVGzsWMGQvoCtz9zSHDDk8us6VUzykyt6XcU10y1NV4AbcTkD2BnVt8nPL6Kf8w8aTafw41tJXhReaoAAAAAElFTkSuQmCC"

ICON_RECOMMENDED_SIZE = 64

BASE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
DEFAULT_LINKS = os.path.join(BASE_DIR, "links.json")
DEFAULT_STATS = os.path.join(BASE_DIR, "stats.json")
LOG_FILE = os.path.join(BASE_DIR, "tray_launcher.log")
APP_NAME = "VegaLauncher"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(APP_NAME)


# ---------------- Utilities (links config) ----------------
def ensure_links_exist(config_path: str):
    d = os.path.dirname(config_path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    if not os.path.exists(config_path): # you can have submenu, url, cmd or path
        sample = [
            {"name": "🔎 Ecosia", "url": "https://www.ecosia.org"},
            {
                "name": "Sottomenù",
                "submenu": [
                    {"name": "🐧 FermoLUG", "url": "https://www.fermolug.org"},
                    {"name": "👨‍💻 Mas.si", "url": "https://www.mas.si"},
                    {"name": "🌐 Istruzioni", "url": "https://federicomassi.it/vega_laucher.html"},
                    {"name": "Vim (type \":q↩\" to exit)", "cmd": "vim"},
                ],
            },
        ]
        try:
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump({"links": sample}, f, indent=2, ensure_ascii=False)
            logger.info("Sample links.json created at %s", config_path)
        except Exception:
            logger.exception("Unable to create sample links.json")


def load_json(path: str) -> Any:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        logger.exception("Failed to read JSON %s", path)
        return None


def save_json(path: str, data: Any):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        logger.exception("Failed to save JSON %s", path)


# ---------------- Icon handling ----------------
def icon_from_base64(b64: str) -> QIcon or None:
    if not b64:
        return None
    try:
        data = base64.b64decode(b64)
        pix = QPixmap()
        if pix.loadFromData(data):
            return QIcon(pix)
    except Exception:
        logger.exception("Failed to load icon from base64")
    return None


def make_placeholder_icon(size: int = ICON_RECOMMENDED_SIZE) -> QIcon:
    pix = QPixmap(size, size)
    pix.fill(QColor(48, 63, 159))
    painter = QPainter(pix)
    try:
        painter.setPen(QColor(255, 255, 255))
        f = QFont()
        f.setBold(True)
        f.setPointSize(int(size * 0.35))
        painter.setFont(f)
        painter.drawText(pix.rect(), Qt.AlignCenter, "VL")
    finally:
        painter.end()
    return QIcon(pix)


# ---------------- Stats dialog ----------------
class StatsDialog(QDialog):
    def __init__(self, stats: dict, lang: str, parent=None):
        super().__init__(parent)
        self.lang = lang
        self.setWindowTitle(APP_NAME + " - " + t("stats", self.lang))
        self.resize(320, 420)
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.setWindowModality(Qt.ApplicationModal)

        layout = QVBoxLayout(self)

        text = "\n".join(
            [f"{k}: {v}" for k, v in sorted(stats.items(), key=lambda x: x[1], reverse=True)]
        ) or t("no_data", self.lang)

        self.textbox = QTextEdit()
        self.textbox.setReadOnly(True)
        self.textbox.setText(text)

        self.close_btn = QPushButton(t("close_window", self.lang))
        self.close_btn.clicked.connect(self.hide)  # nasconde la dialog

        layout.addWidget(self.textbox)
        layout.addWidget(self.close_btn)

    def refresh(self, stats: dict, lang: str = None):
        if lang:
            self.lang = lang
        self.setWindowTitle(APP_NAME + " - " + t("stats", self.lang))
        text = "\n".join(
            [f"{k}: {v}" for k, v in sorted(stats.items(), key=lambda x: x[1], reverse=True)]
        ) or t("no_data", self.lang)
        self.textbox.setText(text)
        self.close_btn.setText(t("close_window", self.lang))


# ---------------- Tray application ----------------
class TrayApp:
    def __init__(self, links_path: str = DEFAULT_LINKS, stats_path: str = DEFAULT_STATS):
        self.app = QApplication.instance() or QApplication(sys.argv)

        # percorsi
        self.links_path = links_path
        self.stats_path = stats_path

        # crea links.json se manca
        ensure_links_exist(self.links_path)
        if not os.path.exists(self.stats_path):
            save_json(self.stats_path, {})

        # carica dati
        self.config = {}
        self.stats = load_json(self.stats_path) or {}

        # lingua iniziale (caricata + file config creato se manca)
        self.lang = load_config_language()

        # GUI: tray
        self.tray = QSystemTrayIcon()
        icon = icon_from_base64(ICON_BASE64)
        if icon is None:
            icon = make_placeholder_icon(ICON_RECOMMENDED_SIZE)
        self.tray.setIcon(icon)
        self.tray.setToolTip(APP_NAME)

        # costruisci menu iniziale
        self.reload_config()

        self.tray.setVisible(True)

    def reload_config(self):
        cfg = load_json(self.links_path)
        if cfg is None:
            logger.error("Config load failed; keeping existing config")
        else:
            if isinstance(cfg, list):
                self.config = {"links": cfg}
            elif isinstance(cfg, dict) and "links" in cfg:
                self.config = cfg
            else:
                self.config = {"links": []}
            logger.info("Links config loaded from %s", self.links_path)
        menu = self.build_menu()
        self.tray.setContextMenu(menu)

    def build_menu(self) -> QMenu:
        menu = QMenu()
        links = self.config.get("links", []) if isinstance(self.config.get("links"), list) else []

        def add_entry(parent_menu: QMenu, entry: Any):
            if isinstance(entry, str):
                action = parent_menu.addAction(entry)
                action.triggered.connect(self._make_slot(self.open_url, entry, entry))
                return

            if not isinstance(entry, dict):
                return

            if entry.get("separator"):
                parent_menu.addSeparator()
                return

            name = entry.get("name", "(unnamed)")
            submenu = entry.get("submenu")
            if isinstance(submenu, list) and len(submenu) > 0:
                sub = QMenu(name, parent_menu)
                for e in submenu:
                    add_entry(sub, e)
                parent_menu.addMenu(sub)
                return

            if entry.get("url"):
                act = parent_menu.addAction(name)
                act.triggered.connect(self._make_slot(self.open_url, entry.get("url"), name))
                return
            if entry.get("cmd"):
                act = parent_menu.addAction(name)
                act.triggered.connect(self._make_slot(self.run_cmd, entry.get("cmd"), name))
                return
            if entry.get("path"):
                act = parent_menu.addAction(name)
                act.triggered.connect(self._make_slot(self.open_file, entry.get("path"), name))
                return

            disabled = parent_menu.addAction(name)
            disabled.setEnabled(False)

        # voci link dinamiche
        for ent in links:
            add_entry(menu, ent)

        menu.addSeparator()

        # voci fisse tradotte
        r = menu.addAction(f"↺ {t('reload', self.lang)}")
        r.triggered.connect(self._make_slot(self.reload_config))

        s = menu.addAction(f"ⓘ {t('stats', self.lang)}")
        s.triggered.connect(self._make_slot(self.show_stats))

        # Modifica (menu principale)
        edit_menu = QMenu(f"✎ {t('edit', self.lang)}", menu)
        # voce per aprire file links.json
        edit_links_act = edit_menu.addAction(t("links", self.lang))
        edit_links_act.triggered.connect(self._make_slot(self.edit_config))
        menu.addMenu(edit_menu)

        # Lingua come voce principale, subito dopo Modifica
        lang_menu = QMenu(t("language", self.lang), menu)
        self._lang_actions = {}
        for code, data in i18n.items():
            display_text = f"{data.get('flag','')} {data.get('name', code)}"
            lang_act = QAction(display_text, self.app, checkable=True)
            lang_act.setChecked(code == self.lang)
            lang_act.triggered.connect(partial(self.set_language, code))
            lang_menu.addAction(lang_act)
            self._lang_actions[code] = lang_act
        menu.addMenu(lang_menu)

        # Esci
        e = menu.addAction(f"🗙 {t('quit', self.lang)}")
        e.triggered.connect(self._make_slot(self.exit))

        return menu

    def set_language(self, lang_code: str, checked: bool = True):
        # select language and save choice in config.json; reload menu and stats dialog if opened
        self.lang = lang_code
        save_config_language(lang_code)
        logger.info("Language to %s", lang_code)
        # reload menu
        self.tray.setContextMenu(self.build_menu())
        # reload stats dialog (if opened)
        if hasattr(self, "stats_dialog") and self.stats_dialog is not None:
            self.stats_dialog.refresh(self.stats, lang=self.lang)

    def _make_slot(self, func, *args, **kwargs):
        def slot(checked: bool = False):
            try:
                func(*args, **kwargs)
            except Exception:
                logger.exception("Error in slot for %s", func)

        return slot

    def open_url(self, url: str, name: str or None = None):
        try:
            webbrowser.open(url)
            self._record_click(name or url)
        except Exception:
            logger.exception("Failed to open URL %s", url)

    def run_cmd(self, cmd: Any, name: str or None = None):
        try:
            if isinstance(cmd, list):
                subprocess.Popen(cmd)
            else:
                subprocess.Popen(cmd, shell=True)
            self._record_click(name or str(cmd))
        except Exception:
            logger.exception("Failed to run cmd %s", cmd)

    def open_file(self, path: str, name: str or None = None):
        try:
            full = path if os.path.isabs(path) else os.path.expanduser(os.path.join(os.path.dirname(self.links_path), path))
            if sys.platform.startswith("darwin"):
                subprocess.Popen(["open", full])
            elif os.name == "nt":
                os.startfile(full)
            else:
                subprocess.Popen(["xdg-open", full])
            self._record_click(name or full)
        except Exception:
            logger.exception("Failed to open file %s", path)

    def _record_click(self, key: str):
        try:
            self.stats = self.stats or {}
            self.stats[key] = self.stats.get(key, 0) + 1
            save_json(self.stats_path, self.stats)
        except Exception:
            logger.exception("Failed to record click")

    def show_stats(self):
        try:
            if not hasattr(self, "stats_dialog") or self.stats_dialog is None:
                self.stats_dialog = StatsDialog(self.stats, self.lang)
            else:
                self.stats_dialog.refresh(self.stats, lang=self.lang)
            if not self.stats_dialog.isVisible():
                self.stats_dialog.show()
            else:
                self.stats_dialog.raise_()
                self.stats_dialog.activateWindow()
        except Exception:
            logger.exception("Failed to show stats")

    def edit_config(self):
        try:
            if sys.platform.startswith("darwin"):
                subprocess.Popen(["open", self.links_path])
            elif os.name == "nt":
                os.startfile(self.links_path)
            else:
                subprocess.Popen(["xdg-open", self.links_path])
        except Exception:
            logger.exception("Impossible to open the file containing links")

    def exit(self):
        try:
            logger.info("Exiting...")
            save_json(self.stats_path, self.stats or {})
            self.tray.setVisible(False)
            QApplication.quit()
        except Exception:
            logger.exception("Error during exit")


# ------------------ main ------------------
def main():
    app = QApplication.instance() or QApplication(sys.argv)
    tray = TrayApp(links_path=DEFAULT_LINKS, stats_path=DEFAULT_STATS)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()