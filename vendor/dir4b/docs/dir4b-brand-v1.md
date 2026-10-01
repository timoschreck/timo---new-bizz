# DIR4B Markenreferenz v1.1.0

Stand: 05.09.2026. Verbindlich für neue Markenanwendungen; maschinenlesbare Quelle: [dir4b-brand-v1.json](dir4b-brand-v1.json). Änderungen an Name, Claims, Farben und Logo-Master erfordern eine neue dokumentierte Version. Die aktuelle Nutzerentscheidung zur Umstellung löst die frühere Markenbezeichnung ab.

## Name und Claims

**DIR4B** · ChatGPT-Projekt **dir4b STARTUP**.

Übergeordneter Markenclaim, exakt einschließlich Interpunktion:

**Business, Intelligently Orchestrated.**

Beleg: „Begrüßung fortsetzen“, Gespräch `6a9c4021-7bb0-83eb-b994-1dc5fcb1aabf`, Nutzerauswahl `bbb211ba-36e0-42ca-84cd-c39b2d203f02`. Auf die Rangliste mit diesem Claim auf Platz 1 folgt „Okay, wir nehmen die Eins.“ Die spätere Aussage im Domainchat, der Wortlaut sei nicht auffindbar, ist durch den Zugriff auf diese Originalquelle geklärt.

Die bestehenden drei auf `main` ausdrücklich verbindlichen Leitclaims bleiben wortgetreu:

| Kontext | Claim |
|---|---|
| Produkt | Eine Basis. Genau die Module, die du brauchst. |
| Integration | Was zusammengehört, arbeitet zusammen. |
| Wachstum | Einfach starten. Modular wachsen. |

Keine Übersetzung, Verkürzung oder neue Premium-Variante als freigegeben ausgeben. Andere im Chat vorgeschlagene Claims sind nicht ausgewählt. Campaign Assist besitzt eine belegte fachliche Leitidee in seiner Strategiedatei; sie ist kein zusätzlicher Dachmarkenclaim. Bestehende redaktionelle Headlines werden nicht automatisch zu Markenclaims.

## Visuelle Weiterentwicklung

Beibehalten: Sternen-Schwarz, Nachthimmel-Blau, Cyan, Blau, Violett, Magenta, Orbit-Linien, Datenpunkte, modulare Struktur sowie die vorhandenen Kern- und UI-Icons. Die Werte bleiben in den bestehenden Tokens erhalten.

Das frühere N-Signet und die NEXOVIA-Wortmarke werden durch ein geometrisches D mit diagonalem Orbit und Datenpunkt sowie die eigens gezeichnete DIR4B-Wortmarke ersetzt. Die Wortmarke besteht aus Pfaden, nicht aus einem ersetzten Textfont. Die bewusst reduzierte Geometrie ermöglicht monochrome und kleine Anwendungen. Das ist ein neuer Entwurf auf Basis der CI, keine behauptete Reinzeichnung der historischen JPG-Datei.

## Revision 1.1.0

Nutzerentscheidung vom 05.09.2026: Das einzelne D-Bildzeichen übernimmt in der horizontalen Fassung den ersten Buchstaben; direkt anschließend steht **IR4B**. D, I, R, 4 und B teilen Höhe und Grundlinie; alle Buchstaben stehen auf ausdrücklichen Nutzerwunsch in Großbuchstaben. Kein zusätzliches D vor der Fortsetzung. In Fließtext, Dateinamen und Alternativtexten bleibt die verbindliche Schreibweise **DIR4B**. Gestapelte Fassungen, Bildzeichen, Favicons, Farben und Claimwortlaut bleiben unverändert.

Alle 30 horizontalen Master mit ihren PNG-, WebP- und PDF-Exporten sowie die davon abhängigen Social-/Printvorlagen, Webanwendungen und das Brandbook verwenden diese Kombination. Der kompatible Pfad `v1/` bleibt bestehen; Git dokumentiert den vorherigen Stand und das Manifest die neue Version.

## Logo-Anwendung

SVG-Master und Exporte: `assets/logos/dir4b/v1/`. `dark` bezeichnet die Anwendung auf dunklem Grund mit heller Wortmarke; `light` die Anwendung auf hellem Grund mit dunkler Wortmarke. Beide Dateien selbst bleiben transparent. Monochrome Fassungen: `mono-white`, `mono-dark`, `mono-cyan`, `mono-violet`.

