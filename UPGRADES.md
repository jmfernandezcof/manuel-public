# MANuel — Upgrades / ideas

Backlog de mejoras para MANuel (técnico virtual L1). Estado actual: workflow n8n
`sSl2NqFNqQog2Lnr` "MANuel Multivend - L1 Tech (Responses API + RAG)", Telegram,
gpt-5.5 + file_search (vector store `vs_6ac368acbc64819186fb0a0b0b2e3864`), fotos y
notas de voz, agrupado de mensajes en ráfaga, sesiones con caducidad 2 h.
Prompt único: `system_prompt.md` de este repo (n8n lo lee vía `/files/manuel-config/system_prompt.md` → symlink).

---

## 1. Canal WhatsApp (prioridad si Multivend dice que sí)

**Recomendación: YCloud** (alternativa seria: 360dialog). Investigado el 2026-10-05.

- **Coste Meta para soporte ≈ 0**: las respuestas de servicio (dentro de la ventana de
  24 h que abre el cliente) son gratis y sin tope; las plantillas utility dentro de la
  ventana, también. Solo se pagan las plantillas que inician conversación
  (España ≈ 0,02 $ utility / 0,07 $ marketing; tarifa según el país del destinatario).
  - OJO: hay blogs que dicen que desde el 1-oct-2026 se cobran los mensajes de servicio
    (1.000 gratis/mes). **Falso según la doc oficial de Meta** (comprobado 2026-10-05).
    Re-verificar en https://developers.facebook.com/docs/whatsapp/pricing antes de presupuestar.
- **Coexistencia** (el cliente sigue usando la app WhatsApp Business en su móvil y ve/contesta
  todo): disponible en todos los países (UE desde nov-2025).
  - Requisitos: número que ya use WhatsApp Business App (no personal, no recién creado);
    abrir la app al menos cada 13 días.
  - Límites: 5 msg/s; sin tick azul (OBA); sin Calling API; no se puede migrar de WABA.
  - Mensajes desde la app: gratis. Desde la API: tarifas Meta.
- **Comparativa**:
  | | Meta directo | YCloud | 360dialog | Twilio |
  |---|---|---|---|---|
  | Cuota | 0 | Free / Growth 39 $/mes | desde 49 €/mes por número | 0 |
  | Margen sobre Meta | — | 0 % | 0 % | ~0,005 $/msg |
  | Inbox para el cliente | no | sí | no | no |
  | Dolor Facebook | máximo | bajo (embedded signup) | bajo | medio |
- **Política IA de Meta (15-ene-2026)**: prohibidos los chatbots de propósito general en la
  API; los bots de soporte de un negocio con su KB (como MANuel) están permitidos.
  Mantener el prompt cerrado a temas del cliente.
- **Implementación** (estimado ~medio día):
  - [ ] Entrada: webhook YCloud → misma lógica (Parse Message → cola → Combine → …).
  - [ ] Salida: envío por API YCloud en vez del nodo Telegram (abstraer canal).
  - [ ] Fotos y audios de WhatsApp: descarga de media vía API del BSP.
  - [ ] **Handoff humano**: escuchar `smb_message_echoes`; si el humano contesta desde la app,
        pausar el bot en ese chat X horas (tabla de pausas). Es lo que más falla en la práctica.
  - [ ] Plantillas utility para avisos proactivos ("técnico en camino", etc.).
- **No usar Evolution API / Baileys (no oficial) para clientes**: riesgo de baneo y contra
  términos de Meta. (Hay un "WhatsApp Evolution Handler" activo en n8n: solo para pruebas.)
- Nota: en los logs de n8n hay un intento fallido de verificar un webhook de Meta
  ("Callback verification failed… 404") contra el workflow `test-bot` (tO8na3rc2Y0Pt7AF, sin
  publicar). Típico dolor de Meta directo.

Fuentes: Meta pricing / pricing updates; chakrahq.com (coexistencia); docs.360dialog.com
(coexistencia, webhooks, precios); ycloud.com (pricing, coexistencia); respond.io (política IA).

## 2. Base de conocimiento

- [ ] Pedir a Multivend los manuales de todo su parque (sobre todo Korinto, Kobalto, Koro,
      Karisma, Concerto, Maestro, Tango/Jazz/Swing/Twist, G-Snack, G-Drink).
- [ ] Manuales G-Snack/G-Drink: existen en img.torebrings.se (no respondía) y ManualsLib.
- [ ] Script/workflow reutilizable para añadir ficheros al vector store sin rehacerlo.
- [ ] Operman: los manuales originales siguen en GitHub `nomadprompters-prog/operman`
      (`manuals/`: CashDro User Manual, HioPOS PortalRest, GM Vending Elite, Versa) por si se
      reactiva MANuel-Operman.

## 3. Producto / UX

- [ ] Línea "Source: …" siempre presente: añadirla en el workflow a partir del manual
      consultado (ahora depende del modelo).
- [ ] Varias fotos en una misma ráfaga: ahora solo se usa la primera imagen
      (y si llegan foto + audio juntos, gana la foto).
- [ ] Responder también con audio (TTS) cuando el usuario manda una nota de voz.
- [ ] Escalado real: crear ticket/aviso al Departamento Técnico (email/Telegram al staff)
      con el resumen de la conversación, en vez de solo dar el teléfono.
- [ ] Identificar usuario/cliente (tabla de clientes con máquinas y ubicación) para no
      preguntar el modelo cada vez.
- [ ] Dashboard de uso: preguntas más frecuentes, modelos, escalados (desde `manuel_mv_logs`).

## 4. Limpieza / seguridad

- [ ] Renombrar la credencial de Telegram "MANuel - Operman" → "MANuel - Multivend".
- [ ] Revocar la API key de OpenAI `sk-proj-…hPkA` que está en claro en 5 workflows
      archivados de Operman, y borrarla de esos workflows.
- [ ] Workflows archivados/antiguos de MANuel-Operman: decidir si se borran.
