-- Schéma minimal d'un portefeuille de monnaie électronique (lab KamaPay).
-- Les montants sont en francs CFA (XAF), entiers, sans décimales.

CREATE TABLE customers (
    id          SERIAL PRIMARY KEY,
    msisdn      VARCHAR(15)  NOT NULL UNIQUE,
    full_name   VARCHAR(120) NOT NULL,
    id_number   VARCHAR(20)  NOT NULL,
    pin_hash    TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE TABLE wallets (
    id           SERIAL PRIMARY KEY,
    customer_id  INTEGER NOT NULL UNIQUE REFERENCES customers(id),
    balance      BIGINT  NOT NULL CHECK (balance >= 0),
    currency     CHAR(3) NOT NULL DEFAULT 'XAF'
);

CREATE TABLE transactions (
    id           BIGSERIAL PRIMARY KEY,
    from_wallet  INTEGER NOT NULL REFERENCES wallets(id),
    to_wallet    INTEGER NOT NULL REFERENCES wallets(id),
    amount       BIGINT  NOT NULL CHECK (amount > 0),
    created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (from_wallet <> to_wallet)
);