Horizontale und gestapelte Fassungen besitzen jeweils Varianten ohne Claim und mit jedem der vier freigegebenen Claims. Claim-Dateien tragen den Zusatz `_claim-premium`, `_claim-product`, `_claim-integration` oder `_claim-growth`. Bildzeichen und Favicons bleiben ohne Claim. PNG und WebP haben einen Alphakanal, PDF bewahrt die Vektorformen. Claims wurden aus dem dokumentierten Arial-Fallback in feste Pfade umgewandelt und benötigen zur Darstellung keine installierte Schrift. Die Pfadquelle mit dem exakten Wortlaut liegt in `assets/logos/dir4b/claim-outlines-v1.json`; die ursprüngliche Fontsoftware wird nicht verteilt. Die gesonderte Rechteprüfung bleibt offen.

Schutzraum: mindestens ein Viertel der Signethöhe zu anderen Objekten. Ohne Claim mindestens 140 CSS-Pixel Breite horizontal bzw. 120 Pixel gestapelt. Mit Claim mindestens 360 Pixel horizontal bzw. 320 Pixel gestapelt; darunter die claimlose Fassung verwenden. Favicons nutzen ein vereinfachtes D ohne feine Orbitlinie bei 16/32/48 Pixel. App-Avatare liegen in 512 und 1024 Pixel vor.

Proportionen erhalten, keine Drehung, kein zusätzlicher Schatten, keine Farbänderung außerhalb der sechs Fassungen. Für kleine oder kontrastkritische Anwendungen monochrom Weiß auf dunklem Grund bzw. Dunkel auf hellem Grund nutzen. Cyan/Violett nicht für kleine Textclaims auf ungeeigneten Hintergründen verwenden. Exporte sind RGB-Arbeitsstände; Druckprofil, Beschnitt und Proof bleiben Aufgabe der konkreten Druckproduktion.

## Domains und technische Namen

`dir4b.de`, `dir4b.com`, `dir4b.eu`: bei ALL-INKL als kostenlose Inklusivdomains bestellt; Registrierung **nicht bestätigt**. Keine aktive Website, E-Mail-Adresse, Weiterleitung oder Canonical-URL daraus ableiten.

Repositoryname `timoschreck/nexovia-future` und die im [A/B/C-Register](dir4b-path-migration.json) als C klassifizierten Pfade und CSS-Bezeichner bleiben aus Kompatibilitätsgründen erhalten. Aktive Arbeitsquellen und die Startseite wurden gemäß Register umbenannt. Die geplante Backendrolle `nexovia_admin` bleibt ein technischer Bezeichner bis zur gesonderten Backendprüfung. Es wurden keine Cloud-Projekte, OAuth-Callbacks, DNS-Einträge oder Auth-Ressourcen umbenannt.

## Freigabestatus

Markenname und Claimwahl sind durch den Nutzerauftrag belegt. Der Logoentwurf ist technisch erstellt, aber nicht als rechtlich geprüfte Marke freigegeben. Die bereits dokumentierten Prüfungen zu Markenrechten, Fonts, Nutzungsrechten und Druckproduktion bleiben offen. Historische Rasterlogos, Quellenauswertungen und Workshop-/Auditprotokolle bleiben nachvollziehbar erhalten und sind keine aktuellen Markenmaster.

## Referenzpflege 1.2.0

Referenzversion 1.2.0 ergänzt Quellenstatus, Schreibweise, Logo-Varianten und Assetpfade; der visuelle Markenstand bleibt 1.1.0. Keine neue Claim- oder Gestaltungsfreigabe. Die folgenden Daten werden mit `python scripts/sync_dir4b_reference.py` aus der JSON-Quelle erzeugt und mit `--check` auf Gleichstand geprüft. Fachliche Anwendungsregeln oberhalb bleiben redaktionell gepflegt.

<!-- DIR4B:GENERATED:START -->

