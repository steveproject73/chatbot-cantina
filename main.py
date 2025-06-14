


from flask import Flask, render_template, request

app = Flask(__name__)
chat_log = []

@app.route("/", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        user_input = request.form["user_input"]
        chat_log.append({"role": "user", "text": user_input})

        response = genera_risposta(user_input)
        chat_log.append({"role": "bot", "text": response})

    return render_template("chatbot.html", chat_log=chat_log)

def genera_risposta(testo):
    testo = testo.lower()

    if "ciao" in testo:
        return "💬 Ciao! Benvenuto nella Cantina Virtuosa. Come posso aiutarti? Ecco cosa posso fare per te:\n🔴 Vini rossi\n⚪ Vini bianchi\n🍷 Prenota una degustazione\nℹ️ Info e orari"
    
    elif "rossi" in testo or "vino rosso" in testo:
        return "🍇 I nostri vini rossi:\n- Chianti Riserva\n- Nero d’Avola\n- Barbera del Monferrato"
    
    elif "bianchi" in testo or "vino bianco" in testo:
        return "🍏 I nostri vini bianchi:\n- Falanghina\n- Chardonnay\n- Vermentino"
    
    elif "prenotazione" in testo or "degustazione" in testo:
        return "📅 Per prenotare una degustazione, scrivi il giorno e l’orario che preferisci!"
    
    elif "orari" in testo or "aperti" in testo or "info" in testo:
        return "🕒 Siamo aperti dal lunedì al sabato, dalle 10:00 alle 19:00."

    elif any(g in testo for g in ["oggi", "domani", "lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]):
        return f"✅ Prenotazione ricevuta! Ti aspettiamo {testo} 🍷"

    elif "grazie" in testo:
        return "🙏 Grazie a te! A presto nella nostra cantina."

    else:
        return "❓ Mi dispiace, non ho capito. Puoi chiedere info su vini, degustazioni o orari."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
