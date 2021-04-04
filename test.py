import sys
import time
from datetime import datetime
import curses
import psutil


class _Main(object):
    def __init__(self):
        self._width = None
        self._height = None
        self._stdscr = None

    def run(self):
        curses.wrapper(self._main)

    def _update_windowsize(self):
        self._height, self._width = self._stdscr.getmaxyx()

    def _main(self, stdscr):
        self._stdscr = stdscr
        self._stdscr.timeout(0)
        self._update_windowsize()
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)
        while True:
            kc = self._stdscr.getch()
            if kc == curses.KEY_RESIZE:
                self._update_windowsize()
            elif kc in (ord('q'), ord('Q')):
                break
            self._stdscr.clear()
            dps = [p.mountpoint for p in psutil.disk_partitions() if p.fstype]
            for y in range(len(dps)):
                p = dps[y]
                x = 5
                self._stdscr.addstr(y, x, p)
                u = psutil.disk_usage(p)
                # ---
                x += 5
                s = "{:.1f}".format(u.free / 1024**3).rjust(8) + " G / "
                self._stdscr.addstr(y, x, s)
                x += len(s) + 2
                s = "{:.1f}".format(u.total / 1024**3).rjust(8) + " G"
                self._stdscr.addstr(y, x, s)
                x += len(s) + 2
                # ---
                pct = 100. - u.percent
                s = "{:.1f}".format(pct).rjust(5) + " % "
                self._stdscr.addstr(y, x, s)
                #
                x += len(s) + 2
                pct /= 100
                c1 = int(pct * (self._width - 1 - x))
                self._stdscr.addstr(y, x, "_" * c1, curses.color_pair(2))
                x += c1
                self._stdscr.addstr(y, x, "_" * (self._width - 1 - x), curses.color_pair(3))
            time.sleep(1)
            self._stdscr.refresh()

