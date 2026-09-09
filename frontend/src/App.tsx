import { useState } from "react";
import type { ScanResponse, Strategy } from "./types";

const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

const SENSITIVITY_STYLES: Record<string, string> = {
  ALTA: "bg-stamp text-parchment",
  MEDIA: "bg-signal text-parchment",
  BAIXA: "bg-sage text-ink",
};

export default function App() {
  const [text, setText] = useState(
    "Meu CPF é 111.444.777-35 e meu email é ana@empresa.com"
  );
  const [strategy, setStrategy] = useState<Strategy>("MASK");
  const [result, setResult] = useState<ScanResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleScan() {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`${API_URL}/v1/scan`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, config: { strategy } }),
      });

      if (!response.ok) {
        const body = await response.json();
        throw new Error(body?.detail?.message ?? "Falha ao escanear o texto.");
      }

      setResult(await response.json());
    } catch (err) {
      setError(err instanceof Error ? err.message : "Erro inesperado ao conectar com a API.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen px-6 py-12 md:px-16">
      <header className="mb-10 border-b border-white/10 pb-6">
        <p className="font-body text-xs tracking-wide text-parchment/60">
          LGPD compliance engine
        </p>
        <h1 className="font-display text-4xl font-semibold text-parchment">
          Data Guardian
        </h1>
      </header>

      <main className="grid gap-10 md:grid-cols-2">
        <section>
          <label className="mb-2 block font-body text-sm text-parchment/70">
            Texto para varredura
          </label>
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            rows={8}
            className="w-full rounded-sm border border-white/10 bg-ink-light p-4 font-body text-sm text-parchment outline-none focus:border-signal"
          />

          <div className="mt-4 flex flex-wrap items-center gap-3">
            <span className="font-body text-sm text-parchment/70">Estratégia:</span>
            {(["MASK", "REDACT", "HASH"] as Strategy[]).map((option) => (
              <button
                key={option}
                onClick={() => setStrategy(option)}
                className={`rounded-sm border px-3 py-1 font-body text-xs uppercase tracking-wide transition ${
                  strategy === option
                    ? "border-stamp bg-stamp text-parchment"
                    : "border-white/20 text-parchment/70 hover:border-white/40"
                }`}
              >
                {option}
              </button>
            ))}
          </div>

          <button
            onClick={handleScan}
            disabled={loading || !text.trim()}
            className="mt-6 rounded-sm bg-stamp px-6 py-3 font-display text-lg font-semibold text-parchment transition hover:bg-stamp-light disabled:opacity-40"
          >
            {loading ? "Escaneando…" : "Escanear documento"}
          </button>

          {error && <p className="mt-4 font-body text-sm text-stamp-light">{error}</p>}
        </section>

        <section>
          <p className="mb-2 font-body text-sm text-parchment/70">Resultado</p>
          <div className="min-h-[220px] rounded-sm bg-parchment p-6 font-body text-sm text-ink shadow-lg">
            {result ? (
              <p className="whitespace-pre-wrap leading-relaxed">{result.sanitized_text}</p>
            ) : (
              <p className="text-ink/40">
                O texto tratado aparece aqui depois do escaneamento.
              </p>
            )}
          </div>

          {result && result.findings.length > 0 && (
            <ul className="mt-4 space-y-2">
              {result.findings.map((finding, index) => (
                <li
                  key={`${finding.type}-${index}`}
                  className="flex items-center justify-between rounded-sm border border-white/10 bg-ink-light px-3 py-2 font-body text-xs"
                >
                  <span className="text-parchment/80">
                    {finding.type} · posição {finding.start}-{finding.end}
                  </span>
                  <span
                    className={`rounded-sm px-2 py-0.5 uppercase tracking-wide ${SENSITIVITY_STYLES[finding.sensitivity]}`}
                  >
                    {finding.sensitivity}
                  </span>
                </li>
              ))}
            </ul>
          )}

          {result && (
            <p className="mt-4 font-body text-xs text-parchment/40">
              {result.audit.total_findings} entidade(s) detectada(s) · estratégia{" "}
              {result.audit.strategy_applied}
            </p>
          )}
        </section>
      </main>
    </div>
  );
}
