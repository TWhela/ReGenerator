"""Desktop window for generating presets."""

import queue
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, ttk

from . import data, inventory
from .cli import DEFAULT_OUTPUT_DIR
from .generator import (SEXES, NpcRequest, generate_npc, next_preset_index,
                        preset_filename, write_npc)

ANY = "Any"
BOTH = "Both"

ETHNICITY_CHOICES = [ANY] + [inventory.ETHNICITY_LABELS[key] for key in data.ethnicities]
ETHNICITY_BY_LABEL = {inventory.ETHNICITY_LABELS[key]: key for key in data.ethnicities}

AGE_CHOICES = [ANY, "Young", "Middle", "Old"]
AGE_BY_LABEL = {"Young": "yo1", "Middle": "md1", "Old": "ol1"}

POLL_INTERVAL_MS = 80


class ReGeneratorApp(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=12)
        self.grid(sticky="nsew")
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.output_dir = tk.StringVar(value=DEFAULT_OUTPUT_DIR)
        self.ethnicity = tk.StringVar(value=ETHNICITY_CHOICES[1])
        self.sex = tk.StringVar(value=BOTH)
        self.age = tk.StringVar(value=ANY)
        self.count = tk.IntVar(value=5)
        self.androgynous = tk.BooleanVar(value=False)
        self.status = tk.StringVar(value="Ready")

        self._results = queue.Queue()

        self._build_controls().grid(row=0, column=0, sticky="ew")
        self._build_tally().grid(row=1, column=0, sticky="ew", pady=(12, 0))
        self._build_log().grid(row=2, column=0, sticky="nsew", pady=(12, 0))
        self._build_status().grid(row=3, column=0, sticky="ew", pady=(8, 0))

        self.refresh_tally()

    # Layout ---------------------------------------------------------------

    def _build_controls(self):
        frame = ttk.LabelFrame(self, text="Generate", padding=10)
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="Race").grid(row=0, column=0, sticky="w", pady=3)
        ttk.Combobox(frame, textvariable=self.ethnicity, values=ETHNICITY_CHOICES,
                     state="readonly", width=14).grid(row=0, column=1, sticky="w")

        ttk.Label(frame, text="Sex").grid(row=1, column=0, sticky="w", pady=3)
        ttk.Combobox(frame, textvariable=self.sex, values=[BOTH] + SEXES,
                     state="readonly", width=14).grid(row=1, column=1, sticky="w")

        ttk.Label(frame, text="Age").grid(row=2, column=0, sticky="w", pady=3)
        ttk.Combobox(frame, textvariable=self.age, values=AGE_CHOICES,
                     state="readonly", width=14).grid(row=2, column=1, sticky="w")

        ttk.Label(frame, text="How many").grid(row=3, column=0, sticky="w", pady=3)
        spin = ttk.Frame(frame)
        spin.grid(row=3, column=1, sticky="w")
        ttk.Spinbox(spin, from_=1, to=200, textvariable=self.count,
                    width=6).grid(row=0, column=0)
        ttk.Label(spin, text="of each sex").grid(row=0, column=1, padx=(8, 0))

        ttk.Checkbutton(frame, text="Androgynous",
                        variable=self.androgynous).grid(row=4, column=1, sticky="w", pady=3)

        ttk.Label(frame, text="Folder").grid(row=5, column=0, sticky="w", pady=(8, 3))
        folder = ttk.Frame(frame)
        folder.grid(row=5, column=1, sticky="ew", pady=(8, 3))
        folder.columnconfigure(0, weight=1)
        ttk.Entry(folder, textvariable=self.output_dir).grid(row=0, column=0, sticky="ew")
        ttk.Button(folder, text="Browse", command=self.choose_folder,
                   width=9).grid(row=0, column=1, padx=(6, 0))

        self.generate_button = ttk.Button(frame, text="Generate", command=self.generate)
        self.generate_button.grid(row=6, column=1, sticky="e", pady=(10, 0))

        return frame

    def _build_tally(self):
        frame = ttk.LabelFrame(self, text="Already in this folder", padding=10)
        frame.columnconfigure(0, weight=1)

        self.tally_view = ttk.Treeview(
            frame, columns=("male", "female", "total"), show="tree headings", height=3
        )
        self.tally_view.heading("#0", text="Race")
        self.tally_view.column("#0", width=140, anchor="w")
        for column, heading in (("male", "Male"), ("female", "Female"), ("total", "Total")):
            self.tally_view.heading(column, text=heading)
            self.tally_view.column(column, width=70, anchor="center", stretch=False)
        self.tally_view.grid(row=0, column=0, sticky="ew")

        ttk.Button(frame, text="Refresh", command=self.refresh_tally,
                   width=9).grid(row=1, column=0, sticky="e", pady=(8, 0))
        return frame

    def _build_log(self):
        frame = ttk.LabelFrame(self, text="Last run", padding=10)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        self.log = tk.Text(frame, height=7, wrap="none", state="disabled")
        self.log.grid(row=0, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.log.yview)
        scroll.grid(row=0, column=1, sticky="ns")
        self.log.configure(yscrollcommand=scroll.set)
        return frame

    def _build_status(self):
        frame = ttk.Frame(self)
        frame.columnconfigure(0, weight=1)
        ttk.Label(frame, textvariable=self.status, anchor="w").grid(row=0, column=0, sticky="ew")
        return frame

    # Actions --------------------------------------------------------------

    def choose_folder(self):
        chosen = filedialog.askdirectory(title="Where should presets be written?")
        if chosen:
            self.output_dir.set(chosen)
            self.refresh_tally()

    def refresh_tally(self, note=None):
        """Redraw the tally. `note` is prefixed to the folder summary in the status bar."""
        presets = inventory.scan(self.output_dir.get())
        counts = inventory.tally(presets)

        self.tally_view.delete(*self.tally_view.get_children())
        grand = 0
        for key, label in inventory.ETHNICITY_LABELS.items():
            row = counts[key]
            total = row["Male"] + row["Female"]
            grand += total
            self.tally_view.insert("", "end", text=label,
                                   values=(row["Male"], row["Female"], total))

        unreadable = sum(1 for preset in presets if not preset.is_recognised)
        summary = f"{grand} preset{'' if grand == 1 else 's'} in {self.output_dir.get()}"
        if unreadable:
            summary += f", {unreadable} not recognised"
        self.status.set(f"{note}. {summary}" if note else summary)

    def requests(self):
        """One NpcRequest per sex being generated, with the chosen race and age applied."""
        ethnicity = ETHNICITY_BY_LABEL.get(self.ethnicity.get())
        age = AGE_BY_LABEL.get(self.age.get())
        sexes = SEXES if self.sex.get() == BOTH else [self.sex.get()]

        return [
            (sex, NpcRequest(
                sex=sex,
                primary_ethnicity=ethnicity,
                age=age,
                androgynous=self.androgynous.get(),
            ))
            for sex in sexes
        ]

    def generate(self):
        try:
            count = int(self.count.get())
        except (tk.TclError, ValueError):
            self.status.set("How many must be a whole number")
            return
        if count < 1:
            self.status.set("How many must be at least 1")
            return

        self.generate_button.state(["disabled"])
        self.status.set("Generating...")
        self._write_log(["Generating..."])

        worker = threading.Thread(
            target=self._generate_worker,
            args=(self.requests(), count, self.output_dir.get()),
            daemon=True,
        )
        worker.start()
        self.after(POLL_INTERVAL_MS, self._poll_worker)

    def _generate_worker(self, requests, count, output_dir):
        written = []
        try:
            for sex, request in requests:
                start = next_preset_index(output_dir, sex)
                for index in range(start, start + count):
                    path = write_npc(generate_npc(request),
                                     Path(output_dir) / preset_filename(sex, index))
                    written.append(path)
        except Exception as error:
            self._results.put(("error", written, f"{type(error).__name__}: {error}"))
        else:
            self._results.put(("ok", written, None))

    def _poll_worker(self):
        try:
            outcome, written, message = self._results.get_nowait()
        except queue.Empty:
            self.after(POLL_INTERVAL_MS, self._poll_worker)
            return

        lines = [f"Created {path}" for path in written]
        if outcome == "error":
            lines.append(f"Stopped: {message}")
            note = f"Stopped after {len(written)}: {message}"
        else:
            note = f"Created {len(written)} preset{'' if len(written) == 1 else 's'}"

        self._write_log(lines or ["Nothing was generated"])
        self.generate_button.state(["!disabled"])
        self.refresh_tally(note)

    def _write_log(self, lines):
        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.insert("1.0", "\n".join(lines))
        self.log.configure(state="disabled")


def main():
    root = tk.Tk()
    root.title("ReGenerator")
    root.minsize(470, 640)
    try:
        ttk.Style().theme_use("vista")
    except tk.TclError:
        pass
    ReGeneratorApp(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
