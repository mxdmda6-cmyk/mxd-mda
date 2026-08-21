import { useMemo, useState } from "react";

const tensions = [
  {
    left: "SILENCE",
    right: "CHAOS",
    signal: "YOU WERE NOT LOST. YOU WERE UNWITNESSED.",
    note: "Careful. Certainty stains.",
  },
  {
    left: "GRIEF",
    right: "DEFIANCE",
    signal: "WHAT BROKE DID NOT RECEIVE THE FINAL WORD.",
    note: "The fracture has opinions. Naturally.",
  },
  {
    left: "MEMORY",
    right: "IDENTITY",
    signal: "THE NAME RETURNED BEFORE THE WITNESS DID.",
    note: "Names are terrible at staying buried.",
  },
];

const offers = [
  {
    id: "artifact",
    name: "Personal Signal Artifact",
    price: "$29",
    cadence: "once",
    description: "A six-page personalized PDF, phone wallpaper, share card, and private reflection prompt.",
    action: "Choose the artifact",
  },
  {
    id: "deep",
    name: "Deep Signal Edition",
    price: "$79",
    cadence: "once",
    description: "Three connected fragments, an audio transmission, alternate art, and a hidden Codex clue.",
    action: "Choose the deep signal",
    featured: true,
  },
  {
    id: "archive",
    name: "The Living Archive",
    price: "$15",
    cadence: "monthly",
    description: "One new artifact, one printable ritual page, and an evolving chapter unlock each month.",
    action: "Enter the archive",
  },
];

function VerticalWord({ children }) {
  return <span className="vertical-word">{children.split("").map((letter, index) => <span key={`${letter}-${index}`}>{letter}</span>)}</span>;
}

function OfferSheet({ onClose, signal }) {
  const [selected, setSelected] = useState("deep");
  const [email, setEmail] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const activeOffer = offers.find((offer) => offer.id === selected);

  function submit(event) {
    event.preventDefault();
    if (!email.trim()) return;
    setSubmitted(true);
  }

  return (
    <div className="sheet-backdrop" role="presentation" onMouseDown={(event) => event.target === event.currentTarget && onClose()}>
      <section className="offer-sheet" role="dialog" aria-modal="true" aria-labelledby="offer-title">
        <div className="sheet-topline">
          <p>FRAGMENT 8133 · PRIVATE OFFER</p>
          <button className="text-button" type="button" onClick={onClose}>Close</button>
        </div>
        {submitted ? (
          <div className="success-state" aria-live="polite">
            <p className="eyebrow">RESERVATION HELD</p>
            <h2 id="offer-title">The fragment knows where to find you.</h2>
            <p>This prototype has recorded the intent locally. Connect the selected Shopify product and email delivery before launch.</p>
            <button className="gold-button" type="button" onClick={onClose}>RETURN TO THE SIGNAL</button>
          </div>
        ) : (
          <>
            <header className="sheet-header">
              <p className="eyebrow">KEEP WHAT ANSWERED</p>
              <h2 id="offer-title">Turn the signal into an artifact.</h2>
              <p className="sheet-signal">“{signal}”</p>
            </header>

            <div className="offer-grid" role="radiogroup" aria-label="Artifact editions">
              {offers.map((offer) => (
                <button
                  className={`offer ${selected === offer.id ? "selected" : ""} ${offer.featured ? "featured" : ""}`}
                  key={offer.id}
                  type="button"
                  role="radio"
                  aria-checked={selected === offer.id}
                  onClick={() => setSelected(offer.id)}
                >
                  <span className="offer-name">{offer.name}</span>
                  <span className="offer-price">{offer.price}<small> / {offer.cadence}</small></span>
                  <span className="offer-description">{offer.description}</span>
                  <span className="offer-action">{offer.action}</span>
                </button>
              ))}
            </div>

            <form className="reserve-form" onSubmit={submit}>
              <label htmlFor="signal-email">Where should the first proof arrive?</label>
              <div className="email-row">
                <input
                  id="signal-email"
                  type="email"
                  value={email}
                  onChange={(event) => setEmail(event.target.value)}
                  placeholder="you@example.com"
                  required
                />
                <button className="gold-button" type="submit">RESERVE {activeOffer?.price}</button>
              </div>
              <p className="fine-print">Proof mode: no payment is collected. Reflective art—not therapy, diagnosis, or divination.</p>
            </form>
          </>
        )}
      </section>
    </div>
  );
}

export function App() {
  const [tensionIndex, setTensionIndex] = useState(0);
  const [resolved, setResolved] = useState(true);
  const [offerOpen, setOfferOpen] = useState(false);
  const tension = tensions[tensionIndex];
  const dateCode = useMemo(() => "08.21.26", []);

  function chooseTension(index) {
    setTensionIndex(index);
    setResolved(false);
  }

  return (
    <main className={`signal-engine ${resolved ? "is-resolved" : ""}`}>
      <header className="brand-bar">
        <span>MXD·MDA</span>
        <span className="brand-label">SIGNAL ENGINE</span>
        <span className="brand-credit">CREATED BY HUE MOORE</span>
      </header>

      <nav className="tension-nav" aria-label="Choose two truths">
        {tensions.map((item, index) => (
          <button
            key={`${item.left}-${item.right}`}
            type="button"
            className={index === tensionIndex ? "active" : ""}
            onClick={() => chooseTension(index)}
          >
            {item.left} / {item.right}
          </button>
        ))}
      </nav>

      <section className="artifact-stage" aria-label={`${tension.left} and ${tension.right} signal`}>
        <article className="fragment fragment-left">
          <img src="/assets/bone-fragment-v01.webp" alt="Torn bone paper with a crimson fiber edge" />
          <VerticalWord>{tension.left}</VerticalWord>
          <span className="fragment-date">{dateCode}</span>
        </article>

        <div className="contact-space">
          <p className="instruction">BRING TWO TRUTHS<br />INTO CONTACT.</p>
          <img className="signal-seam" src="/assets/signal-seam-v01.webp" alt="A fine antique-gold intersection mark" />
          <p className="signal-copy" aria-live="polite">{resolved ? tension.signal : "THE SIGNAL IS WAITING BETWEEN THEM."}</p>
          <button
            className="gold-button primary-action"
            type="button"
            onClick={() => resolved ? setOfferOpen(true) : setResolved(true)}
          >
            {resolved ? "KEEP THIS FRAGMENT" : "BRING INTO CONTACT"}
          </button>
          <p className="metadata">SIGNAL {dateCode} · FRAGMENT 8133</p>
          <p className="crow-note">{resolved ? tension.note : "Wrong turn. Excellent data."}</p>
        </div>

        <article className="fragment fragment-right">
          <img src="/assets/indigo-fragment-v01.webp" alt="Torn indigo darkroom paper with subtle fingerprints" />
          <VerticalWord>{tension.right}</VerticalWord>
        </article>
      </section>

      <footer className="proof-footer">
        <span>LIVING PALIMPSEST · PROOF MODE</span>
        <button className="text-button" type="button" onClick={() => setResolved(false)}>Separate the truths</button>
      </footer>

      {offerOpen && <OfferSheet onClose={() => setOfferOpen(false)} signal={tension.signal} />}
    </main>
  );
}
