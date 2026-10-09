# Knowledge base sources

Vector store `vs_6ac368acbc64819186fb0a0b0b2e3864` ("MANuel Multivend KB"), created 2026-10-05.
PDFs are third-party documents and are not committed; re-download from these URLs.

## Full manuals — Evoca Group North America (official, English)

| File | URL |
|---|---|
| EN_OperaTouch_Manual.pdf | https://evocagroupna.com/docs/OperaTouch/EN_OperaTouch_Manual.pdf |
| EN_OperaTouch_Maintenance.pdf | https://evocagroupna.com/docs/OperaTouch/EN_OperaTouch_Maintenance.pdf |
| EN_Krea_Manual.pdf | https://evocagroupna.com/docs/Krea/EN_Krea_Manual.pdf |
| EN_KreaTouch_Manual.pdf | https://evocagroupna.com/docs/KreaTouch/EN_KreaTouch_Manual.pdf |
| EN_KreaTouch_Maintenance.pdf | https://evocagroupna.com/docs/KreaTouch/EN_KreaTouch_Maintenance.pdf |
| EN_KreaTouch_KHB.pdf | https://evocagroupna.com/docs/KreaTouch/EN_KreaTouch_KHB.pdf |
| EN_Kometa_Manual.pdf | https://evocagroupna.com/docs/Kometa/EN_Kometa_Manual.pdf |
| EN_Kometa_Maintenance.pdf | https://evocagroupna.com/docs/Kometa/EN_Kometa_Maintenance.pdf |

Pattern: `https://evocagroupna.com/docs/<Model>/EN_<Model>_<Manual|Maintenance|KHB|Programming|QuickGuide>.pdf`.
⚠️ The server answers HTTP 200 for missing files (HTML page) — always validate with `file x.pdf`.
Not available there (checked): Korinto, Korinto Prime, Kobalto, Koro, Koro Prime, Karisma,
Tango, Jazz, Swing, Twist, Maestro Touch.

## Brochures / spec sheets

| File | URL |
|---|---|
| Necta_OperaTouch_brochure.pdf | https://newebcdn-necta.evocagroup.com/sites/necta/files/2019-03/OPERA%20TOUCH%20F_L490F2_web.pdf |
| Necta_Tango_brochure.pdf | https://cdn.shopify.com/s/files/1/1829/0759/files/TANGO_UK_L445K0.pdf |
| Necta_Jazz_brochure.pdf | https://cdn.shopify.com/s/files/1/1829/0759/files/Jazz_Brochure.pdf |
| GSnack_Budget_BS8.pdf | https://hosting155807.a2edc.netcup.net/rohrmoser/wp-content/uploads/2021/12/G-Snack_BUDGET_BS8_Master_-_BS8.pdf |
| GSnack_BS8_sheet.pdf | https://cdn.shopify.com/s/files/1/0546/0295/6985/files/BS8.pdf |

G-Snack full user/programming manuals exist at
`https://img.torebrings.se/service-dokument/Varuautomater%20Vendo/G-Snack%20SM08%20Outdoor/` (host unreachable on 2026-10-05) and on ManualsLib.

## Nayax

| File | URL |
|---|---|
| Nayax_error_codes.md | https://devzone.nayax.com/docs/integrate-pos-device/marshall-pro/messaging-protocol/error-codes.md |
| Nayax_EMV_troubleshooting.md | https://devzone.nayax.com/docs/integrate-pos-device/emv-core/rtos/rtos-troubleshooting.md |

## Company profile

`kb_company_profile_multivend.md` (in this repo) — written from https://www.multivendservices.com
(about, vending, HoReCa, brands, technical department pages and media filenames).

## Adding files to the vector store

Upload with `POST /v1/files` (purpose `assistants`) and attach with
`POST /v1/vector_stores/{id}/files` — from an n8n HTTP Request node using the OpenAI credential
(do not export the key to the shell).
