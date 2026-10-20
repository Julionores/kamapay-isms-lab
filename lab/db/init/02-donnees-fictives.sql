-- Données de test entièrement fictives (contrôle 8.33) : aucune donnée de
-- production n'est utilisée hors production. PIN de test : 1357, 2468, 9753.
INSERT INTO customers (msisdn, full_name, id_number, pin_hash) VALUES
  ('237690004521', 'Client Test Un',    'CMR100000451', 'pbkdf2:sha256:600000$rMaD1aMRYohryAv6$e10fca2db39e7cee9eb877636df5c84e83912bd2e2d40b7229ea65f57764d4b7'),
  ('237690007788', 'Client Test Deux',  'CMR100000788', 'pbkdf2:sha256:600000$os7W0c5IuEYDxCjd$cdba43bf94c5eed584178936679465f350de53b032258c4fc1c215995c9d6e0b'),
  ('237690009012', 'Client Test Trois', 'CMR100000912', 'pbkdf2:sha256:600000$B9x1T7X72pDYUzsC$a842cd464acc49950572723d498e42eda05de3e64487eebe40fb0e3b21ecbc91');

INSERT INTO wallets (customer_id, balance) VALUES (1, 150000), (2, 82000), (3, 5000);

INSERT INTO transactions (from_wallet, to_wallet, amount, created_at)
SELECT 1 + (g % 3), 1 + ((g + 1) % 3), 100 + (g * 37) % 900,
       now() - (g || ' minutes')::interval
FROM generate_series(1, 2000) AS g;
