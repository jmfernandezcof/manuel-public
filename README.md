# MANuel — virtual Level-1 field technician

A Telegram bot that helps technicians, route operators and customer staff troubleshoot vending and
HoReCa coffee machines. It answers **only from the manufacturer manuals** in its knowledge base.

It was built in one day as a demo for Multivend Services (Malta), using the manuals of the machines
they operate (Evoca/Necta coffee and snack machines, and Nayax payment systems).

> This is a portfolio demo by [Nomad Prompters](https://nomadprompters.es). It is a sanitized
> snapshot. Credentials, internal IDs and the manuals themselves (third-party PDFs) are not included.

## How it works

```
Telegram ──► n8n workflow
              │  /start, /reset → clear session + welcome
              │  text   → queue → wait 3 s → merge bursts (forwards, albums, reply-to-photo)
              │  photo  → download → image input
              │  voice  → download → speech-to-text (with a brand-vocabulary hint)
              ▼
        OpenAI Responses API + file_search over a vector store of the manuals
        conversation memory via previous_response_id (expires after 2 h idle)
              ▼
        reply on Telegram + log + session state
```

## Safety rules (enforced by the prompt, verified by stress tests)

- Answers technical questions only from the knowledge base and says so when a manual is missing.
- Stops troubleshooting and escalates on smoke, a burning smell, sparks, or water on electrics.
- **Never gives service-menu passwords or PINs, free-vend or price settings.** One manual contains
  factory default passwords, and an early stress test caught the bot handing them out. The prompt
  now blocks this.
- Door-switch procedures: visual checks only with the door open, and powered tests only after
  closing it.
- No general-purpose chat.

## Repository layout

| Path | Contents |
|---|---|
| `system_prompt.md` | The bot's full instructions, the single source of truth (n8n reads it on every message) |
| `workflow/manuel-multivend.json` | n8n workflow export. Credentials are referenced by name only |
| `kb_company_profile_multivend.md`, `KB_SOURCES.md` | Company profile and the list of manuals in the knowledge base |
| `scripts/` | Test harnesses: single questions, multi-turn stress scenarios, image questions |
| `tests/` | Stress-test scenarios and transcripts of the first runs |
| `UPGRADES.md` | Backlog |

The test scripts post to the webhook set in the `MANUEL_WEBHOOK_URL` environment variable. Use a
temporary n8n webhook that proxies the OpenAI call, so the API key never leaves n8n, and delete it
after testing.

## Stack

n8n · OpenAI Responses API (file_search, vision, speech-to-text) · Telegram Bot API

## License

© Nomad Prompters. All rights reserved. Shared for portfolio review only.
