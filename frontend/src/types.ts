export type EntityType =
  | "CPF"
  | "CNPJ"
  | "EMAIL"
  | "TELEFONE"
  | "CEP"
  | "CARTAO_CREDITO"
  | "RG"
  | "NOME"
  | "ENDERECO";

export type Sensitivity = "ALTA" | "MEDIA" | "BAIXA";
export type Strategy = "MASK" | "REDACT" | "HASH";

export interface Finding {
  type: EntityType;
  value_masked: string;
  start: number;
  end: number;
  sensitivity: Sensitivity;
  valid: boolean;
}

export interface ScanResponse {
  findings: Finding[];
  sanitized_text: string;
  audit: {
    timestamp: string;
    total_findings: number;
    strategy_applied: Strategy;
  };
}
