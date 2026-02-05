# Metalcore Piano Lab

A research‑oriented web rhythm game prototype that explores automatic chart generation from audio for metalcore/prog‑core music. The system focuses on onset detection, tempo estimation, adaptive sectioning, and perceptual alignment to build playable piano‑style charts with multi‑lane difficulty settings.

> This project is a lightweight, browser‑native prototype for studying rhythm perception, chart consistency across repeated sections, and player feedback alignment.

---

## Features

- **Automatic chart generation** from uploaded audio (browser‑side)
- **Onset detection + tempo estimation** for rhythmic structure
- **Adaptive sectioning** to stabilize repeated musical segments
- **Beat tracking & time signature estimation** (4/4, 5/4, 7/8, etc.)
- **Multi‑lane difficulty** (4/6/8 keys)
- **Key estimation** for harmonically aligned SFX
- **Real‑time feedback** with particle hits and customizable SFX
- **Aesthetic UI** tuned for a dark, minimal, high‑contrast feel

---

## How It Works (High‑Level)

1. **Audio preprocessing**  
   Band‑limited filtering + pre‑emphasis highlight transient activity.

2. **Onset detection**  
   Energy‑based novelty curve with adaptive thresholding yields candidate onsets.

3. **Tempo estimation**  
   Inter‑onset interval clustering provides a robust BPM estimate.

4. **Beat alignment & sectioning**  
   Onsets are softly quantized against a beat grid and grouped into sections by energy change.

5. **Template alignment**  
   Section templates are derived from dominant onset positions to maintain consistency.

---

## Usage

1. Open `index.html` in a browser  
2. Upload a local audio file (`mp3/wav/m4a`)  
3. Click **Analyze** to generate the chart  
4. Play with D/F/J/K or expand to 6/8 keys

---

## Notes on Limitations

- This is a **browser‑native prototype**, so full stem separation is not feasible here.  
- Complex polymeter or extreme tempo changes may reduce chart accuracy.  
- The algorithm is intentionally lightweight for responsiveness and ease of deployment.

---

## Research Extensions (Planned)

- Full stem separation (drums / guitar / vocals) for improved chart accuracy  
- Section‑aware repetition modeling  
- Adaptive meter inference (non‑fixed time signature)  
- Player‑adaptive chart difficulty scaling

---

## License

MIT (or specify your preferred license)

---

## Author

Haze_zzZ (Fay Lyu)