```json
{
  "schema_version": 1,
  "brand_version": "1.1.0",
  "effective_date": "2026-09-05",
  "name": "DIR4B",
  "chatgpt_project": "dir4b STARTUP",
  "repository": "timoschreck/nexovia-future",
  "primary_claim": "Business, Intelligently Orchestrated.",
  "claims": [
    {
      "id": "premium",
      "text": "Business, Intelligently Orchestrated.",
      "use": "Dachmarke",
      "source": "chat:6a9c4021-7bb0-83eb-b994-1dc5fcb1aabf/turn:bbb211ba-36e0-42ca-84cd-c39b2d203f02",
      "approval": "Nutzerauswahl: Okay, wir nehmen die Eins. Die vorherige Rangliste nennt exakt diesen Claim als Nummer 1.",
      "status": "freigegeben gemäß dokumentiertem Beleg"
    },
    {
      "id": "product",
      "text": "Eine Basis. Genau die Module, die du brauchst.",
      "use": "Produkt und modulare Architektur",
      "source": "README.md und docs/nexovia_masterprompt_corporate_identity.md Abschnitt 5 auf b48b94790b2b8d21b48c3abce34333d349179e56",
      "approval": "Auf main als verbindlicher Leitclaim dokumentiert; Übernahme gemäß Umstellungsauftrag.",
      "status": "freigegeben gemäß dokumentiertem Beleg"
    },
    {
      "id": "integration",
      "text": "Was zusammengehört, arbeitet zusammen.",
      "use": "Integration und Datenfluss",
      "source": "README.md und docs/nexovia_masterprompt_corporate_identity.md Abschnitt 5 auf b48b94790b2b8d21b48c3abce34333d349179e56",
      "approval": "Auf main als verbindlicher Leitclaim dokumentiert; Übernahme gemäß Umstellungsauftrag.",
      "status": "freigegeben gemäß dokumentiertem Beleg"
    },
    {
      "id": "growth",
      "text": "Einfach starten. Modular wachsen.",
      "use": "Einführung und Wachstum",
      "source": "README.md und docs/nexovia_masterprompt_corporate_identity.md Abschnitt 5 auf b48b94790b2b8d21b48c3abce34333d349179e56",
      "approval": "Auf main als verbindlicher Leitclaim dokumentiert; Übernahme gemäß Umstellungsauftrag.",
      "status": "freigegeben gemäß dokumentiertem Beleg"
    }
  ],
  "domains": [
    {
      "name": "dir4b.de",
      "provider": "ALL-INKL",
      "order": "bestellt als kostenlose Inklusivdomain",
      "registration": "nicht bestätigt"
    },
    {
      "name": "dir4b.com",
      "provider": "ALL-INKL",
      "order": "bestellt als kostenlose Inklusivdomain",
      "registration": "nicht bestätigt"
    },
    {
      "name": "dir4b.eu",
      "provider": "ALL-INKL",
      "order": "bestellt als kostenlose Inklusivdomain",
      "registration": "nicht bestätigt"
    }
  ],
  "domain_source": "Aktueller Nutzerauftrag; bestätigt durch Domaincheck DIR4B fortsetzen, 6a9c5349-0a18-83eb-bce1-2698b0a34dec. Kein erneuter Registrar-Livecheck in dieser Umstellung.",
  "colors": {
    "black": "#01091D",
    "navy": "#0C1033",
    "cyan": "#00C8FF",
    "blue": "#256BFF",
    "violet": "#AE00FF",
    "magenta": "#FF70D4",
    "fog": "#F4F6FA",
    "moon": "#A9B8D0"
  },
  "typography": {
    "display": "Orbitron, Bank Gothic, Eurostile, sans-serif",
    "body": "Inter, Aptos, Arial, sans-serif",
    "wordmark": "Eigene geometrische SVG-Pfade",
    "claim_export": "Arial als dokumentierter CI-Fallback, in feste SVG-Pfade umgewandelt; Wortlaut und Pfadquelle versioniert in claim-outlines-v1.json"
  },
  "logo_root": "assets/logos/dir4b/v1",
  "horizontal_lockup": {
    "first_letter": "D-Bildzeichen",
    "continuation": "IR4B",
    "canonical_text": "DIR4B",
    "source": "Nutzerwunsch vom 05.09.2026: Einzellogo D und danach direkt IR4B; kein doppeltes D."
  },
  "logo_status": "DIR4B-Entwurf und technische Masterdateien; keine rechtliche Markenfreigabe",
  "excluded": [
    "DVB als Markenname",
    "ungewählte Claim-Vorschläge",
    "NEXT + VIA als DIR4B-Namensherleitung",
    "unbestätigte Domain als aktive Kontakt- oder Canonical-Adresse"
  ],
  "technical_compatibility": [
    "Repositoryname nexovia-future",
    "C-Pfade gemäß docs/brand/dir4b-path-migration.json",
    "nx-* CSS-Bezeichner",
    "geplante Rolle nexovia_admin bis zur gesonderten Backend-Migration"
  ],
  "reference_version": "1.3.0",
  "updated_at": "2026-09-09",
  "spelling": {
    "canonical": "DIR4B",
    "case": "Großbuchstaben; Ziffer 4",
    "status": "belegt"
  },
  "logo_variants": {
    "layouts": [
      "horizontal",
      "stacked",
      "icon"
    ],
    "styles": [
      "dark",
      "light",
      "mono-white",
      "mono-dark",
      "mono-cyan",
      "mono-violet"
    ],
    "claim_ids": [
      "premium",
      "product",
      "integration",
      "growth"
    ],
    "icon_claims": false,
    "status": "technisch vorhanden; rechtliche Freigabe offen"
  },
  "asset_paths": {
    "logos": "assets/logos/dir4b/v1",
    "manifest": "docs/brand/dir4b-asset-manifest-v1.json",
    "claim_outlines": "assets/logos/dir4b/claim-outlines-v1.json",
    "tokens_json": "tokens/nexovia_design_tokens.json",
    "tokens_css": "tokens/nexovia_design_tokens.css",
    "web_css": "web/nexovia_web_ui.css",
    "background": "assets/backgrounds/nexovia_cosmic_background_animated.svg",
    "homepage": "web/dir4b_startseite_responsive.html",
    "brandbook": "docs/dir4b_brandbook_v1.pdf"
  },
  "sources": [
    {
      "id": "identity",
      "reference": "Nutzerauftrag zur DIR4B-Synchronisation vom 2026-09-05",
      "status": "belegt",
      "scope": "Name, Projekt, Domain-Bestellung; Registrierung nicht bestätigt"
    },
    {
      "id": "claims",
      "reference": "Einzelbelege in claims[].source und claims[].approval",
      "status": "im Repository dokumentiert",
      "scope": "Wortlaut und Verwendungszweck; Originalgespräche in diesem Arbeitspaket nicht erneut geprüft"
    },
    {
      "id": "visual",
      "reference": "docs/brand/dir4b-brand-v1.md und Design-Tokens auf main 19bd8032fb8b79b4187014e1b3e10845cd70b162",
      "status": "technisch abgeglichen",
      "scope": "bestehende Farben, Typografie und Logo-Varianten; Rechteprüfung offen"
    },
    {
      "id": "website-contact-2026-09-09",
      "reference": "Timo Schreck, Nutzerangabe vom 09.09.2026; docs/website/dir4b-contact-v1.json",
      "status": "Nutzerangabe bestätigt; technische und rechtliche Prüfungen offen",
      "scope": "Websitehost .ai und Kontaktquelle; keine Änderung der Claims oder der Bestell-/Registrierungsstände von .de/.com/.eu"
    }
  ],
  "contact_reference": "docs/website/dir4b-contact-v1.json",
  "website": {
    "hostname": "www.dir4b.ai",
    "status": "durch Nutzer als Website bestimmt; technische Verifikation offen",
    "source": "Timo Schreck, Nutzerangabe vom 09.09.2026; docs/website/dir4b-contact-v1.json",
    "registration_dns_tls_verified": false,
    "publication_status": "interne Vorschau; keine Produktivfreigabe"
  }
}
```

<!-- DIR4B:GENERATED:END -->

## Kontakt-/Websitereferenz 1.3.0 – 09.09.2026

Timo Schreck hat www.dir4b.ai als vorgesehene Website sowie info@dir4b.ai, Anschrift und Telefon für den Kontakt bestätigt. [Kontaktregister](../website/dir4b-contact-v1.json) und [Impressumsentwurf](../legal/dir4b-impressum-entwurf-2026-09-09.md) trennen Nutzerangaben von technischen und rechtlichen Nachweisen. Die JSON-Quelle verweist nun auf diese Fachquelle. Referenzversion 1.3.0, visueller Markenstand weiterhin 1.1.0. Keine DNS-/TLS-, Zustell-, Register- oder Produktivbestätigung. Die drei bisher bestellten Domains .de/.com/.eu bleiben unverändert dokumentiert; keine Stornierung oder Umregistrierung. Frühere Abschnitte zur Version 1.2.0 beschreiben den vorherigen Referenzstand.
