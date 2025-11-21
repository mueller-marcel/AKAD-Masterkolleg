# AKAD-Masterkolleg

Dieses Repository enthält den Code für die Prüfungsaufgabe des Moduls ROB84. Das vorliegende Programm führt eine automatisierte Befragung der LLMs zum Framing-Effekt anhand der angegebenen Parametrisierung durch.

## 🔧 Build-Anleitung

1. Repository klonen
```bash
   git clone https://github.com/mueller-marcel/AKAD-Masterkolleg.git
```

2. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

3. Programm ausführen
```bash
python3 main.py
```

> [!NOTE]  
> Im Projekt wurde anstelle des API-Keys für die OpenAI-API ein Platzhalter angegeben.
> Er befindet sich in der Zeile `os.environ["OPENAI_API_KEY"] = "<API KEY>"` und sollte durch einen validen API-Key ersetzt werden, um das Programm lauffähig zu machen.

## ⚙️ Parametrisierung

Für die Durchführung des Verhaltensexperiments werden verschiedene Konfigurationsmöglichkeiten genutzt, welche nachstehehend erläutert werden

### Modell und Temperatur

Für die Durchführung des Verhaltensexperiments wurden die Modelle `gpt-5` und `gpt4` verwendet. Sie können in der Konstante `MODEL` in der Datei `main.py` angegeben werden.
Die Temperatur kann mit der Konstante `TEMPERATURE` konfiguriert werden. Es sind Fließkommazahlen zwischen 0 und 2 zulässig.

### Parametrisierung des Risikoprofils

Das Risikoprofil oder Persona kann in der Datei `main.py` konfiguriert werden. Hierfür steht die Klasse `RiskProfile` zur Verfügung.
Die Klassenvariablen dieser Klasse enthalten bilden die Parametrisierung des Risikoprofils analog zum Fragebogen ab.

| Parameter | Wertebereich | Bedeutung |
|-----------|--------------|-----------|
| age       | x > 0        | Alter der Testperson |
| profession | Freitext | Beruf der Testperson |
| maritial_status | "alleinlebend", "in Partnerschaft", "verheiratet", "mit Familie" | Beziehungsstatus der Testperson |
| decision_style | 1-7 | Entscheidungsstil der Testperson (Erklärung der numerischen Werte im Fragebogen auf Seite 4) |
| information_style | 1-7 | Informationsstil der Testperson (Erklärung der numerischen Werte im Fragebogen auf Seite 4) |
| time_preference | "INSECURE", "NOW", "LATER" | Zeitpräferenz der Testperson |

## 📚 Bibliotheken

Es wurden folgende Bibliotheken für die Lösung der Aufgabe verwendet. Diese werden in der `requirements.txt` angegeben und können über diese Datei installiert werden.

- openai
