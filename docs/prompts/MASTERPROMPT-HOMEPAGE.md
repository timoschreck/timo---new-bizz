# Masterprompt zur Herstellung der persönlichen Homepage

Du setzt die persönliche Homepage von Timo Schreck in diesem Repository um. Arbeite wie ein erfahrener Webdesigner und Entwickler. Die Aufgabe ist eine schlanke professionelle Kontaktseite im DIR4B-Design. Halte den genehmigten Umfang ein und führe ihn zu einer überprüfbaren Umsetzung.

## Quellen zuerst

Lies AGENTS.md, docs/master/START.md, PROJECT_STATUS.md, docs/master/entscheidungen.md, docs/inhalte/homepage-texte.md, docs/design/design-und-motion.md, docs/kontakt/kontaktwege.md, config/site.json, assets/images/manifest.json und vendor/dir4b/PROVENANCE.json. Interne Vertiefung in docs/konzept/gesamtmaster.md dient nur dem Verständnis. Kein DIR4B-Masterauftrag und keine Produkt-App-Aufgabe.

## Ziel und Leitbild

Strategischer Projektpartner für Geschäftsentwicklung und Digitalisierung. Ein fester Ansprechpartner koordiniert Ziele, Expertise und Umsetzung mit Kundenperspektive. Texte auf Deutsch, präzise und persönlich, ohne übertriebene Kompetenz- oder Erfolgsbehauptungen.

## Umfang

Eine kompakte responsive Seite mit vier Bereichen: Einstieg; drei kurze Leistungsfelder; persönliches Vertrauen; Kontakt. Keine Preise/Paketbuchung, langen Phasenpläne, erfundenen Kundenreferenzen, Testimonials oder neuen Bereiche. Endgültiger Homepage-Name wird später geliefert. Bis dahin nur Timo Schreck als Arbeitsbezeichnung, keine erfundene Domain.

## Design

DIR4B-CI aus vendor/dir4b unverändert referenzieren: dunkler Nachthimmel, Cyan/Blau/Violett, sparsame Magenta-Akzente, Originalverläufe, ruhige Flächen, klare Typografie. Eigenes CSS von Quellenkopien trennen. Logos weder kursiv umzeichnen noch Buchstaben verändern. Keine DIR4B-Firmendaten oder Rechtstexte übertragen.

## Bewegung

Vorhandenen animierten kosmischen SVG-Hintergrund nutzen. Hintergrund soll wie die Nutzerreferenz des DIR4B-Pitch-Videos wirken. Lies den belegten Referenzpfad und die noch offene Sichtprüfung in docs/design/design-und-motion.md. Bei verfügbarem Zugriff Video anschauen und Motion abstimmen; ohne Zugriff die Einschränkung offen dokumentieren, keine Gleichheit behaupten. Langsame zurückhaltende Bewegung, sichtbarer Pausenschalter, statischer Zustand bei reduced-motion. Keine Sprache, Pitchtexte oder Musik als Hintergrund.

## Bilder

Nur die vier freigegebenen Motive aus manifest.json nutzen. Porträt im Einstieg; Kundengespräch und Whiteboard passend zur Unterstützung; Naturmotiv beim persönlichen Abschnitt. Auf der schmalen Seite als gezielte Bildakzente, nicht als zusätzliche lange Galerie. Originale behalten und WebP-Webfassungen nutzen. Alt-Texte ehrlich: generierte Szene beschreiben, keine tatsächlichen Kundentermine behaupten. Keine Gesichts- oder Körperänderungen. Keine abgelehnten Varianten wiederherstellen.

## Kontakt

Hauptbutton Lassen Sie uns sprechen führt zu Kontakt. Kontaktwege werden noch erstellt. Kein Linkziel raten, keine privaten Angaben aus anderen Projekten übernehmen. Konfiguration aus config/site.json lesen. Solange enabled=false/target=null nur transparente Vorschau, kein angeblicher Versand/Buchung. Nach konkreter Einrichtung Formular, E-Mail, Telefon/Rückruf und Kalender entsprechend Auswahl anbinden. Echte Zustellung/Buchung prüfen. Fachgespräche mit Spezialisten dürfen stattfinden; Timo bündelt Informationen und Koordination.

## Umsetzung

Bestehende statische Vorschau weiterverwenden, solange für den Umfang ausreichend. Keine unnötigen Frameworks, Abos, Tracker oder Integrationen. Namens- und Kontaktkonfiguration zentral halten. Semantisches HTML, responsive Bilder, schnelle Webassets, Tastaturbedienung, klare Fokuszustände und lesbare Kontraste. Text und Dateien gemäß Quellen halten. Impressum/Datenschutz als offene Veröffentlichungsvoraussetzungen anhand tatsächlicher Daten bearbeiten.

## Abnahme

1. Vier Inhaltsbereiche; Leitbild und Kontakt-CTA sofort erkennbar.
2. CI-Farben/Originale korrekt, Hintergrund bewegt und pausierbar; reduced-motion statisch.
3. Alle Bilddateien lokal vorhanden und passend eingebaut; keine Verzerrung.
4. Keine öffentlichen Preise, ungeprüften Aufträge, erfundene Partner oder fertige Qualifikationen.
5. Keine falschen Kontakt-/Versandfunktionen. Erst eingerichtete Kanäle aktiv.
6. Desktop/Smartphone prüfen, Überläufe/Bildfehler/Browserfehler beheben.
7. Quellen, Änderungen, Prüfungen und offene Schritte in PROJECT_STATUS.md und docs/umsetzung dokumentieren.

Vorschau und Repository sichern. Dieses Paket umfasst keine Veröffentlichung. Berichte konkret, welche Funktionen geprüft sind und welche Angaben noch fehlen. Nicht nochmals nach bereits entschiedenen Konzeptfragen fragen.
