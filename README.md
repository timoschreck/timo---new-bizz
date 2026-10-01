# Timo Schreck – persönliche Homepage

Schlanke Kontaktseite im DIR4B-Design. Der endgültige Homepage-Name und die Kontaktkanäle werden nachgereicht. Aktuell: Konzept, Originalbilder, CI-Kopie, Masterprompt und lokale Seitenvorschau. Keine Veröffentlichung oder aktive Kontaktintegration.

## Einstieg

- [Master und offene Entscheidungen](docs/master/START.md)
- [Masterprompt für die Herstellung](docs/prompts/MASTERPROMPT-HOMEPAGE.md)
- [Öffentliche Texte](docs/inhalte/homepage-texte.md)
- [Interne Angebotsgrundlage](docs/konzept/gesamtmaster.md)
- [Design und Bewegung](docs/design/design-und-motion.md)
- [Kontaktwege](docs/kontakt/kontaktwege.md)
- [Bildregister](assets/images/manifest.json)
- [CI-Herkunft](vendor/dir4b/PROVENANCE.json)

## Fachbereiche

| Bereich | Ablage |
|---|---|
| Steuerung und Entscheidungen | docs/master/ |
| Leitbild und Angebote | docs/konzept/ |
| Öffentliche Inhalte | docs/inhalte/ |
| Design und Bewegungsreferenz | docs/design/ |
| Kontakt und Übergaben | docs/kontakt/ |
| Umsetzungsprompt | docs/prompts/ |
| Originalbilder und Webfassungen | assets/images/ |
| Originale DIR4B-Designquellen | vendor/dir4b/ |
| Seitenvorschau | index.html, styles.css, site.js |
| Offene Konfiguration | config/site.json |

## Vorschau

`python -m http.server 8080` im Repository; danach `http://localhost:8080` öffnen. Alternativ index.html direkt öffnen. Die Vorschau zeigt die Gestaltung und Bildintegration. Kontaktkarten sind absichtlich noch keine aktiven Kanäle.

## Prüfung

`python scripts/validate.py` prüft Konfiguration, lokale Assets und Quellenhashes. Browserprüfungen liegen in docs/umsetzung/VALIDIERUNG.md.
